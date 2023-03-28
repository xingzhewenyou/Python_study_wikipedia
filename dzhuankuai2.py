import pygame
import random

# initialize pygame
pygame.init()

# set the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Brick Breaker")

# set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set the font
font = pygame.font.SysFont(None, 24)

# set the paddle variables
paddle_width = 100
paddle_height = 10
paddle_x = WINDOW_WIDTH / 2 - paddle_width / 2
paddle_y = WINDOW_HEIGHT - paddle_height - 10
paddle_dx = 60

# set the ball variables
ball_radius = 6
ball_x = WINDOW_WIDTH / 2
ball_y = WINDOW_HEIGHT / 2
ball_dx = 5
ball_dy = -5

# set the brick variables
brick_width = 75
brick_height = 20
brick_padding = 10
brick_offset_top = 50
brick_offset_left = 50
brick_color = (255, 0, 0)

# create the bricks
bricks = []
for row in range(3):
    for column in range(8):
        brick_x = column * (brick_width + brick_padding) + brick_offset_left
        brick_y = row * (brick_height + brick_padding) + brick_offset_top
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# set the score
score = 0

# set the clock
clock = pygame.time.Clock()

# main game loop
while True:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    # move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_dx
    elif keys[pygame.K_RIGHT] and paddle_x + paddle_width < WINDOW_WIDTH:
        paddle_x += paddle_dx

    # move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # check for collisions with the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WINDOW_WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius < 0:
        ball_dy = -ball_dy
    if ball_y + ball_radius > WINDOW_HEIGHT:
        ball_x = WINDOW_WIDTH / 2
        ball_y = WINDOW_HEIGHT / 2
        ball_dx = random.choice([-5, 5])
        ball_dy = -5

    # check for collisions with the paddle
    if ball_dy > 0 and paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y < paddle_y + paddle_height:
        ball_dy = -ball_dy

    # check for collisions with the bricks
    for brick in bricks:
        if ball_dy < 0 and brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius * 2,
                                                         ball_radius * 2, ball_radius * 2)):
            ball_dy = -ball_dy
            bricks.remove(brick)
            score += 50
        elif ball_dy > 0 and brick.colliderect(
                pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            ball_dy = -ball_dy
            bricks.remove(brick)
            score += 50

            # draw the background
        window.fill(BLACK)

        # draw the paddle
        pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # draw the ball
        pygame.draw.circle(window, WHITE, (int(ball_x), int(ball_y)), ball_radius)

        # draw the bricks
        for brick in bricks:
            pygame.draw.rect(window, brick_color, brick)

        # draw the score
        score_text = font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))

        # update the display
        pygame.display.update()

        # tick the clock
        clock.tick(60)
