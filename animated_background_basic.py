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
WIDTH, HEIGHT = 632, 382
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Animation")

# Define constant colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load background image
road_background_full = pygame.image.load("images/road_background.png")

road_background_frame_width = 632
road_background_frame_height = 382
road_background_frames_list = [
    road_background_full.subsurface(pygame.Rect(106, 114, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 124, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 134, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 144, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 154, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 164, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 174, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 184, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 194, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 204, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 214, road_background_frame_width, road_background_frame_height)),
    road_background_full.subsurface(pygame.Rect(106, 224, road_background_frame_width, road_background_frame_height))
]

road_frame_duration = 50  # Frame duration in millseconds (ms)
road_frame_current = 0
road_frame_last_change_time = pygame.time.get_ticks()



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

    time_now = pygame.time.get_ticks()
    if time_now - road_frame_last_change_time > road_frame_duration:
        road_frame_current = (road_frame_current + 1) % len(road_background_frames_list)
        road_frame_last_change_time = time_now

    # Draw graphics
    screen.blit(road_background_frames_list[road_frame_current], (0, 0))
       

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
