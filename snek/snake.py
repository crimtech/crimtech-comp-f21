import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1, 0),
    'r' : (1, 0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        self.direction = dir
        return

    def collision(self, x, y):
        if not(x < WIDTH and x >= 0 and y < HEIGHT and y >= 0):
            return True
        for segment in self.body[1:]:
            if segment == (x, y):
                return True
        return False
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        dir = DIR[self.direction]

        old_length = len(self.body) - 1
        if self.l != old_length:
            new_segment = self.body[old_length - 1]

        # Where the new head should be
        new_head = self.body[0]
        new_head = (new_head[0] + dir[0], new_head[1] + dir[1])

        # Go backward from the last body to the one before the first, set to the body in front
        for i in range(old_length, 0, -1):
            self.body[i] = self.body[i - 1]

        # Set head to new head
        self.body[0] = new_head

        # Add new segment at the tail
        if self.l != old_length:
            self.body.append(new_segment)

        # If the new arrangement creates collisions, the snek dies
        if self.collision(new_head[0], new_head[1]):
            self.kill()

        return

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10, 10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        touched = True

        while touched:
            touched = False
            new_position = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
            for segment in snake:
                if segment == new_position:
                    touched = True

        self.position = new_position

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    # Setting up the scoreboard
    score = 0
    font_color = (0, 0, 0)
    font_obj = pygame.font.Font("mono.ttf", 15)

    # Implements Feature 10
    draw_grid(surface) 
    apple.draw(surface)
    snake.draw(surface)
    intro_obj = font_obj.render("Press any key to start.", True, font_color)
    screen.blit(surface, (0,0))
    screen.blit(intro_obj, (WIDTH // 2, HEIGHT // 2))
    pygame.display.update()
    snake.wait_for_key()

    while True:
        # Implements Feature 9
        timer = 10 + (0.05 * pow(snake.l - 1, 2))
        clock.tick(timer)
        snake.check_events()
        draw_grid(surface)        
        snake.move()
        
        snake.draw(surface)
        apple.draw(surface)
        if snake.get_head() == apple.position:
            apple.place(snake.body)
            snake.l += 1
            score += 1
        screen.blit(surface, (0,0))
        
        # Display the score
        score_obj = font_obj.render("Score: " + str(score), True, font_color)
        screen.blit(score_obj, (10, 5))

        pygame.display.update()

        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()