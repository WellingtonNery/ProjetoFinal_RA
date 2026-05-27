import pygame as pg

caixa = None
fonte = None

def carregar():
    global caixa, fonte
    caixa = pg.image.load("Imagens/fala.png").convert_alpha()
    caixa = pg.transform.scale(caixa, (900, 180))

    fonte = pg.font.SysFont("arial", 28)

def desenhar(janela, fala, opcao_esquerda=None, opcao_direita=None):
    caixa_rect = caixa.get_rect()
    caixa_rect.midbottom = (800, 870)

    janela.blit(caixa, caixa_rect)

    cor_texto = (70, 40, 20)

    texto_img = fonte.render(fala, True, cor_texto)
    janela.blit(texto_img, (caixa_rect.x + 60, caixa_rect.y + 60))

    if opcao_esquerda and opcao_direita:
        fonte_opcao = pg.font.SysFont("arial", 24)

        texto_esquerda = fonte_opcao.render(opcao_esquerda, True, cor_texto)
        texto_direita = fonte_opcao.render(opcao_direita, True, cor_texto)

        janela.blit(texto_esquerda, (caixa_rect.x + 170, caixa_rect.y + 120))
        janela.blit(texto_direita, (caixa_rect.right - 260, caixa_rect.y + 120))
