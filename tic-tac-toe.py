import pygame
import sys
import random
pygame.init()

### условие победы
def check_win (mas, sign):
  zeroes = 0
  for row in mas:
    zeroes += row.count(0)
    if row.count(sign) == 3:
      return 'победа '+sign+', нажмите любую клавишу для выхода в меню'
  for col in range(3):
    if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
      return 'победа '+sign+', нажмите любую клавишу для выхода в меню'
  if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
      return 'победа '+sign+', нажмите любую клавишу для выхода в меню'
  if  mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
      return 'победа '+sign+', нажмите любую клавишу для выхода в меню'
  if zeroes == 0:
    return 'ничья нажмите любую клавишу для выхода в меню'

### цвета RGB
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0,0,0)

def Game1():
  ### экран и размер блоков
  mas = [[0] * 3 for i in range(3)]
  size_block = 150
  margin = 15
  width = size_block * 3 + margin * 4
  height = size_block * 3 + margin * 4
  size_window = (width, height)
  sc = pygame.display.set_mode(size_window)
  pygame.display.set_caption("крестики нолики")
  pygame.display.flip()
  query = 0
  game_over = False

  ### основной цикл работы программы и завершения
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
        break
      elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        x_mouse, y_mouse = pygame.mouse.get_pos()
        col = x_mouse // (size_block + margin)
        row = y_mouse // (size_block + margin)
        if mas[row][col] == 0:
          if query%2 == 0:
            mas[row][col] = 'x'
          else:
            mas[row][col] = 'o'
   
          query += 1

      elif event.type == pygame.KEYDOWN and game_over:
        game_over = False
        menu()
    
        
        
      for row in range(3): ### игровое поле
        for col in range(3):
          if mas[row][col] == 'x':
            color = RED
          elif mas[row][col] == 'o':
            color = BLUE
          else:
            color = WHITE
          y = row * size_block + (row + 1) * margin
          x = col * size_block + (col + 1) * margin
          pygame.draw.rect(sc, WHITE, (x, y, size_block, size_block))
          if color == RED:
            pygame.draw.line(sc, RED, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 10)
            pygame.draw.line(sc, RED, (x + size_block - 5, y + 5), (x + 5,  y + size_block - 5), 10)
          if color == BLUE:
            pygame.draw.circle(sc, BLUE, (x + size_block//2, y + size_block//2), size_block//2, 10)
      
  ### конец игры      
      if (query-1) % 2 == 0: #x
        game_over = check_win (mas, 'x')
      else:
        game_over = check_win (mas, 'o')
        
      if game_over:
        sc.fill(BLACK)
        font = pygame.font.SysFont('stxingkai', 22)
        text1 = font.render(game_over, True, GREEN)
        text_rect = text1.get_rect()
        text_x = sc.get_width() / 2 - text_rect.width / 2
        text_y = sc.get_height() / 2 - text_rect.height / 2
        sc.blit(text1, [text_x, text_y])
        
      pygame.display.update()

def Game2():
  ### экран и размер блоков
  mas = [[0] * 3 for i in range(3)]
  size_window = (450, 450)
  sc = pygame.display.set_mode(size_window)
  sc.fill(WHITE)
  pygame.display.set_caption("крестики нолики")
  pygame.display.flip()
  game_over = False
  query = 0
  l=[1, 2, 3]

  def draw2(sc):        
    pygame.draw.line(sc, BLACK, (150, 0), (150, 450), 5)
    pygame.draw.line(sc, BLACK, (300, 0), (300, 450), 5)
    pygame.draw.line(sc, BLACK, (0, 150), (450, 150), 5)
    pygame.draw.line(sc, BLACK, (0, 300), (450, 300), 5)

    
  ### основной цикл работы программы и завершения
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
        break
        
      elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        pos = pygame.mouse.get_pos()
        if mas[pos[1] // 150][pos[0] // 150] == 0:
          mas[pos[1] // 150][pos[0] // 150] = 'x'
          x1, y1 = random.randint(0, 2), random.randint(0, 2)
          while mas[x1][y1] != 0:
            x1, y1 = random.randint(0, 2), random.randint(0, 2)
          mas[x1][y1] = 'o'
          query += 1

        for row in range(3): 
          for col in range(3):
            if mas[row][col] == 'x':
              pygame.draw.line(sc, RED, (col*150+10, row*150+10), (col*150+142, row*150+142), 10)
              pygame.draw.line(sc, RED, (col*150+142, row*150+10), (col*150+10, row*150+142), 10)
            if mas[row][col] == 'o':
              pygame.draw.circle(sc, BLUE, (col*150+75, row*150+75), 67, 10)
              
            
        pygame.display.update()
        pygame.time.wait(100)
            
      draw2(sc)
      player_win = check_win(mas, 'x')         
      random_win = check_win(mas, 'o')
      if player_win:
        game_over = check_win(mas, 'x')
      elif random_win:
        game_over = check_win(mas, 'o')
      elif query == 4:
        game_over = "ничья"
      if game_over:  
        sc.fill(BLACK)
        font = pygame.font.SysFont('stxingkai', 22)
        text1 = font.render(game_over, True, GREEN)
        text_rect = text1.get_rect()
        text_x = sc.get_width() / 2 - text_rect.width / 2
        text_y = sc.get_height() / 2 - text_rect.height / 2
        sc.blit(text1, [text_x, text_y])

      if event.type == pygame.KEYDOWN and game_over:
        game_over = False
        menu()
  
      pygame.display.update()
      

      




def menu():
  ### экран и размер блоков
  size_block = 150
  margin = 15
  width = size_block * 3 + margin * 4
  height = size_block * 3 + margin * 4
  size_window = (width, height)
  sc = pygame.display.set_mode(size_window)
  pygame.display.set_caption("крестики нолики")
  pygame.draw.rect(sc, GREEN, (120, 50, 255, 70))
  pygame.draw.rect(sc, GREEN, (120, 170, 255, 70))
  pygame.draw.rect(sc, GREEN, (120, 390, 255, 70))
  f1 = pygame.font.Font(None, 30)
  text = f1.render('Режим 2 игрока', True, WHITE)
  place = text.get_rect(center = (250, 85))
  sc.blit(text, place)

  f1 = pygame.font.Font(None, 22)
  text = f1.render('Режим игрок против компьютера', True, WHITE)
  place = text.get_rect(center = (250, 205))
  sc.blit(text, place)

  f1 = pygame.font.Font(None, 35)
  text = f1.render('Выйти', True, WHITE)
  place = text.get_rect(center = (250, 425))
  sc.blit(text, place)

  pygame.display.update()
  pygame.display.flip()
  while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit(0)
          break
        elif event.type == pygame.MOUSEBUTTONDOWN:
          x_mouse, y_mouse = pygame.mouse.get_pos()
          if x_mouse > 120 and x_mouse < 375:
            if y_mouse > 50 and y_mouse < 120:
              Game1()
            elif y_mouse > 170 and y_mouse < 240:
              Game2()
            elif y_mouse > 390 and y_mouse < 460:
                  pygame.quit()
                  sys.exit(0)
      
menu()
