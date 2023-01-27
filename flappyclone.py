import pygame
from sys import exit

# Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # import player images
        player_1 = pygame.image.load('graphics/plane/red0.png').convert_alpha()

        self.player_1 = player_1
        self.image = self.player_1
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 410:
            self.gravity -= 20
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 410:
            self.rect.bottom = 410

    def update(self):
        self.player_input()
        self.apply_gravity()

pygame.init()
screen = pygame.display.set_mode((800,480))
pygame.display.set_caption('Flappy Clone')
clock = pygame.time.Clock()
font = pygame.font.Font('graphics/font/BD_Cartoon_Shout.ttf', 50)
game_active = True
start_time = 0
score = 0

# Environment
sky_surf = pygame.image.load('graphics/environment/background.png').convert()
ground_surf = pygame.image.load('graphics/environment/ground.png').convert_alpha()
ceiling_surf = pygame.image.load('graphics/environment/ground.png').convert_alpha()
ceiling_surf = pygame.transform.flip(ceiling_surf, True, True)


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,410))
        screen.blit(ceiling_surf, (0,0))

        player.draw(screen)
        player.update()
    
    pygame.display.update()
    clock.tick(60)