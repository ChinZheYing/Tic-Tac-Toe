import pygame as pg
import time

width = 300
height = 300

pg.init() 
fps = 30
CLOCK = pg.time.Clock() 
screen = pg.display.set_mode((width,height), 0, 32) 

pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 80)
x = myfont.render('X', False, (0, 0, 0))
o = myfont.render('O', False, (0, 0, 0))

status = ['a','b','c','d','e','f','g','h','i']
turn = 'x'


def check_win():
   global turn
   if status[0] == status[1] and status[1] == status[2]:
     pg.draw.line(screen, 0, (0,50),(300,50), 5)
     turn = 'a'
   if status[3] == status[4] and status[4] == status[5]: 
     pg.draw.line(screen, 0, (0,150),(300,150), 5)
     turn = 'a'
   if status[6] == status[7] and status[7] == status[8]: 
     pg.draw.line(screen, 0, (0,250),(300,250), 5)
     turn = 'a'
   
   if status[0] == status[3] and status[3] == status[6]: 
     pg.draw.line(screen, 0, (50,0),(50,300), 5)
     turn = 'a'
   if status[1] == status[4] and status[4] == status[7]: 
     pg.draw.line(screen, 0, (150,0),(150,300), 5)
     turn = 'a'
   if status[2] == status[5] and status[5] == status[8]: 
     pg.draw.line(screen, 0, (250,0),(250,300), 5)
     turn = 'a'
   
   if status[0] == status[4] and status[4] == status[8]: 
     pg.draw.line(screen, 0, (0,0),(300,300), 5)
     turn = 'a'
   if status[2] == status[4] and status[4] == status[6]:
     pg.draw.line(screen, 0, (300,0),(0,300), 5)
     turn = 'a'


def user_click():
  global turn
  posx, posy = pg.mouse.get_pos()
  if turn == 'x':
    if posx < 100 and posy < 100:
      status[0] = turn
      screen.blit(x,(0+20,0))
    elif posx < 200 and posy < 100:
      status[1] = turn
      screen.blit(x,(100+20,0))
    elif posx < 300 and posy < 100:
      status[2] = turn
      screen.blit(x,(200+20,0))
    elif posx < 100 and posy < 200:
      status[3] = turn
      screen.blit(x,(0+20,100-10))
    elif posx < 200 and posy < 200:
      status[4] = turn
      screen.blit(x,(100+20,100-10))
    elif posx < 300 and posy < 200:
      status[5] = turn
      screen.blit(x,(200+20,100-10))
    elif posx < 100 and posy < 300:
      status[6] = turn
      screen.blit(x,(0+20,200-10))
    elif posx < 200 and posy < 300:
      status[7] = turn
      screen.blit(x,(100+20,200-10))
    elif posx < 300 and posy < 300:
      status[8] = turn
      screen.blit(x,(200+20,200-10))
    turn = 'o'
  elif turn == 'o': 
    if posx < 100 and posy < 100:
      status[0] = turn
      screen.blit(o,(0+20,0))
    elif posx < 200 and posy < 100:
      status[1] = turn
      screen.blit(o,(100+20,0))
    elif posx < 300 and posy < 100:
      status[2] = turn
      screen.blit(o,(200+20,0))
    elif posx < 100 and posy < 200:
      status[3] = turn
      screen.blit(o,(0+20,100-10))
    elif posx < 200 and posy < 200:
      status[4] = turn
      screen.blit(o,(100+20,100-10))
    elif posx < 300 and posy < 200:
      status[5] = turn
      screen.blit(o,(200+20,100-10))
    elif posx < 100 and posy < 300:
      status[6] = turn
      screen.blit(o,(0+20,200-10))
    elif posx < 200 and posy < 300:
      status[7] = turn
      screen.blit(o,(100+20,200-10))
    elif posx < 300 and posy < 300:
      status[8] = turn
      screen.blit(o,(200+20,200-10))
    turn = 'x'
  check_win()
  
    

def game_initiating_window(): 
    # updating the display 
    pg.display.update() 
    time.sleep(3)                    
    screen.fill((255,255,255))

    # drawing lines 
    pg.draw.line(screen, 0, (0,100),(300,100), 1)
    pg.draw.line(screen, 0, (0,200),(300,200), 1)
    pg.draw.line(screen, 0, (100,0),(100,300), 1)
    pg.draw.line(screen, 0, (200,0),(200,300), 1)

game_initiating_window() 

while(True): 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            pg.quit() 
        elif event.type is pg.MOUSEBUTTONDOWN: 
            user_click()
        elif event.type == pg.KEYDOWN:
          if event.key == pg.K_SPACE: 
            turn = 'x'
            status = ['a','b','c','d','e','f','g','h','i']
            game_initiating_window() 

    pg.display.update() 
    CLOCK.tick(fps) 