import pygame
import random
pygame.init()
largura = 800
altura = 300
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Star Wars")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/TrupperIco.ico")
pygameDisplay.set_icon(gameIcon)

bg = pygame.image.load("assets/fundo.png")
bg_destroy = pygame.image.load("assets/bg-destroy.jpeg")
# Aqui Começa o jogo

explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
explosaoSound.set_volume(0.5)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event


def dead(pontos):
    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                         " pontos!", True, black)
    textoContinue = fonteContinue.render(
        "Press enter to continue...", True, white)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()


def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 1
    posicaoXNave = 500
    posicaoYNave = 100
    movimentoXNave = 0
    movimentoYNave = 0
    pontos = 0
    missile = pygame.image.load("assets/missile.png")
    nave = pygame.image.load("assets/nave.png")
    missile = pygame.transform.flip(missile, True, False)
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    missileSound = pygame.mixer.Sound("assets/missile.wav")
    missileSound.set_volume(1)
    pygame.mixer.Sound.play(missileSound)

    alturaNave = 150
    larguraNave = 217
    alturaMissel = 52
    larguraMissel = 150
    dificuldade = 29
    jogando = True
    while True:
        # aqui é lido os eventos da tela
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXNave = - 10
                elif event.key == pygame.K_RIGHT:
                    movimentoXNave = 10
                elif event.key == pygame.K_UP:
                    movimentoYNave = -10
                elif event.key == pygame.K_DOWN:
                    movimentoYNave = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXNave = 0
                    movimentoYNave = 0

        if jogando == True:
            # travando o movimento na tela
            posicaoXNave = posicaoXNave + movimentoXNave
            posicaoYNave = posicaoYNave + movimentoYNave
            if posicaoXNave < 0:
                posicaoXNave = 0
            elif posicaoXNave >= largura - larguraNave:
                posicaoXNave = largura - larguraNave

            if posicaoYNave < 0:
                posicaoYNave = 0
            elif posicaoYNave >= altura - alturaNave:
                posicaoYNave = altura - alturaNave

            # aqui termina a leitura de eventos
            # gameDisplay.fill(pink)
            gameDisplay.blit(bg, (0, 0))

            if direcao == True:
                if posicaoX < largura-150:
                    posicaoX = posicaoX + velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    direcao = False
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    missile = pygame.transform.flip(missile, True, False)
                    pontos = pontos + 1
            else:
                if posicaoX >= 0:
                    posicaoX = posicaoX - velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    direcao = True
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    missile = pygame.transform.flip(missile, True, False)
                    pontos = pontos + 1

            gameDisplay.blit(missile, (posicaoX, posicaoY))
            gameDisplay.blit(nave, (posicaoXNave, posicaoYNave))
            # pygame.draw.circle(
            #    gameDisplay, black, [posicaoX, posicaoY], 20, 0)
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 20))

            # análise de colisão (modelo 1)
            '''
            naveRect = nave.get_rect()
            naveRect.x = posicaoXNave
            naveRect.y = posicaoYNave

            missileRect = missile.get_rect()
            missileRect.x = posicaoX
            missileRect.y = posicaoY

            if naveRect.colliderect(missileRect):
                dead(pontos)
            else:
                print("ainda vivo...")
            '''
            # análise de colisão (modelo 2)

            pixelsYNave = list(
                range(posicaoYNave, posicaoYNave + alturaNave+1))
            pixelsXNave = list(
                range(posicaoXNave, posicaoXNave + larguraNave+1))

            pixelsYMissel = list(range(posicaoY, posicaoY+alturaMissel+1))
            pixelsXMissel = list(range(posicaoX, posicaoX+larguraMissel+1))

            # comparar e mostrar elementos iguais em duas listas
            # print(len(list(set(pixelsYMissel) & set(pixelsYNave))))

            if len(list(set(pixelsYMissel) & set(pixelsYNave))) > dificuldade:
                if len(list(set(pixelsXMissel) & set(pixelsXNave))) > dificuldade:
                    jogando = False
                    dead(pontos)

        pygameDisplay.update()
        clock.tick(60)


jogo()
