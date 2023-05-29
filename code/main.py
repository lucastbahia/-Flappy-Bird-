# Inicialização 
# Importa e inicia pacotes
from typing import Any
import pygame
import time
from variaveis import *
import random

pygame.init()
pygame.mixer.init()

# Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Ship')

# Importando as imagens:
assets = dict()
assets['game_on'] = pygame.image.load('../images/game_on.png').convert_alpha()
assets['nave_espacial'] = pygame.image.load('../images/nave_espacial.png').convert_alpha()
assets['buraco_negro'] = pygame.image.load('../images/buraco_negro.png').convert_alpha()
assets['estacao_espacial'] = pygame.image.load('../images/estacao_espacial.png').convert_alpha()
assets['fundo_tela'] = pygame.image.load('../images/fundo_tela.png').convert_alpha()
assets['meteoro1'] = pygame.image.load('../images/meteoro1.png').convert_alpha()
assets['meteoro2'] = pygame.image.load('../images/meteoro2.png').convert_alpha()
assets['buraco_minhoca'] = pygame.image.load('../images/buraco_minhoca.png').convert_alpha()
assets['game_over'] = pygame.image.load('../images/game_over.png').convert_alpha()
assets['score_font'] = pygame.font.Font('../font/PressStart2P.ttf', 28)

# Importando os sons:
pygame.mixer.music.load('../sons/fundo.mp3')
pygame.mixer.music.set_volume(0.4)
batida = pygame.mixer.Sound('../sons/batida.mp3')


#tamanho da nave
nave_WIDTH = 50
nave_HEIGHT = 38
nave = pygame.transform.scale(assets['nave_espacial'], (nave_WIDTH, nave_HEIGHT))

#Tempo inicial
score=0
tempo_inicial = pygame.time.get_ticks()

       
class Nave(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['nave_espacial']
        self.rect = self.image.get_rect()

        
class Buracos_(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
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
        if score % 10 == 0:
            self.speedx *= 1.5

        
buraco1 = Buracos_(assets['buraco_negro'])
buraco2 = Buracos_(assets['buraco_minhoca'])

class Meteoros(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        self.rect.x = WIDTH
        self.rect.y = random.randint(0,HEIGHT)
        self.speedx = random.randint(2, 10)
        self.speedy = 0

    def update(self):
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
        if score % 10 == 0:
            self.speedx *= 1.5

meteoro1 = Meteoros(assets['meteoro1'])
meteoro2 = Meteoros(assets['meteoro2'])



class Estacao(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['estacao_espacial']
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
        if score % 10 == 0:
            self.speedx *= 1.5
estacao1 = Estacao(assets)
estacao2 = Estacao(assets)


# Crinado variaveis para conseguir verificar a colisão
todos_objetos = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
estacoes = pygame.sprite.Group()
buracos = pygame.sprite.Group()

# Criando um dicionario para guardar as variaveis
objetos = {}
objetos['buracos'] = buracos
objetos['estacoes'] = estacoes
objetos['meteoros'] = meteoros

#Criando jogador
player = Nave(assets)
todos_objetos.add(player)

# Adicionando objetos para os grupos
for i in range(2):
    meteoros.add(meteoro1)
    meteoros.add(meteoro2)
    estacoes.add(estacao1)
    estacoes.add(estacao2)
    buracos.add(buraco1)
    buracos.add(buraco2)
    

# Inicia estruturas de dados
game = True

relogio = pygame.time.Clock()
# Carrega o fundo do jogo
background = assets['fundo_tela']
# Redimensiona o fundo
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

# ===== Loop principal =====
#Velocidade inicial da nave
vaelocidade_da_nave_x = 0
velocidade_da_nave_y = 0

#posição inicial da nave
nave_x = (WIDTH/3.5)
nave_y = HEIGHT/2
nave_r=10

# Aceleração a cada frame
ACELERACAO = 2


print('aperte espaço para pular com a nave')

# Loop principal
while game:
    print("Oi")
    

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

    # Como fazer a nave não cair??
    if nave_y +40 > HEIGHT:
        nave_y = HEIGHT - 40
    if nave_y <= 0:
        nave_y = 0

    #Verifica batidas
    hits = pygame.sprite.spritecollide(player, meteoros, True)
    hits.append(pygame.sprite.spritecollide(player, estacoes, True))
    hits.append(pygame.sprite.spritecollide(player, buracos, True))
    if len(hits) > 0:
        batida.play
        time.sleep(1)
        game = False



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

    
    # Desenhando a nave na janela
    window.blit(nave, (nave_x, nave_y))

    # Desenhando o score
    score = tempo_decorrido
    text_surface =assets['score_font'].render("{:05d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    # Atualiza posições dos meteoros, estacoes e buracos:
    meteoros.update()
    estacoes.update()
    buracos.update()

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
    
    # ----- Gera tela principal

# Finalização 
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
