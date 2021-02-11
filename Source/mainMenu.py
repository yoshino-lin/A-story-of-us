from .dialogSystem import *

class MainMenu(linpg.SystemObject):
    def __init__(self,screen):
        #初始化系统模块
        linpg.SystemObject.__init__(self)

        #窗口标题图标
        linpg.display.set_icon("Assets/image/UI/icon.png")
        linpg.display.set_caption(linpg.get_lang('General','game_title'))

        #加载主菜单背景
        self.bg_img = linpg.loadImage("Assets/image/UI/bg0.png",(0,0),screen.get_width(),screen.get_height())
        #初始化返回菜单判定参数
        linpg.set_glob_value("BackToMainMenu",False)
    def display(self,screen):
        #主循环
        while self._isPlaying:
            self._update_event()
            #背景视频
            self.bg_img.draw(screen)
            for event in self.events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    dialog("main_chapter",1,screen,"dialog_example")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    linpg.display.quit()
            linpg.display.flip()