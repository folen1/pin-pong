from pygame import *
import pygame
from random import randint
font.init()
mixer.init()
pygame.init()
window= display.set_mode((700,500))
display.set_caption('сs2')
background = transform.scale(image.load('galaxy.png'),(700,500))
game = True
clock = pygame.time.Clock()
bullets = sprite.Group()
x=400
y=400
s=10
x2=randint(20,700)
y2=0
s2=10
font1 = font.SysFont('Arial',36)





class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,size_z,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_z,size_y))
        self.speed = player_speed
        self.rect= self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Play_game(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_a]and self.rect.x <700:
            self.rect.x-=10
        if keys_pressed[K_d]and self.rect.x <700:
            self.rect.x+=10
        for e in event.get():
            if e.type==QUIT:
                game = False
    

hero= Play_game('platform.png',670,100,5,20,150)
hero1 = Play_game('platform.png',10,100,5,20,150)
lost1 =0

monsters = sprite.Group()
win1=font1.render('=)',True,(255,255,255))
text_lose=font1.render('=(',True,(255,255,255))
bullets = sprite.Group()

finish=False
game = True
health=5
while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
        elif e.type ==KEYDOWN:
            if e.key==K_w:
                hero.fire()

    if finish==False:
        keys_pressed=key.get_pressed()
        window.blit(background,(0,0))




    keys_pressed=key.get_pressed()

    hero.reset()
    hero1.reset()
    hero.update()


    clock.tick(60)
    pygame.display.update()

