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
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    position = (0, 0)
    LAST = 0
    eating = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        self.direction = dir
        pass

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        if (x < 0 or  x > WIDTH or y < 0 or y > HEIGHT):
            return True
        elif((x,y) in self.body):
            return True
        else:
            return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        if (self.collision(self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1])):
            self.kill()
        self.body.insert(0,(self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1]))
        if (self.eating == False):
            self.body.pop(self.l +1)
        else:
            self.eating = False
            self.l += 1
        # pass

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
        # TODO: see section 6, "moving the apple".
        self.position = (random.randrange(WIDTH), random.randrange(HEIGHT))

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def checkEat(snake, pos, apple, score, lturn):
    if (apple.position[0] * SIZE == pos[0] and apple.position[1] * SIZE == pos[1]):
        apple.place(snake)
        snake.l += 1
        snake.body.append((-1,-1))
        print(snake.body)
        score += 1
        print(lturn)
        print("greetings")

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def message_display(message):
    pygame.display.set_caption(message)

def check_key():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            return True
    return False

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
    t = 0
    started = False

    while True:
        # TODO: see section 10, "incremental difficulty".
        # Implements featue #9
        clock.tick(10 + t)
        # Implements feature #10
        if (started == False):
            started = check_key()
        snake.check_events()
        draw_grid(surface)
        if (started == True):
            snake.move()
        snake.draw(surface)
        apple.draw(surface)
        # TODO: see section 5, "Eating the Apple".
        if (snake.body[0] == apple.position):
            apple.place(snake)
            snake.eating = True
            t += 2
            score += 1
        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"
        message_display("Score: " + str(score))

        pygame.display.update()
        if (snake.dead):
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()