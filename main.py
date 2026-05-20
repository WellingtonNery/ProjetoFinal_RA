import pygame as pg

janela = pg.display.set_mode([1280, 720])

pg.display.set_caption('100 days of Shogun')

imagem_fundo = pg.image.load('C:/Users/welli/OneDrive/Área de Trabalho/Projeto final/Imagens/primeiroFundo.png')
imagem_fundo = pg.transform.scale(imagem_fundo, (1280, 720))

loop = True

while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False

    janela.blit(imagem_fundo, (0, 0))

    pg.display.update()