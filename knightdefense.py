


#1-import library

import pygame
from pygame.locals import *
from sys import exit
import random

#2-Initialize the game
pygame.mixer.init(44100,16,2,4096)
pygame.init()
pygame.font.init()
width, height = 600, 720
screen=pygame.display.set_mode((width, height))
display = pygame.display.set_mode((600, 720), 0, 32)
pygame.display.set_caption("knight defense")
speed = 40
X = 202
Y = 480
scoreboard = 0
totalscoreboard = 0
healthbar = 300
intro = True
balltimer = 50
cannonballlist = [[130,-60]]
health_minus_cnbl = 30
health_minus_cnbl_less = 20
dragontimer = 250
dragonlist = []
health_minus_dragon = 50
health_minus_dragon_less = 30
fireballtimer = 251
fireballlist = []
health_minus_fire = 40
health_minus_fire_less = 25
shieldballtimer = 150
shieldballlist = []
health_minus_scnbl = 30
health_minus_scnbl_less = 15
cnblshieldtimer = 151
cnblshieldlist = []
healthtimer = random.randint(1000,2000)
healthlist = []
highscore = 0

#3 - load images
background = pygame.image.load("Mygame/images/background.png")
castle = pygame.image.load("Mygame/images/castle300.png")
knight = pygame.image.load("Mygame/images/knight1.png")
knight2 = pygame.image.load("Mygame/images/knight2.png")
cannonball = pygame.image.load("Mygame/images/cannonball300.png")
cannon = pygame.image.load("Mygame/images/cannon300.png")
sword = pygame.image.load("Mygame/images/sword300.png")
shield = pygame.image.load("Mygame/images/shield3300.png")
knightdefense = pygame.image.load("Mygame/images/knightdefense400.png")
start = pygame.image.load("Mygame/images/start300.png")
shop = pygame.image.load("Mygame/images/shop300.png")
presss = pygame.image.load("Mygame/images/presss100.png")
pressk = pygame.image.load("Mygame/images/pressk100.png")
hppic = pygame.image.load("Mygame/images/0hppic200.png")
dragon = pygame.image.load("Mygame/images/dragon200.png")
fireball = pygame.image.load("Mygame/images/fireball100.png")
shieldball = pygame.image.load("Mygame/images/shieldcannonball300.png")
plus_health = pygame.image.load("Mygame/images/heart300.png")

pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#4 - starting screen
while intro:
# 4.1 - quit the game
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit() 

# 4.2 - start screen draw background screen element
    screen.fill(0)
    screen.blit(background,(0,0))
    screen.blit(knightdefense,(100,-50))
    screen.blit(start, (150,150))
    screen.blit(presss, (250,325))
    screen.blit(shop, (150,300))
    screen.blit(pressk, (250,460))

    myfont = pygame.font.SysFont('Comic Sans MS', 60)
    howtoplay = myfont.render('how to play', False, (0,0,0))
    screen.blit(howtoplay, (150,500))

    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    pressv = myfont.render('press "v" to visit how to play', False, (0,0,0))
    screen.blit(pressv, (160,580))

    screen.blit(knight, (-50,580))
    screen.blit(cannon, (0,550))
    screen.blit(cannonball, (50,550))
    screen.blit(castle, (250,430))
    screen.blit(dragon, (385,260))
    screen.blit(fireball, (25,325))

    

    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    the_highscore = myfont.render(f'Highscore: {highscore}', False, (0,0,0))
    screen.blit(the_highscore, (0,0))
    version = myfont.render('v 2.5.01', False, (0,0,0))
    screen.blit(version, (550,695))

    Key = pygame.key.get_pressed()
    pygame.display.update()

#5 - branching out from the start menu
# 5.1 - how to play menu
    if Key[K_v]:
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() 
                    exit()
            screen.fill(0)
            screen.blit(background,(0,0))
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            line1 = myfont.render('Objective:', False, (0,0,0))
            screen.blit(line1, (275,25))
            line2 = myfont.render('You are playing as the knight and you need to defend', False, (0,0,0))
            screen.blit(line2, (50,50))
            line3 = myfont.render('the castle from being attacked', False, (0,0,0))
            screen.blit(line3, (50,75))
            line4 = myfont.render('Controls:', False, (0,0,0))
            screen.blit(line4, (275,125))
            line5 = myfont.render('Keyboard button "a" and "d" -move the knight ', False, (0,0,0))
            screen.blit(line5, (50,150))
            line6 = myfont.render('left and right', False, (0,0,0))
            screen.blit(line6, (50,175))
            screen.blit(knight, (140,140))
            line7 = myfont.render('Keyboard button "j" -use shield to protect the castle', False, (0,0,0))
            screen.blit(line7, (50,275))
            line8 = myfont.render('against cannonballs and fire', False, (0,0,0))
            screen.blit(line8, (50,302))
            screen.blit(shield, (250,175))
            line9 = myfont.render('Keyboard button "l" -use sword to ', False, (0,0,0))
            screen.blit(line9, (50,350))
            line10 = myfont.render('pierce shields and defeat dragons', False, (0,0,0))
            screen.blit(line10, (50, 375))
            screen.blit(sword, (270,235))
            screen.blit(plus_health, (325, 250))
            line11 = myfont.render('Collecting the heart will give the castle health', False, (0,0,0))
            screen.blit(line11, (50,425))
            line12 = myfont.render('You can buy upgrades in the shop', False, (0,0,0))
            screen.blit(line12, (50, 450))
            line13 = myfont.render('If anything touches the castle, it will lose some hp', False, (0,0,0))
            screen.blit(line13, (50,475))
            line14 = myfont.render("However, if anything touches the knight, it's game", False, (0,0,0))
            screen.blit(line14, (50,500))
            line15 = myfont.render('over immediately', False, (0,0,0))
            screen.blit(line15, (50,525))
            line16 = myfont.render('Good Luck!', False, (0,0,0))
            screen.blit(line16, (50,550))
            line17 = myfont.render('(press "q" mid-game to exit back to main menu)', False, (0,0,0))
            screen.blit(line17, (50,575))
            line18 = myfont.render('press "q" to go back', False, (0,0,0))
            screen.blit(line18, (375,675))
            pygame.display.update()
            Key = pygame.key.get_pressed()
            if Key[K_q]:
                break
# 5.2 - the shop items
    if Key[K_k]:
        while True:
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            buyknight = myfont.render('to buy knight press "c"', False, (0,0,0))
            goldknight = myfont.render('golden knight skin', False, (255,140,0))
            morehp = myfont.render('more hp for castle', False, (225,0,0))
            buycastlehp = myfont.render('to buy castle hp press "m"', False, (0,0,0))
            myfont1 = pygame.font.SysFont('Oswald', 30)
            totalscore = myfont1.render('Total score: ' + str(totalscoreboard), False, (0,0,0))
            scoreneeded = myfont1.render('Score needed: 200', False, (0,0,0))
            myfont2 = pygame.font.SysFont('Ultra', 40)
            bought = myfont2.render('BOUGHT', False, (0,0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() 
                    exit()
            screen.fill(0)
            screen.blit(background, (0,0))
            screen.blit(totalscore, (433,10))
            screen.blit(goldknight, (300,78))
            screen.blit(scoreneeded, (300,110))
            screen.blit(buyknight, (300,125))
            screen.blit(knight2, (-10,30))
            screen.blit(castle, (10,10))
            pygame.draw.rect(screen, (225,0,0), (55,265,200,20))
            screen.blit(morehp, (355,220))
            screen.blit(scoreneeded, (355,250))
            screen.blit(buycastlehp, (355,265))
            linebreak = myfont.render('press "q" to go back', False, (0,0,0))
            screen.blit(linebreak, (375,675))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==K_c:
                        if knight == knight2:
                            continue
                        if totalscoreboard >= 200:
                            knight = knight2
                            totalscoreboard -= 200
                    if event.key==K_m:
                        if health_minus_cnbl == health_minus_cnbl_less:
                            continue
                        if totalscoreboard >= 200:
                            health_minus_cnbl = health_minus_cnbl_less
                            health_minus_dragon = health_minus_dragon_less
                            health_minus_fire = health_minus_fire_less 
                            health_minus_scnbl = health_minus_scnbl_less 
                            totalscoreboard -= 200
            if knight == knight2:
                screen.blit(bought, (20,110))
            if health_minus_cnbl == health_minus_cnbl_less:
                screen.blit(bought, (100,262))
            pygame.display.update()
            Key = pygame.key.get_pressed()
            if Key[K_q]:
                break
                
#5.3 - start game
#5.3.1 - quit
    if Key[K_s]:
        balltimer = 100
        cannonballlist=[[130,-60]]
        scoreboard = 0
        healthbar = 300
        hp = pygame.draw.rect(screen, (225,0,0), (135,675,healthbar,20))
        index_cnbl=0
        index_drag=0
        index_fire=0
        index_scnbl=0
        index_cnbls=0
        X = 202
        Y = 480
        dragontimer = 250
        dragonlist = []
        fireballtimer = 251
        fireballlist = []
        shieldballtimer = 180
        shieldballlist = []
        cnblshieldtimer = 181
        cnblshieldlist = []
        healthtimer = random.randint(1000,2000)
        healthlist = []
        intro = False
        gamestart = True
        pygame.mixer.music.load("Mygame/sound/Defending.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        while gamestart:
            balltimer-=1
            healthtimer-=1
            if scoreboard >= 50:
                shieldballtimer-=1
                cnblshieldtimer-=1
            if scoreboard >= 100:
                dragontimer-=1
                fireballtimer-=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() 
                    exit() 

#5.3.2 - clear screen elements
            screen.fill(0)

#5.3.3 - draw the screen elements
#5.3.3.1 - background
            screen.blit(background,(0,0))
#5.3.3.2 - castle
            screen.blit(castle,(0,420))
            screen.blit(castle,(240,420))
            screen.blit(castle,(480,420))
#5.3.3.3 - cannon
            screen.blit(cannon,(-75,-65))
            screen.blit(cannon,(5,-65)) 
            screen.blit(cannon,(85,-65))
            screen.blit(cannon,(165,-65))
            screen.blit(cannon,(245,-65))
            screen.blit(cannon,(325,-65))
            screen.blit(cannon,(405,-65))
#5.3.3.4 - castle hp
            hp = pygame.draw.rect(screen, (225,0,0), (135,675,healthbar,20))
#5.3.3.5 - health(extra hp) blit

            if healthtimer==0:
                healthlist.append([-110+random.randint(0,6)*80,-100])
                healthtimer=random.randint(1000,2000)

            index_heart=0
            for heart in healthlist:
                heart[1] +=5
                manrect=pygame.Rect.inflate(knight.get_rect(),-120,-130)
                manrect.top=Y+50
                manrect.left=X+50

                heartrect=pygame.Rect.inflate(plus_health.get_rect(),-260,-230)

                heartrect.top=heart[1]+110
                heartrect.left=heart[0]+130

                if manrect.colliderect(heartrect):

                    healthlist.pop(index_heart)
                    healthbar += 80
                    if healthbar > 300:
                        healthbar = 300

                if heart[1]>600:
                    healthlist.pop(index_heart)
                    index_heart+=1

                screen.blit(plus_health,(heart))


#5.3.3.6 - normal cannonball blit

            if balltimer==0:
                cannonballlist.append([-110+random.randint(0,6)*80,-75])
                balltimer=100

            myfont = pygame.font.SysFont('Oswald', 30)
            score = myfont.render('Score: ' + str(scoreboard), False, (0,0,0))
            index_cnbl=0
            Key = pygame.key.get_pressed()
            for cnbl in cannonballlist:
                cnbl[1]+=5
                manrect=pygame.Rect.inflate(knight.get_rect(),-120,-130)
                manrect.top=Y+50
                manrect.left=X+50

                cnblrect=pygame.Rect.inflate(cannonball.get_rect(),-285,-285)
                cnblrect.top=cnbl[1]+140
                cnblrect.left=cnbl[0]+140

                if manrect.colliderect(cnblrect):
                    totalscoreboard += scoreboard
                    if scoreboard > highscore:
                        highscore = scoreboard
                    intro = True
                    gamestart = False
                    pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                if Key[K_j]:
                    shieldrect=pygame.Rect.inflate(shield.get_rect(),-200,-270)
                    shieldrect.top=Y+20
                    shieldrect.left=X+40
                    if shieldrect.colliderect(cnblrect):
                        scoreboard += 10
                        cannonballlist.pop(index_cnbl)

                if cnbl[1]>500:
                    cannonballlist.pop(index_cnbl)
                    index_cnbl+=1
                    healthbar -= health_minus_cnbl

                screen.blit(cannonball, cnbl)


#5.3.3.7 - dragon blit

            if dragontimer==0:
                dragonlist.append([-50+random.randint(0,6)*80,-1900])
                dragontimer=300

            index_drag=0
            Key = pygame.key.get_pressed()
            for drag in dragonlist:
                drag[1] += 12
                manrect=pygame.Rect.inflate(knight.get_rect(),-130,-130)
                manrect.top=Y+50
                manrect.left=X+60

                dragrect=pygame.Rect.inflate(dragon.get_rect(),-125,-80)
                dragrect.top=drag[1]+50
                dragrect.left=drag[0]+60

                if manrect.colliderect(dragrect):
                    totalscoreboard += scoreboard
                    if scoreboard > highscore:
                        highscore = scoreboard
                    intro = True
                    gamestart = False
                    pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                if Key[K_l]:
                    swordrect=pygame.Rect.inflate(sword.get_rect(),-270,-220)
                    swordrect.top=Y-30
                    swordrect.left=X+75
                    if swordrect.colliderect(dragrect):
                        scoreboard += 20
                        dragonlist.pop(index_drag)

                if drag[1]>500:
                    dragonlist.pop(index_cnbl)
                    index_drag+=1
                    healthbar -= health_minus_dragon

                screen.blit(dragon, drag)


#5.3.3.8 - fire blit

            if fireballtimer==0:
                fireballlist.append([drag[0]+45,-100])
                fireballtimer=300

            index_fire=0
            Key = pygame.key.get_pressed()
            for fire in fireballlist:
                fire[1] += 6
                manrect=pygame.Rect.inflate(knight.get_rect(),-130,-130)
                manrect.top=Y+50
                manrect.left=X+60

                firerect=pygame.Rect.inflate(fireball.get_rect(),-60,-44)
                firerect.top=fire[1]+25
                firerect.left=fire[0]+35

                if manrect.colliderect(firerect):
                    totalscoreboard += scoreboard
                    if scoreboard > highscore:
                        highscore = scoreboard
                    intro = True
                    gamestart = False
                    pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                if Key[K_j]:
                    shieldrect=pygame.Rect.inflate(shield.get_rect(),-200,-270)
                    shieldrect.top=Y+20
                    shieldrect.left=X+40
                    if shieldrect.colliderect(firerect):
                        scoreboard += 10
                        fireballlist.pop(index_fire)

                if fire[1]>575:
                    fireballlist.pop(index_fire)
                    index_fire+=1
                    healthbar -= health_minus_fire

                screen.blit(fireball, (fire))


#5.3.3.9 - shielded cannonball blit

            if shieldballtimer==0:
                shieldballlist.append([-110+random.randint(0,6)*80,-80])
                shieldballtimer=300

            index_scnbl=0
            Key = pygame.key.get_pressed()
            for scnbl in shieldballlist:
                scnbl[1] += 6
                manrect=pygame.Rect.inflate(knight.get_rect(),-130,-130)
                manrect.top=Y+50
                manrect.left=X+60

                scnblrect=pygame.Rect.inflate(shieldball.get_rect(),-240,-240)
                scnblrect.top=scnbl[1]+120
                scnblrect.left=scnbl[0]+120

                if manrect.colliderect(scnblrect):
                    totalscoreboard += scoreboard
                    if scoreboard > highscore:
                        highscore = scoreboard
                    intro = True
                    gamestart = False
                    pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                if Key[K_l]:
                    swordrect=pygame.Rect.inflate(sword.get_rect(),-270,-220)
                    swordrect.top=Y-30
                    swordrect.left=X+75
                    if swordrect.colliderect(scnblrect):
                        scoreboard += 10
                        shieldballlist.pop(index_scnbl)

                if scnbl[1]>500:
                    shieldballlist.pop(index_scnbl)
                    index_scnbl+=1
                    healthbar -= health_minus_scnbl

                screen.blit(shieldball, (scnbl))


#5.3.3.10 - cannonball(after shield destroyed) blit

            if cnblshieldtimer==0:
                cnblshieldlist.append([scnbl[0],-74])
                cnblshieldtimer=300

            index_cnbls=0
            Key = pygame.key.get_pressed()
            for cnbls in cnblshieldlist:
                cnbls[1]+=6
                manrect=pygame.Rect.inflate(knight.get_rect(),-120,-130)
                manrect.top=Y+50
                manrect.left=X+50

                cnblsrect=pygame.Rect.inflate(cannonball.get_rect(),-285,-285)
                cnblsrect.top=cnbls[1]+140
                cnblsrect.left=cnbls[0]+140

                if manrect.colliderect(cnblsrect):
                    totalscoreboard += scoreboard
                    if scoreboard > highscore:
                        highscore = scoreboard
                    intro = True
                    gamestart = False
                    pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)

                if Key[K_j]:
                    shieldrect=pygame.Rect.inflate(shield.get_rect(),-200,-270)
                    shieldrect.top=Y+20
                    shieldrect.left=X+40
                    if shieldrect.colliderect(cnblsrect):
                        scoreboard += 10
                        cnblshieldlist.pop(index_cnbls)

                if cnbls[1]>500:
                    cnblshieldlist.pop(index_cnbls)
                    index_cnbls+=1
                    healthbar -= health_minus_cnbl

                screen.blit(cannonball,(cnbls))


#5.3.3.11 - score blit and back to start menu when no hp left

            screen.blit(score, (490,10))
            if healthbar <= 0:
                healthbar = 0
                hp = screen.blit(hppic,(50,595))
                intro = True
                gamestart = False
                totalscoreboard += scoreboard
                if scoreboard > highscore:
                    highscore = scoreboard
                pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)

#5.4 - knight and movement
            Key = pygame.key.get_pressed()
            u = [False, False]
            if Key[K_q]:
                totalscoreboard += scoreboard
                if scoreboard > highscore:
                    highscore = scoreboard
                gamestart = False
                intro = True
                pygame.mixer.music.load("Mygame/sound/Medieval.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
            if Key[K_j]:
                screen.blit(shield, (X-60,375))
            elif Key[K_l]:
                screen.blit(sword, (X-60,350))

            else:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key==K_a:
                            u[0] = 1
                        elif event.key==K_d:
                            u[1] = 1
                    if event.type == pygame.KEYUP: 
                        if event.key==K_a:
                            u[0] = 0
                        elif event.key==K_d:
                            u[1] = 0

                    if u[0]:
                        X-=speed
                    elif u[1]:
                        X+=speed
                    
                    if X > 437:
                        X = 437
                    elif X < -38:
                        X = -38

            display.blit(knight, (X, Y))


#6 - update the screen
            pygame.display.update()
