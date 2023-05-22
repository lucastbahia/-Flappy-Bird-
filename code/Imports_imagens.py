# Inicialização 
# Importa e inicia pacotes
import pygame
from variaveis import *

pygame.init()

# Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# Importando as imagens:
game_on = pygame.image.load('../images/game_on.png').convert_alpha()
nave_espacial = pygame.image.load('../images/nave_espacial.jpg').convert_alpha()
buraco_negro = pygame.image.load('../images/buraco_negro.jpg').convert_alpha()
estacao_espacial = pygame.image.load('../images/estacao_espacial.jpg').convert_alpha()
fundo_tela = pygame.image.load('../images/fundo_tela.png').convert_alpha()
meteoro1 = pygame.image.load('../images/meteoro1.jpeg').convert_alpha()
meteoro2 = pygame.image.load('../images/meteoro2.png').convert_alpha()
buraco_minhoca = pygame.image.load('../images/buraco_minhoca.png').convert_alpha()
game_over = pygame.image.load('../images/game_over.png').convert_alpha()

       
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = nave_espacial
        self.rect = self.image.get_rect()
        
class Buracos(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

black_hole = Buracos(buraco_negro)
minhoca = Buracos(buraco_minhoca)

class Meteoros(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

meteoro_brilhante=Meteoros(meteoro1)
meteoro=Meteoros(meteoro2)

class Estacao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = estacao_espacial
        self.rect = self.image.get_rect()


# # Importando os sons:
# pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
# pygame.mixer.music.set_volume(0.4)
# batida = pygame.mixer.Sound('../sons/batida.mp3')
# fundo= pygame.mixer.Sound('../sons/fundo.mp3')

# Inicia estruturas de dados
game = True

# Carrega o fundo do jogo
background = fundo_tela
# Redimensiona o fundo
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

# Loop principal
while game:
    # Trata eventos
    for event in pygame.event.get():
        # Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca

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

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização 
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados