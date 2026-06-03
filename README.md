# 100 Days of Shogun
<img width="2172" height="724" alt="Banner do projeto 100 Days of Shogun" src="https://github.com/user-attachments/assets/e279e2b4-7c0a-4c66-934f-5ccd50240016" />

## Sobre o Projeto

**100 Days of Shogun** é um jogo indie 2D desenvolvido em **Python**, com uso da biblioteca **Pygame**, inspirado no estilo de jogo **Reigns**.

No jogo, o jogador controla um governante em Takayama, durante a era feudal japonesa, tomando decisões que afetam diretamente o seu reinado. Cada escolha influencia os medidores de contentamento do povo, população e dinheiro, exigindo equilíbrio e estratégia para manter o governo estável.

## Objetivo do Jogo

O objetivo do jogador é acumular o máximo de pontos possível até alcançar a era de ouro. Para isso, é necessário controlar cuidadosamente os recursos do reino.

Caso os medidores fiquem muito baixos, o jogador poderá ser deposto do cargo, sofrer um golpe ou até mesmo ser executado.

## Funcionalidades

* Eventos aleatórios
* Interação com NPCs
* Escolhas com consequências
* Gerenciamento de recursos
* Finais alternativos
* Sistema de passagem de dias

## Tecnologias Utilizadas

* Python
* Pygame
* Pixel art para sprites, cenários e interface

## Estrutura do Projeto

```text
Projeto/
│
├── main.py
├── dias.py
├── pontos.py
├── eventos.py
├── dialogo.py
│
├── Imagens/
│   ├── Calendario/
│   └── Personagens/
│
└── README.md
```

## Adaptações do projeto

A entrada de dados por parte do usuário é coletada por meio de uma função do Pygame, `pg.event.get()`, em vez do `input`. Da mesma forma, utilizamos a função `blit`, também do Pygame, para exibir imagens na tela, substituindo o uso do `print`.
Utilizamos dicionários para armazenar informações do mesmo tipo que possuem valores diferentes, como os pontos, além de também utilizá-los para armazenar os eventos. Já as listas foram utilizadas majoritariamente para armazenar os balões de fala dos personagens, além de uma lista principal usada para armazenar os dicionários de eventos.


## Status do Projeto

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## Autores

* Diego Rhian Bochnia
* João Pedro M. Spielmann
* Lucas R. Frois
* Wellington Nery G. Costa

## Direitos

Todos os direitos reservados.
