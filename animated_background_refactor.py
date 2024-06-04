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

# Define constant colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load background image
road_background_full = pygame.image.load("images/road_background.png")

# Constants for the background frames
ROAD_BACKGROUND_FRAME_WIDTH = 632
ROAD_BACKGROUND_FRAME_HEIGHT = 382
ROAD_BACKGROUND_START_X = 106
ROAD_BACKGROUND_START_Y = 114
NUMBER_OF_FRAMES = 12
FRAME_STEP = 10


def load_background_frames(image, start_x, start_y, frame_width, frame_height, num_frames, step):
    """
    Load a list of background frames from a larger image.

    Parameters:
        image (pygame.Surface): The source image containing the background frames.
        start_x (int): The x-coordinate of the top-left corner of the first frame.
        start_y (int): The y-coordinate of the top-left corner of the first frame.
        frame_width (int): The width of each frame.
        frame_height (int): The height of each frame.
        num_frames (int): The total number of frames to load.
        step (int): The vertical distance between the top-left corners of consecutive frames.

    Returns:
        list of pygame.Surface: A list of surfaces representing the individual frames.
    """
    frames = []
    for i in range(num_frames):
        frame_rect = pygame.Rect(start_x, start_y + i * step, frame_width, frame_height)
        frame = image.subsurface(frame_rect)
        frames.append(frame)
    return frames


road_background_frames_list = load_background_frames(
    road_background_full, 
    ROAD_BACKGROUND_START_X, 
    ROAD_BACKGROUND_START_Y, 
    ROAD_BACKGROUND_FRAME_WIDTH, 
    ROAD_BACKGROUND_FRAME_HEIGHT, 
    NUMBER_OF_FRAMES, 
    FRAME_STEP
)

road_frame_duration = 50  # Frame duration in milliseconds (ms)
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
