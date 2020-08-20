#install init

#life sucks installer thing idk rly know at this point

#from Lego_Minecraft import *


import requests, os, shutil, time, pygame, sys, tkinter, urllib.request
from tkinter import filedialog
from pygame.locals import *
pygame.init()
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


latest_version = '1.0'

os.chmod('install.py', 0o777)

original_file_path = os.getcwd()

#file_path = os.getcwd() + '\\Lego Minecraft Database'

#path = "Lego Minecraft Database/Pictures"

#path_2 = "Lego Minecraft Database/Sounds"

root = tkinter.Tk()

root.withdraw()

dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

file_path = dirname

path = file_path + '/Pictures'

path_2 = file_path + '/Sounds'

#update
#shutil.rmtree(file_path)

def github(url, name):
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)


def create_files(message):
        
    for x in github_pages.keys():
        if x == 'world_day1.jpg':
            os.chdir(file_path + '\\Pictures')
        elif x == 'haggstorm.mp3':
            os.chdir(file_path + '\\Sounds')

        theking1 = x
    #for x in github_pages[theking1]:

        github(github_pages[theking1], theking1)
    
    print(message)



def test():

    

    try:
        os.makedirs(path)

        os.makedirs(path_2)

        os.chdir(file_path)

        print('Downloading...')

        message = 'Lego Minecraft Database Successfully Installed'

        create_files(message)
        
    except FileExistsError:
        try:
            os.chdir(file_path)
    
            version = open('version.txt', 'r')

            version_read = version.read()

            version.close()

            os.chdir(original_file_path)

            if version_read == latest_version:
                message = 'Lego Minecraft Database is Already Installed and is Up to Date'
                print(message)
            
            else:
                print('Updating...')
                '''
                for filename in os.listdir(file_path):
                    file_path_join = os.path.join(file_path, filename)
                    os.chmod(original_file_path, 0o777)
                    os.remove(file_path_join)
                '''
                shutil.rmtree(file_path)
                time.sleep(1)
                message = 'Lego Minecraft Database Successfully Updated'
                os.makedirs(path)
                os.makedirs(path_2)
                os.chdir(file_path)
                create_files(message)
                

        except FileNotFoundError:
            pass
            
        
            

        
            

    
        

   

    

    
   



pygame.font.init()
try:
        font = pygame.font.Font("KINGFONT.ttf", 30)
        font2 = pygame.font.Font("KINGFONT.ttf", 20)
except FileNotFoundError:
        print('Please Provide a Font File and Rename it "'"KINGFONT.ttf"'"')
size = width, height = 900, 900

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
kingkinggolembullbushkingwolf = True

info = "100% legit no scam or virus"

github_pages = {
        'Lego_Minecraft.py':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Lego_Minecraft.py',
        'textbox.py':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/textbox.py',
        'characters.py':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/characters.py',
        'init.py':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/init.py',
        'Updates.txt':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Updates.txt',
        'version.txt':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/version.txt',
        'world_day1.jpg':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Pictures/world_day1.jpg',
        '5893ae1aad54eb2e300e756492593c01.png':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Pictures/5893ae1aad54eb2e300e756492593c01.png',
        'Sun1.png':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Pictures/Sun1.png',
        'haggstorm.mp3':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Sounds/haggstorm.mp3',
        'sweden.mp3':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Sounds/sweden.mp3',
        'wet_hands.mp3':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Sounds/wet_hands.mp3',
        'mice_on_venus.mp3':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Sounds/mice_on_venus.mp3',
        'minecraft.mp3':'https://raw.githubusercontent.com/Ravager6969/Lego-Database/master/Sounds/minecraft.mp3'
}
