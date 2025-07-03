import pygame
import sys
import random
import sqlite3

# === Database Initialization ===
db_conn = sqlite3.connect("snake_game.db")
db_cursor = db_conn.cursor()
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY
    )
""")
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        username TEXT,
        level INTEGER,
        score INTEGER,
        FOREIGN KEY (username) REFERENCES users(username)
    )
""")
db_conn.commit()

# === Player Input ===
player_name = input("Enter your username: ")

db_cursor.execute("SELECT * FROM users WHERE username=?", (player_name,))
user_row = db_cursor.fetchone()
if not user_row:
    db_cursor.execute("INSERT INTO users(username) VALUES(?)", (player_name,))
    db_conn.commit()
    current_level = 1
    current_score = 0
else:
    db_cursor.execute(
        "SELECT level, score FROM scores WHERE username=?", (player_name,))
    score_row = db_cursor.fetchone()
    if score_row:
        current_level, current_score = score_row
    else:
        current_level, current_score = 1, 0

print(f"Welcome, {player_name}! Starting at level {current_level} with score {current_score}")

# === Pygame Initialization ===
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
GRID_SIZE = 20
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()
game_font = pygame.font.SysFont(None, 35)

# === Level Configurations ===
level_data = {
    1: {'speed': 10, 'walls': []},
    2: {'speed': 15, 'walls': [(200, 200, 200, 20), (100, 100, 20, 200)]},
    3: {'speed': 20, 'walls': [(150, 150, 300, 20), (150, 230, 20, 120)]}
}

# === Snake and Food ===
snake_body = [(100, 50), (80, 50), (60, 50)]
snake_direction = (GRID_SIZE, 0)
food_pos = (random.randrange(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE,
            random.randrange(0, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE)

game_paused = False


def render_walls(walls):
    for wall in walls:
        pygame.draw.rect(window, (255, 0, 0), wall)


def store_progress():
    db_cursor.execute("DELETE FROM scores WHERE username=?", (player_name,))
    db_cursor.execute("INSERT INTO scores(username, level, score) VALUES (?, ?, ?)",
                     (player_name, current_level, current_score))
    db_conn.commit()


def end_game():
    global game_active
    store_progress()
    print("Game Over! Your score:", current_score)
    pygame.quit()
    sys.exit()


# === Main Game Loop ===
game_active = True
while game_active:
    game_clock.tick(level_data[current_level]['speed'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            store_progress()
            game_active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_paused = not game_paused
                if game_paused:
                    store_progress()
            elif event.key == pygame.K_UP and snake_direction != (0, GRID_SIZE):
                snake_direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -GRID_SIZE):
                snake_direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (GRID_SIZE, 0):
                snake_direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-GRID_SIZE, 0):
                snake_direction = (GRID_SIZE, 0)

    if game_paused:
        continue

    # Move snake
    head_x, head_y = snake_body[0]
    new_head = (head_x + snake_direction[0], head_y + snake_direction[1])
    snake_body.insert(0, new_head)

    # Check collisions
    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
            new_head in snake_body[1:]):
        end_game()

    for wall in level_data[current_level]['walls']:
        if pygame.Rect(wall).collidepoint(new_head):
            end_game()

    if new_head == food_pos:
        current_score += 10
        if current_score >= current_level * 50 and current_level < len(level_data):
            current_level += 1
        food_pos = (random.randrange(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE,
                    random.randrange(0, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE)
    else:
        snake_body.pop()

    # Draw everything
    window.fill((0, 0, 0))
    render_walls(level_data[current_level]['walls'])
    for segment in snake_body:
        pygame.draw.rect(window, (0, 255, 0), (*segment, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(window, (255, 255, 0), (*food_pos, GRID_SIZE, GRID_SIZE))
    info_text = game_font.render(
        f"User: {player_name}  Level: {current_level}  Score: {current_score}", True, (255, 255, 255))
    window.blit(info_text, (10, 10))
    pygame.display.flip()

# === Save before exit ===
store_progress()
pygame.quit()
db_conn.close()
