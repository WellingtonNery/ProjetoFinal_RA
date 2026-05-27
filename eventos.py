import pygame as pg

spr1 = pg.image.load("Imagens/sprites/artesao.png")
spr2 = pg.image.load("Imagens/sprites/raiden.png")
spr3 = pg.image.load("Imagens/sprites/diabo.png")
spr4 = pg.image.load("Imagens/sprites/lobo.png")

sprites = {
    1: spr1,
    2: spr2,
    3: spr3,
    4: spr4
}

eventos = [
    {
        "sprite": 1,
        "falas": [
            "Meu senhor, os camponeses estão com fome.",
            "Eles pedem arroz dos estoques do castelo.",
            "O que deseja fazer?"
        ],

        "opcao_esquerda": "Ajudar",
        "opcao_direita": "Recusar",

        "efeito_esquerda": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_direita": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        }
    },

    {
        "sprite": 2,
        "falas": [
            "Um samurai pede dinheiro para proteger as estradas.",
            "Ele diz que bandidos estão atacando viajantes.",
            "Qual será sua ordem?"
        ],

        "opcao_esquerda": "Ajudar",
        "opcao_direita": "Recusar",

        "efeito_esquerda": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_direita": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        }
    },

    {
        "sprite": 3,
        "falas": [
            "Lucas inutil",
            "João lindo",
            "Diego"
        ],

        "opcao_esquerda": "Ajudar",
        "opcao_direita": "Recusar",

        "efeito_esquerda": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_direita": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        }
    },

    {
        "sprite": 4,
        "falas": [
            "O sapo não lava o pé",
            "Não lava porque não quer!",
            "Ele mora la na lagoa",
            "Não lava o pé porque não quer!"
        ],

        "opcao_esquerda": "Ajudar",
        "opcao_direita": "Recusar",

        "efeito_esquerda": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_direita": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        }
    }
]

tamanho = (315, 624)

def cortar_transparencia(surface):
    rect = surface.get_bounding_rect()
    return surface.subsurface(rect).copy()

for imagem in sprites:
    sprites[imagem] = cortar_transparencia(sprites[imagem])
    sprites[imagem] = pg.transform.scale(sprites[imagem], tamanho)

def imprimir_sprite(janela, sprite_rect, valor):
    x = sprite_rect.centerx // 2
    y = sprite_rect.centery

    sprite_imprimir = sprites[valor]

    janela.blit(sprite_imprimir, sprite_rect)