import pygame as pg
import dias
import pontos
import eventos
import dialogo
import random

pg.init()
pg.mixer.init()
pg.mixer.set_num_channels(16)

LARGURA = 1600
ALTURA = 900

evento = 0
dia = 1
evento_atual = 0
fala_atual = 0
DIA_MAXIMO = 100
final_ativo = False
final_tipo = None
final_imagem = None

resultado_final = None
texto_final = None
prestigio_final = None
final = False

prestigio = 0

FINAIS = {
    "populacao": "Imagens/Finais/final_populacao.png",
    "dinheiro": "Imagens/Finais/final_dinheiro.png",
    "contentamento": "Imagens/Finais/final_contentamento.png",
    "dia_100": "Imagens/Finais/final_dia_100.png",
    "era_de_ouro": "Imagens/Finais/final_era_de_ouro.png",
}

alpha = 0
apagando = False
esperando = False
tempo_preto = 0

esperando_npc = False
mostrar_npc = True
TEMPO_ESPERANDO = 2500
tempo_sem_npc = 0

mostrando_escolhas = False
tela_inicio = True

ultimas_falas = False
ultima_fala_atual = 0
ultimas_falas_escolha = 0

casou_com_pretendente = False
ajudou_viajante = False
aceitou_karasu = False
tesouro_karasu = False
vendedor_escolha_boa = False
vendedor_escolha_ma = False
guerra1 = False
guerra2 = False
guerra3 = False
luta_feitceiros1 = False
luta_feitceiros2 = False
festival = False
trabalho = False
reidemonio = False
entregar = False
esconder = False
vo_karasu = False
kenji = False

letras_visiveis = 0
tempo_ultima_letra = 0
VELOCIDADE_TEXTO = 30
fala_anterior = ""

fade = pg.Surface((LARGURA, ALTURA))
fade.fill((0, 0, 0))

som = None
sons_fala = [
    pg.mixer.Sound("Audios/vozes1.mp3"),
    pg.mixer.Sound("Audios/vozes2.mp3"),
    pg.mixer.Sound("Audios/vozes3.mp3"),
    pg.mixer.Sound("Audios/vozes4.mp3"),
]
som_andando = pg.mixer.Sound("Audios/som-andando.mp3")
canal_passos = pg.mixer.Channel(0)
canal_fala = pg.mixer.Channel(1)
final_tocar = None
musica_final_tocando = False

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
    global prestigio

    for chave, valor in efeito.items():
        rects_pontos[chave] += valor
        rects_pontos["Contentamento"] = max(0, min(rects_pontos["Contentamento"], 100))
        rects_pontos["Dinheiro"] = max(0, rects_pontos["Dinheiro"])
        rects_pontos["Populacao"] = max(0, rects_pontos["Populacao"])
    prestigio = calcular_prestigio()


def esta_na_era_de_ouro():
    return prestigio >= 300


def carregar_final(tipo):
    caminho = FINAIS[tipo]
    imagem = pg.image.load(caminho).convert_alpha()
    return pg.transform.scale(imagem, (LARGURA, ALTURA))


def verificar_final():
    global final_ativo, final_tipo, final_imagem
    global mostrar_npc, esperando_npc, mostrando_escolhas, apagando, esperando
    global resultado_final, texto_final, final, final_tocar

    if final_ativo:
        return

    if rects_pontos["Populacao"] <= 0:
        final_tipo = "populacao"
        resultado_final = "GAME OVER!\nFinal: Terra Sem Vozes"
        texto_final = "O último sino ecoou, mas não há mais ninguém para ouvi-lo."
        final = True
        final_tocar = False
    elif rects_pontos["Dinheiro"] <= 0:
        final_tipo = "dinheiro"
        resultado_final = "Game over!\nFinal: Cofres Vazios"
        texto_final = "Nem mesmo um shogun governa com promessas quebradas."
        final = True
        final_tocar = False
    elif rects_pontos["Contentamento"] <= 0:
        final_tipo = "contentamento"
        resultado_final = "Game over!\nFinal: Rebelião"
        texto_final = "As tochas iluminaram a noite em que Takayama se levantou contra você."
        final = True
        final_tocar = False
    elif dia >= DIA_MAXIMO:
        if esta_na_era_de_ouro():
            final_tipo = "era_de_ouro"
            resultado_final = "GAME WON!\nFinal: A Era de Ouro"
            texto_final = "A história lembrará este reinado como o amanhecer de uma era dourada."
            final = True
            final_tocar = True
        else:
            final_tipo = "dia_100"
            resultado_final = "GAME WON!\nFinal: O Trono Permanece"
            texto_final = "Entre perdas e vitórias, Takayama chegou ao amanhã. Mas a hora de baixar a guarda ainda não chegou!"
            final = True
            final_tocar = True
    else:
        return

    final_ativo = True
    final_imagem = carregar_final(final_tipo)

    canal_passos.stop()
    canal_fala.stop()

    mostrar_npc = False
    esperando_npc = False
    mostrando_escolhas = False
    apagando = False
    esperando = False


def desenhar_final():
    janela.blit(final_imagem, (0, 0))


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

    if evento < 3:
        tocar_som_passos()


def efeito_digitando(texto):
    global letras_visiveis, tempo_ultima_letra, fala_anterior

    agora = pg.time.get_ticks()

    if texto != fala_anterior:
        fala_anterior = texto
        letras_visiveis = 0
        tempo_ultima_letra = agora

    if letras_visiveis < len(texto):
        if agora - tempo_ultima_letra >= VELOCIDADE_TEXTO:
            letras_visiveis += 1
            tempo_ultima_letra = agora

            if letras_visiveis % 4 == 0:
                som = random.choice(sons_fala)
                som.set_volume(0.1)
                if not canal_fala.get_busy():
                    canal_fala.play(som)

    return texto[:letras_visiveis]


def calcular_prestigio():
    pesos = {
        "Contentamento": 8,
        "Populacao": 10,
        "Dinheiro": 1
    }

    soma_pesos = pesos["Contentamento"] + pesos["Populacao"] + pesos["Dinheiro"]

    prestigioCalc = (
                        rects_pontos["Contentamento"] * pesos["Contentamento"] +
                        rects_pontos["Populacao"] * pesos["Populacao"] +
                        rects_pontos["Dinheiro"] * pesos["Dinheiro"]
                    ) / soma_pesos

    return prestigioCalc

def tocar_som_passos():
    if not esperando and not apagando:
        if not canal_passos.get_busy():
            canal_passos.play(som_andando, loops=-1)

prestigio = calcular_prestigio()

pg.mixer.music.load("Audios/som_fundo.mp3")
pg.mixer.music.set_volume(0.025)
pg.mixer.music.play(-1)

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

LARGURA_LOGO = 950
altura_logo = int(logo.get_height() * (LARGURA_LOGO / logo.get_width()))

logo = pg.transform.smoothscale(logo, (LARGURA_LOGO, altura_logo))
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

quadro_alto = pg.image.load("Imagens/quadro.png").convert_alpha()
quadro_medio = pg.image.load("Imagens/quadro_medio.png").convert_alpha()
quadro_baixo = pg.image.load("Imagens/quadro_baixo.png").convert_alpha()

quadro = quadro_alto
quadro_rect = quadro.get_rect()
quadro_rect.topright = (LARGURA + 40, -100)

personagem_rect = pg.Rect(17, 248, 343, 634)

prestigio_madeira = pg.image.load("Imagens/madeira.png").convert_alpha()
prestigio_madeira = pg.transform.smoothscale(prestigio_madeira, (96, 96))

prestigio_bronze = pg.image.load("Imagens/bronze.png").convert_alpha()
prestigio_bronze = pg.transform.smoothscale(prestigio_bronze, (96, 96))

prestigio_prata = pg.image.load("Imagens/prata.png").convert_alpha()
prestigio_prata = pg.transform.smoothscale(prestigio_prata, (96, 96))

prestigio_ouro = pg.image.load("Imagens/ouro.png").convert_alpha()
prestigio_ouro = pg.transform.smoothscale(prestigio_ouro, (96, 96))

prestigio_atual = prestigio_madeira

rect_prestigio = prestigio_atual.get_rect()
area_visivel = quadro.get_bounding_rect()

rect_prestigio.center = (
    quadro_rect.left + area_visivel.left + 10,
    quadro_rect.top + area_visivel.bottom - 10
)

sombra_opcoes = pg.Surface((LARGURA, ALTURA))
sombra_opcoes.fill((0, 0, 0))
sombra_opcoes.set_alpha(120)

if dia == 1 and evento == 0:
    evento_atual = 0

if dia == 67 and evento == 0:
    evento_atual = 67

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
                                vo_karasu = True
                            if evento_info["sprite"] == 14:
                                tesouro_karasu = True
                            if evento_info["sprite"] == 18:
                                guerra1 = True
                            if evento_info["sprite"] == 77:
                                entregar = True
                            if evento_info["sprite"] == 80:
                                kenji = True
                            if evento_info["sprite"] == 89:
                                vendedor_escolha_boa = True

                        elif rects_escolhas[2]["baixo"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_segunda"])
                            ultimas_falas_escolha = 2
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                            if evento_info["sprite"] == 14:
                                tesouro_karasu = True
                                vo_karasu = True
                            if evento_info["sprite"] == 18:
                                guerra1 = True
                            if evento_info["sprite"] == 77:
                                esconder = True
                            if evento_info["sprite"] == 80:
                                kenji = True
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

                            if evento_info["sprite"] == 36:
                                guerra2 = True
                            if evento_info["sprite"] == 35:
                                luta_feitceiros1 = True
                            if evento_info["sprite"] == 37:
                                luta_feitceiros2 = True
                            if evento_info["sprite"] == 38:
                                guerra3 = True
                            if evento_info["sprite"] == 44:
                                festival = True
                            if evento_info["sprite"] == 48:
                                trabalho = True
                            if evento_info["sprite"] == 51:
                                reidemonio = True

                        elif rects_escolhas[4]["meio-cima"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_segunda"])
                            ultimas_falas_escolha = 2
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                            if evento_info["sprite"] == 36:
                                guerra2 = True
                            if evento_info["sprite"] == 35:
                                luta_feitceiros1 = True
                            if evento_info["sprite"] == 37:
                                luta_feitceiros2 = True
                            if evento_info["sprite"] == 38:
                                guerra3 = True
                            if evento_info["sprite"] == 44:
                                festival = True
                            if evento_info["sprite"] == 48:
                                trabalho = True
                            if evento_info["sprite"] == 51:
                                reidemonio = True

                        elif rects_escolhas[4]["meio-baixo"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_terceira"])
                            ultimas_falas_escolha = 3
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                            if evento_info["sprite"] == 36:
                                guerra2 = True
                            if evento_info["sprite"] == 35:
                                luta_feitceiros1 = True
                            if evento_info["sprite"] == 37:
                                luta_feitceiros2 = True
                            if evento_info["sprite"] == 38:
                                guerra3 = True
                            if evento_info["sprite"] == 44:
                                festival = True
                            if evento_info["sprite"] == 51:
                                reidemonio = True


                        elif rects_escolhas[4]["baixo"].collidepoint(event.pos):
                            aplicar_efeito(evento_info["efeito_quarta"])
                            ultimas_falas_escolha = 4
                            ultimas_falas = True
                            mostrando_escolhas = False
                            ultima_fala_atual = 0

                            if evento_info["sprite"] == 36:
                                guerra2 = True
                            if evento_info["sprite"] == 35:
                                luta_feitceiros1 = True
                            if evento_info["sprite"] == 37:
                                luta_feitceiros2 = True
                            if evento_info["sprite"] == 38:
                                guerra3 = True
                            if evento_info["sprite"] == 44:
                                festival = True
                            if evento_info["sprite"] == 48:
                                trabalho = True
                            if evento_info["sprite"] == 51:
                                reidemonio = True

                else:
                    fala_texto = evento_info["falas"][fala_atual]

                    if letras_visiveis < len(fala_texto):
                        letras_visiveis = len(fala_texto)

                    elif fala_atual < len(evento_info["falas"]) - 1:
                        fala_atual += 1


                    else:
                        mostrando_escolhas = True

    if rects_pontos["Contentamento"] >= 70:
        quadro = quadro_alto
    elif 70 > rects_pontos["Contentamento"] >= 30:
        quadro = quadro_medio
    else:
        quadro = quadro_baixo

    if prestigio >= 300:
        prestigio_atual = prestigio_ouro
        prestigio_final = "Ouro"
    elif prestigio >= 200:
        prestigio_atual = prestigio_prata
        prestigio_final = "Prata"
    elif prestigio >= 100:
        prestigio_atual = prestigio_bronze
        prestigio_final = "Bronze"
    else:
        prestigio_atual = prestigio_madeira
        prestigio_final = "Madeira"

    if tela_inicio:
        janela.blit(fundo_inicio, (0, 0))
        janela.blit(escurecer_inicio, (0, 0))
        janela.blit(logo, logo_rect)
        janela.blit(texto_inicio, texto_inicio_rect)
        pg.display.update()
        continue

    if final_ativo:
        desenhar_final()

        if not musica_final_tocando:
            if not final_tocar:
                pg.mixer.music.load("Audios/musica-triste.wav")
            else:
                pg.mixer.music.load("Audios/final-bom.wav")

            pg.mixer.music.set_volume(0.3)
            pg.mixer.music.play(-1)
            musica_final_tocando = True

        pg.display.update()
        continue

    if esperando_npc:
        agora = pg.time.get_ticks()

        if agora - tempo_sem_npc >= TEMPO_ESPERANDO:
            mostrar_npc = True
            esperando_npc = False

            canal_passos.stop()

            eventos_disponiveis = []

            for indice, evento_info in enumerate(eventos.eventos):
                if evento_info.get("dia_minimo", 1) <= dia:
                    if evento_info["sprite"] == 86 and not casou_com_pretendente:
                        continue

                    if evento_info["sprite"] == 87 and not ajudou_viajante:
                        continue

                    if evento_info["sprite"] == 14 and not aceitou_karasu:
                        continue

                    if evento_info["sprite"] == 33 and not tesouro_karasu:
                        continue

                    if evento_info["sprite"] == 36 and not guerra1:
                        continue

                    if evento_info["sprite"] == 37 and not luta_feitceiros1:
                        continue

                    if evento_info["sprite"] == 38 and not guerra2:
                        continue

                    if evento_info["sprite"] == 39 and not luta_feitceiros2:
                        continue

                    if evento_info["sprite"] == 40 and not guerra3:
                        continue

                    if evento_info["sprite"] == 49 and not festival:
                        continue

                    if evento_info["sprite"] == 56 and not trabalho:
                        continue

                    if evento_info["sprite"] == 77 and not reidemonio:
                        continue

                    if evento_info["sprite"] == 81 and not esconder:
                        continue

                    if evento_info["sprite"] == 82 and not entregar:
                        continue

                    if evento_info["sprite"] == 83 and not kenji:
                        continue

                    if evento_info["sprite"] == 84 and not vo_karasu:
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
            verificar_final()

    else:
        if alpha > 0:
            alpha -= 5

            if alpha < 0:
                alpha = 0

    if evento >= 3 and not apagando and not esperando:
        canal_passos.stop()
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

    janela.blit(prestigio_atual, rect_prestigio)

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

if final:
    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{resultado_final}\n")
        arquivo.write(f"{texto_final}\n")
        arquivo.write(f"Nível de prestígio: {prestigio_final}\n")
        arquivo.write(f"Contentamento final: {rects_pontos['Contentamento']}\n")
        arquivo.write(f"População final: {rects_pontos['Populacao']}\n")
        arquivo.write(f"Dinheiro final: {rects_pontos['Dinheiro']}\n")
        arquivo.write("\n")
else:
    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Jogo fechado por erro!\n")
