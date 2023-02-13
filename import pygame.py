import pygame
import random

# Inicializar o pygame
pygame.init()

# Configurar o tamanho da tela
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Configurar o título da janela
pygame.display.set_caption("Jogo dos Balões")

# Variáveis do jogo
running = True
clock = pygame.time.Clock()

# Classe do Balão
class Balloon:
    def __init__(self):
        self.x = random.randint(0, screen_width - 50)
        self.y = screen_height
        self.speed = random.uniform(1, 5)

    def move(self):
        self.y -= self.speed
        
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, int(self.y)), 20)

# Lista de balões
balloons = []

# Adicionar 10 balões na lista
for i in range(10):
    balloons.append(Balloon())

# Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpar a tela
    screen.fill((255, 255, 255))

    # Atualizar a posição e desenhar cada balão
    for balloon in balloons:
        balloon.move()
        balloon.draw()

    # Atualizar a tela
    pygame.display.update()

    # Definir a taxa de atualização da tela
    clock.tick(60)

# Finalizar o pygame
pygame.quit()
