import glob
import os
import shutil
import time
import pygame
import linpg

class DialogSystem(linpg.DialogSystem):
    def __init__(self):
        linpg.DialogSystem.__init__(self)
    #保存数据
    def save_process(self):
        #别忘了看看Save文件夹是不是都不存在
        if not os.path.exists("Save"):
            os.makedirs("Save")
        #存档数据
        save_thread = linpg.SaveDataThread("Save/save.yaml",{
            "chapterType": self.chapterType,
            "chapterId": self.chapterId,
            "type": self.part,
            "id": self.dialogId,
            "dialog_options": self.dialog_options,
            "collection_name": self.collection_name
        })
        save_thread.start()
        save_thread.join()
        del save_thread
        #检查global.yaml配置文件
        if not os.path.exists("Save/global.yaml"):
            DataTmp = {"chapter_unlocked":1}
            linpg.saveConfig("Save/global.yaml",DataTmp)

#对话系统
def dialog(chapterType,chapterId,screen,part,collection_name=None):
    #卸载音乐
    linpg.unloadBackgroundMusic()
    #初始化对话系统模块
    DIALOG = DialogSystem()
    if chapterType != None:
        DIALOG.new(chapterType,chapterId,part,collection_name)
    else:
        DIALOG.load("Save/save.yaml")
    #DIALOG.auto_save = True
    #主循环
    while DIALOG.is_playing():
        DIALOG.display(screen)
        linpg.display.flip()
    #返回玩家做出的选项
    return DIALOG.dialog_options

#对话编辑器
def dialogCreator(chapterType,chapterId,screen):
    #卸载音乐
    linpg.unloadBackgroundMusic()
    #加载对话
    DIALOG = linpg.DialogSystemDev(chapterType,chapterId)
    #主循环
    while DIALOG.is_playing():
        DIALOG.display(screen)
        linpg.display.flip()