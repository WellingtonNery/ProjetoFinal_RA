import pygame as pg

spr1 = pg.image.load("Imagens/sprites/mensageiro.png")
spr2 = pg.image.load("Imagens/sprites/raiden.png")
spr3 = pg.image.load("Imagens/sprites/diabo.png")
spr4 = pg.image.load("Imagens/sprites/lobo.png")
spr5 = pg.image.load("Imagens/sprites/sapo.png")
spr6 = pg.image.load("Imagens/sprites/construtor.png")
spr7 = pg.image.load("Imagens/sprites/cego.png")
spr8 = pg.image.load("Imagens/sprites/ninja.png")
spr9 = pg.image.load("Imagens/sprites/vendedor.png")
spr10 = pg.image.load("Imagens/sprites/onmyoji.png")

sprites = {
    1: spr1,
    2: spr2,
    3: spr3,
    4: spr4,
    5: spr5,
    6: spr6,
    7: spr7,
    8: spr8,
    9: spr9,
    10: spr10
}

eventos = [
    {
        "sprite": 1,

        "falas": [
            "Olá meu senhor, venho por meio desta  carta lhe informar da situação atual do feudo.",
            "O povo tem passado por dificuldades, a fome tem se alastrado e a população tem diminuído.",
            "Precisamos de sua ajuda para superar essa crise, caso contrário, temo que o feudo possa entrar em colapso.",
            "Sua agenda está cheia durante os próximos 100 dias, até lá você tomará as decisões corretas para que a cidade prospere e cheguemos a era de ouro."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Começar a jornada.",
            "opcao_segunda": "Recusar a jornada.",
        },

        "efeito_primeira": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": -0
        },

        "efeito_segunda": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0
        },


        "falas_pos": {
            1: [
                "Muito bem, senhor. Tenho certeza de que você tomará as decisões corretas para o bem do feudo. Vamos começar!",
            ],
        }
    },

    {
        "sprite": 2,

        "falas": [
            "Olá mero mortal, sou Raiden, a shogun de Inazuma. Venho até você para pedir uma aliança contra Tsaritsa.",
            "Caso recuse... não irá gostar de me provocar.",
            "Qual será sua escolha mortal?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Ajudar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": -15,
            "Populacao": 10,
            "Dinheiro": 50
        },

        "efeito_segunda": {
            "Contentamento": 10,
            "Populacao": -15,
            "Dinheiro": -20
        },

        "falas_pos": {
            1: [
                "Agradeço pela ajuda mortal, juntos derrotaremos Tsaritsa e traremos a paz para Inazuma, vou deixar alguns de meus guardas e um pouco de dinheiro para você.",
                "(-15 de Contentamento, +10 de População, +50 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere ficar do lado de Tsaritsa, não é? Bem, isso é uma escolha errada, AGORA É GUERRA! ",
                "(+10 de Contentamento, -15 de População, -20 de Dinheiro)"

            ]
        }
    },

    {
        "sprite": 3,

        "falas": [
            "Olá humano, eu vim oferecer um pacto... eu irei te dar riquezas e prosperidade, porém irei levar grande parte de almas comigo... ",
            "Você aceita?",
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": -20,
            "Populacao": -40,
            "Dinheiro": 500
        },

        "efeito_segunda": {
            "Contentamento": 20,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Adeus humano, foi um prazer fazer negócios com você, espero que aproveite suas riquezas, até a próxima...",
                "(-20 de Contentamento, -40 de População, +500 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere manter sua alma intacta, não é? Bem, isso é uma escolha sábia, até a próxima... ",
                "(+20 de Contentamento, +0 de População, +0 de Dinheiro)"

            ]
        }
    },

    {
        "sprite": 4,

        "falas": [
            "Olá meu senhor, sou uma yokai que vive na floresta próxima, venho até você para pedir ajuda, a floresta tem sido destruída por madeireiros e caçadores.",
            "Nela existem muitos seres vivos que dependem da floresta para sobreviver. Por favor, me ajude a proteger a floresta e seus habitantes...",
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Ajudar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": -5,
            "Populacao": 10,
            "Dinheiro": -20
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 0,
            "Dinheiro": 20
        },

        "falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor. A floresta e seus habitantes ficarão muito gratos por sua decisão, espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +10 de População, -20 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +0 de População, +20 de Dinheiro)"

            ]
        }
    },

    {
        "sprite": 5,

        "falas": [
            "Meu senhor, sou Gorobei, o sapo monge.",
            "Venho até você informar que os sapos do reino não estão lavando seus pés.",
            "Vossa excelência, por favor o senhor conseguiria construir algumas fontes termais para os sapos se banharem?"
        ],

        "qtd_escolhas":  {
            "opcao_primeira": "Construir fontes termais a todos",
            "opcao_segunda": "Construir um lago específico para os sapos",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 10,
            "Dinheiro": -50
        },

        "efeito_segunda": {
            "Contentamento": 0,
            "Populacao": 10,
            "Dinheiro": -20
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor. A floresta e seus habitantes ficarão muito gratos por sua decisão, espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +10 de População, -20 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +0 de População, +20 de Dinheiro)"

            ],

            3: [
                "Entendo. Você optou por recusar a construção de fontes. Espero que reconsidere no futuro.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 6,

        "falas": [
            "Olá meu senhor, sou um construtor e venho até você para oferecer meus serviços. Posso construir casas, pontes, estradas e muito mais. Se precisar de algo, é só me chamar.",
            "Posso começar a trabalhar imediatamente, basta me dizer o que você precisa."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Construir casas para os moradores",
            "opcao_segunda": "Construir uma ponte para facilitar o comércio",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 20,
            "Dinheiro": -100
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 10,
            "Dinheiro": -50
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor. A floresta e seus habitantes ficarão muito gratos por sua decisão, espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +10 de População, -20 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +0 de População, +20 de Dinheiro)"

            ],

            3: [
                "Entendo. Você optou por recusar a construção de fontes. Espero que reconsidere no futuro.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 7,

        "falas": [
            "Olá meu senhor, sou um monge e venho até você para pedir ajuda. A cidade está sendo atacada por demônios e preciso de seu apoio para enfrentar essa ameaça.",
            "Você aceitaria me ajudar a proteger a cidade dos demônios?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar a missão",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 20,
            "Dinheiro": -100
        },

        "efeito_segunda": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor. A floresta e seus habitantes ficarão muito gratos por sua decisão, espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +10 de População, -20 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +0 de População, +20 de Dinheiro)"

            ],

            3: [
                "Entendo. Você optou por recusar a construção de fontes. Espero que reconsidere no futuro.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 8,

        "falas": [
            "Olá meu senhor, sou um alquimista e venho até você para oferecer meus serviços. Posso criar poções e elixires que podem ajudar a cidade.",
            "Você precisa de alguma coisa específica?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Comprar poções de cura",
            "opcao_segunda": "Comprar poções de força",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 10,
            "Dinheiro": -50
        },

        "efeito_segunda": {
            "Contentamento": 10,
            "Populacao": 20,
            "Dinheiro": -100
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },"falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor. A floresta e seus habitantes ficarão muito gratos por sua decisão, espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +10 de População, -20 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +0 de População, +20 de Dinheiro)"

            ],

            3: [
                "Entendo. Você optou por recusar a construção de fontes. Espero que reconsidere no futuro.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 9,
        "falas": [
            "Olá meu senhor, sou um mercador e venho até você para oferecer meus serviços. Tenho uma ampla seleção de mercadorias para venda.",
            "Você está interessado em algo específico?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Comprar armas",
            "opcao_segunda": "Comprar armaduras",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 10,
            "Dinheiro": -50
        },

        "efeito_segunda": {
            "Contentamento": 10,
            "Populacao": 20,
            "Dinheiro": -100
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor. A floresta e seus habitantes ficarão muito gratos por sua decisão, espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +10 de População, -20 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +0 de População, +20 de Dinheiro)"

            ],

            3: [
                "Entendo. Você optou por recusar a construção de fontes. Espero que reconsidere no futuro.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 10,

        "falas": [
            "Olá meu senhor, sou um onmyoji e venho até você para oferecer meus serviços. Posso exorcizar espíritos malignos e proteger a cidade de ameaças sobrenaturais.",
            "Você precisa de alguma ajuda específica?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Contratar para exorcizar um espírito maligno",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 20,
            "Dinheiro": -100
        },
        "efeito_segunda": {
                "Contentamento": -5,
                "Populacao": 0,
                "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor. A floresta e seus habitantes ficarão muito gratos por sua decisão, espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +10 de População, -20 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +0 de População, +20 de Dinheiro)"

            ],

            3: [
                "Entendo. Você optou por recusar a construção de fontes. Espero que reconsidere no futuro.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
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