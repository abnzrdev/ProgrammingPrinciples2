import pygame
import random
import sys

# Initialize Pygame
#  Step-by-step Racer Game with Coins and Score
pygame.init()

# Set display dimensions and frame rate
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer with Coins")
game_clock = pygame.time.Clock()

# Color definitions
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (50, 50, 50)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLUE = (0, 0, 255)

# Load and set up car image
car_image = pygame.image.load("car.png")  # Replace with your car image
car_image = pygame.transform.scale(car_image, (50, 100))
car_rect = car_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

# Coin settings
coin_radius = 15
coin_list = []
coin_spawn_time = 30  # frames
coin_timer = 0
coin_score = 0

# Speed
car_speed = 5
road_speed = 5

# Font
font = pygame.font.SysFont(None, 36)

# Function to draw coins


def draw_coin(x, y):
    pygame.draw.circle(window, COLOR_YELLOW, (x, y), coin_radius)

# Function to show score


def show_score(score):
    score_text = font.render(f"Coins: {score}", True, COLOR_BLUE)
    window.blit(score_text, (SCREEN_WIDTH - 130, 10))


# Main game loop
running = True
while running:
    game_clock.tick(60)  # 60 FPS
    window.fill(COLOR_GRAY)

    # Draw the road (optional lines can be added here)

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > 0:
        car_rect.x -= car_speed
    if keys[pygame.K_RIGHT] and car_rect.right < SCREEN_WIDTH:
        car_rect.x += car_speed

    # Coin generation
    coin_timer += 1
    if coin_timer >= coin_spawn_time:
        coin_timer = 0
        new_coin_x = random.randint(coin_radius, SCREEN_WIDTH - coin_radius)
        coin_list.append([new_coin_x, 0])  # x, y

    # Move and draw coins
    for coin in coin_list[:]:
        coin[1] += road_speed
        draw_coin(coin[0], coin[1])

        # Collision detection between car and coin
        if car_rect.collidepoint(coin[0], coin[1]):
            coin_list.remove(coin)
            coin_score += 1

        # Remove coins that fall off the screen
        elif coin[1] > SCREEN_HEIGHT:
            coin_list.remove(coin)

    # Draw the car
    window.blit(car_image, car_rect)

    # Show score
    show_score(coin_score)

    pygame.display.update()

#  Full Snake Game with Levels and Collision
# Initialize pygame
pygame.init()

# Screen size and settings
BLOCK_SIZE = 20
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Levels")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GRAY = (40, 40, 40)

# Fonts
font = pygame.font.SysFont(None, 35)

# Snake variables
snake = [(100, 100)]
direction = (BLOCK_SIZE, 0)  # Start moving to the right
food = (0, 0)
score = 0
level = 1
speed = 10

# Function to draw snake


def draw_snake():
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

# Function to place food (not on snake)


def place_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            return (x, y)

# Draw score and level


def draw_score_level():
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))


# Place first food
food = place_food()

# Game loop
running = True
while running:
    clock.tick(speed)
    screen.fill(DARK_GRAY)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Direction change
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, BLOCK_SIZE):
        direction = (0, -BLOCK_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -BLOCK_SIZE):
        direction = (0, BLOCK_SIZE)
    if keys[pygame.K_LEFT] and direction != (BLOCK_SIZE, 0):
        direction = (-BLOCK_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-BLOCK_SIZE, 0):
        direction = (BLOCK_SIZE, 0)

    # Move the snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # Check for wall collision
    if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT):
        print("You hit the wall!")
        running = False

    # Check for self-collision
    if head in snake[1:]:
        print("You hit yourself!")
        running = False

    # Check food collision
    if head == food:
        score += 1

        # Increase level every 4 points
        if score % 4 == 0:
            level += 1
            speed += 2

        food = place_food()
    else:
        snake.pop()  # Remove tail if no food eaten

    # Draw everything
    draw_snake()
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
    draw_score_level()

    pygame.display.update()

# Full Paint App with Shapes, Eraser & Color Picker

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
current_color = BLACK

# Drawing settings
drawing = False
last_pos = None
shape_mode = "free"  # 'free', 'rect', 'circle', 'eraser'
start_pos = None
radius = 10  # for eraser and brush

# UI positions for color buttons


def draw_ui():
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))
    # Shape mode buttons
    pygame.draw.rect(screen, (200, 200, 200), (10, 50, 100, 30))  # Free
    pygame.draw.rect(screen, (200, 200, 200), (120, 50, 100, 30))  # Rect
    pygame.draw.rect(screen, (200, 200, 200), (230, 50, 100, 30))  # Circle
    pygame.draw.rect(screen, (200, 200, 200), (340, 50, 100, 30))  # Eraser

    font = pygame.font.SysFont(None, 24)
    screen.blit(font.render("Free", True, BLACK), (35, 55))
    screen.blit(font.render("Rect", True, BLACK), (145, 55))
    screen.blit(font.render("Circle", True, BLACK), (255, 55))
    screen.blit(font.render("Eraser", True, BLACK), (360, 55))


# Main loop
screen.fill(WHITE)
running = True
while running:
    clock.tick(60)
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse button down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Color selection
            if y < 40:
                index = (x - 10) // 40
                if 0 <= index < len(colors):
                    current_color = colors[index]
                    shape_mode = "free"

            # Shape selection
            elif 50 <= y <= 80:
                if 10 <= x <= 110:
                    shape_mode = "free"
                elif 120 <= x <= 220:
                    shape_mode = "rect"
                elif 230 <= x <= 330:
                    shape_mode = "circle"
                elif 340 <= x <= 440:
                    shape_mode = "eraser"
            else:
                drawing = True
                start_pos = event.pos
                if shape_mode == "free":
                    last_pos = event.pos

        # Mouse button up
        elif event.type == pygame.MOUSEBUTTONUP:
            if shape_mode in ["rect", "circle"] and drawing:
                end_pos = event.pos
                if shape_mode == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    width = x2 - x1
                    height = y2 - y1
                    pygame.draw.rect(screen, current_color,
                                     (x1, y1, width, height), 2)
                elif shape_mode == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                    pygame.draw.circle(screen, current_color,
                                       start_pos, radius, 2)
            drawing = False
            last_pos = None

        # Mouse motion
        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape_mode == "free":
                pygame.draw.line(screen, current_color,
                                 last_pos, event.pos, radius)
                last_pos = event.pos
            elif shape_mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, radius)

    pygame.display.update()

pygame.quit()
sys.exit()