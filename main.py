import pygame


global image
image = pygame.image.load("./zombie.jpg")
idle = [
  image.subsurface(pygame.Rect(10,10, 50, 60)),
  image.subsurface(pygame.Rect(75,10, 50, 60)),
  image.subsurface(pygame.Rect(135,10, 50, 60)),
  image.subsurface(pygame.Rect(195,10, 50, 60)),
  image.subsurface(pygame.Rect(255,10, 50, 60))
]
walking = [
  image.subsurface(pygame.Rect(5,145, 50, 60)),
  image.subsurface(pygame.Rect(45,145, 50, 60)),
  image.subsurface(pygame.Rect(105,145, 50, 60)),
  image.subsurface(pygame.Rect(160,145, 50, 60)),
  image.subsurface(pygame.Rect(220,145, 50, 60)),
  image.subsurface(pygame.Rect(280,145, 50, 60)),
  image.subsurface(pygame.Rect(340,145, 50, 60)),
  image.subsurface(pygame.Rect(390,145, 50, 60)),
  image.subsurface(pygame.Rect(450,145, 50, 60))

]
def init_pygame() -> None:
  pygame.init()
  global screen
  screen = pygame.display.set_mode((500,500))
def flipThrough(images: list):
  while True:
    for image in images:
      screen.blit(image, (0,0))
      pygame.display.flip()
      pygame.time.wait(100)

def start() -> None:
  global screen, image
  screen.fill((255,255,255))
  #screen.blit(idle[1], (100,100))
  flipThrough(walking)
  pygame.display.update()
  while True:
      
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              return
if __name__ == '__main__':
  init_pygame()
  start()
