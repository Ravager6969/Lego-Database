import pygame

class buttontextbox(object):
    def __init__(self,surface,rect,buttonlabels,buttonsize,font,maincolor=15749169,buttoncolor=10244339,buttontextcolor=(0,207,255),bordercolor=13917136,border=5,scrollvalue=20):
        self.surface=surface
        self.rect=rect
        self.buttonlabels=buttonlabels
        
        buttonsize[0]=min(self.rect.width,buttonsize[0])
        buttonsize[1]=min(self.rect.height,buttonsize[1])

        self.buttons=[GOLMBUTTON(self.surface,pygame.Rect(self.rect.left+max(0,int((self.rect.width-buttonsize[0])/2)),self.rect.top+buttonsize[1]*x,buttonsize[0],buttonsize[1]),buttoncolor,border) for x in range(len(buttonlabels))]
        self.font=font
        self.borderrect=pygame.Rect(self.rect.left+border,self.rect.top+border,self.rect.width-border*2,self.rect.height-border*2)
        self.scrollvalue=scrollvalue
        self.scroll=0
        self.maxscroll=max(0,buttonsize[1]*(len(self.buttons))-self.rect.height)
        self.maincolor=maincolor
        self.buttoncolor=buttoncolor
        self.buttontextcolor=buttontextcolor
        self.bordercolor=bordercolor
    
    def displaybuttons(self):
        pygame.draw.rect(self.surface,self.bordercolor,self.rect)
        pygame.draw.rect(self.surface,self.maincolor,self.borderrect)
        for x in range(len(self.buttons)):
            self.buttons[x].display(self.scroll,self.borderrect)
            if (self.buttons[x].rect.centery-int(self.font.size(self.buttonlabels[x])[1]/2)-self.scroll>self.borderrect.top and self.buttons[x].rect.centery+int(self.font.size(self.buttonlabels[x])[1]/2)-self.scroll<self.borderrect.bottom and self.font.size(self.buttonlabels[x])[0]<=self.borderrect.width):#hahahaha big if statement from a very efficient programmer
                self.displaytextoutline(self.surface,self.buttonlabels[x],(self.buttons[x].rect.centerx,self.buttons[x].rect.centery-self.scroll),self.font,color=self.buttontextcolor)
    
    def clickbuttons(self,mouse):
        for x in range(len(self.buttons)):
            if (self.buttons[x].click(mouse,self.scroll,self.rect)):
                return x
                #can change to return self.buttonlabels[x] if you want text but won't work with multiple buttons named the same thing
        return -69
    
    def scrollbox(self,scrollable_clickable_KINGbox,mouse):
        if (mouse[0]>self.rect.left and mouse[0]<self.rect.right and mouse[1]>self.rect.top and mouse[1]<self.rect.bottom):
            if (scrollable_clickable_KINGbox=="down"):
                self.scroll+=self.scrollvalue
            elif (scrollable_clickable_KINGbox=="up"):
                self.scroll-=self.scrollvalue
            else:
                print ("read the instructions next time")#what instructions? i don't see any all i see is messy code
        if (self.scroll<0):#prevent the user from scrolling once they reached the top
            self.scroll=0
        elif (self.scroll>self.maxscroll):
            self.scroll=self.maxscroll
        
    def displaytext(self,surface,text,position,font,color=(0,0,0),align=(0,0)):
        display=font.render(text,True,color)
        rect=display.get_rect()
        rect.centerx=int(position[0]-rect.width*0.5*(align[0]))
        rect.centery=int(position[1]-rect.height*0.5*(align[1]))
        surface.blit(display,rect)

    def displaytextoutline(self,surface,text,position,font,color=(0,0,0),outline_color=(0,0,0),align=(0,0)):
        size=max(1,(font.size(text)[1]*0.6*0.0625))#works best with KINGFONT.ttf
        outline=font.render(text,True,outline_color)
        rect=outline.get_rect()
        for a in range(-1,2):
            for b in range(-1,2):
                if (a!=0 or b!=0):
                    rect.centerx=int(position[0]-rect.width*0.5*(align[0])+int(a*size))
                    rect.centery=int(position[1]-rect.height*0.5*(align[1])+int(b*size))
                    surface.blit(outline,rect)
        self.displaytext(surface,text,position,font,color,align=align)

class GOLMBUTTON(object):
    def __init__(self,wernmrnwenreuwjndfjonbiudfbnjkrensdfoinweornweiornoskdnmvkcnbjklcvnbjkdrkrhjbgerjkltnrjbtidjnbiubndriutnodrngidnfgjkdnbjkcvnkbjndkjrbtjkrnbtjkebriktjberkjbntkjebnrtreter,rect,color,border):
        self.playplaykinggolemwolf=wernmrnwenreuwjndfjonbiudfbnjkrensdfoinweornweiornoskdnmvkcnbjklcvnbjkdrkrhjbgerjkltnrjbtidjnbiubndriutnodrngidnfgjkdnbjkcvnkbjndkjrbtjkrnbtjkebriktjberkjbntkjebnrtreter#don't worry, you can refer to this as playplaykinggolemwolf not what it actually is
        self.rect=rect#actually a normal variable name
        self.rect.left+=border
        self.rect.top+=border
        self.rect.width-=(border*2)
        self.rect.height-=(border*2)
        self.hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked=color
    def display(self,scroll,originalrect):#honestly a very simple function but so hard to read... it's all your fault "senior engineer", totally done by accident and/or lack of a creative mind
        ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone=pygame.Rect(self.rect)
        ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.top-=scroll
        if (ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.bottom<originalrect.top or ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.top>originalrect.bottom):
            return "this button must be hiding in the bush"
        if not (ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.top>=originalrect.top and ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.bottom<=originalrect.bottom):
            if (ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.bottom>=originalrect.top and ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.bottom<=originalrect.bottom):
                changesize=originalrect.top-ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.top
                ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.top+=changesize
                ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.height-=changesize
            elif (ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.top<=originalrect.bottom and ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.top>=originalrect.top):
                changesize=ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.bottom-originalrect.bottom
                ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone.height-=changesize
        pygame.draw.rect(self.playplaykinggolemwolf,self.hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked,ineedanothernameforarectthatiwillonlyuseheresoiamallowedtousealongvariablenameandincaseyoudidntknowimadeanameforoneofthesebutforgotsoiamtryingtocomeupwithanewone)
    def click(self,mouse,scroll,originalrect):
        if (mouse[0]>=originalrect.left and mouse[0]<=originalrect.right and mouse[1]>=originalrect.top and mouse[1]<=originalrect.bottom and mouse[0]>=self.rect.left and mouse[0]<=self.rect.right and mouse[1]>=self.rect.top-scroll and mouse[1]<=self.rect.bottom-scroll):#is that another giant if statment i see?!!??1!!??1!
            return True
        return False

if (__name__=="__main__"):
    pygame.init()
    pygame.font.init()
    screenx=1280
    screeny=900
    screen = pygame.display.set_mode((screenx,screeny))
    pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty > THE KING")
    clock = pygame.time.Clock()
    KINGFONT = pygame.font.Font("KINGFONT.ttf",32)
    KINGFONT1=pygame.font.Font("KINGFONT.ttf",24)
    buttonlist1=["Github?","'no'","Golem?","'no'","is it in our world?","is it in our world?","'you wasted a question'","can i have it back?","'no'","King?","'no'","do i use it?","'sometimes'","RAVAGER?","","","???","","ANSWER ME!!!","","i give up","'yes'","THE KING WINS AGAIN"]
    buttonlist2="You wouldn't dare scroll to the bottom of this text box,0 Spring Trap,6 Olive Branch,6 Open Business,18 Warped Arena,24 Minecart Madness,30 Cobweb,30 Sandy Gems,42 Shoulder Bash,48 Deep Diner,54 Junk Park,54 Parallel Plays,66 Well Cut,72 Double Swoosh,78 Canal Grande,78 Tornado Ring,90 Triple Dribble,96 Bouncing Diner,102 Fenced In,102 Split,114 Pinball Dreams,120 Crystal Arcade,126 Snake Prairie,126 Crossroads,138 Center Field,144 Chill Space,150 Some Assembly Required,150 Tiny Town,162 Pinhole Punt,168 Cell Division,174 Deeper Danger,174 Bandit Cove,186 Beach Ball,192 Stone Fort,198 Crated Factory,198 Massive Attack,210 Field Goal,216 Hard Rock Mine,222 Heat Wave,222 Hot Potato,234 Super Stadium,240 Undermine,246 Nuts & Bolts,246 Control Grande,258 Post Haste,264 Deathcap Trap,270 Land Ahoy,270 Traffic Jam,282 Backyard Bowl,288 Spare Space,294 Factory Rush,294 Perimeter,306 Penalty Kick,312 Escape Velocity,318 Layer Cake,318 Pit Stop,330 Galaxy Arena, , , , ,Congratulations I appreciate your hard work,I'll sign up for GitHub and add to Ravager6969's project".split(",")#yeah don't think you can just see what's at the end by scrolling through the code too bad i'm not signing up, you didn't even scroll through.
    THEKING=buttontextbox(screen,pygame.Rect(100,100,350,700),buttonlist1,[350,100],KINGFONT,scrollvalue=40)
    THEKING2=buttontextbox(screen,pygame.Rect(600,200,600,200),buttonlist2,[600,50],KINGFONT1,scrollvalue=4,border=2,maincolor=53247,buttoncolor=8508989,buttontextcolor=(255,3,204),bordercolor=16777215)

    #do not change information below\
    done=False
    # main program loop
    while (done == False):
        #all event processing goes below
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True#User perssed close
            if event.type==pygame.MOUSEBUTTONDOWN:
                if (event.button==1):
                    print (THEKING.clickbuttons(pygame.mouse.get_pos()),THEKING2.clickbuttons(pygame.mouse.get_pos()))
                elif (event.button==4):
                    THEKING.scrollbox("up",pygame.mouse.get_pos())
                    THEKING2.scrollbox("up",pygame.mouse.get_pos())
                elif (event.button==5):
                    THEKING.scrollbox("down",pygame.mouse.get_pos())
                    THEKING2.scrollbox("down",pygame.mouse.get_pos())
        #-----------------------------------
        


        #-----------------------------------
        screen.fill(0)

        THEKING.displaybuttons()
        THEKING2.displaybuttons()

        #print (clock.get_time(),clock.get_rawtime())
        #-----------------------------------
        pygame.display.flip()
        clock.tick(60)
        #-----------------------------------
    pygame.quit()