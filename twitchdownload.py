# Youtube-DL
from __future__ import unicode_literals

import youtube_dl
from kivy.app import App
from kivy.config import Config
import os

Config.set('kivy','window_icon', 'images/ico/icon.ico')
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class VillagerPvP_TwitterApp(Widget):
    user_vid_input = ObjectProperty(None)


    def btn0(self):
        user_vid_input = self.user_vid_input.text



        def searchhash():
            yt_dl = str(self.user_vid_input.text)

            ydl_opts = {
            'outtmpl': 'Downloads/%(title)s.%(ext)s',
            'download_archive': 'download_history.txt',

            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_dl])



        searchhash()

    def btn1(self):
        self.user_vid_input.text = ""



class VillagerPvP_TwitterAppApp(App):
    def build(self):
        return VillagerPvP_TwitterApp()

if __name__ == "__main__":
    VillagerPvP_TwitterAppApp().run()