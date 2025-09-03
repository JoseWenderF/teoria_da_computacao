import pygame
import sys

# CONFIGURAÇÃO TELA 
mais_altura = 1030
LARGURA, ALTURA = 860, 400
FUNDO = (20, 9, 0)

# Configuracao imagens
pygame.init()
tela = pygame.display.set_mode((LARGURA, mais_altura))
pygame.display.set_caption("Autômato - Chapeuzinho Vermelho")
fonte = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()
diagrama = pygame.image.load("diagramamolde.png")
diagrama = pygame.transform.scale(diagrama, (835, 230))
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
estado_0 = pygame.image.load("estado_0.png")
estado_0 = pygame.transform.scale(estado_0, (70, 75))
estado_m = pygame.image.load("estado_m.png")
estado_m = pygame.transform.scale(estado_m, (70, 75))
estado_f = pygame.image.load("estado_f.png")
estado_f = pygame.transform.scale(estado_f, (70, 75))
estado_c = pygame.image.load("estado_c.png")
estado_c = pygame.transform.scale(estado_c, (70, 75))
estado_v = pygame.image.load("estado_v.png")
estado_v = pygame.transform.scale(estado_v, (70, 75))
estado_q = pygame.image.load("estado_q.png")
estado_q = pygame.transform.scale(estado_q, (70, 75))

i0 = pygame.image.load("i0.png")
i0 = pygame.transform.scale(i0, (880, 440))
i1 = pygame.image.load("i1.png")
i1 = pygame.transform.scale(i1, (800, 440))
i2 = pygame.image.load("i2.png")
i2 = pygame.transform.scale(i2, (800, 440))
i3 = pygame.image.load("i3.png")
i3 = pygame.transform.scale(i3, (800, 440))
i4 = pygame.image.load("i4.png")
i4 = pygame.transform.scale(i4, (800, 440))
i5 = pygame.image.load("i5.png")
i5 = pygame.transform.scale(i5, (800, 440))

legenda = pygame.image.load("legenda.png")
legenda = pygame.transform.scale(legenda, (800, 200))

des = pygame.image.load("fundo2_old.png")
des = pygame.transform.scale(des, (750, 55))





# Configuracaos estados
estados = [
    [1,-1,-1,-1, -1],
    [-1,2,-1,-1, -1],
    [-1,-1,3,-1, -1],
    [-1,-1,-1, 4, -1],
    [-1,-1,-1,-1, 5],
    [-1,-1,-1,-1, -1],
    
]


# Funcao desenho
def desenhar(estado, sequencia, mensagem, acao):
    tela.fill(FUNDO)  # fundo

    #ilustrações
    

    #input    
    tela.blit(teste, (30, 660))


    leg = ""
    leg2 = ""

    #ilustrações
    if estado == 0:
        leg = "Chapeuzinho está em casa com sua mãe"
        tela.blit(i0, (30, 30))
        tela.blit(moldura, (0, 0))
        tela.blit(q0, (15, 440))
    elif estado == 1:
        leg = "Chapeuzinho vai para a floresta e encontra o Lobo Mau."
        tela.blit(i1, (30, 30))
        tela.blit(moldura, (0, 0))
        tela.blit(q1, (15, 440))
    elif estado == 2:
        leg = "O lobo pega um atalho e chega antes na casa da vovozinha,"
        leg2 = "fingindo ser a Chapeuzinho."
        tela.blit(i2, (30, 30))
        tela.blit(moldura, (0, 0))
        tela.blit(q2, (15, 440))
    elif estado == 3:
        leg = " lobo entra na casa da vovozinha, tranca ela no armário e vesti as roupas dela "
        leg2 = "para enganar a chapeuzinho."
        tela.blit(i3, (30, 30))
        tela.blit(moldura, (0, 0))
        tela.blit(q3, (15, 440))
    elif estado == 4:
        leg = "O lobo tenta atacar a chapeuzinho."
        tela.blit(i4, (30, 30))
        tela.blit(moldura, (0, 0))
        tela.blit(q4, (15, 440))
    elif estado == 5:
        leg = "Um caçador que estava por perto ajuda chapeuzinha e sua avó,"
        leg2 = "levando o lobo e salvando as duas."
        tela.blit(i5, (30, 30))
        tela.blit(moldura, (0, 0))
        tela.blit(q5, (15, 440))
    else:
        tela.blit(moldura, (0, 0))
        tela.blit(diagrama, (15, 440))

    fonte = pygame.font.Font(None, 25)
    tela.blit(des, (60, 390))
    superficie_texto = fonte.render(leg, True, (0, 0, 0))
    tela.blit(superficie_texto, (80, 400))
    superficie_texto = fonte.render(leg2, True, (0, 0, 0))
    tela.blit(superficie_texto, (80, 420))


    # cavecote
    if acao == "":
        tela.blit(estado_0, (750,40))
    elif acao == "f":
        tela.blit(estado_f, (750,40))
    elif acao == "m":
        tela.blit(estado_m, (750,40))
    elif acao == "v":
        tela.blit(estado_v, (750,40))
    elif acao == "c":
        tela.blit(estado_c, (750,40))
    elif acao == "q":
        tela.blit(estado_q, (750,40))

    tela.blit(legenda, (30, 800))

    m = "A mãe de chapeuzinho pede para ela ir entregar os doces para a vovozinha."
    f = "Chapeuzinho fala para o lobo que ela está indo para casa da vovozinha."
    v = "A vovozinha abre a porta para o lobo."
    c1 = "Ao chegar na casa do vovozinho e encontrar o lobo na cama, Chapeuzinho" 
    c2 = "fala sobre a aparência do Lobo Mau."
    q = "Chapeuzinho grita por ajuda."

    superficie_texto = fonte.render(m, True, (0, 0, 0))
    tela.blit(superficie_texto, (120, 830))

    superficie_texto = fonte.render(f, True, (0, 0, 0))
    tela.blit(superficie_texto, (120, 855))

    superficie_texto = fonte.render(v, True, (0, 0, 0))
    tela.blit(superficie_texto, (120, 885))

    superficie_texto = fonte.render(c1, True, (0, 0, 0))
    tela.blit(superficie_texto, (120, 910))
    superficie_texto = fonte.render(c2, True, (0, 0, 0))
    tela.blit(superficie_texto, (120, 930))

    superficie_texto = fonte.render(q, True, (0, 0, 0))
    tela.blit(superficie_texto, (120, 960))

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

            if acao == 'm':
                prox = estados[atual][0]
            elif acao == 'f':
                prox = estados[atual][1]
            elif acao == 'v':
                prox = estados[atual][2]
            elif acao == 'c':
                prox = estados[atual][3]
            elif acao == 'q':
                prox = estados[atual][4]
            else:
                mensagem = "Erro. Simbolo não pertence ao alfabeto"
                rodando = False
                desenhar(atual, sequencia, mensagem, acao)
                break

            if prox == -1:
                mensagem = "Entrada Invalida. Não existe esse estado na história"
                rodando = False
                desenhar(prox, sequencia, mensagem, acao)
                pygame.time.delay(1000)
                break

            atual = prox
            idx += 1

            # desenha depois de cada movimento
            desenhar(atual, sequencia, mensagem, acao)
            pygame.time.delay(1000)  # espera 1.0s para ver o movimento

        else:
            # terminou a sequência
            if atual == 5:
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
