import pygame as pg
import random
 
pg.init()
pg.display.set_caption('Pexeso') 
size = 800
screen = pg.display.set_mode((size, size))
done = False
cardsDeck = [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]
cardsPos = [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]
colors = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
cards = [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]

def defineColors():
    for i in range(0, 32):
        colors[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def createCardsDeck():
    num = 0

    for i in range(0, 8):
        for j in range(0, 8):
            cardsDeck[i][j] = num
            num+=1
            if num == 31:
                num=0

    for i in range (0, 8):
        random.shuffle(cardsDeck[i])        

def createCards():
    defineColors()
    createCardsDeck()

    for i in range(0, 8):
        for j in range(0, 8):
            cards[i][j] = [cardsDeck[i][j], (int(100*i), int(100*j)), colors[cardsDeck[i][j]], False]

def drawCards():
    tmp = 0

    for i in range(0, 8):
        for j in range(0, 8):
            pg.draw.rect(screen, (100,100,100), (100*i, 100*j, 99, 99))
            cardsPos[i][j] = (int(100*i), int(100*j))
            if tmp == 31:
                tmp=0
            tmp+=1

createCards()            
drawCards()



print(cards)

iBefore = 0
jBefore = 0
pick = []
turn = 0

while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                        done = True

            if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mousePos = pg.mouse.get_pos()
                            mousePosX = str(mousePos[0])
                            mousePosY = str(mousePos[1])

                            while len(mousePosX) < 3:
                                mousePosX = "0" + mousePosX

                            while len(mousePosY) < 3:
                                mousePosY = "0" + mousePosY

                            mousePos = (int(mousePosX[:1])*100, int(mousePosY[:1])*100)
                            

                            for i in range(0, 8):
                                for j in range(0, 8):
                                    if cards[i][j][1] == mousePos and cards[i][j][3] == False:
                                        if turn == 0:
                                            pick = cards[i][j]
                                            iBefore = i
                                            jBefore = j
                                            pg.draw.rect(screen, cards[i][j][2], (int(mousePosX[:1])*100, int(mousePosY[:1])*100, 99, 99))
                                            turn = 1
                                        
                                        print(pick)
                                        if turn == 1 and mousePos != pick[1]:
                                            if pick[0] == cards[i][j][0]:
                                                cards[i][j][3] = True
                                                cards[iBefore][jBefore][3] = True
                                                pick = []
                                                pg.draw.rect(screen, cards[i][j][2], (int(mousePosX[:1])*100, int(mousePosY[:1])*100, 99, 99))
                                                turn = 0
                                            
                                            else:
                                                pg.draw.rect(screen, cards[i][j][2], (int(mousePosX[:1])*100, int(mousePosY[:1])*100, 99, 99))
                                                pg.display.flip()
                                                pg.time.delay(1000)
                                                pg.draw.rect(screen, (100,100,100), (pick[1][0], pick[1][1], 99, 99))
                                                pick = 69
                                                pg.draw.rect(screen, (100,100,100), (int(mousePosX[:1])*100, int(mousePosY[:1])*100, 99, 99))
                                                turn = 0                                                  

        pg.display.flip()