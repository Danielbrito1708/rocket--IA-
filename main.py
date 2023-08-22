from src.constantes import *

pygame.init()
pygame.display.set_caption(PROJECT_NAME)

SCREEN.fill(BLACK())

if ON_FULLSCREEN:
    pygame.display.toggle_fullscreen()
    
clock = pygame.time.Clock()

# -----+----- #



# -----+----- #

while RUN:
    clock.tick(FPS)
    SCREEN.fill(WHITE(10))
    
    pygame.display.set_caption(f'{PROJECT_NAME}    fps: {str(int(clock.get_fps()))}')

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            RUN = False

        if event.type == pygame.MOUSEWHEEL:
            pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f :
                ON_FULLSCREEN = not ON_FULLSCREEN
                if ON_FULLSCREEN:
                    SCREEN = pygame.display.set_mode(flags=pygame.FULLSCREEN)
                else:
                    SCREEN = pygame.display.set_mode(SIZE_SCREEN)    

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        RUN = False

    if keys[pygame.K_t] :
        pass

    if RUN == True: 
        pygame.display.update()