import pygame
import math
import random
    
# Set up display
pygame.init()

WIDTH, HEIGHT = 800, 550
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Hangman")

# fonts

LETTER_FONT = pygame.font.SysFont('Montserrat', 40)
WORD_FONT = pygame.font.SysFont('Montserrat', 60)
TITLE_FONT = pygame.font.SysFont('Montserrat', 80)

# Load inmages

images = []

for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)


# Button variables

RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400

A = 65

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])
    
    
    
    (letters, x, y, str(chr(65 + i)))

# Game variables

hangman_status = 0

WORDS = ["HELLO", "HELICOPTER", "BANANA", "SAMSUNG", "GAME"]
word = random.choice(WORDS)
guessed = []

# color
WHITE = 255, 255, 255
BLACK = 0, 0, 0




def draw():
    win.fill(WHITE)
    # draw titleFont
    
    text = TITLE_FONT.render("The Hangman", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    
    # Draw word
     
    display_word = " "
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    text = WORD_FONT.render(display_word, 1, BLACK)
    
    win.blit(text, (400, 200))
    #draw buttons 
     
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
    
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()
    

# WIN LOST display
def won_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))  
    pygame.display.update()
    pygame.time.delay(3000)

def lost_message(message):
    pygame.time.delay(1000)
    win.fill(BLACK)
    text = WORD_FONT.render(message, 1, WHITE)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))  
    pygame.display.update()
    pygame.time.delay(3000)

def real_word(word):
    text = WORD_FONT.render(word, 1, WHITE)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 4 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(4000)

def main():
    global hangman_status
    # Setup game loop

    FPS = 60
    clock = pygame.time.Clock()
    run = True
    
    
    
    while run:
        clock.tick(FPS)
        
        # update the display
        #win.fill(WHITE)
        # load image
        #win.blit(images[hangman_status], (150, 100))
        #pygame.display.update()
        
        
    
        
        
        # events
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters: 
                    x, y, ltr, visible = letter
                    dis = math.sqrt((x - m_x)** 2 + (y - m_y)** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)

                        if ltr not in word:
                            hangman_status += 1
        
        draw()                   
        
        
        won = True            
        for letter in word:
            if letter not in guessed:
                won = False
                break
            
            
        if won:
            won_message("You WON!")
    


        if hangman_status == 6:
            
            lost_message("You LOST!")
            real_word("The word was " + word)
            break
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    main()  
    
pygame.quit()
