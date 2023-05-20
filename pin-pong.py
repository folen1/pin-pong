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
        if keys_pressed[K_UP]and self.rect.y > 5:
            self.rect.y-=10
        if keys_pressed[K_DOWN]and self.rect.y < 500:
            self.rect.y+=10
    def update_r(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w]and self.rect.y > 5:
            self.rect.y-=10
        if keys_pressed[K_s]and self.rect.y <500:
            self.rect.y+=10

    

hero= Play_game('platform.png',670,100,5,20,150)
hero1 = Play_game('platform.png',10,100,5,20,150)
ball = GameSprite('ball_1615463127.png',300,100,5,50,50)
lost1 =0

monsters = sprite.Group()

text_lose=font1.render('=(',True,(255,255,255))
bullets = sprite.Group()
win_height = 500
finish=False
game = True
speed_x = 3
speed_y = 3
while game:

    for e in event.get():
        if e.type==QUIT:
            game = False
    

    if finish==False:
        ball.rect.x += speed_x
        ball.rect.y +=speed_y
        window.blit(background,(0,0))
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1        
    if sprite.collide_rect(hero, ball) or sprite.collide_rect(hero1, ball):
        speed_x *= -1 

        
    if ball.rect.x > 650:
        win1=font1.render('Победил первый игрок',True,(255,255,255))
        window.blit(win1,(200,200))
        finish = True
    if ball.rect.x < 10:
        win2=font1.render('Победил второй игрок',True,(255,255,255))
        window.blit(win2,(200,200))
        finish = True

    keys_pressed=key.get_pressed()

    hero.reset()
    hero1.reset()
    ball.reset()

    

    hero.update()
    hero1.update_r()



    clock.tick(60)
    pygame.display.update()
