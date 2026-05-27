import pygame as pg

zero = pg.image.load('Imagens/Calendario/zero.png')
um = pg.image.load('Imagens/Calendario/one.png')
dois = pg.image.load('Imagens/Calendario/two.png')
tres = pg.image.load('Imagens/Calendario/three.png')
quatro = pg.image.load('Imagens/Calendario/four.png')
cinco = pg.image.load('Imagens/Calendario/five.png')
seis = pg.image.load('Imagens/Calendario/six.png')
sete = pg.image.load('Imagens/Calendario/seven.png')
oito = pg.image.load('Imagens/Calendario/eight.png')
nove = pg.image.load('Imagens/Calendario/nine.png')
porcento = pg.image.load('Imagens/porcento.png')

dias = {
    "0": zero,
    "1": um,
    "2": dois,
    "3": tres,
    "4": quatro,
    "5": cinco,
    "6": seis,
    "7": sete,
    "8": oito,
    "9": nove,
}

tamanho_numero = (15, 20)

def cortar_transparencia(surface):
    rect = surface.get_bounding_rect()
    return surface.subsurface(rect).copy()

for chave in dias:
    dias[chave] = cortar_transparencia(dias[chave])
    dias[chave] = pg.transform.scale(dias[chave], tamanho_numero)

porcento = cortar_transparencia(porcento)
porcento = pg.transform.scale(porcento, tamanho_numero)

def atualizar(janela, quadro_rect, valor):
    valor = str(valor)

    espacamento = 1
    largura_numeros = 0

    for algarismo in valor:
        largura_numeros += dias[algarismo].get_width() + espacamento

    x = quadro_rect.centerx - largura_numeros // 2
    y = quadro_rect.centery

    for algarismo in valor:
        numero_img = dias[algarismo]

        numero_rect = numero_img.get_rect()
        numero_rect.midleft = (x, y)

        janela.blit(numero_img, numero_rect)

        x += numero_img.get_width() + 2

def atualizar_contentamento(janela, quadro_rect, valor):
    valor = str(valor)

    espacamento = 1
    largura_numeros = 0

    for algarismo in valor:
        largura_numeros += dias[algarismo].get_width() + espacamento

    x = quadro_rect.centerx - largura_numeros // 2
    y = quadro_rect.centery

    for algarismo in valor:
        numero_img = dias[algarismo]

        numero_rect = numero_img.get_rect()
        numero_rect.midleft = (x, y)

        janela.blit(numero_img, numero_rect)

        x += numero_img.get_width() + 2

        janela.blit(porcento, quadro_rect)