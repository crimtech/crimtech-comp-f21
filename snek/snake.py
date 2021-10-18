import random
import pygame
import sys
import time

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE
EATEN = False

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
    length = 1
    
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
        if x - self.body[self.l - 1][0] <= self.length or y - self.body[self.l - 1][1] <= self.length:
            return True
        pass
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        
        if self.body[-1:][0] == 0:
            self.length += 1
            self.l += 1
            self.body.pop()
        
        new_body = []

        if self.collision(self.body[0][0],self.body[0][1]) == True:
            self.kill()
        if self.direction == "d":
            new_head = (self.body[0][0], self.body[0][1] + DIR[self.direction][1])
            for i in range(1, self.length + 1):
                new_body.append((new_head[0], new_head[1] - i))
        elif self.direction == "u":
            new_head = (self.body[0][0], self.body[0][1] + DIR[self.direction][1])
            for i in range(1, self.length + 1):
                new_body.append((new_head[0], new_head[1] + i))
        elif self.direction == "r":
            new_head = (self.body[0][0] + DIR[self.direction][0], self.body[0][1])
            for i in range(1, self.length + 1):
                new_body.append((new_head[0] - i, new_head[1]))
               
        elif self.direction == "l":
            new_head = (self.body[0][0] + DIR[self.direction][0], self.body[0][1])
            for i in range(1, self.length + 1):
                new_body.append((new_head[0] + i, new_head[1]))
        

        self.body = []
        self.body.append(new_head)
      
        for i in range(len(new_body)):
            
            self.body.append(new_body[i])
            
             
        pass

    def kill(self):
        # Implements feature #
        self.dead = True
        self.dead= False
        time.sleep(1)
        main()


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
    eaten = False
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        self.eaten = True
        self.position = (rand_int(23), rand_int(23))
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
        clock.tick(10 + score / 3)
        snake.check_events()
        draw_grid(surface)        
        snake.move()
        snake.draw(surface)
        apple.draw(surface)
        
        if snake.body[0][0] == apple.position[0] and snake.body[0][1] == apple.position[1]:
            apple.place(snake)
            score +=1
            snake.body.append(0)
        
        screen.blit(surface, (0,0))
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Score: " + str(score), True, (255,255,255))
        screen.blit(text, (0,0))

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()