import pygame
import sys

# CONFIGURAÇÃO TELA 
mais_altura = 840
LARGURA, ALTURA = 860, 400
FUNDO = (20, 9, 0)

# Configuracao imagens
pygame.init()
tela = pygame.display.set_mode((LARGURA, mais_altura))
pygame.display.set_caption("Autômato - Ovelha, Lobo e Feno")
fonte = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()
diagrama = pygame.image.load("diagramamolde.png")
diagrama = pygame.transform.scale(diagrama, (835, 230))
agua = pygame.image.load("agua_pixelart.jpg")
agua = pygame.transform.scale(agua, (150, 150))
grama = pygame.image.load("grama.jpg")
grama = pygame.transform.scale(grama, (200, 200))
lobo = pygame.image.load("cachorro_pixelart.png")
lobo = pygame.transform.scale(lobo, (40, 72))
lobo_leg = pygame.transform.scale(lobo, (27, 48))
ovelha = pygame.image.load("ovelha_pixelart.png")
ovelha = pygame.transform.scale(ovelha, (54, 46))
ovelha_leg = pygame.transform.scale(ovelha, (40, 35))
feno = pygame.image.load("feno_pixelart.png")
feno = pygame.transform.scale(feno, (40, 40))
feno_leg = pygame.transform.scale(feno, (32, 32))
fazendeiro = pygame.image.load("fazendeiro_pixelart.png")
fazendeiro = pygame.transform.scale(fazendeiro, (100, 100))
fazendeiro_leg = pygame.transform.scale(fazendeiro, (50, 50))
teste = pygame.image.load("fundo2.png")
teste = pygame.transform.scale(teste, (800, 151))
moldura= pygame.image.load("moldura.png")
moldura = pygame.transform.scale(moldura, (LARGURA, mais_altura))
moldura_diagrama= pygame.image.load("diagramamolde.png")
moldura_diagrama = pygame.transform.scale(moldura_diagrama, (835, 230))
q0 = pygame.image.load("q0.png")
q0 = pygame.transform.scale(q0, (835, 230))
q1 = pygame.image.load("q1.png")
q1 = pygame.transform.scale(q1, (835, 230))
q2 = pygame.image.load("q2.png")
q2 = pygame.transform.scale(q2, (835, 230))
q3 = pygame.image.load("q3.png")
q3 = pygame.transform.scale(q3, (835, 230))
q4 = pygame.image.load("q4.png")
q4 = pygame.transform.scale(q4, (835, 230))
q5 = pygame.image.load("q5.png")
q5 = pygame.transform.scale(q5, (835, 230))
q6 = pygame.image.load("q6.png")
q6 = pygame.transform.scale(q6, (835, 230))
q7 = pygame.image.load("q7.png")
q7 = pygame.transform.scale(q7, (835, 230))
q8 = pygame.image.load("q8.png")
q8 = pygame.transform.scale(q8, (835, 230))
q9 = pygame.image.load("q9.png")
q9 = pygame.transform.scale(q9, (835, 230))
barco = pygame.image.load("barco.png")
barco = pygame.transform.scale(barco, (120, 144))
estado_0 = pygame.image.load("estado_0.png")
estado_0 = pygame.transform.scale(estado_0, (70, 75))
estado_l = pygame.image.load("estado_l.png")
estado_l = pygame.transform.scale(estado_l, (70, 75))
estado_f = pygame.image.load("estado_f.png")
estado_f = pygame.transform.scale(estado_f, (70, 75))
estado_o = pygame.image.load("estado_o.png")
estado_o = pygame.transform.scale(estado_o, (70, 75))
estado_s = pygame.image.load("estado_s.png")
estado_s = pygame.transform.scale(estado_s, (70, 75))



# Configuracaos estados
estados = [
    [1,-2,-1,-1],
    [0,-3,-5,2],
    [-4,3,5,1],
    [4,2,-5,-1],
    [3,-3,7,-2],
    [6,-3,2,-2],
    [5,7,-5,-1],
    [-4,6,4,8],
    [9,-3,-5,7],
    [8,-2,-1,-1]
]

# configuracao persoangens
personagens = {
    "O": {"pos": "E"},  # Ovelha
    "L": {"pos": "E"},  # Lobo
    "F": {"pos": "E"},  # Feno
    "S": {"pos": "E"}   # Senhor
}

# Funcao desenho
def desenhar(estado, sequencia, mensagem, acao):
    tela.fill(FUNDO)  # fundo

    # margens
    tela.blit(grama, (30, 30))        #Grama margem direita
    tela.blit(grama, (30, 230))

    tela.blit(agua, (230, 30))       #Rio
    tela.blit(agua, (380, 30))
    tela.blit(agua, (530, 30))
    tela.blit(agua, (230, 180))
    tela.blit(agua, (380, 180))
    tela.blit(agua, (530, 180))
    tela.blit(agua, (230, 330))
    tela.blit(agua, (380, 330))
    tela.blit(agua, (530, 330))

    tela.blit(grama, (LARGURA-230, 30))      #Grama margem esquerdar
    tela.blit(grama, (LARGURA-230, 230))
    
    

    # barco
    barco_x = 230 if personagens["S"]["pos"] == "E" else LARGURA-350
    tela.blit(barco, (barco_x , ALTURA//2 - 50))
    
    tela.blit(teste, (30, 660))
    tela.blit(lobo_leg, (670, 685))
    tela.blit(ovelha_leg, (760, 690))
    tela.blit(feno_leg, (670, 740))
    tela.blit(fazendeiro_leg, (755, 730))

    tela.blit(moldura, (0, 0))
    tela.blit(moldura_diagrama, (15, 440))

    if estado == 0:
        tela.blit(q0, (15, 440))
    elif estado == 1:
        tela.blit(q1, (15, 440))
    elif estado == 2:
        tela.blit(q2, (15, 440))
    elif estado == 3:
        tela.blit(q3, (15, 440))
    elif estado == 4:
        tela.blit(q4, (15, 440))
    elif estado == 5:
        tela.blit(q5, (15, 440))
    elif estado == 6:
        tela.blit(q6, (15, 440))
    elif estado == 7:
        tela.blit(q7, (15, 440))
    elif estado == 8:
        tela.blit(q8, (15, 440))
    elif estado == 9:
        tela.blit(q9, (15, 440))
    else:
        tela.blit(diagrama, (15, 440))

    

    # desenhar personagens
    x_left, x_right = 80, LARGURA-150
    y_start = 80
    gap = 50

    for i, (p, data) in enumerate(personagens.items()):
        x = x_left if data["pos"] == "E" else x_right
        y = y_start + i*gap
        if p == "O":
            tela.blit(ovelha, (x,y))
        elif p == "L":
            y += 15
            tela.blit(lobo, (x,y))
        elif p == "F":
            y += 50
            tela.blit(feno, (x,y))
        elif p == "S":
            y += 50
            tela.blit(fazendeiro, (x-30,y))

    if acao == "":
        tela.blit(estado_0, (400,40))
    elif acao == "f":
        tela.blit(estado_f, (400,40))
    elif acao == "l":
        tela.blit(estado_l, (400,40))
    elif acao == "o":
        tela.blit(estado_o, (400,40))
    elif acao == "s":
        tela.blit(estado_s, (400,40))

    fonte = pygame.font.Font(None, 32)
    superficie_texto = fonte.render(sequencia, True, (0, 0, 0))
    tela.blit(superficie_texto, (165, 700))

    superficie_mensagem = fonte.render(mensagem, True, (0, 0, 0))
    tela.blit(superficie_mensagem, (70, 760))

    pygame.display.flip()


def main():
    mensagem = "Inicio"
    atual = 0
    idx = 0  # índice da ação
    sequencia = ""
    desenhar(atual, sequencia, mensagem, "")

    sequencia = ""
    fonte = pygame.font.Font(None, 32)

    rodando = True
    while rodando:
        for evento in pygame.event.get():

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando = False
                elif evento.key == pygame.K_BACKSPACE:
                    sequencia = sequencia[:-1]
                else:
                    sequencia += evento.unicode

        superficie_texto = fonte.render(sequencia, True, (0, 0, 0))
        tela.blit(superficie_texto, (165, 700))
        pygame.display.flip()

    mensagem = "Em processo"

    rodando = True
    while rodando:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # só processa enquanto houver ações
        if idx < len(sequencia):
            acao = sequencia[idx]

            if acao == 'o':
                prox = estados[atual][0]
            elif acao == 'l':
                prox = estados[atual][1]
            elif acao == 'f':
                prox = estados[atual][2]
            elif acao == 's':
                prox = estados[atual][3]
            else:
                mensagem = "Erro"
                rodando = False
                desenhar(atual, sequencia, mensagem, acao)
                break

            if prox < 0:
                if prox == -1 or prox == -2:
                    mover = None
                    if acao == "o": mover = "O"
                    elif acao == "l": mover = "L"
                    elif acao == "f": mover = "F"
                    mover_list = ["S"] + ([mover] if mover else [])

                    for p in mover_list:
                        personagens[p]["pos"] = "D" if personagens[p]["pos"] == "E" else "E"

                    if prox == -1:
                        mensagem = "Entrada Invalida. O Lobo comeu a Ovelha"
                    else:
                        mensagem = "Entrada Invalida. A Ovelha come o Feno"
                elif prox == -3:
                    mensagem = "Entrada Invalida. O fazendeiro está longe do Lobo"
                elif prox == -4:
                    mensagem = "Entrada Invalida. O fazendeiro está longe da Ovelha"
                elif prox == -5:
                    mensagem = "Entrada Invalida. O fazendeiro está longe do Feno"

                rodando = False
                desenhar(prox, sequencia, mensagem, acao)
                pygame.time.delay(1000)
                break

            # define quem vai atravessar
            mover = None
            if acao == "o": mover = "O"
            elif acao == "l": mover = "L"
            elif acao == "f": mover = "F"
            mover_list = ["S"] + ([mover] if mover else [])

            for p in mover_list:
                personagens[p]["pos"] = "D" if personagens[p]["pos"] == "E" else "E"

            atual = prox
            idx += 1

            # desenha depois de cada movimento
            desenhar(atual, sequencia, mensagem, acao)
            pygame.time.delay(1000)  # espera 1.0s para ver o movimento

        else:
            # terminou a sequência
            if atual == 9:
                mensagem = "Entrada Valida"
            else:
                mensagem = "Entrada Invalida. Não chegou ao final"
            rodando = False

            desenhar(atual, sequencia, mensagem, acao)

        clock.tick(30)

    # mantém a janela aberta no final
    fim = True
    while fim:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()
