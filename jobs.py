import pygame
from characters import golemwolf
import buttonscroll
import textbox#multiple lines for my imports make my program look fancy
#-----------------------------------
def getbuttonlist(jobs,categories):#this thing gets all the job information that the boxes display
    BULL=["Job List"]
    POCODOUBLETANKTAKESSOMUCHSKILLWOW=[0]
    RVGR=list(jobs.keys())

    for x in categories:
        BULL.append(x)
        POCODOUBLETANKTAKESSOMUCHSKILLWOW.append(len(BULL)-1)
        for y in range(len(categories[x])):
            if (categories[x][y] in RVGR):
                BULL.append(categories[x][y])
                RVGR.remove(categories[x][y])
    if (len(RVGR)>0):
        BULL.append("Other")
        POCODOUBLETANKTAKESSOMUCHSKILLWOW.append(len(BULL)-1)
        for x in range(len(RVGR)-1,-1,-1):
            BULL.append(RVGR[x])
    
    return (BULL,POCODOUBLETANKTAKESSOMUCHSKILLWOW)
#-----------------------------------
#just the copy and pasted stuff
pygame.init()
pygame.font.init()
screenx=1280
screeny=900
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty > THE KING")
clock = pygame.time.Clock()
KINGFONT = pygame.font.Font("KINGFONT.ttf",36)
#-----------------------------------
#defining variables
categories={
    "Mining and Construction":("Woodcutter","Building Master and World Editor"),
    "Combat and Defenses":("Raid Defender","Structure Guard","Night Patroller"),
    "Village Administration":("Mayor's Assistant","Mayor","Bank Master"),
    "Village Services":("World Gatekeeper","Shipping Company","Farming Master","Trading Master"),
    "Suppliers":("Animal Salesman and Caretaker","Healer and Fish Supplier","Potion Brewer","Blacksmith")
}
GOLM,WOLF=getbuttonlist(golemwolf,categories)
ir=pygame.Rect(800,300,380,500)#ir means information rect
startmouseposition=0
displayjob=""
#-----------------------------------
#defining the scrollable boxes
scrollable_clickable_KINGbox=buttonscroll.buttontextbox(screen,pygame.Rect(ir.left-700,ir.top,600,ir.height),GOLM,[580,80],KINGFONT,maincolor=8508989,scrollbarclickeddowncolor=16777216-65332+3*256,scrollvalue=50)#yes i use very illegal color here
for x in range(len(WOLF)):
    KINGCOLR=[[255,3,204],0]
    if (x==0):
        KINGCOLR=[[255-x for x in KINGCOLR[0]],13917136]
    elif (x==1):
        KINGCOLR[1]=85*(65536+256)+255#wow hard coded numbers, didn't know what else to expect
    elif (x==2):
        KINGCOLR[1]=240*65536+80*256+49
    elif (x==3):
        KINGCOLR[1]=255*(65536+256)+85
    elif (x==4):
        KINGCOLR[1]=85*65537+256**2-256
    elif (x==5):
        KINGCOLR[1]=239*65536+138*256+84
    scrollable_clickable_KINGbox.changebuttoncolor(WOLF[x],KINGCOLR[0])
    scrollable_clickable_KINGbox.changebuttonbackground(WOLF[x],int(KINGCOLR[1]))
jobinformation=textbox.ravager(screen,"Click on a job using the box on the left.",pygame.Rect(ir.left+5,ir.top+5,ir.width-10,ir.height-10),KINGFONT,color=0)
#-----------------------------------
#the signature-hardcoded-games-copied-loop-from-more-than-a-year-ago main loop of the program
#do not change information below\
done=False
# main program loop
while (done == False):
    #all event processing goes below
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True#User perssed close
    #-----------------------------------
    #click and scroll detection
        if event.type==pygame.MOUSEBUTTONDOWN:
            if (event.button==1):
                index1=scrollable_clickable_KINGbox.clickbuttons(pygame.mouse.get_pos())
                if (index1<0):
                    scrollable_clickable_KINGbox.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONDOWN)
                    startmouseposition=pygame.mouse.get_pos()[1]
                elif (index1 not in WOLF):
                    jobname=GOLM[index1]
                    jobmembers=" \\n \\n Workers:"
                    for x in range(len(golemwolf[jobname])):
                        jobmembers+=" \\n "+golemwolf[jobname][x]
                    jobinformation.changetext(jobname+jobmembers)
                elif (index1==0):
                    jobinformation.changetext("You really thought that \"Job List\" was actually a job?! \\n \\n Come on, stop trying to break my program.")
                else:
                    jobinformation.changetext("Spring Trap Olive Branch Open Business Warped Arena \\n Minecart Madness Cobweb Sandy Gems Shoulder Bash \\n Deep Diner Junk Park Parallel Plays Well Cut \\n Double Swoosh Canal Grande Tornado Ring Triple Dribble \\n Bouncing Diner Fenced In Split Pinball Dreams \\n Crystal Arcade Snake Prairie Crossroads Center Field \\n Chill Space Some Assembly Required Tiny Town Pinhole Punt \\n Cell Division Deeper Danger Bandit Cove Beach Ball \\n Stone Fort Crated Factory Massive Attack Field Goal \\n Hard Rock Mine Heat Wave Hot Potato Super Stadium \\n Undermine Nuts & Bolts Control Grande Post Haste \\n Deathcap Trap Land Ahoy Traffic Jam Backyard Bowl \\n Spare Space Factory Rush Perimeter Penalty Kick \\n Escape Velocity Layer Cake Pit Stop Galaxy Arena \\n Play Play King Bolem Wolf")
            elif (event.button==4):
                jobinformation.scroll("up",pygame.mouse.get_pos())
                scrollable_clickable_KINGbox.scrollbox("up",pygame.mouse.get_pos())
            elif (event.button==5):
                jobinformation.scroll("down",pygame.mouse.get_pos())
                scrollable_clickable_KINGbox.scrollbox("down",pygame.mouse.get_pos())
        if event.type==pygame.MOUSEBUTTONUP:
            if (event.button==1):
                scrollable_clickable_KINGbox.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONUP)
    if (scrollable_clickable_KINGbox.beingclicked):
        scrollable_clickable_KINGbox.dragscroll(pygame.mouse.get_pos()[1]-startmouseposition)
        startmouseposition=pygame.mouse.get_pos()[1]
    #-----------------------------------
    #blitting boxes
    screen.fill(0)
    pygame.draw.rect(screen,212*65536+91*256+208,ir)
    jobinformation.display()
    scrollable_clickable_KINGbox.displaybuttons()
    #-----------------------------------
    #






















    #sent
    pygame.display.flip()
    clock.tick(60)
    #-----------------------------------
pygame.quit()