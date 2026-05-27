import pygame as pg
import dias
import pontos
import eventos
import dialogo

def aplicar_efeito(ponto, efeito):
    for chave, valor in efeito.items():
        ponto[chave] += valor

pg.init()

fullscreen = False

ponto_inicial = None
rect_preview = None

LARGURA = 1600
ALTURA = 900

evento = 0
dia = 1
evento_atual = 0
fala_atual = 0

fade = pg.Surface((LARGURA, ALTURA))
fade.fill((0, 0, 0))

alpha = 0
apagando = False
esperando = False
tempo_preto = 0

esperando_npc = False
mostrar_npc = True
tempo_esperando = 5000
agora = 0
tempo_sem_npc = 0

rects_quadro = {
    "cima": pg.Rect(1398, 119, 92, 39),
    "meio": pg.Rect(1397, 177, 95, 39),
    "baixo": pg.Rect(1398, 236, 91, 40),
}

rects_pontos = {
    "Contentamento": 100,
    "Populacao": 0,
    "Dinheiro": 0
}

janela = pg.display.set_mode((LARGURA, ALTURA), pg.FULLSCREEN | pg.SCALED)
dialogo.carregar()

pg.display.set_caption('100 days of Shogun')

fundo_manha = pg.image.load('Imagens/imagem_fundo.png').convert()
fundo_manha = pg.transform.scale(fundo_manha, (LARGURA, ALTURA))
fundo_tarde = pg.image.load('Imagens/fundo_tarde.png').convert()
fundo_tarde = pg.transform.scale(fundo_tarde, (LARGURA, ALTURA))
fundo_noite = pg.image.load('Imagens/fundo_noite.png').convert()
fundo_noite = pg.transform.scale(fundo_noite, (LARGURA, ALTURA))
fundo = fundo_manha

rei = pg.image.load('Imagens/imagem_rei.png').convert_alpha()
largura_rei = rei.get_width()
altura_rei = rei.get_height()

calendario = pg.image.load('Imagens/Calendario/calendario.png').convert_alpha()
largura_cal = calendario.get_width() // 2
altura_cal = calendario.get_height() // 2
calendario = pg.transform.scale(calendario, (largura_cal, altura_cal))

quadro = pg.image.load('Imagens/quadro.png')
quadro_rect = quadro.get_rect()
quadro_rect.topright = (LARGURA + 40, -100)

cal_rect = calendario.get_rect()
cal_rect.topleft = (25, 25)

papel_rect = pg.Rect(86, 125, 153, 83)

personagem_rect = pg.Rect(38, 248, 396, 624)

x_trono = (1600 - largura_rei) // 2
y_trono = ((900 - altura_rei) // 2) - 100

loop = True

while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                loop = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and mostrar_npc and not apagando and not esperando:
                fala_atual += 1

                if fala_atual >= len(eventos.eventos[evento_atual]["falas"]):
                    mostrar_npc = False
                    esperando_npc = True

                    fala_atual = 0
                    evento += 1

                    tempo_sem_npc = pg.time.get_ticks()

    if esperando_npc:
        agora = pg.time.get_ticks()

        if agora - tempo_sem_npc >= tempo_esperando:
            mostrar_npc = True
            esperando_npc = False

            evento_atual += 1

    if apagando:
        alpha += 5

        if alpha >= 255:
            alpha = 255
            apagando = False
            esperando = True
            tempo_preto = pg.time.get_ticks()

    elif esperando:
        if pg.time.get_ticks() - tempo_preto >= 2000:
            esperando = False
            dia += 1
            evento = 0
            fundo = fundo_manha

    else:
        if alpha > 0:
            alpha -= 5

            if alpha < 0:
                alpha = 0

    if evento >= 3 and not apagando and not esperando:
        apagando = True

    elif evento == 2:
        fundo = fundo_noite

    elif evento == 1:
        fundo = fundo_tarde

    janela.blit(fundo, (0, 0))

    janela.blit(rei, (x_trono, y_trono))

    janela.blit(calendario, cal_rect)

    janela.blit(quadro, quadro_rect)

    dias.desenhar_dia_no_papel(janela, papel_rect, dia)

    pontos.atualizar_contentamento(janela, rects_quadro["cima"], rects_pontos["Contentamento"])
    pontos.atualizar(janela, rects_quadro["meio"], rects_pontos["Populacao"])
    pontos.atualizar(janela, rects_quadro["baixo"], rects_pontos["Dinheiro"])

    fade.set_alpha(alpha)
    janela.blit(fade, (0, 0))

    if mostrar_npc and not apagando and not esperando:
        eventos.imprimir_sprite(janela, personagem_rect, eventos.eventos[evento_atual]["sprite"])
        fala = eventos.eventos[evento_atual]["falas"][fala_atual]
        dialogo.desenhar(janela, fala)

    pg.display.update()