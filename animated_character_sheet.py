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

# Load whale sprite sheet
whale_sprite_sheet = pygame.image.load("images/whale_sprites.png")

whale_frame_height = 40
whale_frame_width = 102
whale_frames = [
    whale_sprite_sheet.subsurface(pygame.Rect(0, 40, whale_frame_width, whale_frame_height)),
    whale_sprite_sheet.subsurface(pygame.Rect(0, 120, whale_frame_width, whale_frame_height)),
    whale_sprite_sheet.subsurface(pygame.Rect(0, 220, whale_frame_width, whale_frame_height))
]

whale_rect = whale_frames[0].get_rect()
whale_rect.centerx = WIDTH // 2
whale_rect.centery = HEIGHT // 2

whale_frame_duration = 250  # Frame duration in millseconds (ms)
whale_frame_current = 0
whale_frame_last_change_time = pygame.time.get_ticks()


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
    if time_now - whale_frame_last_change_time > whale_frame_duration:
        whale_frame_current = (whale_frame_current + 1) % len(whale_frames)
        whale_frame_last_change_time = time_now

    # Draw graphics
    screen.blit(ocean_background, (0, 0))
    screen.blit(whale_frames[whale_frame_current], whale_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
