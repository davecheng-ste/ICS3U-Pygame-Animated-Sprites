# Basic Animation in Pygame

## Character Animation
The following is a simple approach to create an animated character sprite in your Pygame project. You can see the completed method in the file [animated_character.py](animated_character.py). 

For this approach, we will do the following:

- Load an entire sprite sheet as a single surface.
- Define smaller areas — called **subsurfaces** — of this larger sprite sheet. Each subsurface represents one frame in the animation.
- Create a list of sequential surfaces or images Each element in the list is one of the above subsurfaces.
- Define a Rect object to draw and move the character sprite.
- Create a timer for tracking how long one frame of the sprite is displayed.
- Draw each frame in the list of surfaces in order, changing the frame sequentially to create an animated effect.

![whale_diagram](images/whale_diagram.png)