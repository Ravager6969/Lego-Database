import sys
#version 2 - released on github, uploaded by kinggolem (though it probably will not get any attention because of whack a king)
#i just bid $69,420,069 on whack a king from my earnings from this program. donate to me on github kinggolem and support hard coded games
#################################        skip the triple quotes if you just want to see the data         ###############3######33##333##333#33##33######3############33####
'''
------------------------------------------------------------
How Skill Points are Determined
------------------------------------------------------------
Skill Points from Gear and Residences:
(W=wood, S=stone, G=gold, I=iron, D=diamond, E=enchanted)

Mining Skill Points:
Tier            W   S   G   I   D   E
Pickaxe         1   -   -   4   5   6
Axe or Shovel   2   -   -   3   -   -

Combat Skill Damage Points:
Tier            W   S   G   I   D   E
Sword           2   3   4   5   6   -
Bow             3   -   -   -   -   6
Axe             1   -   -   3   -   -

Combat Skill Tanking Points:
Tier            W   S   G   I   D   E
Helmet          -   -   0   1   2   -
Chestplate      -   -   1   2   2   -
Leggings/Boots  -   -   1   1   2   -
Full Set        -   -   2   4   6   -

If a character is unable to hold items or wear
armor, they will have preset values for Mining
and Combat skill points.

Residence List and Skill Points from Residences:
Central Village ------- (No skill bonus)
Jungle Tree House ----- (+6 Crafting)
Trading Village ------- (+6 Crafting)
Desert Outpost -------- (+5 Crafting)
Fortress -------------- (+5 Crafting)
Ice Spikes ------------ (+4 Crafting)
Waterfall Base -------- (+4 Crafting)
End Portal Room ------- (+3 Crafting)
Mine ------------------ (+2 Crafting)
The End --------------- (+1 Crafting)

If a character has no arms, they will be
unable to craft and have 0 Crafting points.
------------------------------------------------------------
Club List and Skill Points from Clubs:
Mining Club ----------- (5 members) (+2 Mining)
Warriors Club --------- (6 members) (+2 Combat)
Village Service Club -- (6 members) (+2 Crafting)
Goon Squad ------------ (6 members) (+1 Mining, +1 Crafting)
Mayor's Council ------- (3 members) (+1 of every skill)
Skeleton Club --------- (7 members) (+1 Crafting, +1 Combat)
Villains Club --------- (6 members) (+1 Combat, +1 Mining)

Some people may be a member in more than one Club.
For those in more than one Club, they will gain
skill points from all clubs they are in but they
will be capped at +2 points for each skill.
------------------------------------------------------------
Skill Points from Occupations:
If someone has an occupation, it will give them
+2 points in the skill most related to their.
occupation. If no skill applies, they will just
receive +2 points for Crafting.

Any bonus skill points obtained here will only
be usable when a character is doing their job.
If they are not, they will temporarily lose
the skill points from occupations.
------------------------------------------------------------
Note: Bonuses from Combat skill increase both Damage
and Tanking equally unless otherwise stated.

Max +6 from Gear or Residence
Max +2 from Club
Max +2 from Occupation
The total points available for each skill is 10.
------------------------------------------------------------
Format of the values below:
Keys        "Character Model_Player ID"
Values      (Occupation, Residence, Club, Skills)
Skills      (Mining, Damage, Tanking, Crafting)
------------------------------------------------------------
did you really read all this or just skip to the bottom?
'''
#all characters
kinggolem={
    "Blue Hero_1":(
        "Raid Defender",
        "Jungle Tree House",
        "Warriors Club (Leader)",
        (0,10,4,6)
        ),
    "Steve_2":(
        "Woodcutter",
        "Jungle Tree House",
        "Mining Club",
        (6,0,0,6)
        ),
    "Steve_3":(
        "Animal Salesman and Caretaker",
        "Jungle Tree House",
        "None",
        (0,0,0,8)
        ),
    "Skeleton_4":(
        "None",
        "Desert Outpost",
        "Skeleton Club",
        (0,4,1,6)
        ),
    "Skeleton_5":(
        "None",
        "Desert Outpost",
        "Skeleton Club",
        (0,1,1,6)
        ),
    "Skeleton_6":(
        "None",
        "Desert Outpost",
        "Skeleton Club",
        (0,4,2,6)
        ),
    "Skeleton_7":(
        "None",
        "Desert Outpost",
        "Skeleton Club",
        (0,4,2,6)
        ),
    "Blaze_8":(
        "Nether Portal Guard",
        "Mine",
        "None",
        (0,5,3,0)
        ),
    "Steve_9":(
        "None",
        "Central Village",
        "Goon Squad (Leader) and Mining Club",
        (6,0,0,1)
        ),
    "Zombie_10":(
        "Mine Guard",
        "Mine",
        "None",
        (0,7,4,2)
        ),
    "Zombie_11":(
        "None",
        "Central Village",
        "Goon Squad",
        (1,0,0,1)
        ),
    "Steve_12":(
        "Blacksmith",
        "Central Village",
        "Mining Club",
        (9,0,2,0)
        ),
    "Steve_13":(
        "World Gatekeeper",
        "Central Village",
        "Village Service Club",
        (2,0,0,4)
        ),
    "Alex_14":(
        "Night Patroller",
        "Central Village",
        "Warriors Club",
        (0,8,6,0)
        ),
    "Steve_15":(
        "Mayor's Assistant",
        "Jungle Tree House",
        "Mayor's Council and Warriors Club",
        (1,6,6,9)
        ),
    "Alex_16":(
        "Healer and Fish Supplier",
        "Ice Spikes",
        "Village Service Club",
        (0,0,0,8)
        ),
    "Alex_17":(
        "Shipping Company",
        "Trading Village",
        "Village Service Club",
        (0,0,0,4)
        ),
    "Creeper_18":(
        "None",
        "Central Village",
        "Goon Squad",
        (4,3,0,1)
        ),
    "Steve_19":(
        "Building Master and World Editor",
        "Ice Spikes",
        "Mining Club (Leader)",
        (10,0,2,4)
        ),
    "Steve_20":(
        "Mayor",
        "Jungle Tree House",
        "Mayor's Council (Leader)",
        (1,7,7,9)
        ),
    "Enderman_21":(
        "None",
        "The End",
        "Villains Club",
        (1,6,6,1)
        ),
    "Enderman_22":(
        "None",
        "The End",
        "Villains Club",
        (1,6,6,1)
        ),
    "Spider_23":(
        "End Portal Guard",
        "End Portal Room",
        "None",
        (0,6,7,0)
        ),
    "Skeleton_24":(
        "None",
        "Waterfall Base",
        "Skeleton Club (Leader)",
        (0,4,4,5)
        ),
    "Skeleton_25":(
        "None",
        "Waterfall Base",
        "Skeleton Club",
        (0,4,3,5)
        ),
    "Skeleton_26":(
        "None",
        "Waterfall Base",
        "Skeleton Club",
        (0,4,2,5)
        ),
    "Steve_27":(
        "Bank Master",
        "Fortress",
        "None",
        (0,4,2,7)
        ),
    "Wither Skeleton_28":(
        "Potion Brewer",
        "Fortress",
        "Warriors Club",
        (0,8,6,7)
        ),
    "Zombie_29":(
        "Prison Guard",
        "Fortress",
        "Warriors Club",
        (0,9,8,5)
        ),
    "Steve_30":(
        "Night Patroller",
        "Fortress",
        "Mayor's Council",
        (1,8,7,6)
        ),
    "Alex_31":(
        "Night Patroller",
        "Central Village",
        "None",
        (0,5,4,0)
        ),
    "Steve_32":(
        "Shipping Company",
        "Trading Village",
        "Village Service Club (Leader) and Mining Club",
        (7,0,0,10)
        ),
    "Creeper_33":(
        "None",
        "Central Village",
        "Goon Squad",
        (4,3,0,1)
        ),
    "Zombie_34":(
        "None",
        "Central Village",
        "Goon Squad",
        (1,3,0,1)
        ),
    "Zombie_35":(
        "None",
        "Central Village",
        "Goon Squad",
        (3,0,0,1)
        ),
    "Enderman_36":(
        "None",
        "The End",
        "Villains Club",
        (1,6,6,1)
        ),
    "Enderman_37":(
        "None",
        "The End",
        "Villains Club",
        (1,6,6,1)
        ),
    "Villager_38":(
        "Farming Master",
        "Trading Village",
        "Village Service Club",
        (0,0,0,10)
        ),
    "Villager_39":(
        "Trading Master",
        "Trading Village",
        "Village Service Club",
        (0,0,0,10)
        ),
    "Red Hero_40":(
        "Raid Defender",
        "Fortress",
        "Warriors Club",
        (0,10,4,5)
        ),
    "Pillager_41":(
        "None",
        "Waterfall Base",
        "Villains Club",
        (1,4,3,4)
        ),
    "Pillager_42":(
        "None",
        "Waterfall Base",
        "Villains Club (Leader)",
        (1,4,3,4)
        ),
}
golemwolf={}#jobs
wolfking={}#clubs
bullravager={}#residences

clubskills={
    "Mayor's Council":("The highest ranked club in the entire village. All members work to help the mayor run the village. Admission to the club is only by invite from the mayor himself. Previous club membership is strongly recommended for admission.","Skill Bonus for members: +1 of every skill"),
    "Mining Club":("This club gathers resources, mainly ores for the village. Higher-ranked members in this club also repair and maintain residences. Currently recruiting all hard-working miners, regardless of gear.","Skill Bonus for members: +2 Mining"),
    "Warriors Club":("The most competitive club in the village. Members work together to defend the village from any threats or a wild, misbehaving Golem. New recruits must fight low-ranked members in weekly events to secure a spot in the club.","Skill Bonus for members: +2 Combat"),
    "Village Service Club":("This club is in charge of all services in the village like running the Shipping Company, managing resources, and administrating events. Those wanting to join must already run a service in the village themselves.","Skill Bonus for members: +2 Crafting"),
    "Goon Squad":("Camping by the Desert Outpost, this club is perfect for new characters beginning their Minecraft journey. The only requirements to join this club are a greedy mind and a Combat skill of 2 or lower.","Skill Bonus for members: +1 Mining, +1 Crafting"),
    "Skeleton Club":("The quietest club in the village. Members of this club gather resources together as a club, independent of the rest of the village. Only skeletons are admitted to this club as long as they agree not to leave home more than once per year.","Skill Bonus for members: +1 Crafting, +1 Combat"),
    "Villains Club":("This club spends most of their time upgrading weapons and preparing their forces. Occasionally, they launch massive attacks, capable of wiping out the entire village. To apply, one must have at least 69 Golem kills and the ability to tame a Ravager.","Skill Bonus for members: +1 Combat, +1 Mining"),
}

for x in kinggolem.keys():
    if (kinggolem[x][0]!="None"):
        if (kinggolem[x][0] in golemwolf):
            golemwolf[kinggolem[x][0]].append(x)
        else:
            golemwolf[kinggolem[x][0]]=[x]
    
    if (kinggolem[x][1]!="None"):#hopefully no one is homeless
        if (kinggolem[x][1] in bullravager):
            bullravager[kinggolem[x][1]].append(x)
        else:
            bullravager[kinggolem[x][1]]=[x]

    if (kinggolem[x][2]!="None"):
        clubstring=kinggolem[x][2].split(" and ")#amazing hard coding skills right here
        for y in range(len(clubstring)):
            clubmember=str(x)
            if (" (Leader)" in clubstring[y]):
                clubstring[y]=clubstring[y][:-9]
                clubmember+=" (Leader)"#mess up the format and this program dies

            if (clubstring[y] in wolfking):
                wolfking[clubstring[y]].append(clubmember)
            else:
                wolfking[clubstring[y]]=[clubmember]

for x in wolfking.keys():
    if (x in clubskills):
        for playplaykinggolemwolf in range(1,-1,-1):
            wolfking[x].insert(0,clubskills[x][playplaykinggolemwolf])

if __name__=="__main__":
    GOLEM=[]#quality variable names
    for x in kinggolem.keys():
        GOLEM.append([
            x,
            float(kinggolem[x][3][0]),
            float((kinggolem[x][3][1]+kinggolem[x][3][2])/2),
            float(kinggolem[x][3][3]),
            ])
        GOLEM[-1].append(max(GOLEM[-1][1:]))
        GOLEM[-1].append(sum(GOLEM[-1][1:4]))
    if (len(sys.argv)>1):
        if (sys.argv[1]=="mining"):
            GOLEM.sort(key=lambda BULL: BULL[1],reverse=True)
        elif (sys.argv[1]=="combat"):
            GOLEM.sort(key=lambda BULL: BULL[2],reverse=True)
        elif (sys.argv[1]=="crafting"):
            GOLEM.sort(key=lambda BULL: BULL[3],reverse=True)
        elif (sys.argv[1]=="best"):
            GOLEM.sort(key=lambda BULL: BULL[4],reverse=True)
    else:
        GOLEM.sort(key=lambda BULL: BULL[5],reverse=True)
    print ("Name_ID             Mining   Combat   Crafting Best     Total")#yes very much hard coded
    for x in range(len(GOLEM)):
        print (GOLEM[x][0]+" "*(20-len(GOLEM[x][0])),end="")
        for y in range(1,len(GOLEM[x])):
            print (str(GOLEM[x][y])+" "*(9-len(str(GOLEM[x][y]))),end="")
        print ("")
    
    for menupage in (golemwolf,wolfking,bullravager):
        print ("\n")
        for key1 in menupage:
            print (str(key1)+":",end="")
            for DRAGONPIGMANBULLGOLEMKINGWOLFRAVAGER in range(len(menupage[key1])):
                if (menupage==wolfking):
                    if (DRAGONPIGMANBULLGOLEMKINGWOLFRAVAGER==0):
                        print (" ",end="")
                    print (str(menupage[key1][DRAGONPIGMANBULLGOLEMKINGWOLFRAVAGER]))
                else:
                    if (DRAGONPIGMANBULLGOLEMKINGWOLFRAVAGER!=0):
                        print (",",end="")
                    print (" "+str(menupage[key1][DRAGONPIGMANBULLGOLEMKINGWOLFRAVAGER]),end="")
            print ("")













































#import mohammed_social_security.exe
#mohammed_social_security.free_generate_dot_ru()
#pygame.display.flip()