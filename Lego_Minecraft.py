#variables and initializing
from init import *


#main loop
while True:

    #screen and backround
    screen.fill((0,0,0))

    screen.blit(backround,(0,0))
    
    #display character information
    if characters and main_menu != True:
        test = id(characterchoice, kinggolem[characterchoice][0], kinggolem[characterchoice][1], kinggolem[characterchoice][2])
        test.create_id()

    else:
        characters = False


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
  

    
   

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_e:
                pygame.quit()
            if event.key == K_w: 
                pygame.mixer.music.stop()
            if event.key == K_f:
                if fullscreen == True:
                    
                    screen = pygame.display.set_mode(size)
                    width = screen.get_width()
                    height = screen.get_height()
                    fullscreen = False
                    music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-100), font)
                else:

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
          
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==4:
                patchnotes_display.scroll("up",pygame.mouse.get_pos())
                
            elif event.button==5:
                patchnotes_display.scroll("down",pygame.mouse.get_pos())

    

    #volume control
    if volumeup and volume <= 1:
        volume += 0.01
        pygame.mixer.music.set_volume(volume)
     
    if volumedown and volume >= 0.01:
        volume -= 0.01
        pygame.mixer.music.set_volume(volume)
    if volumeup or volumedown:
        volume_display = golem(str("%.1f" % volume), (random_color), (width-100,height-100), font)
        volume_display.KING()


   
    #title
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


   
   
    #main buttons
    if main_menu == True:
        for i in range(0, 4): 
            if i == 0:
                largebuttons = 'Gallary'
            elif i == 1:
                largebuttons = 'Characters'
            elif i == 2:
                largebuttons = 'Clubs'
            else:
                largebuttons = 'Jobs'

            large_button_width = (width/5 + i*(width/5))-150
           

            b = button(largebuttons, (large_button_width, height/2), (142,155,229), font, (200,100))
            b.createbutton()

        
            click_l = clicked(large_button_width, large_button_width+200, height/2, height/2+100)
            

            if click_l and click_value: 
               
                click_value = False
                if i == 0:
                    print('gallary')
                    
                    gallary = True
                    main_menu = False
                if i == 1:
                    print('characters')
                    
                    main_menu = False
                   
                    characters_choice = True
                if i == 2:
                    print('clubs')
                    main_menu = False
                if i == 3:
                    print('jobs')
                    main_menu = False


        
            elif click_l and click_value == False:
                click_value = False
            else:
                click_value = True
            
        #other buttons
        for i in range(0, 3):
            if i == 0:
                smallbuttons = 'Music'
  
            elif i == 1:
                smallbuttons = 'Quit'
   
            else:
                smallbuttons = 'Options' 
 


            small_button_width = (width/3 + i*(width/5))-200

            b = button(smallbuttons, (small_button_width, height-200), (152,5,152), font, (150,75)) 
            b.createbutton()


            
            click_s = clicked(small_button_width, small_button_width+150, height-200, height-125)
           

            if click_s and click_value:
                
                click_value = False
                if i == 0:
                    print('music')
                    music = True
                    main_menu = False
                if i == 1:
                    print('quit')
                    pygame.quit()
                   
                    main_menu = False
                if i == 2:
                    print('options')
                    options = True
                    main_menu = False
               
            
            elif click_s and click_value == False:
                click_value = False
            else:
                click_value = True
                options = False
  
    #character choice
    if main_menu == False and characters_choice == True:
        character_return = display_characters(character_page, click_value)
       
        
        if character_return == None:
            pass

        elif character_return[0] == False:
            characters_choice = False
            characterchoice = character_return[1]
            characters = True
        
    
        if character_page < 3:
            next_page = button('Next', (width-250, height-150), sky_blue, font, (200,100))
            next_page.createbutton()
            

        if character_page != 1:
            last_page = button('Back', (50, height-150), sky_blue, font, (200,100))
            last_page.createbutton()
       

        click_c = clicked(width-250, width-50, height-150, height-50)
        click_d = clicked(50, 250, height-150, height-50)

        

        
        if (click_c or click_d) and click_value and click_frame:
            click_frame = False
            click_value = False
           
            if character_page < 3 and click_c:
                character_page += 1
            elif character_page > 1 and click_d:
                character_page -= 1
        elif (click_c or click_d) and click_value == True and click_frame == False:
            click_frame = False
            click_value = False
        
        else:
            click_frame = True
            click_value = True


    else:
        characters_choice = False

    #character display
    if main_menu == False and characters == False:

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

    #back button from character display
    if main_menu == False and characters == True:

        back_button = button('Back to', (width-(width-260), height-(height-50)), (0,207,255), font, (200,100))
        back_button.createbutton()
        click_b = clicked(width-(width-260), width-(width-460), height-(height-50), height-(height-150))

        if click_b and click_value:
  
            characters_choice = True
            click_value = False
            characters = False
                
        elif click_b and click_value == False:

            click_value = False

        else:

            click_value = True
    else:
        characters = False


    #stop slideshow
    if pygame.mouse.get_pressed()[0]:
            stop_slideshow = True
    

    #gallary and slideshow
    if main_menu == False and gallary == True:
        gallary_button = button('Slideshow', (width-300, height-(height-200)), sky_blue, font, (200,100))
        gallary_button.createbutton()

        click_g = clicked(width-300, width-100, height-(height-200), height-(height-300))

        if click_g and click_value:
            slideshow = True
            stop_slideshow = False
            click_value = False
                
        elif click_g and click_value == False:

            click_value = False

        else:

            click_value = True

    else:
        gallary = False


    #slideshow    
    if slideshow and stop_slideshow == False:
        

     
        iamatarabullprogrammer=github(timer_69,random_image,timer_max)
        timer_69=iamatarabullprogrammer[0]
        random_image=iamatarabullprogrammer[1]


    #music
    if music and main_menu == False:
        music_box = button('', (50, height/2-250), (255,102,102), font, (400,600))#text pos color font size
        music_box.createbutton()
        music_box_title = golem('Songs', (0,0,0), (250, height/2-210), font)
        music_box_title.KING()

    else:
        music = False




    #options
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

           
           
          
            
            if click_soc and click_value: 

                click_value = False
                if x == 1:
                    print('about')
                    options = False
                    about = True
               
                elif x == 2:
                    print('controls')
                    options = False
                    controls = True
               
                elif x == 3:
                    opengithub()
                    
                

                        
               
    
            elif click_soc and click_value == False:
                click_value = False

            else:
                click_value = True
          

  
    #patch notes
    if main_menu and screen.get_width() == 1920:
        patchnotes_display.display()
   
    

    

  
    
    #static updates text
    if main_menu:
        patchnotes_static_text = button('Updates', (width-(width-50),height-350), sky_blue, font2, (350,25))
        patchnotes_static_text.createbutton()





    clock.tick(144)

    












    
    pygame.display.flip()
