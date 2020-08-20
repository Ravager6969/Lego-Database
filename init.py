#init

import pygame
from pygame.locals import *
import random, sys, time, datetime
from selenium import webdriver
from characters import kinggolem
from textbox import *


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


stop_slideshow = False

click_frame = True

patchnotes = open('Updates.txt', 'r')
patchnotes_read = patchnotes.read()
patchnotes.close()


#characters = [pygame.image.load('Pictures/Characters/character_1.jpg'),pygame.image.load('Pictures/Characters/character_2.jpg'),pygame.image.load('Pictures/Characters/character_3.jpg'),pygame.image.load('Pictures/Characters/character_4.jpg'),pygame.image.load('Pictures/Characters/character_5.jpg'),pygame.image.load('Pictures/Characters/character_6.jpg'),pygame.image.load('Pictures/Characters/character_7.jpg'),pygame.image.load('Pictures/Characters/character_8.jpg'),pygame.image.load('Pictures/Characters/character_9.jpg'),pygame.image.load('Pictures/Characters/character_10.jpg'),pygame.image.load('Pictures/Characters/character_11.jpg'),pygame.image.load('Pictures/Characters/character_12.jpg'),pygame.image.load('Pictures/Characters/character_13.jpg'),pygame.image.load('Pictures/Characters/character_14.jpg'),pygame.image.load('Pictures/Characters/character_15.jpg'),pygame.image.load('Pictures/Characters/character_16.jpg'),pygame.image.load('Pictures/Characters/character_17.jpg'),pygame.image.load('Pictures/Characters/character_18.jpg'),pygame.image.load('Pictures/Characters/character_19.jpg'),pygame.image.load('Pictures/Characters/character_20.jpg'),pygame.image.load('Pictures/Characters/character_21.jpg'),pygame.image.load('Pictures/Characters/character_22.jpg'),pygame.image.load('Pictures/Characters/character_23.jpg'),pygame.image.load('Pictures/Characters/character_24.jpg'),pygame.image.load('Pictures/Characters/character_25.jpg'),pygame.image.load('Pictures/Characters/character_26.jpg'),pygame.image.load('Pictures/Characters/character_27.jpg'),pygame.image.load('Pictures/Characters/character_28.jpg'),pygame.image.load('Pictures/Characters/character_29.jpg'),pygame.image.load('Pictures/Characters/character_30.jpg'),pygame.image.load('Pictures/Characters/character_31.jpg'),pygame.image.load('Pictures/Characters/character_32.jpg'),pygame.image.load('Pictures/Characters/character_33.jpg'),pygame.image.load('Pictures/Characters/character_34.jpg'),pygame.image.load('Pictures/Characters/character_35.jpg'),pygame.image.load('Pictures/Characters/character_36.jpg'),pygame.image.load('Pictures/Characters/character_37.jpg'),pygame.image.load('Pictures/Characters/character_38.jpg'),pygame.image.load('Pictures/Characters/character_39.jpg'),pygame.image.load('Pictures/Characters/character_40.jpg'),pygame.image.load('Pictures/Characters/character_41.jpg'),pygame.image.load('Pictures/Characters/character_42.jpg')]



random_image = random.randint(1,7)

random_image_storage = random_image



slideshow = False

red = (255,0,0)
try:
    font = pygame.font.Font("KINGFONT.ttf",40)
    font2 = pygame.font.Font("KINGFONT.ttf", 25)
except FileNotFoundError:
    print('Please Provide a Font File and Rename it "'"KINGFONT.ttf"'"')
    sys.exit()
cyan = (0,255,255)
random_color = (random.randrange(100,255)),(random.randrange(100,255)), (random.randrange(100,255))
sky_blue = (39,145, 251)
gold = (255,215,0)


size = w, h = 1920, 1080 #change non-fullscreen size
pygame.display.set_caption('Lego Minecraft Database')


#make scrollagble text box for updates and remove updates button and add music button add more music options other than minecraft too like roof and super mario world 3d land and super mario 64 staff roll

characters = False
characters_choice = False


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, pygame.RESIZABLE)



fullscreen = True

width = screen.get_width()
height = screen.get_height()


slideshow_image = pygame.image.load("Pictures/Gallery/world_image_" + str(random_image) + '.jpg')
slideshow_image = pygame.transform.scale(slideshow_image, (width,height))


#large_button_width = (width/5 + i*(width/5))-150

backround = pygame.image.load("Pictures/world_day1.jpg")
sun = pygame.image.load("Pictures/Sun1.png")
moon = pygame.image.load("Pictures/5893ae1aad54eb2e300e756492593c01.png")
sun = pygame.transform.scale(sun, (100,100))
moon = pygame.transform.scale(moon, (100,100))

timer_max = 0.2

timer_69 = timer_max

if current_time.hour >= 20 or current_time.hour <= 9:
    #backround = pygame.image.load("Pictures/world_night1.jpg")#night picture
    night = True

else:
    #backround = pygame.image.load("Pictures/world_day1.jpg")#day picture
    day = True

backround = pygame.transform.scale(backround, (1920,1080))
main_menu = True
click_value = True

character_page = 1

#non main menu screen variables
music = False
options = False
controls = False
about = False
github = False

##def hubgit(random_image):
#    #resize
    


patchnotes_display = ravager(screen,str(patchnotes_read), pygame.Rect(width-(width-50),height-325, 350, 275), font2, sky_blue, gold, scrollvalue=30 )


def long_if_statement(number, click_value):
    for x in kinggolem.keys():
        if str(number) in x:
            return(x)

#id below character
def display_characters(character_page, click_value):

    #character_image = pygame.image.load("Pictures/Characters/character_" + str(x+((character_page-1)*14)))


   

  
    
    
    if character_page == 1:
        for i in range(1,3):
            for x in range(1,8):
                character_width = x*width/9
                character_height = i*height/3

                
                #character_image = characters_list[x+((character_page-1)*14)-1   ]
                #character_image = pygame.transform.scale(character_image, (100,177))
                #screen.blit(character_image, (character_width, character_height))  
                character_image = button('', (character_width, character_height), sky_blue, font, (100,177))
                character_image.createbutton()

                click_l = clicked(character_width, character_width+100, character_height, character_height+177)
          

                if click_l and click_value: 
                
                    click_value = False
                    bruh = long_if_statement(x+(i-1)*7+(character_page-1)*14, click_value)
                
                    characters_choice = False
                    return(characters_choice, bruh)
                    

                elif click_l and click_value == False:
                    click_value = False
                else:
                    click_value = True
                

       

    elif character_page == 2: #make x be the characterchoice int and get the key from the dict and add based on previous ones like 2nd page will have x+14
        for i in range(1,3):
            for x in range(1,8):
                character_width = x*width/9
                character_height = i*height/3

                character_image = button('', (character_width, character_height), red, font, (100,177))
                character_image.createbutton() 

                click_l = clicked(character_width, character_width+100, character_height, character_height+177)
          

                if click_l and click_value: 
                
                    click_value = False
                    bruh = long_if_statement(x+(i-1)*7+(character_page-1)*14, click_value)
                
                    characters_choice = False
                    return(characters_choice, bruh)
                   

                elif click_l and click_value == False:
                    click_value = False
                else:
                    click_value = True
    else:
        for i in range(1,3):
            for x in range(1,8):
                character_width = x*width/9
                character_height = i*height/3

                character_image = button('', (character_width, character_height), gold, font, (100,177))
                character_image.createbutton() 

                click_l = clicked(character_width, character_width+100, character_height, character_height+177)
          

                if click_l and click_value: 
                
                    click_value = False
                    bruh = long_if_statement(x+(i-1)*7+(character_page-1)*14, click_value)
                 
                    characters_choice = False
                    return(characters_choice, bruh)
                  

                elif click_l and click_value == False:
                    click_value = False
                else:
                    click_value = True


#def github(timer_69, random_image, random_image_storage, slideshow_image, timer_max=2):
def github(timer_69,random_image,timer_max=2):
    if timer_69>= timer_max:
        random_image_storage = random_image
        random_image = random.randint(1,7)
        while random_image == random_image_storage:
            random_image = random.randint(1,7)
        timer_69 = 0
    
    else:
        timer_69 += 0.01
    
    slideshow_image = pygame.image.load("Pictures/Gallery/world_image_" + str(random_image) + '.jpg')
    slideshow_image = pygame.transform.scale(slideshow_image, (width,height))
    screen.blit(slideshow_image, (0,0))
    
    return(timer_69,random_image)






def opengithub():
    browser = webdriver.Firefox(executable_path="C:\Temp\geckodriver.exe")
    browser.get('https://github.com/Ravager6969/Lego-Database.git')
    


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
        textrect.center=self.pos #change to left and top rect and make option as an arguement to center of left allighend 
        screen.blit(textdisplay,textrect)
    def KINGS(self):
        textdisplay=(self.font).render(self.text,True,self.color)
        textrect=textdisplay.get_rect()
        textrect.left=self.pos[0]
        textrect.top=self.pos[1] #change to left and top rect and make option as an arguement to center of left allighend 
        screen.blit(textdisplay,textrect)

characterchoice = 'Creeper_33'

def stats_box(x): #make rect so it is bigger than higher the skill level
    #stat_box = golem(str(kinggolem[characterchoice][3][x-1]), red, (width/2+500, height/2+100+x*100), font)
    #stat_box.KINGS()
    #special detection for x == 2
    stat_box_base = button('', (width/2+400, height/2+100+x*100), red, font, (300, 50))
    stat_box_base.createbutton()
    if kinggolem[characterchoice][3][x-1] == 0:
        pass
    else:
        stat_box_fill = button('', (width/2+400, height/2+100+x*100), sky_blue, font, (kinggolem[characterchoice][3][x-1]*30,50))
        stat_box_fill.createbutton()
    stat_box_integer = golem(str(kinggolem[characterchoice][3][x-1]), gold, (width/2+400+150,height/2+100+x*100+3), font)
    stat_box_integer.KINGS()


def stats():
    for x in range(3):
        if x == 0:
         
            stats_name = 'Crafting'
        elif x == 1:
           
            stats_name = 'Mining'
        elif x == 2:

            stats_name = 'Combat'
        
        stats_display = golem(stats_name, red, (width/2+200, height/2+100+x*100), font)
        stats_display.KINGS()
        stats_box(x)

class id(object):
    #def __init__(self, name, job, residence, skills, club, personality, picture): #skills is a [0,0,0]
    def __init__(self, name, job, residence, club):
        self.name = name
       
        
        self.job = job
        
        self.residence = residence
        self.club = club
        '''
        self.picture
        '''

    

    def create_id(self): #change colors
        #name, id, image
        name = golem(self.name.split('_')[0], (red), (width/5+50, height/4+50), font)
        name.KING()

        id_display = golem(self.name.split('_')[1], (239, 255, 42), (width/4-50, height/3+25), font)
        id_display.KING()

        occupation = golem('Occupation:' + '   ' + self.job, (196, 35, 181), (width/2+200, height/4+50), font)
        occupation.KINGS()

        residence = golem('Residence:' + '   ' + self.residence, (255, 157, 89), (width/2+200, height/3+25), font)
        residence.KINGS()

        club = golem('Club:' + '   ' + self.club, (79, 201, 145), (width/2+200, height/3+100), font)
        club.KINGS()

        stats_text = golem('Stats: ', (155, 28, 122), (width/2+200, height/2), font)
        stats_text.KINGS()

        stats()

        best_skill_box = button('', (width-250, height-250), sky_blue, font, (220,220))
        best_skill_box.createbutton()

        if kinggolem[characterchoice][3][0] > kinggolem[characterchoice][3][1] and kinggolem[characterchoice][3][0] > kinggolem[characterchoice][3][3]:
            best_skill = kinggolem[characterchoice][3][0]
        elif kinggolem[characterchoice][3][1] > kinggolem[characterchoice][3][0] and kinggolem[characterchoice][3][1] > kinggolem[characterchoice][3][3]: 
            best_skill = kinggolem[characterchoice][3][1]
                
        else:
            best_skill = kinggolem[characterchoice][3][3]    

        best_skill_text = golem('Best Skill', red, (width-220, height-250), font)
        best_skill_text.KINGS()
        best_skill_integer = golem(str(best_skill) + '/10', red, (width-180, height-200), font)
        best_skill_integer.KINGS()

        sum_skills_text = golem('Sum of Skills', red, (width-250, height-150), font)
        sum_skills_text.KINGS()
        sum_skills_integer = golem(str(kinggolem[characterchoice][3][0] + kinggolem[characterchoice][3][1] + kinggolem[characterchoice][3][3]) + '/30', red, (width-200, height-100), font)
        sum_skills_integer.KINGS()
        

music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
music_choice_display = music_display(musicchoice)
music_text_2 = golem(music_choice_display, cyan, (width/2+150,height-50), font)
music_text_1.KING()
music_text_2.KING()


click_c = clicked(width-250, width-50, height-150, height-50)
click_d = clicked(50, 250, height-150, height-50)