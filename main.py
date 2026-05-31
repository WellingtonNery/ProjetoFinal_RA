import pygame as pg
import dias
import pontos
import eventos
import dialogo
import random

pg.init()

LARGURA = 1600
ALTURA = 900

evento = 0
dia = 1
evento_atual = 0
fala_atual = 0

alpha = 0
apagando = False
esperando = False
tempo_preto = 0

esperando_npc = False
mostrar_npc = True
tempo_esperando = 5000
tempo_sem_npc = 0

mostrando_escolhas = False
tela_inicio = True

ultimas_falas = False
ultima_fala_atual = 0
ultimas_falas_escolha = 0

casou_com_pretendente = False
ajudou_viajante = False
aceitou_karasu = False
vendedor_escolha_boa = False
vendedor_escolha_ma = False

letras_visiveis = 0
tempo_ultima_letra = 0
velocidade_texto = 30
fala_anterior = ""

fade = pg.Surface((LARGURA, ALTURA))
fade.fill((0, 0, 0))

rects_quadro = {
    "cima": pg.Rect(1398, 119, 92, 39),
    "meio": pg.Rect(1397, 177, 95, 39),
    "baixo": pg.Rect(1398, 236, 91, 40),
}

rects_pontos = {
    "Contentamento": 50,
    "Populacao": 100,
    "Dinheiro": 75
}

rects_escolhas = {
    2: {
        "cima": pg.Rect(510, 263, 577, 156),
        "baixo": pg.Rect(512, 469, 578, 163)
    },

    3: {
        "cima": pg.Rect(535, 208, 529, 150),
        "meio": pg.Rect(536, 387, 526, 147),
        "baixo": pg.Rect(533, 564, 532, 150)
    },

    4: {
        "cima": pg.Rect(514, 161, 572, 127),
        "meio-cima": pg.Rect(511, 309, 574, 128),
        "meio-baixo": pg.Rect(515, 454, 571, 127),
        "baixo": pg.Rect(513, 605, 570, 131)
    }
}

janela = pg.display.set_mode((LARGURA, ALTURA), pg.FULLSCREEN | pg.SCALED)
pg.display.set_caption("100 days of Shogun")

dialogo.carregar()


def aplicar_efeito(efeito):
    for chave, valor in efeito.items():
        rects_pontos[chave] += valor
        rects_pontos["Contentamento"] = max(0, min(rects_pontos["Contentamento"], 100))
        rects_pontos["Dinheiro"] = max(0, rects_pontos["Dinheiro"])
        rects_pontos["Populacao"] = max(0, rects_pontos["Populacao"])


def finalizar_evento():
    global mostrar_npc, esperando_npc, mostrando_escolhas, ultimas_falas
    global fala_atual, evento, tempo_sem_npc, ultima_fala_atual, ultimas_falas_escolha

    mostrar_npc = False
    esperando_npc = True
    mostrando_escolhas = False
    ultimas_falas = False

    fala_atual = 0
    ultima_fala_atual = 0
    ultimas_falas_escolha = 0
    evento += 1

    eventos.eventos.pop(evento_atual)

    tempo_sem_npc = pg.time.get_ticks()


def efeito_digitando(texto):
    global letras_visiveis, tempo_ultima_letra, fala_anterior

    agora = pg.time.get_ticks()

    if texto != fala_anterior:
        fala_anterior = texto
        letras_visiveis = 0
        tempo_ultima_letra = agora

    if letras_visiveis < len(texto):
        if agora - tempo_ultima_letra >= velocidade_texto:
            letras_visiveis += 1
            tempo_ultima_letra = agora

    return texto[:letras_visiveis]


fundo_manha = pg.image.load("Imagens/imagem_fundo.png").convert()
fundo_manha = pg.transform.scale(fundo_manha, (LARGURA, ALTURA))

fundo_tarde = pg.image.load("Imagens/fundo_tarde.png").convert()
fundo_tarde = pg.transform.scale(fundo_tarde, (LARGURA, ALTURA))

fundo_noite = pg.image.load("Imagens/fundo_noite.png").convert()
fundo_noite = pg.transform.scale(fundo_noite, (LARGURA, ALTURA))

fundo = fundo_manha

fundo_inicio = pg.transform.smoothscale(fundo_manha, (160, 90))
fundo_inicio = pg.transform.smoothscale(fundo_inicio, (LARGURA, ALTURA))

escurecer_inicio = pg.Surface((LARGURA, ALTURA))
escurecer_inicio.fill((0, 0, 0))
escurecer_inicio.set_alpha(90)

logo = pg.image.load("Imagens/logo.png").convert_alpha()
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

rei = pg.image.load("Imagens/imagem_rei.png").convert_alpha()

largura_rei = rei.get_width()
altura_rei = rei.get_height()

x_rei = (LARGURA - largura_rei) // 2
y_rei = ((ALTURA - altura_rei) // 2) - 100

calendario = pg.image.load("Imagens/Calendario/calendario.png").convert_alpha()

largura_cal = calendario.get_width() // 2
altura_cal = calendario.get_height() // 2

calendario = pg.transform.scale(calendario, (largura_cal, altura_cal))

cal_rect = calendario.get_rect()
cal_rect.topleft = (25, 25)

papel_rect = pg.Rect(86, 125, 153, 83)

quadro = pg.image.load("Imagens/quadro.png").convert_alpha()
quadro_rect = quadro.get_rect()
quadro_rect.topright = (LARGURA + 40, -100)

personagem_rect = pg.Rect(17, 248, 343, 634)

sombra_opcoes = pg.Surface((LARGURA, ALTURA))
sombra_opcoes.fill((0, 0, 0))
sombra_opcoes.set_alpha(120)

if dia == 1 and evento == 0:
    evento_atual = 0

loop = True

while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                loop = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and tela_inicio:
                tela_inicio = False

            elif event.button == 1 and mostrar_npc and not apagando and not esperando:
                evento_info = eventos.eventos[evento_atual]

                if ultimas_falas:
                    falas_finais = evento_info["falas_pos"][ultimas_falas_escolha]
                    fala_final_texto = falas_finais[ultima_fala_atual]

                    if letras_visiveis < len(fala_final_texto):
                        letras_visiveis = len(fala_final_texto)

                    elif ultima_fala_atual < len(falas_finais) - 1:
                        ultima_fala_atual += 1

                    else:
                        finalizar_evento()

                elif mostrando_escolhas:
                    quantidade_escolhas = len(evento_info["qtd_escolhas"])

                    if quantidade_escolhas == 2:
                        if rects_escolhas[2]["cima"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_primeira"])
                            ultimas_falas_escolha = 1
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                            if evento_info["sprite"] == 13:
                                aceitou_karasu = True
                            if evento_info["sprite"] == 89:
                                vendedor_escolha_boa = True

                        elif rects_escolhas[2]["baixo"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_segunda"])
                            ultimas_falas_escolha = 2
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                            if evento_info["sprite"] == 89:
                                vendedor_escolha_ma = True

                    elif quantidade_escolhas == 3:
                        if rects_escolhas[3]["cima"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_primeira"])
                            ultimas_falas_escolha = 1
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                            if evento_info["sprite"] == 85:
                                casou_com_pretendente = True
                            if evento_info["sprite"] == 12:
                                ajudou_viajante = True

                        elif rects_escolhas[3]["meio"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_segunda"])
                            ultimas_falas_escolha = 2
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                        elif rects_escolhas[3]["baixo"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_terceira"])
                            ultimas_falas_escolha = 3
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                    elif quantidade_escolhas == 4:
                        if rects_escolhas[4]["cima"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_primeira"])
                            ultimas_falas_escolha = 1
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                        elif rects_escolhas[4]["meio-cima"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_segunda"])
                            ultimas_falas_escolha = 2
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                        elif rects_escolhas[4]["meio-baixo"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_terceira"])
                            ultimas_falas_escolha = 3
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                        elif rects_escolhas[4]["baixo"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_quarta"])
                            ultimas_falas_escolha = 4
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                else:
                    fala_texto = evento_info["falas"][fala_atual]

                    if letras_visiveis < len(fala_texto):
                        letras_visiveis = len(fala_texto)

                    elif fala_atual < len(evento_info["falas"]) - 1:
                        fala_atual += 1

                    else:
                        mostrando_escolhas = True

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

            eventos_disponiveis = []

            for indice, evento_info in enumerate(eventos.eventos):
                if evento_info.get("dia_minimo", 1) <= dia:
                    if evento_info["sprite"] == 86 and not casou_com_pretendente:
                        continue

                    if evento_info["sprite"] == 87 and not ajudou_viajante:
                        continue

                    if evento_info["sprite"] == 14 and not aceitou_karasu:
                        continue

                    if evento_info["sprite"] == 90 and not vendedor_escolha_boa:
                        continue

                    if evento_info["sprite"] == 91 and not vendedor_escolha_ma:
                        continue
                    eventos_disponiveis.append(indice)

            evento_atual = random.choice(eventos_disponiveis)

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

    else:
        fundo = fundo_manha

    janela.blit(fundo, (0, 0))
    janela.blit(rei, (x_rei, y_rei))

    janela.blit(calendario, cal_rect)
    janela.blit(quadro, quadro_rect)

    dias.desenhar_dia_no_papel(janela, papel_rect, dia)

    pontos.atualizar_contentamento(
        janela,
        rects_quadro["cima"],
        rects_pontos["Contentamento"]
    )

    pontos.atualizar(
        janela,
        rects_quadro["meio"],
        rects_pontos["Populacao"]
    )

    pontos.atualizar(
        janela,
        rects_quadro["baixo"],
        rects_pontos["Dinheiro"]
    )

    if mostrar_npc and not apagando and not esperando:
        evento_info = eventos.eventos[evento_atual]

        eventos.imprimir_sprite(
            janela,
            personagem_rect,
            evento_info["sprite"]
        )

        if mostrando_escolhas:
            janela.blit(sombra_opcoes, (0, 0))
            dialogo.aparecer_escolha(janela, evento_info["qtd_escolhas"])

        elif ultimas_falas:
            fala_ultima = evento_info["falas_pos"][ultimas_falas_escolha][ultima_fala_atual]
            fala_digitada = efeito_digitando(fala_ultima)
            dialogo.desenhar(janela, fala_digitada)

        else:
            fala = evento_info["falas"][fala_atual]
            fala_digitada = efeito_digitando(fala)
            dialogo.desenhar(janela, fala_digitada)

    fade.set_alpha(alpha)
    janela.blit(fade, (0, 0))

    pg.display.update()

pg.quit()
