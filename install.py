#life sucks installer thing idk rly know at this point
#convet to exe
import requests, os
r = requests.get('https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/install_init.py', allow_redirects=True)
open('install_init.py', 'wb').write(r.content)
from install_init import *
backround = pygame.image.load("196481.jpg")
backround = pygame.transform.scale(backround, (900,900))

def testing(kingkinggolembullbushkingwolf):
    screen.fill((0,0,0))
    screen.blit(backround, (0,0))
    title = golem('Install Lego Minecraft', (255,0,0), (width/2, 100), font)
    title.KING()

    buttons = button('Install', (width/2-100, height/2-50), (255,255,0), font, (200,100))
    buttons.createbutton()
    button_clicked = clicked(width/2-100, width/2+100, height/2-50, height/2+50)
    quit_button = button('Quit', (width/2-75, height-137.5), (200,182,193), font, (150,75))
    quit_button.createbutton()
    quit_button_click = clicked(width/2-75, width/2+75, height-137.5, height-62.5)
    
    text = golem(info, (200,236,203), (width/2, height-25), font2)
    text.KING()
    
    if quit_button_click:
        pygame.quit()

    if button_clicked and kingkinggolembullbushkingwolf == True:

        kingkinggolembullbushkingwolf = False

        test()

        os.chdir(original_file_path)

        os.remove('install_init.py')

        sys.exit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()        


    clock.tick(144)
    pygame.display.flip()


   #make it so it download version.txt staraight from github andreads to check instad of hard code
   # make pygame widnow exit after clicing install and open a new one that has a progress bar

   

    
while True:

    testing(kingkinggolembullbushkingwolf)
