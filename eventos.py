import pygame as pg

spr1 = pg.image.load("Imagens/sprites/mensageiro.png")
spr2 = pg.image.load("Imagens/sprites/raiden.png")
spr3 = pg.image.load("Imagens/sprites/diabo.png")
spr4 = pg.image.load("Imagens/sprites/yokai.png")
spr5 = pg.image.load("Imagens/sprites/sapo.png")
spr6 = pg.image.load("Imagens/sprites/construtor.png")
spr7 = pg.image.load("Imagens/sprites/monge.png")
spr8 = pg.image.load("Imagens/sprites/ninja.png")
spr9 = pg.image.load("Imagens/sprites/vendedor.png")
spr10 = pg.image.load("Imagens/sprites/onmyoji.png")
spr11 = pg.image.load("Imagens/sprites/alquimista.png")
spr12 = pg.image.load("Imagens/sprites/viajante tempo.png")

spr13 = spr1
spr71 = spr1
spr85 = spr1
spr110 = spr1
spr157 = spr1
spr189 = spr1
spr229 = spr1
spr230 = spr1

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
    10: spr10,
    11: spr11,
    12: spr12,

    #JOAO
    13: spr13,
    71: spr71,

    #WELLINGTON
    85: spr85,
    110: spr110,

    #DIEGO
    157: spr157,
    189: spr189,

    #LUCAS
    229: spr229,
    230: spr230

}

eventos = [
    {
        "sprite": 1,
        "dia_minimo": 1,

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
            "Dinheiro": 0
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
        "dia_minimo": 1,

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
                "Agradeço pela ajuda mortal, juntos conquistaremos a eternidade e traremos a paz para Inazuma",
                "Irei deixar alguns de meus suditos e um pouco de dinheiro para você!",
                "(-15 de Contentamento, +10 de População, +50 de Dinheiro)"
            ],

            2: ["MUSOU",
                "NO",
                "HITOTACHI",
                "(+10 de Contentamento, -15 de População, -20 de Dinheiro)"

            ]
        }
    },

    {
        "sprite": 3,
        "dia_minimo": 2,

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
        "dia_minimo": 1,

        "falas": [
            "Olá meu senhor, sou uma yokai que vive na floresta próxima",
            "Venho aqui pedir sua ajuda, a floresta tem sido destruída por madeireiros e caçadores!",
            "Nela existem muitos seres vivos que dependem da floresta para sobreviver.",
            "Por favor, me ajude a proteger a floresta e seus habitantes",
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
        "dia_minimo": 2,

        "falas": [
            "Olá senhor, sou Gorobei, o sapo monge.",
            "Os sapos de nosso reino não estão lavando seus pés.",
            "Eles precisam urgentemente da construção de novas fontes termais para se banharem",
            "Posso contar com a sua ajuda?"
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
                "Serei eternamente grato à voce senhor.",
                "Se precisar da ajuda dos sapos não hesite em pedir.",
                "Glória à Takayama!",
                "(+5 de Contentamento, +10 de População, -50 de Dinheiro)"
            ],

            2: ["Ah, obrigado senhor",
                "(+0 de Contentamento, +10 de População, -20 de Dinheiro)"

            ],

            3: [
                "Não acredito que achei que você fosse diferente dos outros tiranos... ",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 6,
        "dia_minimo": 3,

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
                "Obrigado pela confiança senhor! Farei a entrega das casas o mais rápido possível!",
                "Glória à Takayama",
                "(+10 de Contentamento, +20 de População, -100 de Dinheiro)"
            ],

            2: ["Obrigado pela confiança senhor! Entregarei a ponte o mais rápido possível!",
                "Glória à Takayama",
                "(+5 de Contentamento, +10 de População, -50 de Dinheiro)"

            ],

            3: [
                "Entendo sua decisão. Espero que reconsidere no futuro.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 7,
        "dia_minimo": 3,

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
                "Farei de tudo para proteger nossa cidade senhor, você não irá se arrepender dessa decisão!",
                "Glória à Takayama",
                "(+10 de Contentamento, +20 de População, -100 de Dinheiro)"
            ],

            2: ["Você ainda há de se arrepender muito por essa decisão... ",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"

            ]
        }
    },

    {
        "sprite": 8,
        "dia_minimo": 2,

        "falas": [
            "Olá senhor, fiquei sabendo que está tendo problemas com o reino inimigo.",
            "Posso trabalhar pra você e conseguir informações importantes dos inimigos",
            "O que acha de eu te dar uma ajuda em troca de um bom pagamento?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Contratá-lo",
            "opcao_segunda": "Recusar proposta"
        },

        "efeito_primeira": {
            "Contentamento": -5,
            "Populacao": 1,
            "Dinheiro": -100
        },

        "efeito_segunda": {
            "Contentamento": +5,
            "Populacao": -5,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Provarei que todos estão errados sobre mim!",
                "Você não irá se arrepender, nunca desapontei um mestre.",
                "(-5 de Contentamento, +1 de População, -100 de Dinheiro)"
            ],

            2: ["Bom, não venha se queixar se algumas informações de seu reino vazarem!",
                "(+5 de Contentamento, -5 de População)"

            ]
        }
    },

    {
        "sprite": 9,
        "dia_minimo": 3,
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
                "Aqui estão! Tome cuidado ao manuseá-las!",
                "Glória à Takayama",
                "(+5 de Contentamento, +10 de População, -50 de Dinheiro)"
            ],

            2: ["Aqui estão! Com elas ganharemos a luta contra o mal!",
                "Glória à Takayama",
                "(+10 de Contentamento, +20 de População, -100 de Dinheiro)"

            ],

            3: [
                "Entendido. Caso surja a necessidade basta me contatar meu senhor!",
                "Glória à Takayama",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 10,
        "dia_minimo": 4,

        "falas": [
            "Olá meu senhor, venho avisar que tempos sombrios se aproximam!."
            "Posso exorcizar espíritos malignos e proteger a cidade de ameaças sobrenaturais.",
            "O que me diz, mortal?"
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
                "Nenhuma alma vil se aproximará deste reino meu senhor, tens minha garantia!",
                "Glória à Takayama",
                "(+10 de Contentamento, +20 de População, -100 de Dinheiro)"
            ],

            2: ["Me certificarei de que sua queda seja certeira! HAHAHAHAHAHAHHAHAHA",
                "(+5 de Contentamento, +0 de População, +0 de Dinheiro)"

            ]
        }
    },

{
        "sprite": 11,
        "dia_minimo": 4,

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
                "Aqui estão senhor! Caso precise de mais sabe onde me encontrar.",
                "Glória à Takayama",
                "(+5 de Contentamento, +10 de População, -50 de Dinheiro)"
            ],

            2: ["Aqui estão senhor! Caso precise de mais sabe onde me encontrar",
                "Glória à Takayama",
                "(+10 de Contentamento, +20 de População, -100 de Dinheiro)"

            ],

            3: [
                "Que pena! Se mudar de ideia sabe onde me encontrar.",
                "(-5 de Contentamento, +0 de População, +0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 12,

        "dia_minimo": 10,

        "falas": [
            "Olá, rei. Eu venho de um futuro distante, cerca de 15 mil anos à frente do seu tempo.",
            "No meu mundo, uma doença letal está exterminando cidades inteiras.",
            "Preciso de cobaias para um experimento arriscado. Pode parecer cruel, mas é a única chance de salvar o meu povo.",
            "Se me permitir levar dez pessoas comigo, retornarei em alguns dias com uma grande recompensa.",
            "Qual sua resposta?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Permitir",
            "opcao_segunda": "Recusar educadamente",
            "opcao_terceira": "Executá-lo"
        },

        "efeito_primeira": {
            "Contentamento": -10,
            "Populacao": -10,
            "Dinheiro": 0
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "efeito_terceira": {
            "Contentamento": 10,
            "Populacao": 0,
            "Dinheiro": 100,
        },

        "falas_pos": {
            1: [
                "Muito obrigado senhor, você realmente é nobre de coração como haviam me dito!",
                "Em alguns dias trarei sua recompensa e o compensarei por tudo isso!",
                "(-10 de Contentamento, -10 de População)"
            ],

            2: ["Entendo sua decisão, tentarei achar outro jeito de salvar meu povo!",
                "(5 de Contentamento)"

                ],

            3: [
                "NÃO! POR FAVOR ME PERDOE",
                "SE ME DEIXAR PARTIR PROMETO QUE NUNCA MAIS ME VERÁ",
                "POR FAVOR SENHOR"
                "(+10 de Contentamento, +100 de Dinheiro)"
            ]
        }
    },

{
        "sprite": 1,

        "dia_minimo": 1,

        "falas": [
            ""
        ],

        "qtd_escolhas": {
            "opcao_primeira": "",
            "opcao_segunda": "",
            "opcao_terceira": "",
            "opcao_quarta": ""
        },

        "efeito_primeira": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "efeito_segunda": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "efeito_terceira": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0,
        },

        "efeito_quarta": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "",
                "",
                "(0 de Contentamento, 0 de População, 0 de Dinheiro)"
            ],

            2: ["",
                "",
                "(0 de Contentamento, 0 de População, 0 de Dinheiro)"

            ],

            3: [
                "",
                "(0 de Contentamento, 0 de População, 0 de Dinheiro)"
            ],

            4: [
                "",
                "(0 de Contentamento, 0 de População, 0 de Dinheiro)"
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
    