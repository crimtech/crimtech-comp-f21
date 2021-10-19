import random
import pygame
import sys

from pygame.locals import *
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 20)

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

    def collision(self, x, y):
        # Section 2
        if x < 0 or x > WIDTH - 1:
            return True
        if y < 0 or y > HEIGHT - 1:
            return False
        
        # Section 4
        # Check if the snake collided with itself
        for i in range(1, len(self.body)):
            if x == self.body[i][0] and y == self.body[i][1]:
                return True

        # If collision does not happen
        return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # Section 1
        # Get the new position
        pos2 = [self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1]]
        # Move the snake
        for i in range(len(self.body) - 1, 0 , -1):
            self.body[i] = self.body[i - 1]
        self.body[0] = pos2

        # Section 4
        # Check if collision happened
        if self.collision(self.body[0][0], self.body[0][1]):
            self.kill() 
        
        # Section 7
        # Make the snake grow
        if len(self.body) <= self.l:
            grow = self.body[-1]
            self.body.append(grow)

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
        # Section 10
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    return


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # Section 6
        while True:
            x2, y2 = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
            indicator = True
            # Find the new position for the apple
            for i in snake:
                if x2 == i[0] or y2 == i[0]:
                    indicator = False
            if indicator:
                break

        self.position = [x2, y2]

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

    # Implements feature 10
    print("Press space to start playing")
    snake.wait_for_key()

    score = 0

    while True:
        # Implements feature #9
        clock.tick(10 + (score * 0.2))

        snake.check_events()
        draw_grid(surface)        
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        
        # Section 5
        if snake.body[0] == apple.position:
            # Put a new apple
            apple.place(snake.body)
            # Increment the score and the length by 1
            score += 1
            snake.l += 1
        
        screen.blit(surface, (0,0))
        
        # Section 8
        my_score = myfont.render("Score: " + str(score), False, (0, 0, 0))
        screen.blit(my_score, (0, 0))

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()