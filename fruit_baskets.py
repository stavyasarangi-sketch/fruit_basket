import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Fruit Game")

class Basket:
    def __init__(self):
        self.image = pygame.image.load('Images/basket.jpeg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (160, 120))
        self.w, self.h = 120, 120
        self.x = 340
        self.y = 500

    def update(self):
        self.x = pygame.mouse.get_pos()[0] - (self.w // 2)
        if self.x < 0:
            self.x = 0
        elif self.x > 800 - self.w:
            self.x = 800 - self.w

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Fruit:
    def __init__(self):
        self.x = random.randint(20, 780)
        self.y = 0
        self.radius = 15

    def update(self):
        self.y += 1

    def draw(self):
        pygame.draw.circle(screen, (213, 50, 80), (self.x, self.y), self.radius)


basket = Basket()
fruits = []
score = 0
font = pygame.font.SysFont("Arial", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if random.randint(1, 400) == 1:
        fruits.append(Fruit())

    basket.update()
    for fruit in fruits:
        fruit.update()

    for fruit in fruits[:]:
        if (basket.y <= fruit.y <= basket.y + basket.h) and (basket.x <= fruit.x <= basket.x + basket.w):
            score += 1
            fruits.remove(fruit)
        elif fruit.y > 600:
            fruits.remove(fruit)

    screen.fill((255, 255, 255))
    basket.draw()
    for fruit in fruits:
        fruit.draw()

    score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

    pygame.display.update()
