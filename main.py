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
    def __init__(self,sprite_img,x,y):
        self.x = x
        self.y = y
        super().__init__()
        self.sprite = pygame.transform.scale(sprite_img,(100,100))
    def create_player(self):
        screen.blit(self.sprite,(self.x,self.y))


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
            self.x -= self.speed
class Bullet():
    def __init__(self,bullet_img, x,y):
        self.x = x
        self.y = y
        # self.bullet_img = bullet_img
        scale_size = (50,50)
        self.bullet_img = pygame.transform.scale(bullet_img, scale_size)


pspeed = 10
player_x = 250
player_y = 600
bullet_state = "rest"
player_sprite = pygame.image.load("player.png")
player = Player(player_sprite,player_x,player_y)
# screen.blit(player.sprite,(player_x,player_y))
bullet_img = pygame.image.load("bullet.png")
# player.create_player()
enemy_list = []
# enemy = Enemy()
for i in range(5):
    enemy = Enemy()
    enemy_list.append(enemy)

bullet_list = []
running = True
while running:
    for event in pygame.event.get():
        # print("events:", pygame.event.get(), running)
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x-= pspeed
            if event.key == pygame.K_RIGHT:
                player_x +=pspeed
            if event.key == pygame.K_SPACE:
                if len(bullet_list) == 0:
                    bullet_list.append("Bullet")
                    bullet_state = "fire"
                    bullet_x = player_x+25
                    bullet_y = player_y-25

    screen.blit(background,(0,0))
    screen.blit(player.sprite,(player_x,player_y))
    if bullet_state=="fire":
        bullet = Bullet(bullet_img, player_x,player_y)
        if bullet_y>100:
            pygame.time.delay(20)
            bullet_y -=5
            screen.blit(bullet.bullet_img,(bullet_x,bullet_y))
            for enemy in enemy_list:
                print(enemy.x, enemy.y,bullet_x, bullet_y)
                if bullet_x <= enemy.x+20 and bullet_x >= enemy.x-20 and bullet_y == enemy.y:
                    print("inside")
                    bullet_y == 5000000
                    enemy_list.remove(enemy)                    
        else:
            bullet_state = "rest"
            bullet_list.pop(0)
    # if bullet_x == enemy.x and bullet_y == enemy.y:
    #     bullet_y == 5000000
    #     enemy.y == 1000000
    for enemy in enemy_list:
        enemy.create_enemy()
        enemy.move()

    if len(enemy_list) == 0:
        font = pygame.font.SysFont("Arial",70)
        screen.blit((font.render("GAME OVER!", True, (255,255,255))), (150,250))
        pygame.time.delay(1000)
        running = False



    pygame.display.flip()


pygame.quit()