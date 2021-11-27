import random
import pygame
import sys
import math

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 5
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    eating = False
    start = False

    def __init__(self):
        self.dead = False
        self.start = False
        self.l = 5
        self.body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
        self.direction = 'r'
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # Section 3, "Turning the snake".
        if not (self.direction, dir) in [('l', 'r'), ('r', 'l'), ('u', 'd'), ('d', 'u')]:
            self.direction = dir

    def collision(self, x, y):
        # Section 2, "Collisions", and section 4, "Self Collisions"

        if x > WIDTH - 1 or x < 0 or y > HEIGHT - 1 or y < 0: 
            return True

        else:
            for segment in self.body[1:]:
                if x == segment[0] and y == segment[1]:
                    return True

        return False
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # Section 1, "Move the snake!". You will be revisiting this section a few times.

        if self.start:
            head = self.get_head()

            self.body.insert(0, (
                head[0] + DIR[self.direction][0],
                head[1] + DIR[self.direction][1]
            ))

            if self.collision(self.body[0][0], self.body[0][1]):
                self.kill()

            if self.eating:
                self.l += 1
                self.eating = False
            else:
                self.body.pop(-1)

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
            # If game-relevant key pressed, start game.
            if self.start:
                self.handle_keypress(event.key)
            else:
                self.wait_for_key()
    
    def wait_for_key(self):
        # Implements feature #10 ( using check_events() )
        self.start = True
        


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # See section 6, "moving the apple".
        new_pos = (rand_int(23), rand_int(23))

        while new_pos in snake:
            new_pos = (rand_int(23), rand_int(23))

        self.position = new_pos

        pass

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

    score = 0

    while True:
        # Implements feature #9
        # Uses a shifted logistic model
        speed = int(
            round(
                40/(1 + math.pow(math.e, -0.04 * score)) - 10
                )
            ) 
        # Set FPS
        clock.tick(speed)

        snake.check_events()
        draw_grid(surface)        
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        # Section 5, "Eating the Apple".
        if snake.body[0] == apple.position:
            snake.eating = True
            score += 1
            apple.place(snake.body)

        # Section 8, "Display the Score"
        score_font = pygame.font.SysFont('Chicago', 36)
        score_display = score_font.render("Score: " + str(score), False, (40, 0, 40))

        screen.blit(surface, (0,0))
        screen.blit(score_display, (1,1))

        pygame.display.update()

        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()

            # Implements feature #11
            main()
            # sys.exit(0)

if __name__ == "__main__":
    main()