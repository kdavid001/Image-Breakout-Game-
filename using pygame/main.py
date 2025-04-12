import pygame
import sys
from paddle import Paddle
from ball import Ball
from block import Block
from score import Score

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Breakout Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize paddle, ball, and score
paddle = Paddle(200, 20, WIDTH)
ball = Ball(10)
score = Score()

# Initialize blocks
block_width = 60
block_height = 20
rows = 5
cols = WIDTH // (block_width + 10)
blocks = [Block(col * (block_width + 10) + 5, row * (block_height + 10) + 40, block_width, block_height)
          for row in range(rows) for col in range(cols)]

font = pygame.font.Font(None, 36)

def reset_ball_and_paddle():
    ball.reset(WIDTH, HEIGHT)
    paddle.x = (WIDTH - paddle.width) // 2

clock = pygame.time.Clock()
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")

    ball.move()

    # Collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.dx = -ball.dx
    if ball.top <= 0:
        ball.dy = -ball.dy
    if ball.colliderect(paddle):
        ball.dy = -ball.dy

    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball.dy = -ball.dy
            score.increase_score()
            break

    if ball.bottom >= HEIGHT:
        score.check_highscore()
        score.reset_score()
        blocks.clear()
        for row in range(rows):
            for col in range(cols):
                blocks.append(Block(col * (block_width + 10) + 5, row * (block_height + 10) + 40, block_width, block_height))
        reset_ball_and_paddle()

    if not blocks:
        blocks.clear()
        for row in range(rows):
            for col in range(cols):
                blocks.append(Block(col * (block_width + 10) + 5, row * (block_height + 10) + 40, block_width, block_height))
        reset_ball_and_paddle()

    # Drawing
    screen.fill( )
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    score_text = font.render(f"Score: {score.score}", True, WHITE)
    highscore_text = font.render(f"Highscore: {score.highscore}", True, WHITE)
    screen.blit(score_text, (20, 10))
    screen.blit(highscore_text, (WIDTH - 200, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()