import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision Example")

# Colors
WHITE = (255, 255, 255)
PINK = (255, 192, 203)
YELLOW = (255, 255, 150)

# Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def change_color(self, color):
        self.image.fill(color)

# Create sprite groups
all_sprites = pygame.sprite.Group()
sprite1 = MySprite(PINK, 50, 50)
sprite2 = MySprite(YELLOW, 50, 50)

# Set initial positions
sprite1.rect.x = 100
sprite1.rect.y = 100
sprite2.rect.x = 200
sprite2.rect.y = 200

all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move sprite2 with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite2.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        sprite2.rect.x += 5
    if keys[pygame.K_UP]:
        sprite2.rect.y -= 5
    if keys[pygame.K_DOWN]:
        sprite2.rect.y += 5

    # Check for collision
    if pygame.sprite.collide_rect(sprite1, sprite2):
        sprite1.change_color(YELLOW)
    else:
        sprite1.change_color(PINK)

    # Clear screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()