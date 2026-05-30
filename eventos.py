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
                "(+20 de Contentamento)"

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
                "(+10 de População, -20 de Dinheiro)"

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
                "(-5 de Contentamento)"
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
                "(-5 de Contentamento)"

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
                "(-5 de Contentamento)"
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
                "(+5 de Contentamento)"

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
                "(+5 de Contentamento, +10 de População, -50 de Dinheiro)"
            ],

            2: ["Aqui estão senhor! Caso precise de mais sabe onde me encontrar",
                "Glória à Takayama",
                "(+10 de Contentamento, +20 de População, -100 de Dinheiro)"

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
            "Olá grande shogun, eu sou Karasu, um guerreiro que ainda não tem feitos, porém muita vontade e corajem para lutar.",
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
                "(+100 de Dinheiro)"
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
                "(10 de Contentamento, 5 de População, -20 de Dinheiro)"
            ],

            2: ["Oh, que ótimo! Vou cuidar dos cidadãos com muito carinho e dedicação!",
                "(15 de Contentamento, 10 de População, -50 de Dinheiro)"

            ],

            3: [
                "OH, que ótimo! Vou fazer o melhor hospital para a saúde da nação!",
                "(20 de Contentamento, 15 de População, -100 de Dinheiro)"
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
                "Entendo, talvez outra hora seja melhor..."
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
            "Dinheiro": 50
        },

        "efeito_terceira": {
            "Contentamento": 20,
            "Populacao": 10,
            "Dinheiro":-100
        },

        "efeito_quarta": {
            "Contentamento": -10,
            "Populacao": 0,
            "Dinheiro": 0
        },

        "falas_pos": {
            1: [
                "Muito obrigado senhor! Minhas obras de arte trarão beleza e cultura para a cidade!",
                "(10 de Contentamento, 1 de População, -30 de Dinheiro)"
            ],

            2: [
                "Muito obrigado senhor! Meus utensílios de cerâmica serão muito úteis para a população!",
                "(15 de Contentamento, 5 de População, 50 de Dinheiro)"

            ],

            3: [
                "Muito obrigado senhor! Nossa parceria criará um museu incrível para a cidade!",
                "(20 de Contentamento, 10 de População, -100 de Dinheiro)"
            ],

            4: [
                "Entendo, talvez outra hora seja melhor...",
                "( -10 de Contentamento)"
            ]
        }
    },

    {
        "sprite": 18,

        "dia_minimo": 4,

        "falas": [
            "Com sua licença shogun, sou uma mensageira de outro feuo.",
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
                "Muito obrigado por ouvir minha mensagem, senhor. ",
                "A mensagem é a seguinte: 'O feudo vizinho está planejando um ataque surpresa contra o seu feudo, eles estão se preparando para atacar em breve, então esteja preparado para se defender.'",
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
                "( -5 de Contentamento,  -10 de População)"
            ],
        }
    },

    {
        "sprite": 20,

        "dia_minimo": 3,

        "falas": [
            "Olá caro shogun, sou um pintor e vim oferecer meus serviços a ti."
            "Posso criar belas pinturas para decorar a cidade, ou posso criar retratos de pessoas importantes para a história da cidade. O que acha?"
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
