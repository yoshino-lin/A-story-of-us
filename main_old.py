#image purchased from unity store and internet
import os
import time
from sys import exit

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 640), 0, 32)
pygame.display.set_caption("A Story Of Us")

'''

'''
#talking
#first part
my_font = pygame.font.SysFont("other/font.ttf", 42)
my_font_2 = pygame.font.SysFont("other/font.ttf", 26)
text_surface0 = my_font.render("", True, (0,0,0))
text_surface1 = my_font.render("This is our world...the place we live...", True, (255,255,255))
text_surface2 = my_font.render("A world, which hates witches, and its magic.", True, (255,255,255))
text_surface3 = my_font.render("The king killed nearly all witches.", True, (255,255,255))
text_surface4 = my_font.render("Fortunately, as two little witches, we are still alive.", True, (255,255,255))
text_surface5 = my_font.render("We live in deep in the forest, and hope that no one", True, (255,255,255))
text_surface5_1 = my_font.render("will find us.", True, (255,255,255))
text_surface6 = my_font.render("Until one day...and this is the beginning of our story", True, (255,255,255))
#second part
text_surface7 = my_font.render('Maria: "Lucy, are you ready to go out? We have a', True, (255,255,255))
text_surface7_1 = my_font.render("lot of work to do today!", True, (255,255,255))
text_surface8 = my_font.render("My name is Maria, and, as you see, I am a witch.", True, (255,255,255))
text_surface9 = my_font.render('Lucy: "Yeah! Give me one moment."', True, (255,255,255))
text_surface10 = my_font.render("This is my little sister, Lucy. She is a witch, too.", True, (255,255,255))
text_surface10_1 = my_font.render("However, she is very naughty and always brings", True, (255,255,255))
text_surface10_2 = my_font.render("me a lot of troubles", True, (255,255,255))
text_surface11 = my_font.render('Lucy: "Wait a second, you cannot say that!"', True, (255,255,255))
text_surface12 = my_font.render('Maria: "What? I never say any words!"', True, (255,255,255))
text_surface13 = my_font.render("We always argue with each other, but still, we love", True, (255,255,255))
text_surface13_1 = my_font.render("each other very much.", True, (255,255,255))
text_surface14 = my_font.render("In addition, today we need to go out to find some", True, (255,255,255))
text_surface14_1 = my_font.render("food.", True, (255,255,255))
text_surface15 = my_font.render("It has already rained heavily for many days, and we", True, (255,255,255))
text_surface15_1 = my_font.render("are running out of food.", True, (255,255,255))
text_surface16 = my_font.render("Nevertheless, today is a sunny day, and it is nice", True, (255,255,255))
text_surface16_1 = my_font.render("to go out to have some fun.", True, (255,255,255))
#third part
text_surface17 = my_font.render('Lucy: "I miss the sun light so much!"', True, (255,255,255))
text_surface18 = my_font.render('Maria: "Me too! But do not forget our mission.', True, (255,255,255))
text_surface18_1 = my_font.render('We need to find some food."', True, (255,255,255))
text_surface19 = my_font.render('Lucy: " Ok.. I see."', True, (255,255,255))
text_surface20 = my_font.render("After rainy days, it is easy for us to find a lot of", True, (255,255,255))
text_surface20_1 = my_font.render("mushrooms in the forest. Most of them are filled with", True, (255,255,255))
text_surface20_2 = my_font.render("nutrition and energy. Besides, they are delicious.", True, (255,255,255))
text_surface21 = my_font.render("Suddenly, I hear some noise.", True, (255,255,255))
text_surface22 = my_font.render('Maria: "Do you hear something? What is that?"', True, (255,255,255))
text_surface23 = my_font.render('Lucy: "I also hear that. The sound from the horses!"', True, (255,255,255))
text_surface24 = my_font.render('Maria: "Hide yourself! Right now!"', True, (255,255,255))
text_surface25 = my_font.render("We hide ourselves into the bushes nearby.", True, (255,255,255))
text_surface26 = my_font.render("We see some knights coming by riding their houses.", True, (255,255,255))
text_surface26_1 = my_font.render("Then they stop.", True, (255,255,255))
text_surface27 = my_font.render('Lucy: "Are they looking for us?"', True, (255,255,255))
text_surface28 = my_font.render('Maria: "It looks like not. Let us be careful and see."', True, (255,255,255))
text_surface29 = my_font.render('Knight: "Learn up, we must find him! He must', True, (255,255,255))
text_surface29_1 = my_font.render('be somewhere nearby!"', True, (255,255,255))
text_surface30 = my_font.render('Other knights: "Yes, sir!"', True, (255,255,255))
text_surface31 = my_font.render("Then they spread out.", True, (255,255,255))
text_surface32 = my_font.render('Maria: "We have to leave now and go home,', True, (255,255,255))
text_surface32_1 = my_font.render('otherwise they will find us."', True, (255,255,255))
text_surface33 = my_font.render('Lucy: "Ok...what a pity."', True, (255,255,255))
text_surface34 = my_font.render("Then we leave without any sound.", True, (255,255,255))
text_surface35 = my_font.render("To be continue...", True, (255,255,255))
text_surface36 = my_font.render("Thanks for playing the demo!", True, (255,255,255))
text_surface36_1 = my_font.render("Please click to go back the main menu.", True, (255,255,255))

text_surface_i1 = my_font_2.render("Thanks for playing this game!", True, (255,255,255))
text_surface_i2 = my_font_2.render("Any bug reports please email:", True, (255,255,255))
text_surface_i3 = my_font_2.render("yoshino1347716570@gmail.com", True, (255,255,255))
text_surface_i4 = my_font_2.render("No commercial use!", True, (255,255,255))
text_surface_i5 = my_font_2.render("Version:[0.1]", True, (255,255,255))
text_surface_i6 = my_font_2.render("This version is used as a demo.", True, (255,255,255))
text_surface_i7 = my_font_2.render("It doesn't represent the final effect.", True, (255,255,255))

#https://textcraft.net/
bg0 = pygame.image.load('Assets/image/UI/bg0.png').convert_alpha()
bg1 = pygame.image.load('Assets\image\dialog_background/bg1.png').convert_alpha()
bg2 = pygame.image.load('Assets\image\dialog_background/bg2.png').convert_alpha()
bg3 = pygame.image.load('Assets\image\dialog_background/bg3.png').convert_alpha()
char1 = pygame.image.load('img/char1.png').convert_alpha()
char2 = pygame.image.load('img/char2.png').convert_alpha()
char1_dark = pygame.image.load('img/char1_dark.png').convert_alpha()
char2_dark = pygame.image.load('img/char2_dark.png').convert_alpha()
talk_chart = pygame.image.load('img/talk_chart.png').convert_alpha()
important = pygame.image.load('img/important.png').convert_alpha()
quit_game = pygame.image.load('img/quit.png').convert_alpha()
notice = pygame.image.load('img/notice.png').convert_alpha()
initpintu = pygame.image.load('img/initpintu.png').convert_alpha()

#other setting
screen_num = 0
music_stop_num = 0
many_chart = 0
text_surface_m2 = text_surface0
text_surface_m3 = text_surface0

char_print1 = char1
char_print2 = char2_dark
show_notice = False


def mouse_p():
  global screen_num
  global show_notice
  pos = pygame.mouse.get_pos()
  mouse_x = pos[0]
  mouse_y = pos[1]
  if 705 <= mouse_x <= 740 and 5 <= mouse_y <= 40:
    show_notice = True
  if 750 <= mouse_x <= 784 and 5 <= mouse_y <= 40:
    exit()
  if show_notice == False:
    screen_num += 1
  if show_notice == True:
    if 327.5 <= mouse_x <= 472.5 and 400 <= mouse_y <= 440:
      show_notice = False

while True:
  text_surface_1 = text_surface_i1
  text_surface_2 = text_surface_i2
  text_surface_3 = text_surface_i3
  text_surface_4 = text_surface_i4
  text_surface_5 = text_surface_i5
  text_surface_6 = text_surface_i6
  text_surface_7 = text_surface_i7
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
    elif event.type == MOUSEBUTTONDOWN:
      pressed_array = pygame.mouse.get_pressed()        
      for index in range(len(pressed_array)):
        if pressed_array[index]:
          if index == 0:
            mouse_p()
  if screen_num == 0:
    background = bg0
    text_surface = text_surface0
  elif screen_num == 1:
    if music_stop_num != 2:
      music_stop_num += 1
    background = bg1
    text_surface = text_surface0
  elif screen_num == 2:
    text_surface = text_surface1
  elif screen_num == 3:
    text_surface = text_surface2
  elif screen_num == 4:
    text_surface = text_surface3
  elif screen_num == 5:
    text_surface = text_surface4
  elif screen_num == 6: 
    text_surface = text_surface5
    many_chart = 1
    text_surface_m2 = text_surface5_1
  elif screen_num == 7: 
    many_chart = 0
    text_surface = text_surface6
  elif screen_num == 8:#second screen
    if music_stop_num != 4:
      music_stop_num += 1
    background = bg2
    text_surface = text_surface0
  elif screen_num == 9:
    many_chart = 1
    text_surface = text_surface7
    text_surface_m2 = text_surface7_1
  elif screen_num == 10:
    many_chart = 0
    text_surface = text_surface8
    char_print1 = char1_dark
  elif screen_num == 11:
    char_print2 = char2
    text_surface = text_surface9
  elif screen_num == 12:
    many_chart = 2
    char_print2 = char2_dark
    text_surface = text_surface10
    text_surface_m2 = text_surface10_1
    text_surface_m3 = text_surface10_2
  elif screen_num == 13:
    many_chart = 0
    text_surface = text_surface11
    char_print2 = char2
  elif screen_num == 14:
    text_surface = text_surface12
    char_print2 = char2_dark
    char_print1 = char1
  elif screen_num == 15:
    many_chart = 1
    text_surface = text_surface13
    text_surface_m2 = text_surface13_1
    char_print1 = char1_dark
  elif screen_num == 16:
    text_surface = text_surface14
    text_surface_m2 = text_surface14_1
  elif screen_num == 17:
    text_surface = text_surface15
    text_surface_m2 = text_surface15_1
  elif screen_num == 18:
    text_surface = text_surface16
    text_surface_m2 = text_surface16_1
  elif screen_num == 19: #third screen
    many_chart = 0
    if music_stop_num != 6:
      music_stop_num += 1
    background = bg3
    text_surface = text_surface0
  elif screen_num == 20:
    text_surface = text_surface17
    char_print2 = char2
  elif screen_num == 21:
    many_chart = 1
    char_print1 = char1
    char_print2 = char2_dark
    text_surface = text_surface18
    text_surface_m2 = text_surface18_1
  elif screen_num == 22:
    many_chart = 0
    char_print1 = char1_dark
    char_print2 = char2
    text_surface = text_surface19
  elif screen_num == 23:
    many_chart = 2
    char_print2 = char2_dark
    text_surface = text_surface20
    text_surface_m2 = text_surface20_1
    text_surface_m3 = text_surface20_2
  elif screen_num == 24:
    many_chart = 0
    text_surface = text_surface21
  elif screen_num == 25:
    char_print1 = char1
    text_surface = text_surface22
  elif screen_num == 26: #change bgm
    char_print1 = char1_dark
    char_print2 = char2
    text_surface = text_surface23
    if music_stop_num != 8:
      music_stop_num += 1
  elif screen_num == 27:
    char_print1 = char1
    char_print2 = char2_dark
    text_surface = text_surface24
  elif screen_num == 28:
    char_print1 = char1_dark
    text_surface = text_surface25
  elif screen_num == 29:
    many_chart = 1
    text_surface = text_surface26
    text_surface_m2 = text_surface26_1
  elif screen_num == 30:
    many_chart = 0
    text_surface = text_surface27
    char_print2 = char2
  elif screen_num == 31:
    char_print1 = char1
    char_print2 = char2_dark
    text_surface = text_surface28
  elif screen_num == 32:
    many_chart = 1
    char_print1 = char1_dark
    text_surface = text_surface29
    text_surface_m2 = text_surface29_1
  elif screen_num == 33:
    many_chart = 0
    text_surface = text_surface30
  elif screen_num == 34:
    text_surface = text_surface31
  elif screen_num == 35: #music change back
    many_chart = 1
    char_print1 = char1
    text_surface = text_surface32
    text_surface_m2 = text_surface32_1
    if music_stop_num != 12:
      music_stop_num += 1
  elif screen_num == 36:
    many_chart = 0
    char_print1 = char1_dark
    char_print2 = char2
    text_surface = text_surface33
  elif screen_num == 37:
    char_print2 = char2_dark
    text_surface = text_surface34
  elif screen_num == 38:
    text_surface = text_surface35
  elif screen_num == 39:
    many_chart = 1
    text_surface = text_surface36
    text_surface_m2 = text_surface36_1
  elif screen_num == 40:
    many_chart = 0
    text_surface = text_surface0
    pygame.mixer.music.stop()
    music_stop_num = 0
    screen_num = 0
  while pygame.mixer.music.get_busy() != 1:
    if screen_num == 0:
      pygame.mixer.music.load('music/main_menu_bgm.ogg')
      pygame.mixer.music.play(loops=9999, start=0.0)
    elif screen_num == 1:
      pygame.mixer.music.load('music/bgm1.ogg')
      pygame.mixer.music.play(loops=9999, start=0.0)
    elif screen_num == 8:
      pygame.mixer.music.load('music/bgm2.ogg')
      pygame.mixer.music.play(loops=9999, start=0.0)
    elif screen_num == 19:
      pygame.mixer.music.load('music/bgm3.ogg')
      pygame.mixer.music.play(loops=9999, start=0.0)
    elif screen_num == 26:
      pygame.mixer.music.load('music/bgm4.ogg')
      pygame.mixer.music.play(loops=9999, start=0.0)
    elif screen_num == 35:
      pygame.mixer.music.load('music/bgm3.ogg')
      pygame.mixer.music.play(loops=9999, start=0.0)
  if music_stop_num == 1 or music_stop_num == 3 or music_stop_num == 5 or music_stop_num == 7 or music_stop_num == 9 or music_stop_num == -1:
    if pygame.mixer.music.get_busy() != 0:
      pygame.mixer.music.stop()
      music_stop_num += 1
  screen.blit(background,(0,0))
  if screen_num >= 9 and screen_num != 19:
    screen.blit(char_print1,(-85,144))
    screen.blit(char_print2,(450,145))
  if screen_num >= 2 and screen_num != 8 and screen_num != 19:
    screen.blit(talk_chart,(0,445))
  screen.blit(text_surface,(42,485))
  #button
  screen.blit(important,(705,5))
  screen.blit(quit_game,(750,5))
  if many_chart == 1:
    screen.blit(text_surface_m2,(42,520))
  elif many_chart == 2:
    screen.blit(text_surface_m2,(42,520))
    screen.blit(text_surface_m3,(42,555))
  if show_notice == True:
    screen.blit(initpintu,(200,186))
    screen.blit(notice,(327.5,400))
    screen.blit(text_surface_1,(250,230))
    screen.blit(text_surface_2,(250,255))
    screen.blit(text_surface_3,(250,280))
    screen.blit(text_surface_4,(250,305))
    screen.blit(text_surface_5,(250,330))
    screen.blit(text_surface_6,(250,355))
    screen.blit(text_surface_7,(250,380))
  pygame.display.update()
