import random
import pygame
import sys

from pygame.locals import *

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

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
        # Section 3, turns the snake
        self.direction = dir
        pass

    def collision(self, x, y):
        # Section 2, checks for collisions of walls
        if x < 0 or x > 23:
            return True
        if y < 0 or y > 23:
            return True
        
        # Section 4, checks for snake's collision with itself
        for i in range(1, len(self.body)):
            if x == self.body[i][0] and y == self.body[i][1]:
                return True

        return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # Section 1, moves the snake
        new_location = [self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1]]
        for i in range(len(self.body) - 1, 0 , -1):
            self.body[i] = self.body[i-1]
        self.body[0] = new_location 

        # Section 7, grows the snake 
        if self.l >= len(self.body):
            growth = self.body[-1]
            self.body.append(growth)

        # Section 4, checks for collision
        if self.collision(self.body[0][0], self.body[0][1]):
            self.kill()        


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
        # Implements feature 10, "wait for user input".
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
        # Section 6, moves the apple to a new location not within the snake
        while True:
            newx = random.randint(0, 23)
            newy = random.randint(0, 23)
            unique = True
            for i in snake:
                if newx != i[0] or newy != i[0]:
                    continue
                else:
                    unique = False
            if unique:
                break

        self.position = [newx, newy]

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

    # Implements feature 10, "wait for user input"
    print("Press Space to Play")
    snake.wait_for_key()

    while True:
        # Implements feature #9: "incremental difficulty"
        if score < 10:
            clock.tick(10 + (score * 0.5))
        else:
            clock.tick(15)
        snake.check_events()
        draw_grid(surface)   
        snake.move()

        snake.draw(surface)
        apple.draw(surface)

        # Section 5, snake eats the apple, placing a new apple and incrementing score and length
        if snake.body[0] == apple.position:
            apple.place(snake.body)
            score += 1
            snake.l += 1

        screen.blit(surface, (0,0))

        # Section 8, displays the current score
        score_screen = myfont.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_screen, (0, 0))
        
        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()