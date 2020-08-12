import pygame
from pygame.locals import *
import random, sys, time, datetime
#init
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
current_time = datetime.datetime.now()
#make it print the time in the left bottom corner
#music things#width/5+(width/5)
pygame.mixer.set_num_channels(2)
backround_music = pygame.mixer.Channel(1)

musicchoice = random.choice(['Sounds/haggstorm.mp3', 'Sounds/mice_on_venus.mp3', 'Sounds/minecraft.mp3', 'Sounds/wet_hands.mp3', 'Sounds/sweden.mp3'])
pygame.mixer.music.load(musicchoice)
pygame.mixer.music.play()
music_message_timer = 0
volumeup, volumedown = False, False
volume = 1
night = False
day = False

red = (255,0,0)
font = pygame.font.Font("KINGFONT.ttf",40)
cyan = (0,255,255)
random_color = (random.randrange(100,255)),(random.randrange(100,255)), (random.randrange(100,255))


size = w, h = 1920, 1080 #change non-fullscreen size
pygame.display.set_caption('Lego Minecraft Database')


#make scrollagble text box for updates and remove updates button and add music button add more music options other than minecraft too like roof and super mario world 3d land and super mario 64 staff roll



screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, pygame.RESIZABLE)

fullscreen = True

width = screen.get_width()
height = screen.get_height()

#large_button_width = (width/5 + i*(width/5))-150

backround = pygame.image.load("Pictures/world_day1.jpg")
sun = pygame.image.load("Pictures/Sun1.png")
moon = pygame.image.load("Pictures/5893ae1aad54eb2e300e756492593c01.png")
sun = pygame.transform.scale(sun, (100,100))
moon = pygame.transform.scale(moon, (100,100))


if current_time.hour >= 20 or current_time.hour <= 9:
    #backround = pygame.image.load("Pictures/world_night1.jpg")#night picture
    night = True

else:
    #backround = pygame.image.load("Pictures/world_day1.jpg")#day picture
    day = True

backround = pygame.transform.scale(backround, (1920,1080))
main_menu = True

click_value = True


#non main menu screen variables
music = False
options = False






def music_display(musicchoice):
    if musicchoice == 'Sounds/haggstorm.mp3':
        return('Haggstorm')
    elif musicchoice == 'Sounds/mice_on_venus.mp3':
        return('Mice on Venus')
    elif musicchoice == 'Sounds/minecraft.mp3':
        return('Minecraft')
    elif musicchoice == 'Sounds/wet_hands.mp3':
        return('Wet Hands')
    else:
        return('Sweden')


def clicked(pos1, pos2, pos3, pos4): #pos1 left, pos2 right, pos3 top, pos4 bottom
        mousepos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if mousepos[0] > pos1 and mousepos[0] < pos2 and mousepos[1] > pos3 and mousepos[1] < pos4 and pressed[0]:
            return(True)

class button(object):
    def __init__(self, text, pos, color, font, size):
        self.text = text
        self.pos = pos
        self.color = color
        self.font = font
        self.size = size
        self.buttonpos = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        
    
    def createbutton(self):
        global buttonrect
        buttonrect = pygame.draw.rect(screen, self.color, self.buttonpos)
        buttontext=golem(self.text,(212,91,208),(int(self.pos[0]+self.size[0]/2),int(self.pos[1]+self.size[1]/2)),self.font)
        buttontext.KING()
        
        
class golem(object):
    def __init__(self, text, color, pos, font):
        self.text = text
        self.color = color
        self.pos = pos
        self.font = font
    def KING(self):
        textdisplay=(self.font).render(self.text,True,self.color)
        textrect=textdisplay.get_rect()
        textrect.center=self.pos
        screen.blit(textdisplay,textrect)



class id(object):
    def __init__(self, name, id_number, job, residence, skills, club, personality, picture): #skills is a [0,0,0]
        self.name = name
        self.id_number = id_number
        self.job = job
        self.residence = residence
        self.skills = skills
        self.club = club
        self.personality = personality
        self.picture
    def create_id(self):
        #blit
        screen.blit(self.picture, ())

music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
music_choice_display = music_display(musicchoice)
music_text_2 = golem(music_choice_display, cyan, (width/2+150,height-50), font)
music_text_1.KING()
music_text_2.KING()


while True and __name__ == '__main__':

    screen.fill((0,0,0))

    screen.blit(backround,(0,0))

    
    #music
    if pygame.mixer.music.get_busy() == 0:
        musicchoice = random.choice(['Sounds/haggstorm.mp3', 'Sounds/mice_on_venus.mp3', 'Sounds/minecraft.mp3', 'Sounds/wet_hands.mp3', 'Sounds/sweden.mp3'])
        pygame.mixer.music.load(musicchoice)
        pygame.mixer.music.play()
        music_message_timer = 0
    
    elif music_message_timer < 1:
        music_choice_display = music_display(musicchoice)
        music_text_2 = golem(music_choice_display, cyan, (width/2+150,height-50), font)
        music_text_1.KING()
        music_text_2.KING()
        music_message_timer += 0.01
  
    #print(clock.get_rawtime())
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_e:
                pygame.quit()
            if event.key == K_w: #cycle music
                pygame.mixer.music.stop()
            if event.key == K_f:
                if fullscreen == True:
                    pygame.display.quit()
                    pygame.display.init()
                    screen = pygame.display.set_mode(size)
                    width = screen.get_width()
                    height = screen.get_height()
                    fullscreen = False
                    music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-100), font)
                else:
                    pygame.display.quit()
                    pygame.display.init()
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    width = screen.get_width()
                    height = screen.get_height()
                    fullscreen = True
                    music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-100), font)
            if event.key == K_p:
                patchnotes = open('updates.txt', 'r')
                patchnotesread = patchnotes.read()
                patchnotes.close()
                print(patchnotesread)
            if event.key == K_UP:
                volumeup = True
                
            if event.key == K_DOWN:
                volumedown = True

            if event.key == K_b:
                main_menu = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                volumeup = False

            if event.key == K_DOWN:
                volumedown = False
             


  
    if volumeup and volume <= 1:
        volume += 0.01
        pygame.mixer.music.set_volume(volume)
     
    if volumedown and volume >= 0.01:
        volume -= 0.01
        pygame.mixer.music.set_volume(volume)
    if volumeup or volumedown:
        volume_display = golem(str("%.1f" % volume), (random_color), (width-100,height-100), font)
        volume_display.KING()


    #main 

    text = golem('Lego Minecraft Database', red, (width/2,height-(height-100)), font)
    text.KING()

    
    #moon and sun
    if night:
        screen.blit(moon, (width-125, height-(height-50)))#sun and moon 200x200

    if day:
        screen.blit(sun, (width-125, height-(height-50)))#sun and moon 200x200
    

    #time
    if current_time.minute-10 < 0:

        current_time_display = str(str(current_time.hour) + ':' + str(0) + str(current_time.minute))

    else:

        current_time_display = str(str(current_time.hour) + ':' + str(current_time.minute))
  
    timedisplay = golem(current_time_display, random_color, (width-200, height-(height-100)), font)
    timedisplay.KING()


    if main_menu == True:
        for i in range(0, 4): #main buttons
            if i == 0:
                largebuttons = 'Gallary'
            elif i == 1:
                largebuttons = 'Characters'
            elif i == 2:
                largebuttons = 'Clubs'
            else:
                largebuttons = 'Jobs'

            large_button_width = (width/5 + i*(width/5))-150
            #store width as variable and do another if statement to determine the pos for the click function


            #b = button('hello', ((width/5 + i*(width/5))-300, height/2), (142,155,229), font, (200,100)) #create button #five buttons

            b = button(largebuttons, (large_button_width, height/2), (142,155,229), font, (200,100)) #create button
            b.createbutton()

            #print(large_button_width)
            #print(pygame.mouse.get_pos())
            #print(height/2)
        
            click_l = clicked(large_button_width, large_button_width+200, height/2, height/2+100)
            #print(large_button_width, large_button_width+200, height/2, height/2+100)
            #print(click)

            if click_l and click_value: #back button sets main_menu to True
                #print('king')
                click_value = False
                if i == 0:
                    print('gallary')
                    #add images after village set

                    main_menu = False
                if i == 1:
                    print('characters')
                    #dict take [0] to find the values and put into id function
                    main_menu = False
                if i == 2:
                    print('clubs')
                    main_menu = False
                if i == 3:
                    print('jobs')
                    main_menu = False


            #make it so it makes antoher variabgle true and starts to print another function getting rid of the main screen
            elif click_l and click_value == False:
                click_value = False
            else:
                click_value = True
            

        for i in range(0, 3):
            if i == 0:
                smallbuttons = 'Music'
  
            elif i == 1:
                smallbuttons = 'Quit'
   
            else:
                smallbuttons = 'Options' #options will have about inside it and have copyright information for mojang on it
 


            small_button_width = (width/3 + i*(width/5))-200

            b = button(smallbuttons, (small_button_width, height-200), (152,5,152), font, (150,75)) #create button
            b.createbutton()


            #implement into for loop above
            click_s = clicked(small_button_width, small_button_width+150, height-200, height-125)
            #print(small_button_width)
            #print(small_button_width, small_button_width+150, height-200, height-125)

            if click_s and click_value:
                
                click_value = False
                if i == 0:
                    print('music')
                    music = True
                    main_menu = False
                if i == 1:
                    print('quit')
                    pygame.quit()
                    #dict take [0] to find the values and put into id function
                    main_menu = False
                if i == 2:
                    print('options')
                    options = True
                    main_menu = False
               
                #make it so it makes antoher variabgle true and starts to print another function getting rid of the main screen
            elif click_s and click_value == False:
                click_value = False
            else:
                click_value = True


    if main_menu == False:

        back_button = button('Back', (width-(width-50), height-(height-50)), (0,207,255), font, (200,100))
        back_button.createbutton()
        click_b = clicked(width-(width-50), width-(width-250), height-(height-50), height-(height-150))

        if click_b and click_value:
            main_menu = True
            click_value = False
                
        elif click_b and click_value == False:

            click_value = False

        else:

            click_value = True




    #buttons
    if music and main_menu == False:
        music_box = button('', (50, height/2-250), (255,102,102), font, (400,600))#text pos color font size
        music_box.createbutton()
        music_box_title = golem('Songs', (0,0,0), (250, height/2-210), font)
        music_box_title.KING()

    else:
        music = False





    if options and main_menu == False:
        for x in range(1,4): #about(world information, dates, minecraft copyright, program information like lines of code idk), controls, github page and maybe other social pages
            if x == 1:
                options_text = 'About'
            elif x == 2:
                options_text = 'Controls'
            else:
                options_text = 'Github'



            main_options_box_height = x*(1080/4)-50

            main_options_box = button(options_text,  (width/2-150, main_options_box_height), (165,132,192) , font, (300, 100))

            main_options_box.createbutton()

            click_soc = clicked(width/2-150, width/2+150, main_options_box_height, main_options_box_height+100)

           
           
          
            
            if click_soc and click_value: #810 1110

                click_value = False
                if x == 1:
                    print('about')
                    options = False
                    about = True
               
                elif x == 2:
                    print('controls')
                    options = False
                    controls = True
               
                else:
                    print('github')
                    options = False
                    github = True #if learn java or some shit than add link
               
                    
               

            elif click_soc and click_value == False:

                click_value = False

            else:
                click_value = True
            #print(click_value)

   












    clock.tick(144)

    













    pygame.display.flip()
