import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 2

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Player
player_img = pygame.image.load("player.png")
player_x = SCREEN_WIDTH // 2 - 32
player_y = SCREEN_HEIGHT - 64
player_x_change = 0

# Enemies
enemies = []
for _ in range(6):
    enemy_img = pygame.image.load("enemy.png")
    enemy_x = random.randint(0, SCREEN_WIDTH - 64)
    enemy_y = random.randint(50, 200)
    enemies.append({"img": enemy_img, "x": enemy_x, "y": enemy_y})

# Bullets
bullets = []
bullet_img = pygame.image.load("bullet.png")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player_x_change = PLAYER_SPEED
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + 16
                bullet_y = player_y
                bullets.append({"img": bullet_img, "x": bullet_x, "y": bullet_y})

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    if player_x < 0:
        player_x = 0
    elif player_x > SCREEN_WIDTH - 64:
        player_x = SCREEN_WIDTH - 64

    # Update enemies
    for enemy in enemies:
        enemy["y"] += ENEMY_SPEED

    # Update bullets
    for bullet in bullets:
        bullet["y"] -= BULLET_SPEED

    # Render everything
    screen.fill((0, 0, 0))
    screen.blit(player_img, (player_x, player_y))

    for enemy in enemies:
        screen.blit(enemy["img"], (enemy["x"], enemy["y"]))

    for bullet in bullets:
        screen.blit(bullet["img"], (bullet["x"], bullet["y"]))

    pygame.display.update()

pygame.quit()
