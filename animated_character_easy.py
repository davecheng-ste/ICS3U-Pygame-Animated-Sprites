"""
Author: D. Cheng
Date: 2024-06-04
Description: Pygame demonstration with animated sprites.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Ocean")

# Define constant colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load background image
ocean_background = pygame.image.load("images/water_background.png")
ocean_background = pygame.transform.scale(ocean_background, (WIDTH, HEIGHT))

# Load shark sprites into a list
shark_frames = [
    pygame.image.load("images/shark01.png"),
    pygame.image.load("images/shark02.png")
]

# Define Rect object to move and blit shark sprites
shark_rect = shark_frames[0].get_rect()
shark_rect.centerx = WIDTH // 2
shark_rect.centery = HEIGHT // 2

# Set up animation frame refresh mechanism
shark_frame_duration = 250  # Frame duration in millseconds (ms)
shark_frame_index = 0  # List index to be used with shark_frames
shark_time_changed = pygame.time.get_ticks()


# Define main game loop
running = True
clock = pygame.time.Clock()  # Create a Clock object for controlling frame rate

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # # Handle key presses
    # keys = pygame.key.get_pressed()

    time_now = pygame.time.get_ticks()
    if time_now - shark_time_changed > shark_frame_duration:
        if shark_frame_index == (len(shark_frames) - 1):
            shark_frame_index = 0
        else:
            shark_frame_index += 1
        shark_time_changed = time_now

    # Draw graphics
    screen.blit(ocean_background, (0, 0))
    screen.blit(shark_frames[shark_frame_index], shark_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
