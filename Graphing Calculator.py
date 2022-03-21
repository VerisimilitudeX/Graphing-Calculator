menu Code

Assignments

My Code
today
Classes
Code

 
 
PROJECT
CODE ASSIST
Graphing_Calculator
Reset project
Code

Graphing_Calculator.py

Add Code
Images

Add Image
Sounds
library_music
Add Sound
Data

Add Data
Fonts

Roboto-Regular.ttf

Add Font
play_arrowRunPrint
format_size
Font Size
fullscreen
FullscreenFullscreen
Graphing_Calculator.py
  noprev = True
  for x in range(0, WIDTH):
    xv = screenx_to_coord(x)
    try:
      yv = eval_node(eq, {"x": xv})
    except (ZeroDivisionError, ValueError):
      noprev = True
      continue
    
    if noprev:
      prevxv = xv
      prevyv = yv
      noprev = False
    else:
      (x, y) = coord_to_screen(xv, yv) # Pixel by pixel eval func
      (prevx, prevy) = coord_to_screen(prevxv, prevyv) # Pixel by pixel eval func
      pygame.draw.line(win, (255, 0, 0), (prevx, prevy), (x, y), width=2)
      prevxv = xv
      prevyv = yv
​
  pygame.display.flip()
​
# Main loop
running = True
draw()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  keys = pygame.key.get_pressed()
  changed = False
​
  speed = 3
  speedscale = 1.01
  if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
    speed = 6
    speedscale = 1.1
​
  if keys[pygame.K_LEFT]:
    offx += speed
    changed = True
  if keys[pygame.K_RIGHT]:
    offx -= speed
    changed = True
  if keys[pygame.K_UP]:
    offy += speed
    changed = True
  if keys[pygame.K_DOWN]:
    offy -= speed
    changed = True
  if keys[pygame.K_EQUALS]: # Plus
    scale *= speedscale
    changed = True
  if keys[pygame.K_MINUS]: # Minus
    scale /= speedscale
    changed = True
​
  # Shortcuts
  if keys[pygame.K_h]:
    # Home
    scale = WIDTH / 20
    offx = WIDTH / 2
    offy = HEIGHT / 2
    draw()
  
  if changed:
    draw()
ASSIGNMENT
Solution CodeSolution Code
 Solution Codex
