import pygame

class Pad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:/板子圖.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)
        self.rect.y = screen.get_height() - self.rect.height - 20
    
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("打磚塊遊戲")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()
bricks = pygame.sprite.Group()
pad = Pad()  # 建立 Pad 物件
allsprite.add(pad)  # 加入 allsprite 群組
clock = pygame.time.Clock()
Running = True

while Running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    # 更新 pad 的位置
    allsprite.update()

    # 繪製所有元素
    screen.blit(background, (0, 0))
    allsprite.draw(screen)

    pygame.display.update()

pygame.quit()
        
