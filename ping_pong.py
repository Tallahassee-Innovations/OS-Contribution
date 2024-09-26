import pygame
import sys

class PingPongGame:
    def __init__(self):
        pygame.init()
        
        # Constants
        self.WIDTH, self.HEIGHT = 800, 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Set up the display
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Ping Pong Game")

        # Game variables
        self.paddle_width, self.paddle_height = 10, 100
        self.ball_size = 10
        self.paddle_speed = 7
        self.ball_speed_x, self.ball_speed_y = 5, 5

        # Paddle positions
        self.left_paddle = pygame.Rect(30, (self.HEIGHT - self.paddle_height) // 2, self.paddle_width, self.paddle_height)
        self.right_paddle = pygame.Rect(self.WIDTH - 40, (self.HEIGHT - self.paddle_height) // 2, self.paddle_width, self.paddle_height)

        # Ball position
        self.ball = pygame.Rect(self.WIDTH // 2, self.HEIGHT // 2, self.ball_size, self.ball_size)

        # Game loop
        self.clock = pygame.time.Clock()
        self.run_game()

    def run_game(self):
        while True:
            self.handle_events()
            self.move_paddles()
            self.move_ball()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def move_paddles(self):
        keys = pygame.key.get_pressed()
        # Only move if the key is pressed
        if keys[pygame.K_w] and self.left_paddle.top > 0:
            self.left_paddle.y -= self.paddle_speed
        if keys[pygame.K_s] and self.left_paddle.bottom < self.HEIGHT:
            self.left_paddle.y += self.paddle_speed

        # AI control for the right paddle
        if self.right_paddle.centery < self.ball.centery and self.right_paddle.bottom < self.HEIGHT:
            self.right_paddle.y += self.paddle_speed
        elif self.right_paddle.centery > self.ball.centery and self.right_paddle.top > 0:
            self.right_paddle.y -= self.paddle_speed

    def move_ball(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        # Ball collision with top and bottom
        if self.ball.top <= 0 or self.ball.bottom >= self.HEIGHT:
            self.ball_speed_y = -self.ball_speed_y

        # Ball collision with paddles
        if self.ball.colliderect(self.left_paddle) or self.ball.colliderect(self.right_paddle):
            self.ball_speed_x = -self.ball_speed_x

        # Ball out of bounds (reset position)
        if self.ball.left <= 0 or self.ball.right >= self.WIDTH:
            self.reset_ball()

    def reset_ball(self):
        self.ball.x = self.WIDTH // 2
        self.ball.y = self.HEIGHT // 2
        self.ball_speed_x = -self.ball_speed_x  # Change direction

    def draw(self):
        self.screen.fill(self.BLACK)
        pygame.draw.rect(self.screen, self.WHITE, self.left_paddle)
        pygame.draw.rect(self.screen, self.WHITE, self.right_paddle)
        pygame.draw.ellipse(self.screen, self.WHITE, self.ball)
        pygame.draw.aaline(self.screen, self.WHITE, (self.WIDTH // 2, 0), (self.WIDTH // 2, self.HEIGHT))
        
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    PingPongGame()