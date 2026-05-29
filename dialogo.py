import pygame as pg

caixa = None
escolha2 = None
escolha3 = None
escolha4 = None
fonte = None

def carregar():
    global caixa, fonte, escolha2, escolha3, escolha4
    caixa = pg.image.load("Imagens/fala.png").convert_alpha()
    caixa = pg.transform.scale(caixa, (900, 180))
    escolha2 = pg.image.load("Imagens/escolha2.png").convert_alpha()
    escolha2 = pg.transform.scale(escolha2, (escolha2.get_width() * 1.5, escolha2.get_height() * 1.5))
    escolha3 = pg.image.load("Imagens/escolha3.png").convert_alpha()
    escolha3 = pg.transform.scale(escolha3, (escolha3.get_width() * 1.5, escolha3.get_height() * 1.5))
    escolha4 = pg.image.load("Imagens/escolha4.png").convert_alpha()
    escolha4 = pg.transform.scale(escolha4, (escolha4.get_width() * 1.5, escolha4.get_height() * 1.5))

    fonte = pg.font.SysFont("arial", 28)

def desenhar(janela, fala, opcao_esquerda=None, opcao_direita=None):
    caixa_rect = caixa.get_rect()
    caixa_rect.midbottom = (800, 870)

    janela.blit(caixa, caixa_rect)

    cor_texto = (70, 40, 20)

    largura_max = caixa_rect.width - 120

    palavras = fala.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste_linha = linha_atual + palavra + " "

        if fonte.size(teste_linha)[0] <= largura_max:
            linha_atual = teste_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "

    linhas.append(linha_atual)

    y = caixa_rect.y + 50

    for linha in linhas:
        texto_img = fonte.render(linha, True, cor_texto)
        janela.blit(texto_img, (caixa_rect.x + 60, y))
        y += 35  

    if opcao_esquerda and opcao_direita:
        fonte_opcao = pg.font.SysFont("arial", 24)

        texto_esquerda = fonte_opcao.render(opcao_esquerda, True, cor_texto)
        texto_direita = fonte_opcao.render(opcao_direita, True, cor_texto)

        janela.blit(texto_esquerda, (caixa_rect.x + 170, caixa_rect.y + 150))
        janela.blit(texto_direita, (caixa_rect.right - 260, caixa_rect.y + 150))

def aparecer_escolha(janela, escolhas):
    cor_texto = (70, 40, 20)

    if len(escolhas) == 2:
        centro_tela = janela.get_rect().center

        imagem_rect = escolha2.get_rect()
        imagem_rect.center = centro_tela

        janela.blit(escolha2, imagem_rect)

        posicoes_texto = [
            (800, 340),
            (800, 550)
        ]

    elif len(escolhas) == 3:
        centro_tela = janela.get_rect().center

        imagem_rect = escolha3.get_rect()
        imagem_rect.center = centro_tela

        janela.blit(escolha3, imagem_rect)

        posicoes_texto = [
            (800, 285),
            (800, 460),
            (800, 640)
        ]

    elif len(escolhas) == 4:
        centro_tela = janela.get_rect().center

        imagem_rect = escolha4.get_rect()
        imagem_rect.center = centro_tela

        janela.blit(escolha4, imagem_rect)

        posicoes_texto = [
            (800, 225),
            (800, 370),
            (800, 520),
            (800, 670)
        ]

    else:
        return

    textos = list(escolhas.values())

    for i, texto in enumerate(textos):
        texto_img = fonte.render(texto, True, cor_texto)

        texto_rect = texto_img.get_rect()
        texto_rect.center = posicoes_texto[i]

        janela.blit(texto_img, texto_rect)


