import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([38, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("打磚塊遊戲")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
allsprite = pygame.sprite.Group()
bricks = pygame.sprite.Group()
clock = pygame.time.Clock()

for row in range(0, 4):
    for column in range(0, 15):
        if row == 0 or row == 1:
            brick = Brick((0, 255, 0), column * 40 + 1, row * 15 + 1)
        if row == 2 or row == 3:
            brick = Brick((0, 0, 255), column * 40 + 1, row * 15 + 1)
        bricks.add(brick)
        allsprite.add(brick)

Running = True
while Running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    screen.blit(background, (0, 0))
    allsprite.draw(screen)
    bricks.draw(screen)
    pygame.display.update()

pygame.quit()