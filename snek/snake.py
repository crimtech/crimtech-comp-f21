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
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    ateApple = False
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
        pass

    def collision(self, x, y):
        if x > 23 or x < 0 or y > 23 or y < 0: 
            return True
        
        count = 0
        for (a,b) in self.body: 
            if x == a or y == b:
                count +=1 
                if count >=2: 
                    return True
            else: 
                return False
            return False
        pass
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        x_change = DIR[self.direction][0]
        y_change = DIR[self.direction][1]
        headCoordinate = (self.body[0][0] + x_change, self.body[0][1] + y_change)
        self.body.insert(0, headCoordinate)
        
        if not self.ateApple:
            self.body.remove((self.body[-1][0], self.body[-1][1]))
        else: 
            self.l += 1
            self.ateApple = False
        if self.collision(self.body[0][0], self.body[0][1]): 
            self.kill()

        pass

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
        # TODO: see section 10, "wait for user input".
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        while self.position in snake: 
            self.position = (random.randint(0,23), random.randint(0,23))
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

    #Implements feature 10
    while True: 
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            while True:
                # TODO: see section 10, "incremental difficulty"
                clock.tick(10)
                snake.check_events()
                draw_grid(surface)      
                
                snake.move()

                if (apple.position == snake.body[0]): 
                    print("The snake is eating the apple!")
                    snake.ateApple = True
                    score += 1
                    apple.place(snake.body)  

                snake.draw(surface)
                apple.draw(surface)
            
                screen.blit(surface, (0,0))
                pygame.font.init()
                myfont = pygame.font.SysFont("Comic Sans MS", 30)
                scoreString = "Score: " + str(score)
                textsurface = myfont.render(scoreString, False, (0, 0, 0))
                screen.blit(textsurface, (0, 0))
                pygame.display.update()
            
                if snake.dead:
                    print('You died. Score: %d' % score)
                    
                    #Implements feature 11
                    snake.ateApple = False
                    score = 0
                    snake.l = 1
                    snake.body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
                    snake.dead = False
                    
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()