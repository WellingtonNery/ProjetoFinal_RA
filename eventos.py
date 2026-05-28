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

        "qtd_escolhas": {
            "opcao_primeira": "Ajudar",
            "opcao_segunda": "Recusar",
            "opcao_terceira": "Dar a bunda",
            "opcao_quarta": "Dar um beijo no Diego"
        },

        "efeito_primeira": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_segunda": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        },

        "efeito_terceira": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        },

        "efeito_quarta": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        },

        "falas_pos": {
            1: [
                "Euuu",
                "Diegooo"
            ],

            2: ["a"

            ],

            3: ["b"

            ],

            4: ["c"

            ]
        }
    },

    {
        "sprite": 2,

        "falas": [
            "Um samurai pede dinheiro para proteger as estradas.",
            "Ele diz que bandidos estão atacando viajantes.",
            "Qual será sua ordem?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Ajudar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_segunda": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        },

        "falas_pos": {
            1: [
                "Euuu",
                "Diegooo"
            ],

            2: ["a"

            ]
        }
    },

    {
        "sprite": 3,

        "falas": [
            "Lucas inutil",
            "João lindo",
            "Diego"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Ajudar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_segunda": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        },

        "falas_pos": {
            1: [
                "Euuu",
                "Diegooo"
            ],

            2: ["a"

            ]
        }
    },

    {
        "sprite": 4,

        "falas": [
            "O sapo não lava o pé.",
            "Não lava porque não quer!",
            "Ele mora lá na lagoa.",
            "Não lava o pé porque não quer!"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Ajudar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -30
        },

        "efeito_segunda": {
            "Contentamento": -15,
            "Populacao": -5,
            "Dinheiro": 20
        },

        "falas_pos": {
            1: [
                "Euuu",
                "Diegooo"
            ],

            2: ["a"

            ]
        }
    }
]

rect_limite = pg.Rect(17, 248, 343, 634)

def cortar_transparencia(surface):
    rect = surface.get_bounding_rect()
    return surface.subsurface(rect).copy()

for chave in sprites:
    sprites[chave] = cortar_transparencia(sprites[chave])

    largura = sprites[chave].get_width()
    altura = sprites[chave].get_height()

    escala_largura = rect_limite.width / largura
    escala_altura = rect_limite.height / altura

    escala = min(escala_largura, escala_altura)

    if escala < 1:
        nova_largura = int(largura * escala)
        nova_altura = int(altura * escala)

        sprites[chave] = pg.transform.scale(sprites[chave], (nova_largura, nova_altura))


def imprimir_sprite(janela, sprite_rect, valor):
    sprite_imprimir = sprites[valor]

    sprite_imprimir_rect = sprite_imprimir.get_rect()
    sprite_imprimir_rect.center = sprite_rect.center

    janela.blit(sprite_imprimir, sprite_imprimir_rect)