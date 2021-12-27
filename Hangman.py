# Hangman
import random
import pygame
import time
import os, string

data = [i.replace('\n', '') for i in list(open('Word.txt'))]
high_score = [i.replace('\n', '') for i in list(open('Hangman Highscore.txt'))]

# Opens and writes up the high scores
def set_score(highscores): 
    f = open('Hangman Highscore.txt','w')
    f.write(str(highscores[0]) + '\n')
    f.write(highscores[1])
    f.close()

# This is the main part of the visuals. It displays the text the user is guessing.
def text(visual, incorrect): 
    show = ''
    for i in visual:
        show += i
    screen = pygame.display.set_mode((500, 600), 0, 32)
    topScreen = pygame.Rect(0, 0, 500, 500)
    bottomScreen = pygame.Rect(0, 500, 500, 100)
    if incorrect > 11:
        incorrect = 11
    try: # The part below handles the hangman image.
        topImage = pygame.image.load(os.path.join('Tries', 'Tries ' + str(incorrect) + '.png'))
        bottomImage = pygame.image.load('Start Button Images/Start Button None.png')
        screen.blit(bottomImage, bottomScreen)
        screen.blit(topImage, topScreen)
        retroFont = pygame.font.Font(os.path.join('Fonts', 'PressStart2P.ttf'), 20)
        text = retroFont.render(show, True, (255, 255, 255))
        textBox = text.get_rect(center=(250, 80))
        screen.blit(text, textBox)
    except:
        return ()


def exclaim(screen): # This is the error exclamation that pops up.
    retroFont = pygame.font.Font(os.path.join('Fonts', 'PressStart2P.ttf'), 20)
    text = retroFont.render('!', True, (255, 255, 255))
    textBox = text.get_rect(center=(255, 108))
    screen.blit(text, textBox)
    pygame.display.update()

# This pauses events until the user has placed an input.
def pause(): 
    breaks = True
    while breaks is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                breaks = False

        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            breaks = False

# This checks the users input and ensures that it is a valid letter.
# Returns upper case of letter pressed, false otherwise
def check(): 
    alphabet = list(string.ascii_lowercase)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                selected_key = event.unicode
                if selected_key in alphabet:
                    return selected_key.upper()
                    break
                elif selected_key not in alphabet:
                    return False
                    break
                if event.key == 27:
                    pygame.quit()

# Start screen, this function only runs once and displays the main title.
def start(load): 
    screen = pygame.display.set_mode((500, 600), 0, 32)
    topScreen = pygame.Rect(0, 0, 500, 500)
    screenImage = pygame.image.load('HangMan.png')
    buttonImage = pygame.image.load('Start Button Images/Start Button Norm.png')
    buttonInvert = pygame.image.load('Start Button Images/Start Button Select.png')
    screen.blit(screenImage, topScreen)
    x = 30

    while load:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        startButton = pygame.Rect(0, 500, 500, 100)

        if startButton.collidepoint(mouse):
            x += 1
            if x >= 30:
                screen.blit(buttonInvert, startButton)

            if x >= 60:
                x = 0
                screen.blit(buttonImage, startButton)

            if click[0] == 1:
                return screen
                load = False
        else:
            screen.blit(buttonImage, startButton)

        pygame.display.update()

# Displays screen to replay
# This function asks for the user if they wish to play again.
def replay(screen): 
    bottomScreen = pygame.Rect(0,500,100,100)
    defaultImage = pygame.image.load('Start Button Images/Start Button Again.png')
    screen.blit(defaultImage, bottomScreen)
    yesBox = pygame.Rect(100,550,50,25)
    noBox = pygame.Rect(330,557,40,25)
    yesImage = pygame.image.load('Start Button Images/Start Button Yes.png')
    noImage = pygame.image.load('Start Button Images/Start Button No.png')
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if yesBox.collidepoint(mouse):
            screen.blit(yesImage, bottomScreen)
            if click[0] == 1:
                return True
        elif noBox.collidepoint(mouse):
            screen.blit(noImage, bottomScreen)
            if click[0] == 1:
                return False
        else:
            screen.blit(defaultImage, bottomScreen)
        pygame.display.update()

# This is the main screen of H_ngM_n. It handles the options/gamemodes the user can select.
def mainScreen(screen): 
    topScreen = pygame.Rect(0, 0, 500, 500)
    screenImage = pygame.image.load(os.path.join('Select Screen', 'Select Screen Norm.png'))
    tutorialImage = pygame.image.load(
        os.path.join('Select Screen', 'Select Screen Tutorial.png'))  # 130-170 and 131-374
    playImage = pygame.image.load(os.path.join('Select Screen', 'Select Screen Play.png'))
    freeImage = pygame.image.load(os.path.join('Select Screen', 'Select Screen Free.png'))
    highImage = pygame.image.load(os.path.join('Select Screen', 'Select Screen High.png'))
    buttonImage = pygame.image.load('Start Button Images/Start Button None.png')
    tutorialDescImage = pygame.image.load('Start Button Images/Start Button Tutorial Desc.png')
    playDescImage = pygame.image.load('Start Button Images/Start Button Play Desc.png')
    freeDescImage = pygame.image.load('Start Button Images/Start Button Free Desc.png')
    highDescImage = pygame.image.load('Start Button Images/Start Button High Desc.png')
    startButton = pygame.Rect(0, 500, 500, 100)
    screen.blit(buttonImage, startButton)

    screen.blit(screenImage, topScreen)
    pygame.display.update()
    time.sleep(0.5)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[1] >= 120 and mouse[1] <= 180 and mouse[0] >= 140 and mouse[0] <= 380:
            screen.blit(tutorialImage, topScreen)
            screen.blit(tutorialDescImage, startButton)
            if click[0] == 1:
                return 'TUTORIAL'

        elif mouse[1] >= 210 and mouse[1] <= 270 and mouse[0] >= 170 and mouse[0] <= 330:
            screen.blit(playImage, topScreen)
            screen.blit(playDescImage, startButton)
            if click[0] == 1:
                return 'PLAY'

        elif mouse[1] >= 290 and mouse[1] <= 350 and mouse[0] >= 115 and mouse[0] <= 390:
            screen.blit(freeImage, topScreen)
            screen.blit(freeDescImage, startButton)
            if click[0] == 1:
                return 'FREE'

        elif mouse[1] >= 385 and mouse[1] <= 430 and mouse[0] >= 110 and mouse[0] <= 390:
            screen.blit(highImage, topScreen)
            screen.blit(highDescImage,startButton)
            if click[0] == 1:
                return 'HIGH'

        else:
            screen.blit(screenImage, topScreen)
            screen.blit(buttonImage, startButton)
        pygame.display.update()


def dialogue(pause_1, pause_2, text, screen, side_1, side_2, side_3, top): # This displays the text said by the main character.
    # Top variable defines whether the top screen is being used or not.
    printedLine1 = ''
    printedLine2 = ''
    printedLine3 = ''

    if top is True:
        topScreen = pygame.Rect(0, 0, 500, 500)
        topImage = pygame.image.load('Tutorial Top Screen.png')
        blinkImage = pygame.image.load('HangMan Blink.png')
        screen.blit(topImage, topScreen)

    bottomScreen = pygame.Rect(0, 500, 500, 100)
    buttonImage = pygame.image.load('Start Button Images/Start Button None.png')
    screen.blit(buttonImage, bottomScreen)

    x = 0

    retroFont = pygame.font.Font(os.path.join('Fonts', 'PressStart2P.ttf'), 14)

    # 3 printed line variables since some messages might extend past the allocated text box
    for letter in text:
        if len(printedLine1) <= pause_1:
            printedLine1 += letter
        elif len(printedLine2) <= pause_2:
            printedLine2 += letter
        else:
            printedLine3 += letter

        blink = random.randint(1, 20)

        if blink == 5 and top is True:
            x += 1
            screen.blit(blinkImage, topScreen)
        elif blink != 5 and x == 4 and top is True:
            x = 0
            screen.blit(topImage, topScreen)

        display = retroFont.render(printedLine1, 0, (255, 255, 255), (0, 0, 0))
        screen.blit(display, (side_1, 525))

        display = retroFont.render(printedLine2, 0, (255, 255, 255), (0, 0, 0))
        screen.blit(display, (side_2, 544))

        display = retroFont.render(printedLine3, 0, (255, 255, 255), (0, 0, 0))
        screen.blit(display, (side_3, 563))
        time.sleep(0.01)

        pygame.display.update()

    if top is True:
        screen.blit(topImage, topScreen)

    pygame.display.update()
    if top is True:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                break
            if event.type == pygame.KEYDOWN:
                break


def game(guess, visual, incorrect, word,
         tried):  # This handles the main calculation of whether the guess is in the word or not.
    hit = False
    for i in range(len(word)):
        if guess == word[i].upper():
            visual[i] = guess
            tried.append(guess)
            hit = True
    if hit == False:
        tried.append(guess)
        incorrect += 1
    return visual, incorrect, tried


def check_win(visual, word): # This checks to see if the user has won the game already.
    start = 0
    for i in range(len(word)):
        if visual[i] == word[i].upper():
            start += 1

    if start == len(word):
        return True


def show_guess(tried, visual, screen): # This shows the letters the user has guessed.
    retroFont = pygame.font.Font(os.path.join('Fonts', 'PressStart2P.ttf'), 14)
    message = 'Guessed: '
    box = pygame.Rect(19, 470, 480, 40)
    tried.sort()
    for i in range(len(tried)):
        if tried[i] not in visual:
            message += tried[i] + ' '

    display = retroFont.render(message, 0, (255, 255, 255), None)
    screen.blit(display, box)


def scoring(score): # This shows the score the user is currently on.
    retroFont = pygame.font.Font(os.path.join('Fonts', 'PressStart2P.ttf'), 14)
    message = 'Score: ' + str(score)
    box = pygame.Rect(25, 25, 20, 100)
    display = retroFont.render(message, 0, (255, 255, 255), None)
    screen.blit(display, box)


def death(files,location,screen): # Death animation for the tutorial
    topScreen = pygame.Rect(0,0,500,500)
    for number in range(files):
        time.sleep(0.03)
        topImage = pygame.image.load(location + str(number) + '.png')
        screen.blit(topImage, topScreen)
        pygame.display.update(topScreen)


def showHighscore(info, screen): # Shows highscore, used for high score screen
    playHigh = info[0]
    freeHigh = info[1]
    retroFont = pygame.font.Font(os.path.join('Fonts', 'PressStart2P.ttf'), 20)
    topScreen = pygame.Rect(0, 0, 500, 500)
    topImage = pygame.image.load('Select Screen/Select Screen Blank.png')
    screen.blit(topImage, topScreen)

    playMessage = retroFont.render(('Play Highscore: ' + str(playHigh)),0,(255,255,255),(0,0,0))
    playBox = playMessage.get_rect(center=(250,200))
    screen.blit(playMessage, playBox)

    freeMessage = retroFont.render(('FreePlay Highscore: ' + str(freeHigh)),0,(255,255,255),(0,0,0))
    freeBox = freeMessage.get_rect(center=(250,350))
    screen.blit(freeMessage, freeBox)






load = True
pygame.font.init()

screen = start(load)
clock = pygame.time.Clock()

while True:
    seconds = 0
    again = True
    action = mainScreen(screen)
    if action == 'TUTORIAL': # The tutorial section of the game
        incorrect = -1 # -1 Image shows just the main character without any nooses and gallows.
        word = 'Dr.' # Game is rigged since '.' is not a valid input
        visual = [] # Handles whats being shown to the user
        position = {}
        exclamation = False # Variable used to display the exclamation if the user has done something wrong.
        error = None # Error value detects whether or not there was an error with the users previous input

        tried = []

        for letter in word:
            visual.append('_')

        for number in range(len(word)): # Adding positions of each letter
            position[str(number)] = word[number]

        dialogue(29, 58, 'HELLO, I AM YOUR GUIDE TO THE TUTORIAL.', screen, 26, 24, 0, True)
        dialogue(28, 27, "I'M FIDDLE ME BONES AND I'LL BE TEACHING YOU HOW TO PLAY H_NGM_N.", screen, 25, 26, 26, True)
        dialogue(30, 29, "I DIDN'T REALLY WANT THIS JOB, BUT YOU CANT BE PICKY IN THIS ECONOMY!", screen, 25, 26, 26, True)
        dialogue(29, 29, "I HAVE A FAMILY RELYING ON ME TO FEED THEM.", screen, 25, 26, 26, True)
        dialogue(30, 29, "ANYWAY, IN THIS GAME YOUR GOAL IS TO GUESS THE SECRET WORD.", screen, 25, 26, 26, True)
        dialogue(31, 29, "YOU DO THIS BY PRESSING BUTTONS ON YOUR KEYBOARD!", screen, 25, 26, 26, True)
        dialogue(28, 27, "THE AMOUNT OF LETTERS IN THE SECRET WORD WOULD APPEAR UP HERE.", screen, 25, 26, 26, False)
        pause()
        text(visual, incorrect)
        pygame.display.update()
        pause()
        dialogue(30, 29, "IF YOU GET ANY LETTERS CORRECT IT WOULD APPEAR UP HERE!", screen, 25, 26, 26, True)

        dialogue(28, 29, "THE LETTERS YOU HAVE GUESSED INCORRECTLY WOULD APPEAR DOWN HERE.", screen, 25, 26, 26, True)

        show_guess(tried,visual,screen)
        pygame.display.update()
        time.sleep(0.5)
        pause()

        dialogue(25, 29, "AN EXCLAMATION APPEARS IF YOU'VE DONE SOMETHING WRONG.", screen, 25, 26, 26, True)
        exclaim(screen)
        pause()


        dialogue(26, 28, "EACH TIME YOU GET A LETTER WRONG, I GET CLOSER TO BEING HUNG.", screen, 25, 26, 26, True)
        dialogue(27, 27, "HOPEFULLY YOU\'LL BE ABLE TO FIND THE WORD IN TIME!", screen, 25, 26, 26, True)
        dialogue(32, 27, "GOOD LUCK! I'LL BE GETTING READY NOW.", screen, 25, 26, 26, True)



        score = 0
        incorrect = 0
        while incorrect != 11:
            while True:
                if exclamation is False:
                    text(visual, incorrect)
                    show_guess(tried, visual, screen)
                    scoring(score)
                    pygame.display.update()

                if exclamation is True:
                    show_guess(tried, visual, screen)
                    exclaim(screen)
                    if error == 'Tried':
                        dialogue(27, 30, 'You have already tried that letter!', screen, 26, 26, 26, False)
                    if error == 'Not-Letter':
                        dialogue(27, 30, 'That is not a letter!', screen, 26, 26, 26, False)
                    error = None
                    exclamation = False

                guess = check()
                try:
                    if guess is not False:
                        if guess not in tried:
                            store = game(guess, visual, incorrect, word, tried)
                            visual = store[0]
                            incorrect = store[1]
                            tried = store[2]
                            win = check_win(visual, word)
                            if incorrect == 11:
                                text(visual, incorrect)
                                pygame.display.update()
                                dialogue(30, 30, 'OH NO! YOU SEEM TO HAVE GOTTEN THE WORD WRONG!',screen, 26, 26, 26, False)
                                pause()
                                dialogue(29, 30,'BUT DONT WORRY THIS IS JUST A TUTORIAL SO I WONT BE HUNG.',screen, 26, 26, 26, False)
                                pause()
                                break

                        else:
                            exclamation = True
                            error = 'Tried'
                            pass
                    else:
                        exclamation = True
                        error = 'Not-Letter'
                        pass



                except:
                    pass
                    exclaim(screen)

        dialogue(29, 30, 'I HAVE A FAMILY RELYING ON ME TO FE-', screen, 26, 26, 26, False)
        pause()
        death(9, 'Animate/Animate ',screen)
        dialogue(30,30,'...', screen, 26, 26, 26, False)
        pause()
        dialogue(30,30,'...', screen, 26, 26, 26, False)
        pause()
        dialogue(30,30,'...', screen, 26, 26, 26, False)
        pause()
        psych = pygame.image.load('Animate/Animate 10.png')
        screen.blit(psych, pygame.Rect(0,0,500,500))
        pygame.display.update()
        dialogue(29, 30, 'PSYCH!', screen, 26, 26, 26, False)
        pause()
        dialogue(29, 30, 'A SKELETON CANT DIE IDIOT!', screen, 26, 26, 26, False)
        pause()
        dialogue(29, 30, 'ANYWAY, YOU SHOULD KNOW HOW TO PLAY NOW SO GOOD LUCK AND HAVE FUN.', screen, 26, 26, 26, False)
        pause() #

    if action == 'PLAY':
        score = 0
        while again:

            set_score(high_score)
            incorrect = 0
            word = random.choice(data)
            visual = []
            position = {}
            exclamation = False
            error = None

            tried = []
            for letter in word:
                visual.append('_')

            for number in range(len(word)):
                position[str(number)] = word[number]
            while True:
                clock.tick()
                if exclamation is False:
                    text(visual, incorrect)
                    show_guess(tried, visual, screen)
                    scoring(score)
                    pygame.display.update()

                if exclamation is True:
                    show_guess(tried, visual, screen)
                    exclaim(screen)
                    if error == 'Tried':
                        dialogue(27, 30, 'You have already tried that letter!', screen, 26, 26, 26, False)
                    if error == 'Not-Letter':
                        dialogue(27, 30, 'That is not a letter!', screen, 26, 26, 26, False)
                    error = None
                    exclamation = False

                if seconds/1000 > 60:
                    text(visual, incorrect)
                    dialogue(31, 30, 'You have ran out of time!', screen, 26, 26, 26, False)
                    time.sleep(1)
                    pause()

                    visual = []
                    for number in range(len(word)):
                        visual.append(word[number].upper())
                    text(visual, incorrect)
                    dialogue(31,30, 'The word was...',screen,26,26,26, False)
                    pygame.display.update()
                    time.sleep(0.5)
                    pause()
                    if score > int(high_score[0]):
                        high_score[0] = score
                    seconds = 0
                    score = 0
                    again = replay(screen)

                    break
                guess = check()

                try:
                    if guess is not False:
                        if guess not in tried:
                            store = game(guess, visual, incorrect, word, tried)
                            visual = store[0]
                            incorrect = store[1]
                            tried = store[2]
                            win = check_win(visual, word)
                            if win is True:
                                score += len(word)
                                text(visual, incorrect)
                                scoring(score)
                                dialogue(31, 30, 'You win! Press any button to go onto the next word.', screen, 26, 26, 26,
                                        False)
                                pause()
                                break

                            if incorrect == 11:
                                text(visual, incorrect)
                                dialogue(31, 30, 'You have lost!', screen, 26, 26, 26, False)
                                time.sleep(0.5)
                                pause()

                                visual = []
                                for number in range(len(word)):
                                    visual.append(word[number].upper())
                                text(visual, incorrect)
                                dialogue(31,30, 'The word was...',screen,26,26,26, False)
                                pygame.display.update()
                                time.sleep(0.5)
                                pause()
                                if score > int(high_score[0]):
                                    high_score[0] = score

                                score = 0
                                again = replay(screen)
                                seconds = 0
                                break
                        else:
                            exclamation = True
                            error = 'Tried'
                            pass
                    else:
                        exclamation = True
                        error = 'Not-Letter'
                        pass


                except:
                    pass
                    exclaim(screen)
                    # Again screen  # 22/05 Started word text + above lines

                clock.tick()
                seconds += clock.get_time()
                print(int(seconds/1000))

    if action == 'FREE':
        score = 0
        while True:
            set_score(high_score)
            incorrect = 0
            word = random.choice(data)
            visual = []
            position = {}
            exclamation = False
            error = None

            tried = []
            for letter in word:
                visual.append('_')

            for number in range(len(word)):
                position[str(number)] = word[number]
            while True:
                if exclamation is False:
                    text(visual, incorrect)
                    show_guess(tried, visual, screen)
                    scoring(score)
                    pygame.display.update()

                if exclamation is True:
                    show_guess(tried, visual, screen)
                    exclaim(screen)
                    if error == 'Tried':
                        dialogue(27, 30, 'You have already tried that letter!', screen, 26, 26, 26, False)
                    if error == 'Not-Letter':
                        dialogue(27, 30, 'That is not a letter!', screen, 26, 26, 26, False)
                    error = None
                    exclamation = False

                guess = check()

                try:
                    if guess is not False:
                        if guess not in tried:
                            store = game(guess, visual, incorrect, word, tried)
                            visual = store[0]
                            incorrect = store[1]
                            tried = store[2]
                            win = check_win(visual, word)
                            if win is True:
                                score += len(word)
                                text(visual, incorrect)
                                scoring(score)
                                dialogue(31, 30, 'You win! Press any button to go onto the next word.', screen, 26, 26, 26,
                                        False)
                                pause()
                                break

                            if incorrect == 11:
                                text(visual, incorrect)
                                dialogue(31, 30, 'You have lost! Press any button to go onto the next word.', screen, 26, 26,
                                        26, False)
                                pause()
                                if score > int(high_score[0]):
                                    high_score[0] = score

                                score = 0
                                # Again?
                                break
                        else:
                            exclamation = True
                            error = 'Tried'
                            pass
                    else:
                        exclamation = True
                        error = 'Not-Letter'
                        pass

                except:
                    pass
                    exclaim(screen)
                    # Again screen  # 22/05 Started word text + above lines

    if action == 'HIGH':
        showHighscore(high_score,screen)
        dialogue(30,30,'Press any button to go back.',screen, 26,26,26,False)
        time.sleep(0.5)
        pause()


