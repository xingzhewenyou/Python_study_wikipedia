import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the ball properties
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5
ball_dy = -5

# set up the paddle properties
paddle_width = 100
paddle_height = 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - paddle_height - 10
paddle_dx = 0

# set up the brick properties
brick_width = 75
brick_height = 20
brick_gap = 10
brick_rows = 5
brick_cols = WIDTH // (brick_width + brick_gap)
bricks = []
for i in range(brick_rows):
    for j in range(brick_cols):
        brick_x = j * (brick_width + brick_gap) + brick_gap // 2
        brick_y = i * (brick_height + brick_gap) + brick_gap // 2 + 50
        brick_color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# set up the score
score = 0
font = pygame.font.Font(None, 36)

# set up the game loop
clock = pygame.time.Clock()
game_running = True
while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                paddle_dx = -30
            elif event.key == pygame.K_d:
                paddle_dx = 30
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                paddle_dx = 0

    # move the paddle
    paddle_x += paddle_dx
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > WIDTH - paddle_width:
        paddle_x = WIDTH - paddle_width

    # move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # check for collisions with the walls
    if ball_x < ball_radius or ball_x > WIDTH - ball_radius:
        ball_dx = -ball_dx
    if ball_y < ball_radius:
        ball_dy = -ball_dy
    elif ball_y > HEIGHT - ball_radius:
        game_running = False

    # check for collisions with the paddle
    if ball_dy > 0 and paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height and \
            paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy = -ball_dy
        score += 10

    # check for collisions with the bricks
    for brick in bricks:
        if ball_dy < 0 and brick.colliderect(
                pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            ball_dy = -ball_dy
            bricks.remove(brick)
            score += 50

            # clear the screen
        window.fill(BLACK)

        # draw the paddle
        pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # draw the ball
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)

        # draw the bricks
        for brick in bricks:
            pygame.draw.rect(window, brick_color, brick)

        # draw the score
        score_text = font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))

        # update the screen
        pygame.display.update()

        # set the frame rate
        clock.tick(60)
