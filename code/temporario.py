# Inicialização 
# Importa e inicia pacotes
import pygame
from variaveis import *
import random

pygame.init()
pygame.mixer.init()

# Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# Importando as imagens:
assets = dict()
assets['game_on'] = pygame.image.load('../images/game_on.jpg').convert_alpha()
assets['nave_espacial'] = pygame.image.load('../images/nave_espacial.png').convert_alpha()
assets['buraco_negro'] = pygame.image.load('../images/buraco_negro.png').convert_alpha()
assets['estacao_espacial'] = pygame.image.load('../images/estacao_espacial.png').convert_alpha()
assets['fundo_tela'] = pygame.image.load('../images/fundo_tela.png').convert_alpha()
assets['meteoro1'] = pygame.image.load('../images/meteoro1.png').convert_alpha()
assets['meteoro2'] = pygame.image.load('../images/meteoro2.png').convert_alpha()
assets['buraco_minhoca'] = pygame.image.load('../images/buraco_minhoca.png').convert_alpha()
assets['game_over'] = pygame.image.load('../images/game_over.jpg').convert_alpha()
assets['score_font'] = pygame.font.Font('../font/PressStart2P.ttf', 28)

# ----- Inicia estruturas de dados
game = False

# ===== Loop principal =====
while not game:  # Não iniciar jogo, ate que ele sej verdadeiro
    # Carrega o fundo do jogo
    background = assets['game_on']
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    window.blit(background, background_rect)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = True  #jogo verdadeiro
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game = True  #jogo verdadeiro

    # ----- Atualiza estado do jogo
    pygame.display.update()

import time
time.sleep(1)

# Tamanho da nava
nave_WIDTH = 50
nave_HEIGHT = 38
nave = pygame.transform.scale(assets['nave_espacial'], (nave_WIDTH, nave_HEIGHT))

# Aceleração a cada frame
ACELERACAO = 2
class Nave(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['nave_espacial']
        self.image = pygame.transform.scale(self.image, (nave_WIDTH, nave_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_da_nave_y = 0
        
class Buracos_(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.image = pygame.transform.scale(self.image, (nave_WIDTH, nave_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0,HEIGHT)
        self.speedx = - random.randint(2, 10)

    def update(self):
        # Atualizando a posição do buraco
        self.rect.x += self.speedx
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = WIDTH
            self.rect.y = random.randint(0,HEIGHT)
            self.speedx = - random.randint(2, 10)
            self.speedy = 0

buraco1 = Buracos_(assets['buraco_negro'])
buraco2 = Buracos_(assets['buraco_minhoca'])

class Meteoros(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.image = pygame.transform.scale(self.image, (nave_WIDTH, nave_HEIGHT))
        self.rect = self.image.get_rect()

        self.rect.x = WIDTH
        self.rect.y = random.randint(0,HEIGHT)
        self.speedx = random.randint(2, 10)
        self.speedy = 0

    def update(self):
        # print(self.rect.x)
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = WIDTH
            self.rect.y = random.randint(0, HEIGHT)
            self.speedx = - random.randint(2, 10)
            self.speedy = 0


meteoro1=Meteoros(assets['meteoro1'])
meteoro2=Meteoros(assets['meteoro2'])

class Estacao(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['estacao_espacial']
        self.image = pygame.transform.scale(self.image, (nave_WIDTH, nave_HEIGHT))
        self.rect = self.image.get_rect()

        self.rect.x = WIDTH
        self.rect.y = random.randint(0,HEIGHT)
        self.speedx = - random.randint(2, 10)
        self.speedy = 0

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = WIDTH
            self.rect.y = random.randint(0,HEIGHT)
            self.speedx = - random.randint(2, 10)
            self.speedy = 0

estacao1 = Estacao(assets)
estacao2 = Estacao(assets)

# Importando os sons:
pygame.mixer.music.load('../sons/fundo.mp3')
pygame.mixer.music.set_volume(0.4)
batida = pygame.mixer.Sound('../sons/batida.mp3')

# Inicia estruturas de dados
game = True

relogio = pygame.time.Clock()
# Carrega o fundo do jogo
background = assets['fundo_tela']
# Redimensiona o fundo
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

# ===== Loop principal =====
#Velocidade inicial da bola
vaelocidade_da_nave_x = 0
velocidade_da_nave_y = 0

#posição inicial da bola
nave_x = (WIDTH/3.5)
nave_y = HEIGHT/2
nave_r=10



#tempo inicial
score=0
tempo_inicial = pygame.time.get_ticks()

# Crinado variaveis para conseguir verificar a colisão
todos_objetos = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
estacoes = pygame.sprite.Group()
buracos = pygame.sprite.Group()

# # Criando um dicionario para guardar as variaveis
objetos = {}
objetos['buracos'] = buracos
objetos['estacoes'] = estacoes
objetos['meteoros'] = meteoros

# #Criando jogador
# player = Nave(assets, nave_x, nave_y)
# todos_objetos.add(player)

# # Adicionando objetos para os grupos
# for i in range(2):

todos_objetos.add(meteoro1)
todos_objetos.add(meteoro2)
todos_objetos.add(estacao1)
todos_objetos.add(estacao2)
todos_objetos.add(buraco1)
todos_objetos.add(buraco2)

# Loop principal
while game:

    meteoro1.update()
    meteoro2.update()
    estacao1.update()
    estacao2.update()
    buraco1.update()
    buraco2.update()

    # Trata eventos
    relogio.tick(FPS)
    for event in pygame.event.get():
        # Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocidade_da_nave_y = -20
        tempo_atual = pygame.time.get_ticks()
        tempo_decorrido = (tempo_atual - tempo_inicial) // 1000  # Converte para segundos
    # ----- Atualiza estado do jogo
    #aplicando a aceleração da gravidade
    velocidade_da_nave_y += ACELERACAO
    nave_y += velocidade_da_nave_y

    # Como fazer a bolinha não cair??
    if nave_y +40 > HEIGHT:
        nave_y = HEIGHT - 40
    if nave_y <= 0:
        nave_y = 0

    # Atualiza a posição da imagem de fundo.
    background_rect.x += world_speed
    # Se o fundo saiu da janela, faz ele voltar para dentro.
    if background_rect.right < 0:
        background_rect.x += background_rect.width
    # Desenha o fundo e uma cópia para a direita.
    # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
    # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
    window.blit(background, background_rect)
    # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
    background_rect2 = background_rect.copy()
    background_rect2.x += background_rect2.width
    window.blit(background, background_rect2)

    # Desenhando o score
    score = tempo_decorrido
    text_surface =assets['score_font'].render("{:05d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    # Desenhando a nave na janela
    window.blit(nave, (nave_x, nave_y))

    # Desenhando os objetos:
    todos_objetos.update()
    todos_objetos.draw(window)

    posicao_nave = nave.get_rect()
    posicao_nave = posicao_nave.move(nave_x, nave_y)
    is_hit = [posicao_nave.colliderect(meteoro1.rect)]
    is_hit.append(posicao_nave.colliderect(meteoro2.rect))
    is_hit.append(posicao_nave.colliderect(estacao1.rect))
    is_hit.append(posicao_nave.colliderect(estacao2.rect))
    is_hit.append(posicao_nave.colliderect(estacao2.rect))
    is_hit.append(posicao_nave.colliderect(buraco1.rect))
    is_hit.append(posicao_nave.colliderect(buraco2.rect))
    for hit in is_hit:
        if hit:
            # tela = 'Game over'
            game = False

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # Carrega o fundo do jogo
    background = assets['game_over']
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    window.blit(background, background_rect)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    pygame.display.update() 

# Finalização 
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
