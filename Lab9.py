# Racer
import math
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Load fonts
font = pygame.font.SysFont("Arial", 20)

# Player settings
player = pygame.Rect(175, 500, 50, 70)
player_speed = 5

# Enemy settings
enemy = pygame.Rect(random.randint(0, 350), 0, 50, 70)
enemy_speed = 3

# Coin settings
coins = []  # List to hold coins
coin_timer = 0
coin_spawn_delay = 30  # frames
coin_weights = [1, 2, 3]  # Different coin weights

# Game state

# snake


# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 10

# Snake settings
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)  # Moving right initially

# Food list – holds multiple food with weight and timer
foods = []
food_weights = [1, 2, 3]  # Different weights
food_lifetime = 50  # frames

# Score
score = 0
font = pygame.font.SysFont("Arial", 20)

# Add a new food to the board


def spawn_food():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    weight = random.choice(food_weights)
    foods.append({"pos": (x, y), "weight": weight, "timer": food_lifetime})


# Game loop
running = True
spawn_food()  # Spawn the first food

while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # Move the snake
    head_x, head_y = snake[0]
    new_head = (head_x + snake_dir[0], head_y + snake_dir[1])
    snake.insert(0, new_head)

    # Check wall collision
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Check self-collision
    if new_head in snake[1:]:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Check food collision
    eaten = False
    for food in foods[:]:
        if new_head == food["pos"]:
            score += food["weight"]
            foods.remove(food)
            spawn_food()
            eaten = True
            break

    if not eaten:
        snake.pop()  # Only grow if food was eaten

    # Update and draw foods
    for food in foods[:]:
        # Draw food as yellow square
        pygame.draw.rect(screen, YELLOW, (*food["pos"], CELL_SIZE, CELL_SIZE))
        food["timer"] -= 1
        if food["timer"] <= 0:
            foods.remove(food)
            spawn_food()

    # Draw snake
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))

    # Show score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# paint

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)

# Font
font = pygame.font.SysFont("Arial", 20)

# Clock
clock = pygame.time.Clock()

# Drawing state
drawing = False
start_pos = None
shape = "square"  # default shape

# Function to draw a square


def draw_square(surface, start, end):
    size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], size, size)
    rect.normalize()
    pygame.draw.rect(surface, BLUE, rect, 2)

# Function to draw right triangle


def draw_right_triangle(surface, start, end):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, BLUE, points, 2)

# Function to draw equilateral triangle


def draw_equilateral_triangle(surface, start, end):
    x1, y1 = start
    x2, y2 = end
    size = math.dist(start, end)
    point1 = (x1, y1)
    point2 = (x2, y2)
    # Find 3rd point using rotation
    angle = math.radians(60)
    dx, dy = x2 - x1, y2 - y1
    x3 = x1 + dx * math.cos(angle) - dy * math.sin(angle)
    y3 = y1 + dx * math.sin(angle) + dy * math.c