import pygame as pg

LARGURA = 1600
ALTURA = 900

janela = pg.display.set_mode([LARGURA, ALTURA])

pg.display.set_caption('100 days of Shogun')

fundo = pg.image.load('Imagens/imagem_fundo.png').convert()
fundo = pg.transform.scale(fundo, (LARGURA, ALTURA))

rei = pg.image.load('Imagens/imagem_rei.png').convert_alpha()
largura_rei = rei.get_width()
altura_rei = rei.get_height()

calendario = pg.image.load('Imagens/Calendario/calendario.png').convert_alpha()
largura_cal = calendario.get_width() / 2
altura_cal = calendario.get_height() / 2
calendario = pg.transform.scale(calendario, (largura_cal, altura_cal))

x_trono = (1600 - largura_rei) // 2
y_trono = ((900 - altura_rei) // 2) - 100


loop = True

while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            x_trono += 5

        if event.key == pg.K_LEFT:
            x_trono -= 5

        if event.key == pg.K_DOWN:
            y_trono += 5

        if event.key == pg.K_UP:
            y_trono -= 5

    janela.blit(fundo, (0, 0))
    janela.blit(rei, (x_trono, y_trono))
    janela.blit(calendario, (25, 25))

    pg.display.update()