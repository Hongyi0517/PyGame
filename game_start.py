import pygame

pygame.init()
score = 0
font = pygame.font.Font("C:/mingliu.ttc", 20)
font1 = pygame.font.Font("C:/mingliu.ttc", 32)
screen = pygame.display.set_mode((600, 640))
pygame.display.set_caption("打磚塊遊戲")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()
clock = pygame.time.Clock()
message_start = "按滑鼠左鍵開始遊戲!!!"
playing = False
Running = True

while Running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not playing:
            playing = True

    if not playing:
        message = font.render(message_start, 1, (255,0,255))
        screen.blit(message, (screen.get_width()/2-100, screen.get_height()/2))
        pygame.display.update()
    else:
        allsprite.update()
        allsprite.draw(screen)
        pygame.display.update()

pygame.quit()
        
        

