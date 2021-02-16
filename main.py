from Source.mainMenu import *

if __name__ == "__main__":
    #pygame.DOUBLEBUF | pygame.SCALED | pygame.FULLSCREEN
    flags = pygame.SCALED
    # 创建窗口
    screen = linpg.display.init_screen(flags)
    mainMenu = MainMenu(screen)
    mainMenu.display(screen)
