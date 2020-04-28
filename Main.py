
#Importing and Intizaliving Pygame
import pygame
pygame.init()
pygame.mixer.init()
import Classes
import random

#This is bascially just me importhing the instrtion adnd vicotry screens into main
victory = pygame.image.load("win.png")
instruct1 = pygame.image.load('HowToPlayOne.png')
instruct2 = pygame.image.load("HowToPlayTwo.png")
YouLose = pygame.image.load("YouLose.png")
Endsound = pygame.mixer.Sound("GameEnd.wav")

def main():
    '''This Fuction is the main for the game and calls all the fuctions and does all that business'''

    #Display Configuration
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Protect Ba Sing Se")

    #Entities


    #Setting up the playing of the background music
    pygame.mixer.music.load("AgniKai.mp3")

    #Making so it starts playing
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(0)

    #This list holds the user attacks indexed into it so I can run tests on thm with a for loop
    attacks = []

    # This list holds the reandomly generated attacks indexed into it so I can run tests on thm with a for loop
    ai_attacks = []

    #Making object to hold my score
    score = Classes.Score_counter("Your Current Score: ", (600,20))

    #Making an object for the player, the Aang name is who the chatcer is
    Aang = Classes.User_char()
    allsprites = pygame.sprite.Group(Aang)

    #Action Bit

    #Assigning Values and Variable Stuf
    clock = pygame.time.Clock()#Clock
    KEEPGOING = True#Main game loop

    #These Two varibbles are used when dispalying the insctuions.
    INSTRUCTION = True#The insctrutions game loop
    Instruct = 0#this varbile is used to figurre out which instction screen should be displaed

    #The Varivle that tuns the end screen
    TRIUMPTH = False

    FAILED = False

    #Sub Instructions loop
    while INSTRUCTION:
        #Bascially displays the first images untill the user clicks, than swithcs to the second image by addng 1 to
        #a varaivle that determies wich image is displayed
        if Instruct == 0:
            screen.blit(instruct1, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Instruct += 1
        if Instruct == 1:
            screen.blit(instruct2, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Instruct += 1

        if Instruct == 2:
            INSTRUCTION = False





    #Main Game-Loop

    #Impotring the background to be used
    background = pygame.image.load("Level One.png")
    while KEEPGOING:

        #Timer for Framerate
        clock.tick(30)

        #Event Handleing

        #Getting rid of any attacks that travel of screen by removing them form
        #The attacks and ai_attacks lists
        for attack in attacks: #Doing the above for user attacks
            if attack.x > 640 :
                attacks.pop(attacks.index(attack))

        for ai_attack in ai_attacks:#Doing the above for Computr Attacks
            if ai_attack.x < 0:
                Aang.passed += 1
                ai_attacks.pop(ai_attacks.index(ai_attack))

        if len(ai_attacks) < 8:#This lisne make sure my computer doesn't break by limithing the number of
                                #Attacks that can be on the screen on any given moment
            if random.randint(1, Aang.Generator) == 1:#Only geneaatoes a ai_attck if a random inteager is 1
                type = random.randint(1, 5)
                if type == 1:#If type is air makes an air attack
                    ai_attacks.append(Classes.Computer_Attack(-8, 1, random.randint(0,Aang.level_row+1)))
                elif type == 2:#If type is water makes a water attack
                    ai_attacks.append(Classes.Computer_Attack(-8, 2, random.randint(0,Aang.level_row+1)))
                elif type == 3: #If Type = Earth ai attack is water
                    ai_attacks.append(Classes.Computer_Attack(-8, 3, random.randint(0,Aang.level_row+1)))
                elif type == 4:#if the type is fire, it makes a fire attack
                    ai_attacks.append(Classes.Computer_Attack(-8, 4, random.randint(0,Aang.level_row+1)))

        #Cheaking for events,
        for event in pygame.event.get():#Getting main loop to false if user closes window
            if event.type == pygame.QUIT:
                KEEPGOING = False


            elif event.type == pygame.KEYDOWN:
                # If the up arrow is pressed the charcter .update() is called, and moves Aang one up
                if event.key == pygame.K_UP:
                    Aang.update(-1,screen)
                #If the down arrow is pressed Aang moves down
                elif event.key == pygame.K_DOWN:
                    Aang.update(1,screen)
            #The bending attack class makes a air attck if the user plresses "A"
                elif event.key == pygame.K_a:
                    Aang.Attacking = True
                    if len(attacks) < 6:
                        attacks.append(Classes.Bending_Attack(10,1,Aang.row))
                # The bending attack class makes a water attck if the user plresses "S"
                elif event.key == pygame.K_s:
                    Aang.Attacking = True
                    if len(attacks) < 6:
                        attacks.append(Classes.Bending_Attack(10, 2, Aang.row))
                # The bending attack class makes a Earth attck if the user plresses "D"
                elif event.key == pygame.K_d:
                    Aang.Attacking = True
                    if len(attacks) < 6:
                        attacks.append(Classes.Bending_Attack(10,3,Aang.row))
                # The bending attack class makes a Fire attck if the user plresses "F"
                elif event.key == pygame.K_f:
                    Aang.Attacking = True
                    if len(attacks) < 6:
                        attacks.append(Classes.Bending_Attack(10,4,Aang.row))


        #This cheaks if the projecitle are in the same row and if they are close enough
        for projectile in attacks:
            for thing in ai_attacks:
                if projectile.type == thing.beat and thing.x - projectile.x < 15 and thing.y == projectile.y:
                    try:#If this is the case, the attacks will be deleted
                        ai_attacks.pop(ai_attacks.index(thing))
                        attacks.pop(attacks.index(projectile))
                        score.counter += 1#The score get updated
                        score.update()
                    except ValueError:
                        continue

        #Calling the win loop if the user get enough points
        if score.counter == 12:
            KEEPGOING = False
            TRIUMPTH = True

        #The amount of lives is lost the game ends
        if Aang.passed == 8:

            KEEPGOING = False
            FAILED = True


        #Refresh Screen

        allsprites.clear(screen, background)

        screen.blit(background, (0, 0))
        if Aang.Attacking == True:
            Aang.update(0,screen)
            Aang.Attacking = False

        allsprites.draw(screen)

        for attack in attacks:
            attack.update()
            screen.blit(attack.image, (attack.x,attack.y))
        for ai_attack in ai_attacks:
            ai_attack.update()
            
            screen.blit(ai_attack.image, (ai_attack.x,ai_attack.y))
        screen.blit(score.image,(450, 20))

        score.update()

        pygame.display.flip()

    while TRIUMPTH:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                TRIUMPTH = False
        
        screen.blit(victory, (0, 0))
        pygame.display.flip()

    while FAILED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                FAILED = False
        
        screen.blit(YouLose, (0, 0))
        pygame.display.flip()


    #Closing Window if the User Wants to Quit
    pygame.quit()

main()
