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
spr13 = pg.image.load("Imagens/sprites/karasu.png")
spr14 = pg.image.load("Imagens/sprites/karasu.png")
spr15 = pg.image.load("Imagens/sprites/herbista.png")
spr16 = pg.image.load("Imagens/sprites/gaviao.png")
spr17 = pg.image.load("Imagens/sprites/argilista.png")
spr18 = pg.image.load("Imagens/sprites/mensageira2.png")
spr19 = pg.image.load("Imagens/sprites/cacadora.png")
spr20 = pg.image.load("Imagens/sprites/pintor.png")

spr71 = spr1

spr85 = pg.image.load("Imagens/sprites/pretendente.png")
spr86 = pg.image.load("Imagens/sprites/pretendente_gravida.png")
spr87 = pg.image.load("Imagens/sprites/viajante_futuro.png")
spr88 = pg.image.load("Imagens/sprites/glob.png")
spr89 = pg.image.load("Imagens/sprites/vendedor_neko.png")
spr90 = pg.image.load("Imagens/sprites/nekomata.png")
spr91 = pg.image.load("Imagens/sprites/nekomata.png")
spr92 = pg.image.load("Imagens/sprites/guardiao_lanterna.png")
spr93 = pg.image.load("Imagens/sprites/yukionna.png")
spr94 = pg.image.load("Imagens/sprites/tengu.png")
spr95 = pg.image.load("Imagens/sprites/tsukomogami.png")
spr96 = pg.image.load("Imagens/sprites/cozinheiro.png")
spr97 = pg.image.load("Imagens/sprites/sacerdotisa.png")
spr98 = pg.image.load("Imagens/sprites/artesao.png")
spr99 = pg.image.load("Imagens/sprites/carpinteiro.png")
spr100 = pg.image.load("Imagens/sprites/pescador.png")

spr110 = spr1

spr157 = pg.image.load("Imagens/sprites/astronoma.png")
spr158 = pg.image.load("Imagens/sprites/engenheiro_canais.png")
spr159 = pg.image.load("Imagens/sprites/capita_guarda.png")
spr160 = pg.image.load("Imagens/sprites/apicultor.png")
spr161 = pg.image.load("Imagens/sprites/tecela.png")
spr162 = pg.image.load("Imagens/sprites/embaixador_rival.png")
spr163 = pg.image.load("Imagens/sprites/parteira.png")
spr164 = pg.image.load("Imagens/sprites/cartografo.png")
spr165 = pg.image.load("Imagens/sprites/cervejeira_arroz.png")
spr166 = pg.image.load("Imagens/sprites/ronin.png")
spr167 = pg.image.load("Imagens/sprites/sacerdotista_chuva.png")
spr168 = pg.image.load("Imagens/sprites/coletor_impostos.png")
spr169 = pg.image.load("Imagens/sprites/guardia_floresta.png")
spr170 = pg.image.load("Imagens/sprites/inventor_pipas.png")
spr171 = pg.image.load("Imagens/sprites/cozinheira_real.png")
spr172 = pg.image.load("Imagens/sprites/domador_cavalos.png")
spr173 = pg.image.load("Imagens/sprites/viuva_soldado.png")
spr174 = pg.image.load("Imagens/sprites/artesao_mascaras.png")

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
    14: spr14,
    15: spr15,
    16: spr16,
    17: spr17,
    18: spr18,
    19: spr19,
    20: spr20,
    71: spr71,

    #WELLINGTON
    85: spr85,
    86: spr86,
    87: spr87,
    88: spr88,
    89: spr89,
    90: spr90,
    91: spr91,
    92: spr92,
    93: spr93,
    94: spr94,
    95: spr95,
    96: spr96,
    97: spr97,
    98: spr98,
    99: spr99,
    100: spr100,
    110: spr110,

    #DIEGO
    157: spr157,
    158: spr158,
    159: spr159,
    160: spr160,
    161: spr161,
    162: spr162,
    163: spr163,
    164: spr164,
    165: spr165,
    166: spr166,
    167: spr167,
    168: spr168,
    169: spr169,
    170: spr170,
    171: spr171,
    172: spr172,
    173: spr173,
    174: spr174,

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
            "Olá, sou Raiden, também conhecida como arconte electro!",
            "Venho até você pedir ajuda para alcançar a eternidade.",
            "Caso recuse... não irá gostar de me provocar.",
            "O que me diz?"
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
                "Agradeço pela ajuda mortal, juntos conquistaremos a eternidade e traremos paz para Inazuma",
                "Irei deixar alguns de meus suditos e um pouco de dinheiro para você!",
                "(-15 de Contentamento, +10 de População, +50 de Dinheiro)"
            ],

            2: ["MUSOU",
                "NO",
                "HITOTACHI!",
                "(Você sente a terra estremecer)",
                "(+10 de Contentamento, -15 de População, -20 de Dinheiro)"

            ]
        }
    },

    {
        "sprite": 3,
        "dia_minimo": 2,

        "falas": [
            "Olá humano, eu vim oferecer um pacto...",
            "Eu lhe darei riquezas e prosperidade, porém irei levar uma parte de almas comigo... ",
            "Pense com cuidado HAHAHA",
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
                "Adeus humano, foi um prazer fazer negócios com você!",
                "Faça bom proveito de suas riquezas, até a próxima...",
                "(-20 de Contentamento, -40 de População, +500 de Dinheiro)"
            ],

            2: ["Ah, entendo. Você prefere manter sua alma intacta, não é?",
                "Bem, isso é uma escolha sábia, até a próxima... ",
                "(+20 de Contentamento)"

            ]
        }
    },

    {
        "sprite": 4,
        "dia_minimo": 1,

        "falas": [
            "Olá meu senhor, sou uma yokai que vive na floresta próxima.",
            "Venho aqui pedir sua ajuda, a floresta tem sido destruída por madeireiros e caçadores...",
            "Nela existem muitos seres vivos que dependem da floresta para sobreviver.",
            "Por favor, me ajude a proteger a floresta e seus habitantes.",
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Ajudar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": -5,
            "Populacao": 30,
            "Dinheiro": 0
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 0,
            "Dinheiro": 100
        },

        "falas_pos": {
            1: [
                "Muito obrigado por sua ajuda, senhor.",
                "A floresta e seus habitantes ficarão muito gratos por sua decisão!",
                "Espero que possamos contar com seu apoio no futuro.",
                "(-5 de Contentamento, +30 de População)"
            ],

            2: ["Ah, entendo. Você prefere não se envolver, não é? Bem, até a próxima... ",
                "(+5 de Contentamento, +100 de Dinheiro)"

            ]
        }
    },

    {
        "sprite": 5,
        "dia_minimo": 2,

        "falas": [
            "Olá senhor, sou Gorobei, o sapo monge.",
            "Os sapos de nosso reino não estão lavando seus pés.",
            "Eles precisam urgentemente da construção de novas fontes termais para se banhar!",
            "Posso contar com a sua ajuda?"
        ],

        "qtd_escolhas":  {
            "opcao_primeira": "Construir fontes termais a todos",
            "opcao_segunda": "Construir um lago específico para os sapos",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 10,
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
                "Serei eternamente grato à voce senhor.",
                "Se precisar da ajuda dos sapos não hesite em pedir.",
                "Glória à Takayama!",
                "(+10 de Contentamento, +10 de População, -100 de Dinheiro)"
            ],

            2: ["Ah, obrigado senhor",
                "(+5 de Contentamento, +10 de População, -50 de Dinheiro)"

            ],

            3: [
                "Não acredito que achei que você fosse diferente dos outros tiranos... ",
                "(-5 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 6,
        "dia_minimo": 3,

        "falas": [
            "Olá meu senhor, sou um construtor e venho até você para oferecer meus serviços.",
            "Posso construir casas, pontes, estradas e muito mais. Se precisar de algo, é só me chamar!",
            "Posso começar a trabalhar imediatamente, basta me dizer o que você precisa..."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Construir casas para os moradores",
            "opcao_segunda": "Construir uma ponte para facilitar o comércio",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 25,
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
                "(+10 de Contentamento, +25 de População, -100 de Dinheiro)"
            ],

            2: ["Obrigado pela confiança senhor! Entregarei a ponte o mais rápido possível!",
                "Glória à Takayama",
                "(+5 de Contentamento, +10 de População, -50 de Dinheiro)"

            ],

            3: [
                "Entendo sua decisão. Espero que reconsidere no futuro.",
                "(-5 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 7,
        "dia_minimo": 3,

        "falas": [
            "Olá meu senhor, sou um monge e venho até você para pedir ajuda...",
            "A cidade está sendo atacada por demônios e preciso de seu apoio para enfrentar essa ameaça.",
            "Você aceitaria me ajudar a proteger a cidade dos demônios?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar a missão",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 15,
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
                "(+15 de Contentamento, +20 de População, -100 de Dinheiro)"
            ],

            2: ["Você ainda há de se arrepender muito por essa decisão... ",
                "(-5 de Contentamento)"

            ]
        }
    },

    {
        "sprite": 8,
        "dia_minimo": 2,

        "falas": [
            "Olá senhor, fiquei sabendo que está tendo problemas com o reino inimigo.",
            "Posso trabalhar pra você e conseguir informações importantes dos inimigos!",
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
                "(-5 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 10,
        "dia_minimo": 4,

        "falas": [
            "Olá meu senhor, venho avisar que tempos sombrios se aproximam!."
            "Posso expurgar espíritos malignos e proteger a cidade de ameaças sobrenaturais.",
            "O que me diz?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Contratar para expurgar os espíritos malignos",
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

            2: ["Se você pudesse ouvir os espíritos saberia do erro que está cometendo!",
                "(Você sente um calafrio em sua espinha)",
                "(+5 de Contentamento)"

            ]
        }
    },

{
        "sprite": 11,
        "dia_minimo": 4,

        "falas": [
            "Olá meu senhor, sou um alquimista e venho até você para oferecer meus serviços.",
            "Posso criar poções e elixires que podem ajudar a cidade, você precisa de alguma coisa específica?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Comprar poções de cura",
            "opcao_segunda": "Comprar poções de força",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 10,
            "Dinheiro": -25
        },

        "efeito_segunda": {
            "Contentamento": 10,
            "Populacao": 20,
            "Dinheiro": -50
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0

        },"falas_pos": {
            1: [
                "Aqui estão senhor! Caso precise de mais sabe onde me encontrar.",
                "Glória à Takayama",
                "(+5 de Contentamento, +10 de População, -25 de Dinheiro)"
            ],

            2: ["Aqui estão senhor! Caso precise de mais sabe onde me encontrar",
                "Glória à Takayama",
                "(+10 de Contentamento, +20 de População, -50 de Dinheiro)"

            ],

            3: [
                "Que pena! Se mudar de ideia sabe onde me encontrar.",
                "(-5 de Contentamento)"
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
        "sprite": 13,

        "dia_minimo": 1,

        "falas": [
            "Olá grande shogun, eu sou Karasu, um guerreiro que ainda não tem feitos, porém muita vontade e corajem para lutar!",
            "Posso ser um grande aliado para o senhor, me deixe provar minha lealdade e coragem em batalha, e prometo que não irá se arrepender."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 2,
            "Populacao": 1,
            "Dinheiro": -20
        },

        "efeito_segunda": {
            "Contentamento": -2,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito muito muito OBRIGADO shogunzinho, prometo não te decepcionar!",
                "Irei me esforçar para trazer uma recompensa ao senhor assim que possível!",
                "(+2 de Contentamento, +1 de População, -20 de Dinheiro)"
            ],

            2: ["Ah tudo bem então...",
                "(-2 de Contentamento)"

            ]
        }
    },

    {
        "sprite": 14,

        "dia_minimo": 2,

        "falas": [
            "Olá meu senhor! Lembra de mim?",
            "Aqui está os tesouros que havia prometido! Espero que ainda possamos trabalhar juntos!"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar friamente.",
            "opcao_segunda": "Aceitar e elogiar Karasu",
        },

        "efeito_primeira": {
            "Contentamento": -2,
            "Populacao": 0,
            "Dinheiro": 100
        },

        "efeito_segunda": {
            "Contentamento": 2,
            "Populacao": 0,
            "Dinheiro": 100
        },

        "falas_pos": {
            1: [
                "Oloko meu senhor, podia agradecer pelo menos né... ",
                "(-2 de Contentamento, +100 de Dinheiro)"
            ],

            2: [
                "Obrigado senhor, sempre estarei aqui para ajudá-lo!",
                "(+2 de Contentamento, +100 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 15,

        "dia_minimo": 3,

        "falas": [
            "Caro shogun, sou uma herbista que vive na floresta próxima. ",
            "Tenho uma grande variedade de ervas medicinais que podem ser usadas para criar poções e remédios para a cidade. ",
            "Se estiver interessado, posso lhe mostrar minha coleção e ajudá-lo a escolher as melhores ervas."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Comprar ervas medicinais",
            "opcao_segunda": "Contratar para cuidar dos cidadões",
            "opcao_terceira": "Fazer parceria para criar um hospital",
            "opcao_quarta": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 5,
            "Dinheiro": -20
        },

        "efeito_segunda": {
            "Contentamento": 15,
            "Populacao": 10,
            "Dinheiro": -50
        },

        "efeito_terceira": {
            "Contentamento": 20,
            "Populacao": 15,
            "Dinheiro": -100
        },

        "efeito_quarta": {
            "Contentamento": -5,
            "Populacao": -2,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Oh, muito obrigado senhor! Essas ervas serão muito úteis para a cidade!",
                "(+10 de Contentamento, +5 de População, -20 de Dinheiro)"
            ],

            2: ["Oh, que ótimo! Vou cuidar dos cidadãos com muito carinho e dedicação!",
                "(+15 de Contentamento, +10 de População, -50 de Dinheiro)"

            ],

            3: [
                "OH, que ótimo! Vou fazer o melhor hospital para a saúde da nação!",
                "(+20 de Contentamento, +15 de População, -100 de Dinheiro)"
            ],

            4: [
                "Entendo, talvez outra hora seja melhor...",
                "( -5 de Contentamento,  -2 de População)"
            ]
        }
    },

    {
        "sprite": 16,

        "dia_minimo": 1,

        "falas": [
            "Com lincença shogun, sou um treinador de falcões e venho até você para oferecer meus serviços.",
            "Posso treinar falcões para ajudar na defesa da cidade, ou para caçar presas para a população. O que acha?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Contratar serviços",
            "opcao_segunda": "Dispensá-lo"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 1,
            "Dinheiro": -45
        },

        "efeito_segunda": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado senhor! Meus falcões serão muito úteis para a cidade!",
                "(5 de Contentamento, 1 de População, -45 de Dinheiro)"
            ],

            2: [
                "Entendo, talvez não seja a melhor hora..."
            ],

        }
    },

    {
        "sprite": 17,

        "dia_minimo": 3,

        "falas": [
            "Olá meu senhor, sou um argilista e venho até você para oferecer meus serviços.",
            "Posso criar belas esculturas e obras de arte para decorar a cidade, ou posso criar utensílios de cerâmica para uso diário. O que acha?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Contratar para criar obras de arte",
            "opcao_segunda": "Contratar para criar utensílios de cerâmica",
            "opcao_terceira": "Fazer parceria para criar um museu",
            "opcao_quarta": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 1,
            "Dinheiro": -30
        },

        "efeito_segunda": {
            "Contentamento": 15,
            "Populacao": 5,
            "Dinheiro": -50
        },

        "efeito_terceira": {
            "Contentamento": 20,
            "Populacao": 10,
            "Dinheiro": -100
        },

        "efeito_quarta": {
            "Contentamento": -10,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado senhor! Minhas obras de arte trarão beleza e cultura para a cidade!",
                "(+10 de Contentamento, +1 de População, -30 de Dinheiro)"
            ],

            2: [
                "Muito obrigado senhor! Meus utensílios de cerâmica serão muito úteis para a população!",
                "(+15 de Contentamento, +5 de População, -50 de Dinheiro)"

            ],

            3: [
                "Muito obrigado senhor! Nossa parceria criará um museu incrível para a cidade!",
                "(+20 de Contentamento, +10 de População, -100 de Dinheiro)"
            ],

            4: [
                "Entendo, talvez outra hora seja melhor...",
                "(-10 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 18,

        "dia_minimo": 4,

        "falas": [
            "Com sua licença shogun, sou uma mensageira de outro feudo.",
            "Venho aqui para entregar uma mensagem importante para você, mas antes de entregá-la, gostaria de saber se você está disposto a ouvir o que tenho a dizer."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Ver a mensagem",
            "opcao_segunda": "Ignorar a mensageira"
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
                "Muito obrigado por ouvir minha mensagem, senhor! A mensagem é a seguinte:",
                "'O feudo vizinho está planejando um ataque surpresa contra o seu feudo, eles estão se preparando para atacar em breve, então esteja preparado para se defender.'",
                "Até mais..."

            ],

            2: [
                "Tudo bem então...",
            ]
        }
    },

    {
        "sprite": 19,

        "dia_minimo": 1,

        "falas": [
            "Com licença shogun, sou uma caçadora.",
            "Vim até você oferecer meus serviços para caçar animais selvagens que estão ameaçando a população da cidade. O que acha?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar",
            "opcao_segunda": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 1,
            "Dinheiro": -20
        },

        "efeito_segunda": {
            "Contentamento": -5,
            "Populacao": -10,
            "Dinheiro": 0
        },


        "falas_pos": {
            1: [
                "Obrigado senhor! Meus serviços de caça ajudarão a proteger a população da cidade!",
                "(+5 de Contentamento, +1 de População, -20 de Dinheiro)"
            ],

            2: [
                "Entendo, talvez outra hora seja melhor...",
                "(As feras atacam alguns cidadãos)"
                "(-5 de Contentamento, -10 de População)"
            ],
        }
    },

    {
        "sprite": 20,

        "dia_minimo": 3,

        "falas": [
            "Olá caro shogun, sou um pintor e vim oferecer meus serviços a ti."
            "Posso criar belas pinturas para decorar a cidade, ou posso criar retratos de pessoas importantes para a história da cidade.",
            "O que acha?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Contratar para criar pinturas",
            "opcao_segunda": "Contratar para criar retratos",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 1,
            "Dinheiro": -30
        },

        "efeito_segunda": {
            "Contentamento": 15,
            "Populacao": 1,
            "Dinheiro": -45
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0,
        },

        "falas_pos": {
            1: [
                "Muito obrigado senhor! Minhas pinturas trarão beleza e cultura para a cidade!",
                "(+10 de Contentamento, +1 de População, -30 de Dinheiro)"
            ],

            2: [
                "Muito obrigado senhor! Meus retratos trarão felicidade e cultura para a cidade!",
                "(+15 de Contentamento, +1 de População, -45 de Dinheiro)"

            ],

            3: [
                "Entendo, talvez outra hora seja melhor...",
                "(-5 de Contentamento)"
            ],
        }
    },

    {
        "sprite": 85,

        "dia_minimo": 1,

        "falas": [
            "Olá, sou Ayahime, filha casa Hayashi.",
            "Minha família controla quase todas as rotas comerciais de Takayama!",
            "Creio que deve conhecer meu pai, Hayashi Nobumasa.",
            "Pensando de forma estratégica, não seria nada mal se pudessemos juntar nossos sobrenomes!",
            "O que me diz, belo moço?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Casar-se com ela",
            "opcao_segunda": "Dispensá-la",
            "opcao_terceira": "Cortar negócios com a sua família"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 0,
            "Dinheiro": 1000
        },

        "efeito_segunda": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "efeito_terceira": {
            "Contentamento": -15,
            "Populacao": -15,
            "Dinheiro": -500,
        },

        "falas_pos": {
            1: [
                "Que ótima notícia!",
                "De agora em diante farei de tudo para prosperar ao seu lado, meu amor!",
                "(+10 de Contentamento, +1000 de Dinheiro)"
            ],

            2: ["É como dizem, nem todos têm bom gosto!",
                "(-5 de Contentamento)"

            ],

            3: [
                "COMO SE ATREVE?",
                "VOCÊ SE ARREPENDERÁ AMARGAMENTE DISSO!"
                "(-15 de Contentamento, -15 de População, -500 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 86,

        "dia_minimo": 1,

        "falas": [
            "Meu amor, trago ótimas notícias!",
            "Em alguns dias nascerá nosso primogênito",
            "Finalmente teremos alguém para continuar nosso legado!",
            "Creio que neste momento não exista ninguém mais feliz do que eu ao seu lado."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Que ótima notícia meu amor!",
            "opcao_segunda": "Vamos começar os preparativos para receber-lô!",
            "opcao_terceira": "Eu não estou pronto pra isso, se retire!"
        },

        "efeito_primeira": {
            "Contentamento": 15,
            "Populacao": 1,
            "Dinheiro": 0
        },

        "efeito_segunda": {
            "Contentamento": 15,
            "Populacao": 1,
            "Dinheiro": -100
        },

        "efeito_terceira": {
            "Contentamento": -20,
            "Populacao": -16,
            "Dinheiro": -200,
        },

        "falas_pos": {
            1: [
                "Vou começar os preparos para recebê-lo imediatamente, meu amor!",
                "(+10 de Contentamento, +1 de População)"
            ],

            2: ["Você é o melhor marido que eu poderia ter!",
                "(+15 de Contentamento, +1 de População, -100 de Dinheiro)"
                ],

            3: [
                "COMO VOCÊ OUSA DIZER ISSO?",
                "EU MESMA ME GARANTIREI DE DESTRUIR O SEU LEGADO!",
                "(-20 de Contentamento, -16 de População, -200 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 87,

        "dia_minimo": 1,

        "falas": [
            "Muito obrigado por sua ajuda nobre senhor!",
            "Com os experimentos que o senhor me possibilitou foi possivel encontrar uma cura pro meu povo!",
            "Mas se todos estão bem é graças a você, leve isso como recompensa."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Fico feliz em ouvir isso!",
            "opcao_segunda": "Ótimo, agora caia fora daqui!"
        },

        "efeito_primeira": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 1000
        },

        "efeito_segunda": {
            "Contentamento": -1,
            "Populacao": 0,
            "Dinheiro": 1000
        },

        "falas_pos": {
            1: [
                "Agora tenho que voltar para o meu tempo.",
                "Até a proxima, senhor!",
                "(+1000 de Dinheiro)"
            ],

            2: ["Nossa... perdão pelo incômodo.",
                "(-1 de Contentamento, +1000 de Dinheiro)"
                ]
        }
    },

    {
        "sprite": 88,

        "dia_minimo": 1,

        "falas": [
            "Glob. gLob. glOb. gloB.",
            "glob ggggllloooooob globglob",
            "glu- GLOB"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Glob!",
            "opcao_segunda": "?",
            "opcao_terceira": "Adotar"
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
            "Contentamento": 5,
            "Populacao": +1,
            "Dinheiro": 0,
        },

        "falas_pos": {
            1: [
                "GLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOB",
                "(Que bicho esquisito...)"
            ],

            2: ["glob glob glob glob GLOB GLOB gggggglllloooooobbbbb",
                "(Você sente que quase consegue entendê-lo)"

            ],

            3: [
                "GLOBBBBBBBBBBB GLOB GLOB :3",
                "(Você se sente estranhamente alegre com a presença dele)",
                "(+5 de Contentamento, +1 de População)"
            ]
        }
    },

    {
        "sprite": 89,

        "dia_minimo": 1,

        "falas": [
            "Olá meu senhor, ouvi dizer que tempos sobrios hão de se aproximar...",
            "Sei que sua tarefa está ainda mais difícil durante este período, então lhe trouxe isso.",
            "Por apenas 50 pratas eu lhe vendo estes amulhetos, que certamente serão úteis para sua proteção...",
            "Então, o que me diz?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Comprar",
            "opcao_segunda": "Não comprar"
        },

        "efeito_primeira": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": -50
        },

        "efeito_segunda": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Isso foi uma ótima decisão meu senhor!",
                "Tenho certeza que estes amuletos serão grandes alidos contra a má sorte!",
                "(-50 de Dinheiro)"
            ],

            2: [
                "Entendi... Talvez o senhor se arrependa disto!",
                "(Você tem a impressão de que ele está falando sério)"
            ]
        }
    },

    {
        "sprite": 90,

        "dia_minimo": 1,

        "falas": [
            "Olá hahaha.",
            "Posso entrar?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Permitir",
            "opcao_segunda": "Proibir"
        },

        "efeito_primeira": {
            "Contentamento": +20,
            "Populacao": 0,
            "Dinheiro": 333
        },

        "efeito_segunda": {
            "Contentamento": +10,
            "Populacao": 0,
            "Dinheiro": 222
        },

        "falas_pos": {
            1: [
                "Ebaaaaaa hahahaha.",
                "(Você sente que aqueles amuletos funcionaram)",
                "(+20 de Contentamento, +1 de População, +333 de Dinheiro)"
            ],

            2: [
                "Poxa hahahaha.",
                "(Você sente que aqueles amuletos funcionaram)",
                "(+10 de Contentamento, 222 de Dinheiro)"
                ]
        }
    },

    {
        "sprite": 91,

        "dia_minimo": 1,

        "falas": [
            "Olá hahaha.",
            "Posso entrar?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Permitir",
            "opcao_segunda": "Proibir"
        },

        "efeito_primeira": {
            "Contentamento": -11,
            "Populacao": -22,
            "Dinheiro": -333
        },

        "efeito_segunda": {
            "Contentamento": -33,
            "Populacao": -22,
            "Dinheiro": -111
        },

        "falas_pos": {
            1: [
                "HAHAHAHAHAHAHA.",
                "(Você se arrepende de não ter comprado os amuletos)"
                "(-11 de Contentamento, -22 de População, -333 de Dinheiro)"
            ],

            2: [
                "AHHAHAHAHAHAHAHAHAHHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHA.",
                "(Você se arrepende de não ter comprado os amuletos)"
                "(-33 de Contentamento, -22 de População, -111 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 92,

        "dia_minimo": 1,

        "falas": [
            "Sou Torobei, guardião das lanternas ancestrais, carrego a luz daquele que ja se foram.",
            "Ultimamente, as chamas andam inquietas... Takayama esqueceu seus mortos.",
            "Tenho um pedido a lhe fazer: restaure o santuário abandonado para que eu possa realizar uma cerimônia fúnebre!"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Restaurar o santuário",
            "opcao_segunda": "Negar o pedido"
        },

        "efeito_primeira": {
            "Contentamento": +10,
            "Populacao": 0,
            "Dinheiro": -77
        },

        "efeito_segunda": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado, meu senhor!",
                "Tenho certeza que honrar o passado é a chave para vencer essa crise!",
                "Agora tenho de ir, até a proxima."
                "(+10 de Contentamento, -77 de Dinheiro)"
            ],

            2: [
                "Entendo... só nao sei se os espíritos também entenderão.",
                "(Você se questiona se fez a decisão certa)",
                "(-5 de Contentamento)"
                ]
        }
    },

    {
        "sprite": 94,

        "dia_minimo": 20,

        "falas": [
            "Me chamo Akabane Sogen, guardião das montanhas de Takayama.",
            "Estou observando seu reino do alto dos morros tem um tempo.",
            "O que tenho pra te dizer é que não estou nada contente com o que vejo!",
            "Seus homens são fracos. Sua corte está confortável demais!",
            "Lhes ofereço um tratamento árduo nas montanhas, somente os dignos retornarão!",
            "O que me diz?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar o pedido",
            "opcao_segunda": "Negar o pedido"
        },

        "efeito_primeira": {
            "Contentamento": -5,
            "Populacao": -10,
            "Dinheiro": +100
        },

        "efeito_segunda": {
            "Contentamento": 10,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Esta foi uma decisão sábia! Este reino está em boas mãos, em alguns dias estará em mãos melhores ainda!",
                "(-5 de Contentamento, -10 de População, +100 de Dinheiro)"
            ],

            2: [
                "Pelo que consigo ver o mais fraco daqui é você mesmo.",
                "Sua queda é certeira!",
                "(+10 de Contentamento)"
                ]
        }
    },



    {
        "sprite": 93,

        "dia_minimo": 1,

        "falas": [
            "Olá, venho do passo de Shirakawa.",
            "De onde venho é de onde eles partem dessa vida.",
            "A nevasca... ela engole, ela sufoca, ela acaba.",
            "Feche as rotas comerciais, proteja seu povo..."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Fechar as rotas",
            "opcao_segunda": "Preservar o comércio",
            "opcao_terceira": "Prender a suspeita"
        },

        "efeito_primeira": {
            "Contentamento": -15,
            "Populacao": 30,
            "Dinheiro": -50
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": -30,
            "Dinheiro": 50
        },

        "efeito_terceira": {
            "Contentamento": 10,
            "Populacao": -15,
            "Dinheiro": 50,
        },

        "falas_pos": {
            1: [
                "Você tem um coração bom!",
                "Isso é raro!",
                "Até mais!",
                "Que Takayama permaneça sob boas estrelas!",
                "(-15 de Contentamento, +30 de População, -50 de Dinheiro)"
            ],

            2: ["Isso é um erro!",
                "Quando a neve cair, se despeça daqueles que ama...",
                "(+5 de Contentamento, -30 de População, +50 de Dinheiro)"

                ],

            3: [
                "Quando a lua romper o véu da noite",
                "serei apenas um devaneio em suas memórias.",
                "Mas aqueles que brilharem sob a neve",
                "jamais verão o sol raiar.",
                "(+10 de Contentamento, -15 de População, +50 de Dinheiro)"
            ],

            4: [
                "",
                "(0 de Contentamento, 0 de População, 0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 95,

        "dia_minimo": 1,

        "falas": [
            "Meu senhor, vim informá-lo de algo que está acontecendo em nosso reino.",
            "A principio parecia uma maldição... mas descobri que era apenas descuido!",
            "Objetos por toda Takayama estão criando vida, como este guarda-chuva.",
            "Ferramentas abandonadas começam a sentir rancor por terem sido deixados de lado...",
            "Isso faz com que eles fiquem dessa forma, então proponho que criemos uma oficina de restauração de ferramentas.",
            "O que me diz, meu senhor?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Criar a oficina",
            "opcao_segunda": "Queimar os objetos",
            "opcao_terceira": "Vender os objetos"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 0,
            "Dinheiro": -75
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": -25,
            "Dinheiro": 0
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": +50,
        },

        "falas_pos": {
            1: [
                "Obrigado meu senhor!",
                "Tenho certeza de que não teremos mais problemas assim daqui em diante.",
                "(+10 de Contentamento, -75 de Dinheiro)"
            ],

            2: [
                "Você não deveria fazer isso...",
                "As consequencias serão terríveis!",
                "(+5 de Contentamento, -25 de População)"

                ],

            3: [
                "Isso resolverá por agora, mas eles não pararão de surgir...",
                "(-5 de Contentamento, +50 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 96,

        "dia_minimo": 1,

        "falas": [
            "Meu senhor, venho da cozinha do castelo com más notícias.",
            "Parte do arroz reservado para o povo foi tomado por mofo durante a noite.",
            "Se a notícia se espalhar, a vila entrará em pânico.",
            "O que deseja fazer?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Descartar o arroz",
            "opcao_segunda": "Distribuir assim mesmo",
            "opcao_terceira": "Comprar arroz novo"
        },

        "efeito_primeira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": -10
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": -5,
            "Dinheiro": 0
        },

        "efeito_terceira": {
            "Contentamento": 8,
            "Populacao": 3,
            "Dinheiro": -25
        },

        "falas_pos": {
            1: [
                "Como ordenar, meu senhor.",
                "O povo sentirá a falta do arroz, mas ao menos não adoecerá.",
                "(-5 de Contentamento, 0 de População, -10 de Dinheiro)"
            ],

            2: [
                "Entendido... mandarei preparar tudo antes que percebam o cheiro.",
                "Que os deuses sejam gentis com os estômagos da vila.",
                "(+5 de Contentamento, -5 de População, 0 de Dinheiro)"
            ],

            3: [
                "Uma decisão nobre, meu senhor.",
                "Os cofres sentirão o peso, mas o povo lembrará de sua generosidade.",
                "(+8 de Contentamento, +3 de População, -25 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 97,

        "dia_minimo": 1,

        "falas": [
            "Meu senhor, venho das margens do Rio Miyagawa.",
            "Os pescadores encontraram um peixe enorme esta manhã.",
            "O povo acredita que ele seja um presságio dos espíritos do rio.",
            "O que deseja fazer?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Guardar como presságio",
            "opcao_segunda": "Servir no banquete",
            "opcao_terceira": "Vender no mercado",
            "opcao_quarta": "Devolver ao rio"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 0,
            "Dinheiro": -5
        },

        "efeito_segunda": {
            "Contentamento": 8,
            "Populacao": 3,
            "Dinheiro": -10
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 20
        },

        "efeito_quarta": {
            "Contentamento": 5,
            "Populacao": 5,
            "Dinheiro": -5
        },

        "falas_pos": {
            1: [
                "Como desejar, meu senhor.",
                "O peixe será levado ao santuário antes que alguém ouse tocá-lo.",
                "(+5 de Contentamento, 0 de População, -5 de Dinheiro)"
            ],

            2: [
                "Um banquete com peixe sagrado... isso dará assunto por muitos dias.",
                "Espero que os espíritos também tenham bom apetite.",
                "(+8 de Contentamento, +3 de População, -10 de Dinheiro)"
            ],

            3: [
                "Os mercadores pagarão bem por uma criatura tão rara.",
                "Mas alguns pescadores dirão que vendemos um sinal dos deuses.",
                "(-5 de Contentamento, 0 de População, +20 de Dinheiro)"
            ],

            4: [
                "Então ele voltará às águas de onde veio.",
                "Talvez o rio se lembre de sua misericórdia.",
                "(+5 de Contentamento, +5 de População, -5 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 98,

        "dia_minimo": 1,

        "falas": [
            "Meu senhor, os campos estão secos e o povo começa a temer a colheita.",
            "O santuário deseja realizar um pequeno festival para pedir chuva.",
            "Mas lanternas, músicos e oferendas exigirão recursos do castelo.",
            "Qual será sua decisão?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Financiar o festival",
            "opcao_segunda": "Fazer algo simples",
            "opcao_terceira": "Proibir o ritual"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 3,
            "Dinheiro": -25
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 0,
            "Dinheiro": -10
        },

        "efeito_terceira": {
            "Contentamento": -8,
            "Populacao": 0,
            "Dinheiro": 5
        },

        "falas_pos": {
            1: [
                "Sua generosidade será lembrada nas preces, meu senhor.",
                "Que as nuvens escutem o nome de seu castelo.",
                "(+10 de Contentamento, +3 de População, -25 de Dinheiro)"
            ],

            2: [
                "Faremos algo humilde, mas sincero.",
                "Às vezes, os espíritos escutam melhor quando há menos ouro entre as palavras.",
                "(+5 de Contentamento, 0 de População, -10 de Dinheiro)"
            ],

            3: [
                "Entendo sua ordem.",
                "Mas quando o céu permanecer vazio, o povo procurará alguém para culpar.",
                "(-8 de Contentamento, 0 de População, +5 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 99,

        "dia_minimo": 2,

        "falas": [
            "Meu senhor, um artesão da praça terminou uma estátua em sua homenagem.",
            "Ela foi feita com devoção... mas talvez não com muito talento.",
            "O povo já começou a rir perto do mercado.",
            "O que faremos com ela?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar a homenagem",
            "opcao_segunda": "Mandar refazer"
        },

        "efeito_primeira": {
            "Contentamento": 8,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "efeito_segunda": {
            "Contentamento": 3,
            "Populacao": 0,
            "Dinheiro": -15
        },

        "falas_pos": {
            1: [
                "Aceitará mesmo assim? Que atitude inesperadamente nobre.",
                "O povo rirá da estátua, mas talvez também ria com o senhor.",
                "(+8 de Contentamento, 0 de População, 0 de Dinheiro)"
            ],

            2: [
                "Chamarei o artesão para corrigir a obra.",
                "Desta vez, pedirei que ele olhe para o senhor antes de esculpir.",
                "(+3 de Contentamento, 0 de População, -15 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 100,

        "dia_minimo": 2,

        "falas": [
            "Meu senhor, trago notícias da ponte do caminho norte.",
            "A madeira está rangendo mais do que deveria.",
            "Comerciantes ainda passam por lá, mas os carpinteiros temem a próxima chuva.",
            "Qual será sua ordem?"
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Consertar agora",
            "opcao_segunda": "Fechar a passagem",
            "opcao_terceira": "Ignorar por enquanto"
        },

        "efeito_primeira": {
            "Contentamento": 5,
            "Populacao": 5,
            "Dinheiro": -25
        },

        "efeito_segunda": {
            "Contentamento": -5,
            "Populacao": 3,
            "Dinheiro": -5
        },

        "efeito_terceira": {
            "Contentamento": -8,
            "Populacao": -5,
            "Dinheiro": 10
        },

        "falas_pos": {
            1: [
                "Os carpinteiros começarão ainda hoje.",
                "A ponte ficará firme, mesmo que os cofres reclamem.",
                "(+5 de Contentamento, +5 de População, -25 de Dinheiro)"
            ],

            2: [
                "Fecharemos a ponte até segunda ordem.",
                "Os comerciantes não gostarão, mas ao menos ninguém cairá no rio.",
                "(-5 de Contentamento, +3 de População, -5 de Dinheiro)"
            ],

            3: [
                "Entendido, meu senhor.",
                "A ponte continuará aberta... e os deuses decidirão se ela também continuará de pé.",
                "(-8 de Contentamento, -5 de População, +10 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 157,
        "dia_minimo": 12,

        "falas": [
            "Meu senhor, observei sinais estranhos nos ceus durante tres noites.",
            "As estrelas indicam uma estacao dificil, mas tambem uma chance de preparar o feudo.",
            "Com recursos, posso orientar agricultores e navegadores antes que os problemas cheguem."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Financiar os estudos",
            "opcao_segunda": "Cobrar impostos pelo pressagio",
            "opcao_terceira": "Ignorar os pressagios"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 3,
            "Dinheiro": -140
        },

        "efeito_segunda": {
            "Contentamento": -10,
            "Populacao": 0,
            "Dinheiro": 160
        },

        "efeito_terceira": {
            "Contentamento": -3,
            "Populacao": -2,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Com tempo e instrumentos, poderemos evitar perdas antes que elas acontecam.",
                "(+10 de Contentamento, +3 de Populacao, -140 de Dinheiro)"
            ],

            2: [
                "Os cofres crescerao, mas o povo nao gostara de pagar por medo das estrelas.",
                "(-10 de Contentamento, +160 de Dinheiro)"
            ],

            3: [
                "Entao torcamos para que os ceus estejam errados, meu senhor.",
                "(-3 de Contentamento, -2 de Populacao)"
            ]
        }
    },

    {
        "sprite": 158,
        "dia_minimo": 16,

        "falas": [
            "Meu senhor, os campos proximos ao rio poderiam produzir muito mais.",
            "Se cavarmos canais de irrigacao, as colheitas futuras serao melhores.",
            "Mas a obra exigira dinheiro e trabalhadores por alguns dias."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Construir os canais",
            "opcao_segunda": "Fazer uma obra pequena",
            "opcao_terceira": "Adiar a construcao"
        },

        "efeito_primeira": {
            "Contentamento": 12,
            "Populacao": 8,
            "Dinheiro": -260
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 3,
            "Dinheiro": -100
        },

        "efeito_terceira": {
            "Contentamento": -6,
            "Populacao": -2,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Os campos beberao do rio. O povo colhera os frutos dessa decisao.",
                "(+12 de Contentamento, +8 de Populacao, -260 de Dinheiro)"
            ],

            2: [
                "Nao sera perfeito, mas ja ajudara parte das plantacoes.",
                "(+5 de Contentamento, +3 de Populacao, -100 de Dinheiro)"
            ],

            3: [
                "A terra continuara seca em muitos lugares, meu senhor.",
                "(-6 de Contentamento, -2 de Populacao)"
            ]
        }
    },

    {
        "sprite": 159,
        "dia_minimo": 10,

        "falas": [
            "Meu senhor, os caminhos comerciais estao sendo atacados por bandidos.",
            "Posso enviar patrulhas para proteger as estradas.",
            "Isso trara seguranca, mas manter soldados fora da cidade custa caro."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Enviar patrulhas",
            "opcao_segunda": "Cobrar escolta",
            "opcao_terceira": "Nao deslocar soldados"
        },

        "efeito_primeira": {
            "Contentamento": 8,
            "Populacao": 2,
            "Dinheiro": -130
        },

        "efeito_segunda": {
            "Contentamento": -4,
            "Populacao": 0,
            "Dinheiro": 120
        },

        "efeito_terceira": {
            "Contentamento": -9,
            "Populacao": -3,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "As estradas serao vigiadas. Comerciantes e viajantes respirarao melhor.",
                "(+8 de Contentamento, +2 de Populacao, -130 de Dinheiro)"
            ],

            2: [
                "Quem puder pagar estara seguro. Quem nao puder, reclamara.",
                "(-4 de Contentamento, +120 de Dinheiro)"
            ],

            3: [
                "Entao os viajantes seguirao por conta propria. Alguns talvez nao cheguem.",
                "(-9 de Contentamento, -3 de Populacao)"
            ]
        }
    },

    {
        "sprite": 160,
        "dia_minimo": 7,

        "falas": [
            "Meu senhor, minhas colmeias estao crescendo bem.",
            "Com apoio, posso ensinar outras familias a produzir mel.",
            "O mel alimenta, cura e vende bem."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Apoiar os apicultores",
            "opcao_segunda": "Comprar o mel para revenda",
            "opcao_terceira": "Deixar como esta"
        },

        "efeito_primeira": {
            "Contentamento": 9,
            "Populacao": 2,
            "Dinheiro": -70
        },

        "efeito_segunda": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 110
        },

        "efeito_terceira": {
            "Contentamento": 1,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "As colmeias se espalharao pelas vilas. O povo tera alimento e trabalho.",
                "(+9 de Contentamento, +2 de Populacao, -70 de Dinheiro)"
            ],

            2: [
                "Sera lucrativo, mas as familias sentirao falta do mel em casa.",
                "(-5 de Contentamento, +110 de Dinheiro)"
            ],

            3: [
                "Continuarei cuidando das minhas colmeias, meu senhor.",
                "(+1 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 161,
        "dia_minimo": 9,

        "falas": [
            "Meu senhor, nossas tecelas produzem bons tecidos, mas faltam teares.",
            "Com novos equipamentos, poderemos vender mais e empregar familias.",
            "O investimento nao sera pequeno."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Comprar novos teares",
            "opcao_segunda": "Exigir mais producao",
            "opcao_terceira": "Recusar"
        },

        "efeito_primeira": {
            "Contentamento": 11,
            "Populacao": 5,
            "Dinheiro": -180
        },

        "efeito_segunda": {
            "Contentamento": -12,
            "Populacao": -1,
            "Dinheiro": 140
        },

        "efeito_terceira": {
            "Contentamento": -4,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "As oficinas ficarao cheias de trabalho. O feudo vestira sua prosperidade.",
                "(+11 de Contentamento, +5 de Populacao, -180 de Dinheiro)"
            ],

            2: [
                "Produziremos mais, mas a custa do cansaco e da raiva das artesas.",
                "(-12 de Contentamento, -1 de Populacao, +140 de Dinheiro)"
            ],

            3: [
                "Entao continuaremos trabalhando devagar, com ferramentas antigas.",
                "(-4 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 162,
        "dia_minimo": 18,

        "falas": [
            "Meu senhor, venho em nome do feudo vizinho.",
            "Meu mestre propoe um acordo comercial entre nossas terras.",
            "Mas ele exige uma taxa inicial como prova de boa vontade."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aceitar o acordo",
            "opcao_segunda": "Negociar melhor",
            "opcao_terceira": "Recusar com firmeza"
        },

        "efeito_primeira": {
            "Contentamento": 4,
            "Populacao": 2,
            "Dinheiro": -120
        },

        "efeito_segunda": {
            "Contentamento": 2,
            "Populacao": 0,
            "Dinheiro": 80
        },

        "efeito_terceira": {
            "Contentamento": -3,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "O acordo sera firmado. Que ambas as terras lucrem com prudencia.",
                "(+4 de Contentamento, +2 de Populacao, -120 de Dinheiro)"
            ],

            2: [
                "Vejo que nao sera facil engana-lo, meu senhor. Levarei sua contraproposta.",
                "(+2 de Contentamento, +80 de Dinheiro)"
            ],

            3: [
                "Meu mestre ficara ofendido, mas respeitara sua clareza.",
                "(-3 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 163,
        "dia_minimo": 11,

        "falas": [
            "Meu senhor, muitas familias vivem longe de ajuda quando nascem suas criancas.",
            "Se eu puder treinar novas parteiras, salvaremos maes e bebes.",
            "Preciso de apoio para viajar pelas vilas."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Financiar o treinamento",
            "opcao_segunda": "Ajudar a vila central",
            "opcao_terceira": "Negar apoio"
        },

        "efeito_primeira": {
            "Contentamento": 13,
            "Populacao": 7,
            "Dinheiro": -160
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 2,
            "Dinheiro": -50
        },

        "efeito_terceira": {
            "Contentamento": -9,
            "Populacao": -3,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Viajarei amanha. Muitas vidas pequenas agradecerao sem saber seu nome.",
                "(+13 de Contentamento, +7 de Populacao, -160 de Dinheiro)"
            ],

            2: [
                "A vila central ficara mais segura, mas as distantes ainda precisarao de ajuda.",
                "(+5 de Contentamento, +2 de Populacao, -50 de Dinheiro)"
            ],

            3: [
                "Entao farei o que puder sozinha, meu senhor.",
                "(-9 de Contentamento, -3 de Populacao)"
            ]
        }
    },

    {
        "sprite": 164,
        "dia_minimo": 15,

        "falas": [
            "Meu senhor, retornei das montanhas com mapas incompletos, mas promissores.",
            "Encontrei trilhas, fontes e possiveis rotas comerciais.",
            "Com uma escolta, posso terminar o levantamento."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Enviar escolta",
            "opcao_segunda": "Comprar os mapas",
            "opcao_terceira": "Dispensa-lo"
        },

        "efeito_primeira": {
            "Contentamento": 6,
            "Populacao": 3,
            "Dinheiro": -110
        },

        "efeito_segunda": {
            "Contentamento": 1,
            "Populacao": 0,
            "Dinheiro": -40
        },

        "efeito_terceira": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Com protecao, voltarei com rotas seguras para comercio e expansao.",
                "(+6 de Contentamento, +3 de Populacao, -110 de Dinheiro)"
            ],

            2: [
                "Os mapas ainda podem servir, embora faltem partes importantes.",
                "(+1 de Contentamento, -40 de Dinheiro)"
            ],

            3: [
                "Entendo. Talvez outro senhor veja valor nos caminhos que encontrei.",
                "(0 de Contentamento, 0 de Populacao, 0 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 165,
        "dia_minimo": 13,

        "falas": [
            "Meu senhor, minha familia sabe produzir uma bebida de arroz excelente.",
            "Ela pode render lucro em festivais e tavernas.",
            "Mas alguns monges dizem que isso trara desordem."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Permitir a producao",
            "opcao_segunda": "Taxar fortemente",
            "opcao_terceira": "Proibir"
        },

        "efeito_primeira": {
            "Contentamento": 8,
            "Populacao": 1,
            "Dinheiro": 90
        },

        "efeito_segunda": {
            "Contentamento": -7,
            "Populacao": 0,
            "Dinheiro": 180
        },

        "efeito_terceira": {
            "Contentamento": -5,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "As tavernas brindarao por sua decisao, meu senhor.",
                "(+8 de Contentamento, +1 de Populacao, +90 de Dinheiro)"
            ],

            2: [
                "Os cofres gostarao. Os clientes e produtores, nem tanto.",
                "(-7 de Contentamento, +180 de Dinheiro)"
            ],

            3: [
                "Entao os barris permanecerao fechados... oficialmente.",
                "(-5 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 166,
        "dia_minimo": 20,

        "falas": [
            "Meu senhor, sou um samurai sem mestre.",
            "Procuro um lugar onde minha espada ainda tenha proposito.",
            "Posso servir ao seu feudo, se aceitar minha lealdade."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Contratar o ronin",
            "opcao_segunda": "Treinar os guardas",
            "opcao_terceira": "Recusar sua espada"
        },

        "efeito_primeira": {
            "Contentamento": 3,
            "Populacao": 1,
            "Dinheiro": -100
        },

        "efeito_segunda": {
            "Contentamento": 7,
            "Populacao": 0,
            "Dinheiro": -70
        },

        "efeito_terceira": {
            "Contentamento": -2,
            "Populacao": -1,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Minha espada sera sua, meu senhor.",
                "(+3 de Contentamento, +1 de Populacao, -100 de Dinheiro)"
            ],

            2: [
                "Treinarei seus guardas para que muitos protejam o que antes um so protegia.",
                "(+7 de Contentamento, -70 de Dinheiro)"
            ],

            3: [
                "Entao seguirei pela estrada. Que seu feudo nao precise de mim.",
                "(-2 de Contentamento, -1 de Populacao)"
            ]
        }
    },

    {
        "sprite": 167,
        "dia_minimo": 17,

        "falas": [
            "Meu senhor, os campos comecam a secar.",
            "Posso conduzir um ritual pela chuva, mas precisarei de oferendas.",
            "Alguns acreditarao. Outros dirao que e desperdicio."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Realizar o ritual",
            "opcao_segunda": "Comprar agua",
            "opcao_terceira": "Esperar a chuva"
        },

        "efeito_primeira": {
            "Contentamento": 9,
            "Populacao": 2,
            "Dinheiro": -90
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 3,
            "Dinheiro": -180
        },

        "efeito_terceira": {
            "Contentamento": -8,
            "Populacao": -4,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "As preces subirao com a fumaca das oferendas.",
                "(+9 de Contentamento, +2 de Populacao, -90 de Dinheiro)"
            ],

            2: [
                "A agua chegara em barris. Nao sera barato, mas salvara plantacoes.",
                "(+5 de Contentamento, +3 de Populacao, -180 de Dinheiro)"
            ],

            3: [
                "A terra aguardara. Espero que ela tenha paciencia.",
                "(-8 de Contentamento, -4 de Populacao)"
            ]
        }
    },

    {
        "sprite": 168,
        "dia_minimo": 8,

        "falas": [
            "Meu senhor, os impostos deste mes podem ser aumentados.",
            "Os cofres precisam se fortalecer para decisoes futuras.",
            "Mas o povo ja sente o peso das cobrancas."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Aumentar impostos",
            "opcao_segunda": "Manter como esta",
            "opcao_terceira": "Reduzir impostos"
        },

        "efeito_primeira": {
            "Contentamento": -15,
            "Populacao": -2,
            "Dinheiro": 260
        },

        "efeito_segunda": {
            "Contentamento": 0,
            "Populacao": 0,
            "Dinheiro": 80
        },

        "efeito_terceira": {
            "Contentamento": 14,
            "Populacao": 2,
            "Dinheiro": -120
        },

        "falas_pos": {
            1: [
                "Os cofres ficarao cheios, mas as ruas ficarao amargas.",
                "(-15 de Contentamento, -2 de Populacao, +260 de Dinheiro)"
            ],

            2: [
                "Seguiremos com a cobranca habitual, meu senhor.",
                "(+80 de Dinheiro)"
            ],

            3: [
                "O povo sentira alivio imediato. Os cofres, nem tanto.",
                "(+14 de Contentamento, +2 de Populacao, -120 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 169,
        "dia_minimo": 19,

        "falas": [
            "Meu senhor, cacadores estao entrando fundo demais na floresta.",
            "Se continuarem, os animais desaparecerao e as vilas perderao equilibrio.",
            "Peco limites antes que seja tarde."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Criar area protegida",
            "opcao_segunda": "Permitir caca controlada",
            "opcao_terceira": "Liberar a caca"
        },

        "efeito_primeira": {
            "Contentamento": 6,
            "Populacao": 2,
            "Dinheiro": -70
        },

        "efeito_segunda": {
            "Contentamento": 4,
            "Populacao": 1,
            "Dinheiro": 60
        },

        "efeito_terceira": {
            "Contentamento": -10,
            "Populacao": -3,
            "Dinheiro": 170
        },

        "falas_pos": {
            1: [
                "A floresta tera tempo para respirar. As proximas geracoes notarao.",
                "(+6 de Contentamento, +2 de Populacao, -70 de Dinheiro)"
            ],

            2: [
                "Cacaremos com medida. Nem fome, nem destruicao.",
                "(+4 de Contentamento, +1 de Populacao, +60 de Dinheiro)"
            ],

            3: [
                "A carne sera abundante agora. Depois, talvez so reste silencio.",
                "(-10 de Contentamento, -3 de Populacao, +170 de Dinheiro)"
            ]
        }
    },

    {
        "sprite": 170,
        "dia_minimo": 6,

        "falas": [
            "Meu senhor! Criei pipas enormes que podem levar mensagens pelo vento.",
            "Tambem podem alegrar as criancas nos dias de descanso.",
            "So preciso de bambu, papel e um pouco de confianca."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Apoiar a invencao",
            "opcao_segunda": "Usar so em mensagens",
            "opcao_terceira": "Manda-lo embora"
        },

        "efeito_primeira": {
            "Contentamento": 10,
            "Populacao": 1,
            "Dinheiro": -60
        },

        "efeito_segunda": {
            "Contentamento": -2,
            "Populacao": 0,
            "Dinheiro": -30
        },

        "efeito_terceira": {
            "Contentamento": -3,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "As criancas verao dragoes no ceu, e os mensageiros terao novas rotas.",
                "(+10 de Contentamento, +1 de Populacao, -60 de Dinheiro)"
            ],

            2: [
                "Funciona tambem... mas e triste ver uma pipa sem riso por perto.",
                "(-2 de Contentamento, -30 de Dinheiro)"
            ],

            3: [
                "Certo... talvez outro senhor goste de dragoes voadores.",
                "(-3 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 171,
        "dia_minimo": 5,

        "falas": [
            "Meu senhor, sobras do castelo poderiam alimentar muita gente.",
            "Posso organizar uma cozinha comunitaria para os mais necessitados.",
            "Isso custara pouco, mas exigira ordem e funcionarios."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Criar cozinha comunitaria",
            "opcao_segunda": "Vender sobras baratas",
            "opcao_terceira": "Guardar tudo no castelo"
        },

        "efeito_primeira": {
            "Contentamento": 12,
            "Populacao": 4,
            "Dinheiro": -90
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 1,
            "Dinheiro": 30
        },

        "efeito_terceira": {
            "Contentamento": -9,
            "Populacao": -2,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Ninguem deveria dormir com fome sob um bom governante.",
                "(+12 de Contentamento, +4 de Populacao, -90 de Dinheiro)"
            ],

            2: [
                "Nao sera caridade completa, mas ja aliviara muitas mesas.",
                "(+5 de Contentamento, +1 de Populacao, +30 de Dinheiro)"
            ],

            3: [
                "As panelas do castelo ficarao cheias. As das ruas, talvez nao.",
                "(-9 de Contentamento, -2 de Populacao)"
            ]
        }
    },

    {
        "sprite": 172,
        "dia_minimo": 21,

        "falas": [
            "Meu senhor, cavalos fortes chegaram das planicies.",
            "Com eles, mensageiros, patrulhas e comerciantes viajarao mais rapido.",
            "Mas bons cavalos custam caro."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Comprar cavalos",
            "opcao_segunda": "Comprar poucos",
            "opcao_terceira": "Nao comprar"
        },

        "efeito_primeira": {
            "Contentamento": 8,
            "Populacao": 4,
            "Dinheiro": -300
        },

        "efeito_segunda": {
            "Contentamento": 3,
            "Populacao": 1,
            "Dinheiro": -120
        },

        "efeito_terceira": {
            "Contentamento": -2,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Seu feudo parecera menor quando as noticias correrem a cavalo.",
                "(+8 de Contentamento, +4 de Populacao, -300 de Dinheiro)"
            ],

            2: [
                "Os guardas montarao melhor, ainda que o povo veja pouco beneficio.",
                "(+3 de Contentamento, +1 de Populacao, -120 de Dinheiro)"
            ],

            3: [
                "Entao seguiremos no passo dos proprios pes.",
                "(-2 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 173,
        "dia_minimo": 14,

        "falas": [
            "Meu senhor, meu marido serviu aos guardas do feudo e morreu protegendo a estrada.",
            "Minha familia ficou sem sustento.",
            "Peco que sua lealdade nao seja esquecida."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Conceder pensao",
            "opcao_segunda": "Dar pagamento unico",
            "opcao_terceira": "Negar ajuda"
        },

        "efeito_primeira": {
            "Contentamento": 14,
            "Populacao": 1,
            "Dinheiro": -150
        },

        "efeito_segunda": {
            "Contentamento": 6,
            "Populacao": 0,
            "Dinheiro": -60
        },

        "efeito_terceira": {
            "Contentamento": -14,
            "Populacao": -1,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Meu marido descansara sabendo que sua casa nao foi abandonada.",
                "(+14 de Contentamento, +1 de Populacao, -150 de Dinheiro)"
            ],

            2: [
                "A ajuda aliviara este mes. Depois, veremos como sobreviver.",
                "(+6 de Contentamento, -60 de Dinheiro)"
            ],

            3: [
                "Entao a lealdade dele morreu com ele, meu senhor.",
                "(-14 de Contentamento, -1 de Populacao)"
            ]
        }
    },

    {
        "sprite": 174,
        "dia_minimo": 10,

        "falas": [
            "Meu senhor, proponho um festival de mascaras para atrair visitantes.",
            "Havera musica, teatro e comercio nas ruas.",
            "Pode ser belo, lucrativo... ou uma grande confusao."
        ],

        "qtd_escolhas": {
            "opcao_primeira": "Autorizar o festival",
            "opcao_segunda": "Cobrar entrada",
            "opcao_terceira": "Proibir aglomeracoes"
        },

        "efeito_primeira": {
            "Contentamento": 16,
            "Populacao": 3,
            "Dinheiro": -100
        },

        "efeito_segunda": {
            "Contentamento": 5,
            "Populacao": 1,
            "Dinheiro": 120
        },

        "efeito_terceira": {
            "Contentamento": -10,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "As ruas terao musica, cor e historias ate a lua subir.",
                "(+16 de Contentamento, +3 de Populacao, -100 de Dinheiro)"
            ],

            2: [
                "Havera festa, mas alguns ficarao do lado de fora contando moedas.",
                "(+5 de Contentamento, +1 de Populacao, +120 de Dinheiro)"
            ],

            3: [
                "Guardarei as mascaras. Rostos serios tambem contam uma historia.",
                "(-10 de Contentamento)"
            ]
        }
    },

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
