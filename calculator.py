import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
BROWN = (139, 69, 19)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angry Birds Clone")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Fonts
font_large = pygame.font.SysFont("comicsansms", 50)

# Physics constants
GRAVITY = 0.5

# Bird class
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = RED
        self.vel_x = 0
        self.vel_y = 0
        self.dragging = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        if not self.dragging:
            self.vel_y += GRAVITY
            self.x += self.vel_x
            self.y += self.vel_y

    def reset(self):
        self.x, self.y = 100, HEIGHT - 100
        self.vel_x, self.vel_y = 0, 0
        self.dragging = False

# Target class
class Target:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = GREEN

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Sling class
class Sling:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, bird):
        if bird.dragging:
            pygame.draw.line(screen, BROWN, (self.x, self.y), (bird.x, bird.y), 5)

# Game loop
def game_loop():
    running = True
    bird = Bird(100, HEIGHT - 100)
    target = Target(random.randint(WIDTH // 2, WIDTH - 100), HEIGHT - 100, 50, 50)
    sling = Sling(100, HEIGHT - 100)

    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if math.hypot(event.pos[0] - bird.x, event.pos[1] - bird.y) < bird.radius:
                    bird.dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                if bird.dragging:
                    bird.dragging = False
                    bird.vel_x = (bird.x - sling.x) * -0.3
                    bird.vel_y = (bird.y - sling.y) * -0.3

            if event.type == pygame.MOUSEMOTION:
                if bird.dragging:
                    bird.x, bird.y = event.pos

        bird.update()

        if bird.y > HEIGHT or bird.x > WIDTH:
            bird.reset()

        if bird.x + bird.radius > target.x and bird.x - bird.radius < target.x + target.width and \
           bird.y + bird.radius > target.y and bird.y - bird.radius < target.y + target.height:
            target = Target(random.randint(WIDTH // 2, WIDTH - 100), HEIGHT - 100, 50, 50)
            bird.reset()

        sling.draw(bird)
        bird.draw()
        target.draw()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
