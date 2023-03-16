import pygame,random,math

class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    
    def __init__(self,screen,speed,srx,sry,radium,color):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.x = srx
        self.y = sry
        self.image = pygame.Surface((radium*2, radium*2))
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (srx, sry)
        diraction = random.randint(20,70)
        rad = math.radians(diraction)
        self.dx = speed * math.cos(rad)
        self.dy = -speed * math.sin(rad)
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= self.screen.get_width()):
            self.dx *= -1
        elif(self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height()):
            self.dy *= -1

    def collidebounce(self):
        self.dx *= -1
pygame.init()
screen = pygame.display.set_mode((640,640))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()
ball_1 = Ball(screen, 10, 100, 100, 20, (0, 0, 0))
allsprite.add(ball_1)
clock = pygame.time.Clock()
Running = True
while Running:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    screen.blit(background, (0, 0))
    ball_1.update()
    allsprite.draw(screen)
    pygame.display.update()
pygame.quit()


