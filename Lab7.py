import pygame
import time
import math
from datetime import datetime

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load clock face image (we'll create a simple one)
clock_face = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.draw.circle(clock_face, WHITE, (WIDTH//2, HEIGHT//2), 180)
pygame.draw.circle(clock_face, BLACK, (WIDTH//2, HEIGHT//2), 180, 2)

# Create Mickey's hands
# Right hand (minutes) - longer and thinner
right_hand = pygame.Surface((150, 20), pygame.SRCALPHA)
pygame.draw.rect(right_hand, BLACK, (0, 8, 150, 4))

# Left hand (seconds) - shorter and thicker
left_hand = pygame.Surface((120, 20), pygame.SRCALPHA)
pygame.draw.rect(left_hand, RED, (0, 6, 120, 8))

# Clock center
center = (WIDTH//2, HEIGHT//2)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # Calculate angles (0 degrees is at the top, clockwise is positive)
    # Subtract 90 degrees to make 0 point to the right (like a unit circle)
    minute_angle = -math.radians(minutes * 6 - 90)
    second_angle = -math.radians(seconds * 6 - 90)

    # Clear screen
    screen.fill(WHITE)

    # Draw clock face
    screen.blit(clock_face, (0, 0))

    # Rotate and draw right hand (minutes)
    rotated_right = pygame.transform.rotate(right_hand, math.degrees(minute_angle))
    right_rect = rotated_right.get_rect(center=center)
    screen.blit(rotated_right, right_rect.topleft)

    # Rotate and draw left hand (seconds)
    rotated_left = pygame.transform.rotate(left_hand, math.degrees(second_angle))
    left_rect = rotated_left.get_rect(center=center)
    screen.blit(rotated_left, left_rect.topleft)

    # Draw center circle
    pygame.draw.circle(screen, BLACK, center, 10)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()