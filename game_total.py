import pygame,random,math

class Ball(pygame.sprite.Sprite):
    dx = 0 #更新後x座標
    dy = 0 #更新後y座標
    x = 0 #初始x座標
    y = 0 #初始y座標
    
    def __init__(self,screen,speed,srx,sry,radium,color):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.x = srx
        self.y = sry
        #球的背景
        self.image = pygame.Surface((radium*2, radium*2))
        self.image.fill((255,255,255))
        #球
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        #檢測碰撞的區域
        self.rect = self.image.get_rect()
        self.rect.center = (srx, sry)
        #反彈角度設定
        diraction = random.randint(20,70)
        rad = math.radians(diraction)
        self.dx = speed * math.cos(rad)
        self.dy = -speed * math.sin(rad)
    
    def update(self): #更新球位置
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.centerx = self.x  
        self.rect.centery = self.y
        if(self.rect.left <= 0 or self.rect.right >= self.screen.get_width()):
            self.dx *= -1
        elif(self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height()):
            self.dy *= -1

    def collidebounce(self): #撞到左或右邊界
        self.dx *= -1
        
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([38, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Pad(pygame.sprite.Sprite):
    def __init__(self): #板子初始設定
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:/板子圖.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)
        self.rect.y = screen.get_height() - self.rect.height - 20
        self.screen = pygame.display.get_surface()
    
    def update(self): #滑鼠操控板子
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

pygame.init() # 啟動遊戲
screen = pygame.display.set_mode((600,640)) # 視窗大小
pygame.display.set_caption("打磚塊遊戲")
#背景設定
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
#遊戲起始畫面設定
font = pygame.font.Font("C:/mingliu.ttc", 20)
font1 = pygame.font.Font("C:/mingliu.ttc", 32)
allsprite = pygame.sprite.Group() #群組 
ball_1 = Ball(screen, 10, 100, 100, 15, (0, 0, 0)) # 設定球
allsprite.add(ball_1)
bricks = pygame.sprite.Group() #設定bricks
allsprite.add(bricks)
pad = Pad()  #設定pad
allsprite.add(pad)  
clock = pygame.time.Clock()
for row in range(0, 4): #行數
    for column in range(0, 15): #列數
        if row == 0:
            brick = Brick((0,0,139), column * 40 + 1, row * 16 + 1)
        if row == 1:
            brick = Brick((0,0,205), column * 40 + 1, row * 16 + 1)
        if row == 2:
            brick = Brick((65,105,225), column * 40 + 1, row * 16 + 1)
        if row == 3:
            brick = Brick((100,149,237), column * 40 + 1, row * 16 + 1)
        bricks.add(brick)
        allsprite.add(brick)
message_start = "按滑鼠左鍵開始遊戲!!!"
playing = False
Running = True
while Running: #遊戲基礎設定
    clock.tick(50) #遊戲幀率
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #關閉視窗
            Running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not playing: #偵測遊戲是否開始
            playing = True
    if not playing: #遊戲起始介面
        message = font.render(message_start, 1, (255,0,255))
        screen.blit(message, (screen.get_width()/2-100, screen.get_height()/2))
        pygame.display.update()
    else: #遊戲中
        #更新物件
        ball_1.update()
        pad.update()
        bricks.update()
        allsprite.draw(screen)
        pygame.display.update()
    screen.blit(background, (0, 0))
    allsprite.draw(screen)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()