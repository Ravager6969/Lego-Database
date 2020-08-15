import pygame,random

class golem(object):#100% original code written together by me and myself copyright 2020 my github page visit me at ravager6969 donate to me to help support the creation of massive projects like this
    def __init__(self,text,color,position,font):
        self.text=text
        self.thetextistoolargetofitinthetextboxdonttellmethisisabadvariablenameiwastoolazytothinkofaverydescriptiveone=color
        self.position=position
        self.font = font
    def KING(self,surgegalemrpvssproutjackyemzforworstmetaof2020):
        textdisplay=(self.font).render(self.text,True,self.thetextistoolargetofitinthetextboxdonttellmethisisabadvariablenameiwastoolazytothinkofaverydescriptiveone)
        hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked=textdisplay.get_rect()
        hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked.left=int(surgegalemrpvssproutjackyemzforworstmetaof2020[0])
        hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked.top=int(surgegalemrpvssproutjackyemzforworstmetaof2020[1])
        screen.blit(textdisplay,hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked)
    def __repr__(self):
        return self.text#you really do be wanting to print those golems

class ravager(object):
    def __init__(self,string,rect,font,color=(129,214,61),textcolor=(142,155,229),scrollvalue=20):
        self.textboxrect=rect
        self.string=string
        self.font=font
        if (color==(129,214,61)):#this color can go commit become king
            self.color=random.choice([(156,80,243),(240,80,49),(0,207,255),(212,91,208)])
        else:
            self.color=color
        self.textcolor=textcolor
        self.scrollvalue=scrollvalue#how many pixels to scroll by each input
        self.scrolly=int(self.textboxrect.top)#shifts all the text up by this amount of pixels
        self.GOLEMS=[]
        THEKINGx=0#yes it is the blit spot in the box
        THEKINGy=0
        line=""
        self.string=self.string.split(" ")#you could have just made string a list
        for x in range(len(self.string)):
            self.string[x]=" "+self.string[x]
            kingsize=self.font.size(self.string[x])
            if (THEKINGx+kingsize[0]>self.textboxrect.width):
                if (" " not in line):
                    while (self.font.size(line)[0]>self.textboxrect.width):
                        line=line[:-1]
                self.GOLEMS.append(golem(line,self.textcolor,(self.textboxrect.left,THEKINGy+self.textboxrect.top),self.font))
                line=self.string[x][1:]
                THEKINGx=kingsize[0]
                THEKINGy+=kingsize[1]
            else:
                if (THEKINGx==0):
                    line+=self.string[x][1:]#remove space at beginning of new line
                else:
                    line+=self.string[x]
                THEKINGx+=kingsize[0]
            if (x==len(self.string)-1):#add last line even if it does not take up the whole width
                self.GOLEMS.append(golem(line,self.textcolor,(self.textboxrect.left,THEKINGy+self.textboxrect.top),self.font))
    def scroll(self,direction,mouse):
        if (mouse[0]>self.textboxrect.left and mouse[0]<self.textboxrect.right and mouse[1]>self.textboxrect.top and mouse[1]<self.textboxrect.bottom):
            if (direction=="down"):
                self.scrolly+=self.scrollvalue
            elif (direction=="up"):
                self.scrolly-=self.scrollvalue
            else:
                print ("read the instructions next time")#what instructions? i don't see any all i see is messy code
        if (self.scrolly<self.textboxrect.top):#prevent the user from scrolling once they reached the top
            self.scrolly=self.textboxrect.top
        elif (self.scrolly>self.GOLEMS[-1].position[1]+self.font.size(self.GOLEMS[-1].text)[1]-self.textboxrect.height):
            self.scrolly=self.GOLEMS[-1].position[1]+self.font.size(self.GOLEMS[-1].text)[1]-self.textboxrect.height
    def display(self):
        pygame.draw.rect(screen,self.color,self.textboxrect)
        for x in range(len(self.GOLEMS)):
            if (self.GOLEMS[-1].position[1]+self.font.size(self.GOLEMS[x].text)[1]-self.textboxrect.top>self.textboxrect.height):#multiple lines
                if (self.GOLEMS[x].position[1]>=self.scrolly) and (self.GOLEMS[x].position[1]+self.font.size(self.GOLEMS[x].text)[1]<=self.scrolly+self.textboxrect.height):
                    self.GOLEMS[x].KING((self.GOLEMS[x].position[0],self.GOLEMS[x].position[1]-(self.scrolly-self.textboxrect.top)))
            else:#one line
                self.GOLEMS[x].KING((self.GOLEMS[x].position[0],self.GOLEMS[x].position[1]))

if (__name__=="__main__"):
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1280,900))# i am dirty hard coder so your display set mode thing must be called screen
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty")
    font1 = pygame.font.Font("KINGFONT.ttf",48)
    font2 = pygame.font.Font("KINGFONT.ttf",36)
    string = "Spring Trap Olive Branch Open Business Warped Arena Minecart Madness Cobweb Sandy Gems Shoulder Bash Deep Diner Junk Park Parallel Plays Well Cut Double Swoosh Canal Grande Tornado Ring Triple Dribble Bouncing Diner Fenced In Split Pinball Dreams Crystal Arcade Snake Prairie Does Anyone Remember How Terrible The 6 Week Cycle Map Rotation Was Imagine Only Playing Snake Prairie Every 3 Weeks Crossroads Center Field Chill Space Some Assembly Required The One Fat Pam Who Assigned This Is Definitely Sprout Ja-- Wait That Was A Long Time Ago Now That One Fat Pam is Definitely Surge Gale Mr.P Very Unplayable Terrible No Good Very Bad Tiny Town Pinhole Punt Cell Division Deeper Danger Bandit Cove Beach Ball Stone Fort Crated Factory Massive Attack Field Goal Hard Rock Mine Heat Wave Hot Potato Super Stadium Undermine Nuts & Bolts Control Grande Post Haste Sorry For The Interruption If You Count The Exact Number Of Words Here I Will Bid On Whack A King On GitHub Deathcap Trap Land Ahoy Traffic Jam Backyard Bowl Spare Space Factory Rush Perimeter Penalty Kick Escape Velocity Layer Cake Pit Stop Galaxy Arena Depression In Season Reset Golem King King Golem Wolf"
    #string="bolem ging sfsdjfklwejlkrjweirjwelkrjweklrkabcdefghijklmnopqrstuvwxyz gj"
    string2 = "a a a a aa  a a a a aa k k k k k k k k k kl l l l l l l l l 4 4 4 4 4 4 5 5 5 5 55 5 6 6 6 6 6 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 ^ 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9"

    textboxrect=ravager(string2,pygame.Rect(50,50,300,500),font1,color=(255,3,204),textcolor=(85,255,85),scrollvalue=60)#create instance of ravager
    textboxrect2=ravager(string,pygame.Rect(650,100,300,750),font2,scrollvalue=40)

    done=False
    # main program loop
    while (done == False):
        #all event processing goes below
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True#User perssed close
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==4:
                    textboxrect.scroll("up",pygame.mouse.get_pos())#scroll 20 pixels per spin
                    textboxrect2.scroll("up",pygame.mouse.get_pos())#scroll 20 pixels per spin
                elif event.button==5:
                    textboxrect.scroll("down",pygame.mouse.get_pos())
                    textboxrect2.scroll("down",pygame.mouse.get_pos())
            
        screen.fill((0,0,0))
        textboxrect.display()
        textboxrect2.display()
        
        

        
















        #just send that pygame display flip thing down there













        pygame.display.flip()
        clock.tick(60)

    pygame.quit()