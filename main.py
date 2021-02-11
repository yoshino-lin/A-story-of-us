from Source.mainMenu import *

if __name__ == "__main__":
    flags =  pygame.DOUBLEBUF | pygame.SCALED | pygame.FULLSCREEN
    # 创建窗口
    screen = linpg.display.init_screen(flags)
    mainMenu = MainMenu(screen)
    mainMenu.display(screen)
