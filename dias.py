import pygame as pg

dia = pg.image.load('Imagens/Calendario/days.png')
dia0 = pg.image.load('Imagens/Calendario/zero.png')
dia1 = pg.image.load('Imagens/Calendario/one.png')
dia2 = pg.image.load('Imagens/Calendario/two.png')
dia3 = pg.image.load('Imagens/Calendario/three.png')
dia4 = pg.image.load('Imagens/Calendario/four.png')
dia5 = pg.image.load('Imagens/Calendario/five.png')
dia6 = pg.image.load('Imagens/Calendario/six.png')
dia7 = pg.image.load('Imagens/Calendario/seven.png')
dia8 = pg.image.load('Imagens/Calendario/eight.png')
dia9 = pg.image.load('Imagens/Calendario/nine.png')

tamanho_dias = (135, 65)
tamanho_numero = (35, 50)

dia = pg.transform.scale(dia, tamanho_dias)

dias = {
    "0": dia0,
    "1": dia1,
    "2": dia2,
    "3": dia3,
    "4": dia4,
    "5": dia5,
    "6": dia6,
    "7": dia7,
    "8": dia8,
    "9": dia9,
}

def cortar_transparencia(surface):
    rect = surface.get_bounding_rect()
    return surface.subsurface(rect).copy()

dia = cortar_transparencia(dia)

for chave in dias:
    dias[chave] = cortar_transparencia(dias[chave])
    dias[chave] = pg.transform.scale(dias[chave], tamanho_numero)


def desenhar_dia_no_papel(janela, papel_rect, valor):
    valor = str(valor)

    espacamento = 20

    largura_numeros = 0

    for algarismo in valor:
        largura_numeros += dias[algarismo].get_width() + espacamento

    largura_total = dia.get_width() + espacamento + largura_numeros

    x = papel_rect.centerx - largura_total // 2
    y = papel_rect.centery

    dias_rect = dia.get_rect()
    dias_rect.midleft = (x + 25, y)

    janela.blit(dia, dias_rect)

    x = dias_rect.right + espacamento

    for algarismo in valor:
        numero_img = dias[algarismo]

        numero_rect = numero_img.get_rect()
        numero_rect.midleft = (x, y)

        janela.blit(numero_img, numero_rect)

        x += numero_img.get_width() + 2