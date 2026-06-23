import pygame
import sys
import random
import asyncio

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner Game")

# Player
player = pygame.Rect(50, 300, 40, 40)
velocity_y = 0
gravity = 1

# Enemy
enemy = pygame.Rect(800, 300, 40, 40)
enemy_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

running = True
game_over = False


async def main():
    global velocity_y, score, game_over, running

    while running:

        await asyncio.sleep(0)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # Desktop: SPACE key
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and player.bottom >= 340:
                    velocity_y = -15

                if event.key == pygame.K_r and game_over:
                    player.y = 300
                    player.bottom = 340
                    velocity_y = 0
                    enemy.x = 800
                    score = 0
                    game_over = False

            # Mobile: Touch Screen
            if event.type == pygame.MOUSEBUTTONDOWN:

                if game_over:
                    player.y = 300
                    player.bottom = 340
                    velocity_y = 0
                    enemy.x = 800
                    score = 0
                    game_over = False

                elif player.bottom >= 340:
                    velocity_y = -15

        if not game_over:

            # Gravity
            velocity_y += gravity
            player.y += velocity_y

            if player.bottom >= 340:
                player.bottom = 340
                velocity_y = 0

            # Enemy movement
            enemy.x -= enemy_speed

            if enemy.right < 0:
                enemy.x = random.randint(700, 1000)
                score += 1

            # Collision
            if player.colliderect(enemy):
                game_over = True

        # Draw
        screen.fill((0, 0, 0))

        # Ground
        pygame.draw.line(screen, (255, 255, 255), (0, 340), (WIDTH, 340), 2)

        # Player
        pygame.draw.rect(screen, (0, 255, 0), player)

        # Enemy
        pygame.draw.rect(screen, (255, 0, 0), enemy)

        # Score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Game Over
        if game_over:
            over_text = font.render(
                "Game Over! Touch Screen To Restart",
                True,
                (255, 0, 0)
            )
            screen.blit(over_text, (70, 180))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

asyncio.run(main())
