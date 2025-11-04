import pygame
from element import Element

# --- SECTION 1: INITIALIZATION ---
# Initialize all the Pygame modules
pygame.init()
screen_width = 800
screen_height = 600

# --- SECTION 2: SETUP (Runs Once) ---
# Create the main display screen and set its caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors Simulation")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a font object for rendering emojis. This only needs to be done once.
# 'Segoe UI Emoji' is a good font on Windows. SysFont will find a default if not available.
try:
    emoji_font = pygame.font.SysFont('Segoe UI Emoji', 24)
except pygame.error:
    emoji_font = pygame.font.SysFont(None, 30)  # A default fallback font

# Create a list of 20 Element objects using a list comprehension
elements = [Element(screen_width, screen_height) for _ in range(20)]

# --- SECTION 3: MAIN LOOP ---
running = True
while running:
    # Event handling: check for user input, like closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game Logic ---
    # 1. Move every element in the list
    for element in elements:
        element.move(screen_width, screen_height)

    # 2. Collision Detection and Resolution (nested loop to check every pair)
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            element1 = elements[i]
            element2 = elements[j]

            # Calculate squared distance for efficiency (avoids slow square root)
            dist_sq = (element1.x - element2.x) ** 2 + (element1.y - element2.y) ** 2

            # If the distance is less than the sum of radii, they are colliding
            if dist_sq < (element1.radius + element2.radius) ** 2:

                # --- Apply Rock-Paper-Scissors Rules ---
                # Paper wins vs Rock
                if (element1.type == 'paper' and element2.type == 'rock') or \
                        (element1.type == 'rock' and element2.type == 'paper'):
                    if element1.type == 'rock':
                        element1.type = 'paper'
                    else:
                        element2.type = 'paper'

                # Rock wins vs Scissors
                elif (element1.type == 'rock' and element2.type == 'scissors') or \
                        (element1.type == 'scissors' and element2.type == 'rock'):
                    if element1.type == 'scissors':
                        element1.type = 'rock'
                    else:
                        element2.type = 'rock'

                # Scissors wins vs Paper
                elif (element1.type == 'scissors' and element2.type == 'paper') or \
                        (element1.type == 'paper' and element2.type == 'scissors'):
                    if element1.type == 'paper':
                        element1.type = 'scissors'
                    else:
                        element2.type = 'scissors'

                # --- Apply Bounce Physics ---
                # Swap velocities for a simple, effective bounce effect
                element1.vx, element2.vx = element2.vx, element1.vx
                element1.vy, element2.vy = element2.vy, element1.vy

    # --- Drawing ---
    # 1. Fill the background with a dark grey color
    screen.fill((25, 25, 25))

    # 2. Draw every element onto the screen
    for element in elements:
        element.draw(screen, emoji_font)  # Pass the font object to the draw method

    # 3. Update the full display to show everything that was drawn
    pygame.display.flip()

    # 4. Limit the frame rate to 60 frames per second
    clock.tick(60)

# --- Clean Up ---
# Uninitialize Pygame modules
pygame.quit()
