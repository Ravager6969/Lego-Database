#variables and initializing
from init import *
#for x in golemwolf.keys():
     #print(x)
#for x in wolfking.keys():
    #print(x)
#print(golemwolf, wolfking)
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
#add repeat button

    #music
    if other_music == False:
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
    else:
        if pygame.mixer.music.get_busy() == 0 and repeat == False:
            other_music = False
        
    

    
   
    
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
                    music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
                else:

                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    width = screen.get_width()
                    height = screen.get_height()
                    fullscreen = True
                    music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
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

            if event.button == 1:
                if music:

                    
                    if pygame.mouse.get_pos()[0] > width-1010 and pygame.mouse.get_pos()[0] < width-940 and pygame.mouse.get_pos()[1] > height-80 and pygame.mouse.get_pos()[1] < height:
                        print('golem')
                        pygame.mixer.music.load(random.choice(["Sounds/Music/TOP_SECRET/playplaykinggolemwolf.mp3", "Sounds/Music/TOP_SECRET/kingkingking.mp3", "Sounds/Music/TOP_SECRET/LGBTIIIIIIIIIIIIIIIIIIIII.mp3"])) #yes here it finally is
                        pygame.mixer.music.play()




                    elif music_box.clickbuttons(pygame.mouse.get_pos()) == -69 and playlist_box_display.clickbuttons(pygame.mouse.get_pos()) == -69:
                        pass
                    
                    elif playlist_box_display.clickbuttons(pygame.mouse.get_pos()) >= 0:
                        other_music = True
                        music_text_3 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
                        music_text_4 = golem(playlist[playlist_keys[playlist_choice]][playlist_box_display.clickbuttons(pygame.mouse.get_pos())], cyan, (width/2+150,height-50), font)    
                        other_music_load = 'Sounds\\Music\\' +  playlist[playlist_keys[playlist_choice]][playlist_box_display.clickbuttons(pygame.mouse.get_pos())] + '.mp3'
                        pygame.mixer.music.load(other_music_load)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.play()
                        music_message_timer = 0
                    

                   

                    else:
                        other_music = True
                    #elif other_music:
                        
                        music_text_3 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
                        music_text_4 = golem(music_list[music_box.clickbuttons(pygame.mouse.get_pos())], cyan, (width/2+150,height-50), font)    
                        other_music_load = 'Sounds\\Music\\' + music_list[music_box.clickbuttons(pygame.mouse.get_pos())] + '.mp3'
                        pygame.mixer.music.load(other_music_load)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.play()
                        music_message_timer = 0

                    
                elif manage_playlist:
                    if playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos()) >= 0:
                        playlist_manage_choice = playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos())
                        
                        '''
                        if playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos()) == playlist_manage_choice:
                            playlist_manage_choice = ''
                        else:
                            playlist_manage_choice = playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos())
                        '''

            
            elif event.button==4:
                patchnotes_display.scroll("up",pygame.mouse.get_pos())
                music_box.scrollbox("up",pygame.mouse.get_pos())
                playlist_box_display.scrollbox("up", pygame.mouse.get_pos())
                playlist_manage_box_display.scrollbox("up", pygame.mouse.get_pos())
                playlist_manage_box_display_options.scrollbox("up", pygame.mouse.get_pos())
            elif event.button==5:
                patchnotes_display.scroll("down",pygame.mouse.get_pos())
                music_box.scrollbox("down",pygame.mouse.get_pos())
                playlist_box_display.scrollbox("down", pygame.mouse.get_pos())
                playlist_manage_box_display.scrollbox("down", pygame.mouse.get_pos())
                playlist_manage_box_display_options.scrollbox("down", pygame.mouse.get_pos())

    if pygame.mixer.music.get_busy() == 0 and repeat:  
        pygame.mixer.music.load(other_music_load)
        pygame.mixer.music.play()
        music_message_timer = 0 
        test_count += 1

  
    #volume control
    if volumeup and volume <= 1:
        volume += 0.01
        pygame.mixer.music.set_volume(volume)
     
    if volumedown and volume >= 0.01:
        volume -= 0.01
        pygame.mixer.music.set_volume(volume)
    if volumeup or volumedown:
        volume_display = golem(str("%.1f" % volume), (random_color), (width-100,height-250), font)
        volume_display.KING()
   

    if other_music:
        if music_message_timer >= 1:
            pass
            
            
        elif music_message_timer < 1:
            music_text_3.KING()
            music_text_4.KING()
            music_message_timer += 0.01
    
        
    
    
    #title
    text = KINGOUTLINE(screen, 'Lego Minecraft Database', (width/2, height-(height-100)), font, red)
    
    #moon and sun
    if night:
        screen.blit(moon, (width-125, height-(height-50)))#sun and moon 200x200

    if day:
        screen.blit(sun, (width-125, height-(height-50)))#sun and moon 200x200
    

    #time
    current_time = datetime.datetime.now()
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
                    club_choice = True
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
    if main_menu == False and characters == False and manage_playlist == False:

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
    
    #clubs
    
    if club_choice and main_menu == False:
        for x in range(3):
            
            if not x == 2:
                club_number = 3
            else:
                club_number = 1
            for i in range(club_number):
                if not x == 2:
                    club_display_width = width/6 + i*width/4
                    club_display_height = height/4 + x*height/2
                    club_display_color = sky_blue
                else:
                    club_display_width = width/2-160
                    club_display_height = height/2
                    club_display_color = gold
                club_display = button(list_clubs[i+(3*x-1)], (club_display_width, club_display_height), club_display_color, font, (300,100))
                club_display.createbutton()
    else:
        club_choice = False

    #clubs = True
    clubs = False
    #main_menu = False
    if clubs: #and main_menu != True:

        clubchoice = 'king'
        clubs_display = club_display(clubchoice, 3)
        clubs_display.create_club_display()

    else:
        clubs = False
        




    

    #music
    if music and main_menu == False:

        playlist_name = button(str(playlist_keys[playlist_choice]), (width-500, 180), (0,0,102), font, (400,70), cyan)

        playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), playlist[playlist_keys[playlist_choice]], [400,100], font, 102)

        #playlists and repeats

        playlist_name.createbutton()       

        playlist_box_display.displaybuttons() 
       
        repeat_button_1.createbutton()
        repeat_button_2.createbutton()
        repeat_title.KING()
        if pygame.mixer.music.get_busy() == 1:
            clicked_r = clicked(width-150, width-50, height-150, height-50)
            if repeat_thing:
                if clicked_r and repeat == False:
                    repeat = True
                elif clicked_r and repeat == True:
                    repeat = False
            
            if repeat and pygame.mouse.get_pressed()[0] == 1:
                repeat_thing = False
            elif repeat == False and pygame.mouse.get_pressed()[0] == 1:
                repeat_thing = False
            else:
                repeat_thing = True
        if repeat:
            screen.blit(checkmark, (width-125, height-125))

        music_box.displaybuttons()
        music_box_title.createbutton()

        screen.blit(toad, (width/2-int(607/3), height/2-int(718/3)))
        screen.blit(treble, (50, 190))
        screen.blit(bass, (400,190))

        #next and back buttons
        
        if playlist_choice < 2:
            next_page = button('Next', (width-290, height-200), sky_blue, font, (100,50))
            next_page.createbutton()
            
        

        if  playlist_choice != 0:
            last_page = button('Back', (width-490, height-200), sky_blue, font, (100,50))
            last_page.createbutton()
       

        click_c = clicked(width-290, width-190, height-200, height-150)
        click_d = clicked(width-490, width-390, height-200, height-150)

    
        if (click_c or click_d) and click_value and click_frame:
            click_frame = False
            click_value = False
           
            if playlist_choice < 2 and click_c:
                playlist_choice += 1
            elif playlist_choice > 0 and click_d:
                playlist_choice -= 1

        elif (click_c or click_d) and click_value == True and click_frame == False:
            click_frame = False
            click_value = False
        
        else:
            click_frame = True
            click_value = True

        manage_playlist_button = button('Manage Playlists', (width-550, height-100), (0,0,102), font, (350,50), cyan)
        manage_playlist_button.createbutton()

        clicked_p = clicked(width-550, width-200, height-100, height-50)

        if clicked_p:
            manage_playlist = True
            music = False

    else:
        music = False

    if manage_playlist and main_menu == False:

        back_button = button('Back to', (width-(width-260), height-(height-50)), (0,207,255), font, (200,100))
        back_button.createbutton()
        click_b = clicked(width-(width-260), width-(width-460), height-(height-50), height-(height-150))

        if click_b:
            manage_playlist = False
            music = True

    
        
        playlist_manage_title.KING()
        playlist_manage_box_display.displaybuttons()


        try:
            print(playlist_manage_choice)
            playlist_manage_box_display_options.displaybuttons()
            
            playlist_manage_box_display_options_title.KING()
            playlist_manage_box_display_options_delete.createbutton()
            playlist_manage_box_display_options_create_new.createbutton()

        except NameError:
            pass


    

        
    else:
        manage_playlist = False
    

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
   
    

    if about and main_menu == False:
        #credids make a loop that blits a large height box with credits more and more upwards like in the movies or video games
        #information box on one of the corners
        #information includes how long it toke when it aobut started and finished and how long toke stuff like that king
        for x in range(3):
            about_information = button(information[x], (width-350, height-(x*100+150)), sky_blue, font2, (300,100), gold)
            about_information.createbutton_color()

        ravager_credits_display = button('Credits', (width-350, height-500), cyan, font, (300,100), red)
        ravager_credits_display.createbutton_color()

        clicked_c = clicked(width-350, width-50, height-500, height-400)

        if clicked_c and click_value:

            display_credits = True
                
            
        
        elif click_c and click_value == False:
            click_value = False

        else:
            click_value = True
        
    else:
        about = False

    if display_credits:
  
        if pygame.mouse.get_pressed()[0] == False:
            about = False

        if about == False:
            for x in range(1000):
                credits_height = x
                credits_height_2 = x+height
                credits_display = button('king', (0,credits_height), sky_blue, font, (width,height))
                credits_display.createbutton()
                credits_display = button('king', (0, credits_height_2), gold, font, (width, height))
                credits_display.createbutton()
                if pygame.mouse.get_pressed()[0]:
                    about = True
                    display_credits = False
        '''
        print(credits_click)
        
        about = False
        
        if pygame.mouse.get_pressed()[0] == False:
            credits_click = True
            display_credits = False
            about = True   
        if pygame.mouse.get_pressed()[0] and credits_click == True:
            about = True
            display_credits = False
        '''
    #static updates text
    if main_menu:
        patchnotes_static_text = button('Updates', (width-(width-50),height-350), sky_blue, font2, (350,25))
        patchnotes_static_text.createbutton()


    title = get_title(gallary, characters_choice, characters, club_choice, options, music, characterchoice)

    title_display = golem(title, (3, 254, 155), (width/2, 180), font)

    title_display.KING()

    clock.tick(144)

    
    pygame.display.flip()
