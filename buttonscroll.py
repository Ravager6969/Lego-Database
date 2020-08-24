import pygame,math

class buttontextbox(object):
    def __init__(self,surface,rect,buttonlabels,buttonsize,font,maincolor=15749169,buttoncolor=10244339,buttontextcolor=(0,207,255),bordercolor=13917136,scrollbarclickeddowncolor=9346021,border=5,scrollbarborder=20,scrollvalue=20):
        self.surface=surface
        self.rect=rect
        self.buttonlabels=buttonlabels
        
        buttonsize[0]=min(self.rect.width-scrollbarborder,buttonsize[0])
        buttonsize[1]=min(self.rect.height,buttonsize[1])

        self.buttons=[GOLMBUTTON(self.surface,pygame.Rect(self.rect.left+max(0,int((self.rect.width-scrollbarborder-buttonsize[0])/2)),self.rect.top+buttonsize[1]*x,buttonsize[0],buttonsize[1]),buttoncolor,border) for x in range(len(buttonlabels))]
        self.font=font
        self.borderrect=pygame.Rect(self.rect.left+border,self.rect.top+border,self.rect.width-border*2,self.rect.height-border*2)
        self.scrollvalue=int(scrollvalue)
        self.scroll=0
        self.scrollfloat=0.0
        self.maxscroll=max(0,buttonsize[1]*(len(self.buttons))-self.rect.height)
        self.maincolor=maincolor
        self.buttoncolor=buttoncolor
        self.buttontextcolor=buttontextcolor
        self.bordercolor=bordercolor
        self.scrollbarclickeddowncolor=scrollbarclickeddowncolor
        self.scrollbarborder=scrollbarborder
        self.beingclicked=False

        self.scrollbarrecttop1=self.rect.height*self.scroll/(self.maxscroll+self.rect.height)
        self.scrollbarrect=pygame.Rect(self.rect.right-self.scrollbarborder,self.rect.top+math.floor(self.scrollbarrecttop1),self.scrollbarborder,math.ceil(self.rect.height**2/(self.maxscroll+self.rect.height)))
    
    def displaybuttons(self):
        pygame.draw.rect(self.surface,self.bordercolor,self.rect)
        pygame.draw.rect(self.surface,self.maincolor,self.borderrect)
        if (self.beingclicked):
            pygame.draw.rect(self.surface,self.scrollbarclickeddowncolor,self.scrollbarrect)
        else:
            pygame.draw.rect(self.surface,self.bordercolor,self.scrollbarrect)
        for x in range(len(self.buttons)):
            self.buttons[x].display(self.scroll,self.borderrect)
            if (self.buttons[x].rect.centery-int(self.font.size(self.buttonlabels[x])[1]/2)-self.scroll>self.borderrect.top and self.buttons[x].rect.centery+int(self.font.size(self.buttonlabels[x])[1]/2)-self.scroll<self.borderrect.bottom and self.font.size(self.buttonlabels[x])[0]<=self.buttons[x].rect.width):#hahahaha big if statement from a very efficient programmer
                self.displaytextoutline(self.surface,self.buttonlabels[x],(self.buttons[x].rect.centerx,self.buttons[x].rect.centery-self.scroll),self.font,color=self.buttontextcolor)
    
    def clickbuttons(self,mouse):
        for x in range(len(self.buttons)):
            if (self.buttons[x].click(mouse,self.scroll,self.rect)):
                return x
                #can change to return self.buttonlabels[x] if you want text but won't work with multiple buttons named the same thing
        return -69
    
    def clickscroll(self,mouse,event):
        if (self.beingclicked and event==pygame.MOUSEBUTTONUP):
            self.beingclicked=False
        elif (mouse[0]>=self.scrollbarrect.left and mouse[0]<=self.scrollbarrect.right and mouse[1]>=self.scrollbarrect.top and mouse[1]<=self.scrollbarrect.bottom and self.beingclicked==False and event==pygame.MOUSEBUTTONDOWN):
            self.beingclicked=True
    
    def scrollbox(self,scrollable_clickable_KINGbox,mouse):
        if (self.beingclicked):
            return "T H E  K I N G  W I N S  A G A I N"
        elif (mouse[0]>self.rect.left and mouse[0]<self.rect.right and mouse[1]>self.rect.top and mouse[1]<self.rect.bottom):
            if (scrollable_clickable_KINGbox=="down"):
                self.scroll+=self.scrollvalue
                self.scrollfloat+=self.scrollvalue
            elif (scrollable_clickable_KINGbox=="up"):
                self.scroll-=self.scrollvalue
                self.scrollfloat-=self.scrollvalue
            else:
                print ("read the instructions next time")#what instructions? i don't see any all i see is messy code
        if (self.scroll<0):#prevent the user from scrolling once they reached the top
            self.scroll=0
        elif (self.scroll>self.maxscroll):
            self.scroll=self.maxscroll
        if (self.scrollfloat<0.0):#prevent the user from scrolling once they reached the top
            self.scrollfloat=0.0
        elif (self.scrollfloat>self.maxscroll):
            self.scrollfloat=float(self.maxscroll)
        
        #self.scrollbarrect=pygame.Rect(self.rect.right-self.scrollbarborder,self.rect.top+math.floor(self.rect.height*self.scroll/(self.maxscroll+self.rect.height)),self.scrollbarborder,math.ceil(self.rect.height**2/(self.maxscroll+self.rect.height)))
        self.scrollbarrecttop1=self.rect.height*self.scroll/(self.maxscroll+self.rect.height)
        self.scrollbarrect=pygame.Rect(self.rect.right-self.scrollbarborder,self.rect.top+math.floor(self.scrollbarrecttop1),self.scrollbarborder,math.ceil(self.rect.height**2/(self.maxscroll+self.rect.height)))
    
    def dragscroll(self,Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepository):
        oldscrollbarrecttop=int(self.scrollbarrect.top)
        self.scrollbarrect.top+=Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepository
        Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepositoryy=(self.scrollbarrect.top-oldscrollbarrecttop)#this 1000+character variable name has an extra y (has to be different from the one above and i couldn't think of a different name)
        
        newscroll=round(((self.rect.height*self.scrollfloat/(self.maxscroll+self.rect.height)+Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepositoryy)*(self.maxscroll+self.rect.height)/self.rect.height),10)
        
        self.scrollfloat=float(newscroll)

        if (self.scrollfloat<0.0):#prevent the user from scrolling once they reached the top
            self.scrollfloat=0.0
        elif (self.scrollfloat>self.maxscroll):
            self.scrollfloat=float(self.maxscroll)
        
        self.scroll=int(self.scrollfloat)
        
        self.scrollbarrecttop1=self.rect.height*self.scroll/(self.maxscroll+self.rect.height)
        self.scrollbarrect=pygame.Rect(self.rect.right-self.scrollbarborder,self.rect.top+math.floor(self.scrollbarrecttop1),self.scrollbarborder,math.ceil(self.rect.height**2/(self.maxscroll+self.rect.height)))
        
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
    KINGFONT1=pygame.font.Font("KINGFONT.ttf",22)
    buttonlist1=["Github?","'no'","Golem?","'no'","is it in our world?","is it in our world?","'you wasted question'","can i have it back?","'no'","King?","'no'","do i use it?","'sometimes'","RAVAGER?","","","???","","ANSWER ME!!!","","i give up","'yes'","THE KING WINS AGAIN"]
    buttonlist2="You wouldn't dare scroll to the bottom of this text box,0 Spring Trap,6 Olive Branch,6 Open Business,18 Warped Arena,24 Minecart Madness,30 Cobweb,30 Sandy Gems,42 Shoulder Bash,48 Deep Diner,54 Junk Park,54 Parallel Plays,66 Well Cut,72 Double Swoosh,78 Canal Grande,78 Tornado Ring,90 Triple Dribble,96 Bouncing Diner,102 Fenced In,102 Split,114 Pinball Dreams,120 Crystal Arcade,126 Snake Prairie,126 Crossroads,138 Center Field,144 Chill Space,150 Some Assembly Required,150 Tiny Town,162 Pinhole Punt,168 Cell Division,174 Deeper Danger,174 Bandit Cove,186 Beach Ball,192 Stone Fort,198 Crated Factory,198 Massive Attack,210 Field Goal,216 Hard Rock Mine,222 Heat Wave,222 Hot Potato,234 Super Stadium,240 Undermine,246 Nuts & Bolts,246 Control Grande,258 Post Haste,264 Deathcap Trap,270 Land Ahoy,270 Traffic Jam,282 Backyard Bowl,288 Spare Space,294 Factory Rush,294 Perimeter,306 Penalty Kick,312 Escape Velocity,318 Layer Cake,318 Pit Stop,330 Galaxy Arena, , , , ,Congratulations I appreciate your hard work,I'll sign up for GitHub and add to Ravager6969's project".split(",")#yeah don't think you can just see what's at the end by scrolling through the code too bad i'm not signing up, you didn't even scroll through.
    THEKING=buttontextbox(screen,pygame.Rect(100,100,350,700),buttonlist1,[330,100],KINGFONT,scrollvalue=40)
    THEKING2=buttontextbox(screen,pygame.Rect(600,200,600,200),buttonlist2,[600,50],KINGFONT1,scrollvalue=4,border=5,maincolor=53247,buttoncolor=8508989,buttontextcolor=(255,3,204),bordercolor=16777215)

    startmouseposition=0
    
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
                    #print (THEKING.clickbuttons(pygame.mouse.get_pos()))
                    THEKING.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONDOWN)
                    THEKING2.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONDOWN)
                    startmouseposition=pygame.mouse.get_pos()[1]
                elif (event.button==4):
                    THEKING.scrollbox("up",pygame.mouse.get_pos())
                    THEKING2.scrollbox("up",pygame.mouse.get_pos())
                elif (event.button==5):
                    THEKING.scrollbox("down",pygame.mouse.get_pos())
                    THEKING2.scrollbox("down",pygame.mouse.get_pos())
            if event.type==pygame.MOUSEBUTTONUP:
                if (event.button==1):
                    THEKING.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONUP)
                    THEKING2.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONUP)
        #-----------------------------------

        if (THEKING.beingclicked):
            THEKING.dragscroll(pygame.mouse.get_pos()[1]-startmouseposition)
        if (THEKING2.beingclicked):
            THEKING2.dragscroll(pygame.mouse.get_pos()[1]-startmouseposition)
        startmouseposition=pygame.mouse.get_pos()[1]

        #-----------------------------------
        screen.fill(0)

        THEKING.displaybuttons()
        THEKING2.displaybuttons()
        #print (THEKING.scrollbarrect)
        
        #print (clock.get_time(),clock.get_rawtime())
        #-----------------------------------
        pygame.display.flip()
        clock.tick(60)
        #-----------------------------------
    pygame.quit()
