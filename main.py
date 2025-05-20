import pygame
import sys

#inicializa o pygame - biblioteca games
pygame.init()

tela = pygame.display.set_mode((400,500))
pygame.display.set_caption("yuri-playmobil")

#cores
ROXO = (28, 0, 
        128)
PRETO = (0, 0, 0)


#tamanho da nave
x = 100
y = 100
tamanho = 50
velocidade = 10



rodando = True
while rodando:
  pygame.time.delay(50)
  for evento in pygame.event.get():
    if evento.type == pygame.quit:
      rodando = False
  teclas = pygame.key.get_pressed()
  if teclas[pygame.K_UP]:
    y -= velocidade

  if teclas[pygame.K_DOWN]:
    y += velocidade

  if teclas[pygame.K_LEFT]:
    x -= velocidade

  if teclas[pygame.K_RIGHT]:
    x += velocidade
  tela.fill((PRETO))
  pygame.draw.rect(tela, ROXO, (x, y, tamanho, tamanho))

  pygame.display.update()


pygame.quit()
sys.exit()
    