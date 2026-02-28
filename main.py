import pygame
import random
pygame.init()
screen = pygame.display.set_mode((700,700))
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(700,700))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.jpg")
pygame.display.set_icon(icon)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_sprite = pygame.image.load("player.png")
        self.player_sprite = pygame.transform.scale(self.player_sprite,(100,100))
    def create_player(self):
        screen.blit(self.player_sprite,(250,600))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.enemy_sprite = pygame.image.load("enemy.png")
        self.enemy_sprite = pygame.transform.scale(self.enemy_sprite,(50,50))
        self.x = random.randint(100,600)
        self.y = 100
        self.speed = random.randint(1,10)
    def create_enemy(self):
        screen.blit(self.enemy_sprite,(self.x,self.y))
    def move(self):
        while True:
            self.enemy_sprite.x -= self.speed

player = Player()
enemy_list = []
for i in range(5):
    enemy_list.append(Enemy())
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    player.create_player()
    for enemy in enemy_list:
        enemy.create_enemy()
    pygame.display.update()
pygame.quit()