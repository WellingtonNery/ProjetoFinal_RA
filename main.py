import pygame as pg
import dias
import pontos
import eventos
import dialogo

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
tela_inicio = True

rects_quadro = {
    "cima": pg.Rect(1398, 119, 92, 39),
    "meio": pg.Rect(1397, 177, 95, 39),
    "baixo": pg.Rect(1398, 236, 91, 40),
}

rects_pontos = {
    "Contentamento": 100,
    "Populacao": 50,
    "Dinheiro": 75
}

rect_opcao_esquerda = pg.Rect(340, 760, 300, 90)
rect_opcao_direita = pg.Rect(960, 760, 300, 90)

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

fundo_inicio = pg.transform.smoothscale(fundo_manha, (160, 90))
fundo_inicio = pg.transform.smoothscale(fundo_inicio, (LARGURA, ALTURA))
escurecer_inicio = pg.Surface((LARGURA, ALTURA))
escurecer_inicio.fill((0, 0, 0))
escurecer_inicio.set_alpha(90)

logo = pg.image.load('Imagens/logo.png').convert_alpha()
logo.set_colorkey((0, 0, 0))
largura_logo = 950
altura_logo = int(logo.get_height() * (largura_logo / logo.get_width()))
logo = pg.transform.smoothscale(logo, (largura_logo, altura_logo))
logo_rect = logo.get_rect()
logo_rect.center = (LARGURA // 2, ALTURA // 2 - 70)

fonte_inicio = pg.font.SysFont("arial", 34)
texto_inicio = fonte_inicio.render("toque para começar", True, (245, 226, 177))
texto_inicio_rect = texto_inicio.get_rect()
texto_inicio_rect.center = (LARGURA // 2, ALTURA - 135)

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

def aplicar_efeito(efeito):
    for chave, valor in efeito.items():
        rects_pontos[chave] += valor

while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                loop = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and tela_inicio:
                tela_inicio = False

            elif event.button == 1 and mostrar_npc and not apagando and not esperando:
                evento_info = eventos.eventos[evento_atual]
                ultima_fala = fala_atual == len(evento_info["falas"]) - 1

                if ultima_fala and rect_opcao_esquerda.collidepoint(event.pos):
                    aplicar_efeito(evento_info["efeito_esquerda"])
                    mostrar_npc = False
                    esperando_npc = True

                    fala_atual = 0
                    evento += 1

                    tempo_sem_npc = pg.time.get_ticks()

                elif ultima_fala and rect_opcao_direita.collidepoint(event.pos):
                    aplicar_efeito(evento_info["efeito_direita"])
                    mostrar_npc = False
                    esperando_npc = True

                    fala_atual = 0
                    evento += 1

                    tempo_sem_npc = pg.time.get_ticks()

                elif not ultima_fala:
                    fala_atual += 1

    if tela_inicio:
        janela.blit(fundo_inicio, (0, 0))
        janela.blit(escurecer_inicio, (0, 0))
        janela.blit(logo, logo_rect)
        janela.blit(texto_inicio, texto_inicio_rect)
        pg.display.update()
        continue

    if esperando_npc:
        agora = pg.time.get_ticks()

        if agora - tempo_sem_npc >= tempo_esperando:
            mostrar_npc = True
            esperando_npc = False

            evento_atual += 1
            if evento_atual >= len(eventos.eventos):
                evento_atual = 0

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
        evento_info = eventos.eventos[evento_atual]

        eventos.imprimir_sprite(janela, personagem_rect, evento_info["sprite"])
        fala = evento_info["falas"][fala_atual]

        if fala_atual == len(evento_info["falas"]) - 1:
            dialogo.desenhar(janela, fala, evento_info["opcao_esquerda"], evento_info["opcao_direita"])
        else:
            dialogo.desenhar(janela, fala)

    pg.display.update()
