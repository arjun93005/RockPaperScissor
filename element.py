import random
import pygame


class Element:
    """
    Represents a single element (Rock, Paper, or Scissors) in the simulation.
    Manages its own position, velocity, type, and drawing logic.
    """

    def __init__(self, screen_width, screen_height):
        # --- Properties ---
        self.radius = 15
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.type = random.choice(['rock', 'paper', 'scissors'])

        # Start with a random non-zero velocity
        self.vx = random.choice([-3, -2, 2, 3])
        self.vy = random.choice([-3, -2, 2, 3])

        # Dictionary to map the element's type to its emoji character
        self.emojis = {
            'rock': '🪨',
            'paper': '📃',
            'scissors': '✂️'
        }

    def move(self, screen_width, screen_height):
        """
        Updates the element's position and handles bouncing off the walls.
        """
        # Update position based on velocity
        self.x += self.vx
        self.y += self.vy

        # Wall bounce logic: reverse velocity if the edge is hit
        if self.x + self.radius > screen_width or self.x - self.radius < 0:
            self.vx = -self.vx
        if self.y + self.radius > screen_height or self.y - self.radius < 0:
            self.vy = -self.vy

    def draw(self, screen, font):
        """
        Renders the element's emoji onto the screen.

        Args:
            screen: The main Pygame screen surface to draw on.
            font: The Pygame font object used to render the emoji.
        """
        # 1. Render the emoji character into a new image surface
        emoji_surface = font.render(self.emojis[self.type], True, (255, 255, 255))

        # 2. Get the rectangle for the new image and center it on the element's (x, y)
        emoji_rect = emoji_surface.get_rect(center=(self.x, self.y))

        # 3. "Blit" (copy) the emoji image onto the main screen at the correct position
        screen.blit(emoji_surface, emoji_rect)
