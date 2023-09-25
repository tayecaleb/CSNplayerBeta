import os
import sys
from pathlib import Path
from kivy.clock import Clock


from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
import os

from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
import requests
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout

import sqlite3
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import os
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random
from tinytag import TinyTag
from kivy.factory import Factory
from kivy.uix.popup import Popup
from pathlib import Path
import os
import time
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.modalview import ModalView
from kivymd.uix.list import OneLineAvatarListItem
from kivy.core.window import Window
# from wakepy import set_keepawake, unset_keepawake

# set_keepawake(keep_screen_awake=True)

Window.size = (1300, 600)

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

class Songlist(OneLineListItem):
    musicname = StringProperty()
    

class Content(BoxLayout):
    pass

class Item(OneLineAvatarListItem):
    divider = None

kv = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import gch kivy.utils.get_color_from_hex
#:import MagicBehavior kivymd.uix.behaviors.MagicBehavior
#:import environ os.environ
#:import gch kivy.utils.get_color_from_hex
#:import IconRightWidget kivymd.uix.list.IconRightWidget
#:import colors kivymd.color_definitions.colors
#:import gch kivy.utils.get_color_from_hex
#:import Clock kivy.clock.Clock
#:import rgba kivy.utils.get_color_from_hex

<Item>:

<Songlist>
    
    text: root.musicname
    id: song
    # text: f"[font=Consolas.ttf]The Skies will sore"
    theme_text_color: 'Custom'
    text_color: rgba("#ffffff")
    secondary_text: f"[font=Consolas.ttf]contains 41 songs"
    secondary_theme_text_color: 'Custom'
    secondary_text_color: rgba("#d6e4d4")
    on_press: app.playaudio2(song.text)
        

<LoadDialog>:
    id: flo
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        
        ScrollView:
            scroll_type: ['bars']
            bar_width: "15dp"
            canvas.before:
                Color:
                    rgba: rgba("#F0F8FF")
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                            
            MDList:
                id: content1
                custom_divider: gch(colors[app.theme_cls.primary_palette]["50"])
            

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Load"
                on_release: root.load(filechooser.path, filechooser.selection)

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "show"
                on_release: root.showplaylist()

            
        


<Content>
    orientation: "vertical"
    size_hint_y: None
    height: 130
    MDLabel:
        id: t1album
    
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1albumartist
        text: ""
    
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1artist
        text: ""
        
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1duration
        text: ""
        
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1filesize
        text: ""
        
        
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1genre
        text: ""
        
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1title
        text: ""
    
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1track
        text: ""
    
    Widget:
        size_hint_y: None
        height: 5
        
    MDLabel:
        id: t1year
        text: ""
      

ScreenManager:
    transition: FadeTransition()
    id: screen_manager
              
    
    Screen:
        name: "Home screen"
        canvas.before:
            Color:
                rgba: rgba('#f8f5f4')
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'legal.png'

        MDBoxLayout:
            adaptive_height: True
            pos_hint: {"center_x": .5, "center_y": 0.97}
            MDBoxLayout:
                adaptive_height: True
                orientation: "vertical"
                
                MDBoxLayout:
                    adaptive_height: True
                    
                    MDBoxLayout:
                        adaptive_height: True
                        orientation: "vertical"
                        size_hint_x: None
                        width: 190

                        pos_hint: {"center_x": .5, "center_y": .1}
                        canvas.before:
                            Color:
                                rgb: rgba("#76a170")
                            Rectangle:
                                pos: self.pos
                                size: self.size
                    
                    
                        Widget: 
                            size_hint_y: None
                            height: 25
                        BoxLayout:
                            Widget:
                                size_hint_x: None
                                width: 30
                            MDLabel:
                                text: "CSNPlayer"
                                color: rgba("#ffffff")
                                # halign: "center"
                        
                        Widget: 
                            size_hint_y: None
                            height: 7
                        

                        BoxLayout:
                            size_hint_y: None
                            height: 35
                            padding: 10
                            
                            MDIconButton:
                                icon: "volume-plus"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press: app.volumeup()
                                icon_size: "21sp"
                                text_color:  rgba("#ffffff")
                                theme_text_color: "Custom"
                                    
                                
                            Widget:
                            BoxLayout:
                                size_hint_x: None
                                width: 50

                                canvas.before:
                                    Color:
                                        rgba: rgba("#B0C4DE")
                                    RoundedRectangle:
                                        size: self.size
                                        pos: self.pos
                                        
                                Label:
                                    text: '100%'
                                    id: valume
                                    italic: True
                                    
                            Widget:

                        
                                
                                
                                
                            MDIconButton:
                                icon: "volume-minus"
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press: app.volumedown() 
                                icon_size: "21sp"
                                text_color:  rgba("#ffffff")
                                theme_text_color: "Custom"

                        BoxLayout:
                            orientation: "horizontal"
                            size_hint_y: None
                            height: 30
                            
                            
                            Button:
                                
                                background_color: rgba("#6bc9a9")
                                color: rgba("#FFFFFF")
                                text: "Browse Your PC"
                                on_press: app.show_load()
                        Widget:

                        BoxLayout:
                            orientation: "horizontal"
                            size_hint_y: None
                            height: 30
                            
                            
                            Button:
                                on_press: app.show_simple_dialog()
                                background_color: rgba("#6bc9a9")
                                color: rgba("#FFFFFF")
                                text: "View Detail"
                                
                        
                      
                        

                                
                                

                                                      
                            
                        Widget:
                            size_hint_y: None
                            height:  70

                    MDBoxLayout:
                        adaptive_height: True
                        orientation: "vertical"
                        pos_hint: {"center_x": .5, "center_y": .05}
                    
                        Widget: 
                            size_hint_y: None
                            height: 10
                        BoxLayout:
                            size_hint_y: None
                            height: 40
                            Widget:
                                size_hint_x: None
                                width: 10
                            MDLabel:
                                text: "Home"
                        MDBoxLayout:
                            adaptive_height: True
                            padding: 10
                            BoxLayout:
                                orientation: "vertical"
                                padding: 20
                                spacing: 10
                                size_hint_y: None
                                height: 390
                                canvas.before:
                                    Color:
                                        rgb: rgba("#d6e4d4")
                                    RoundedRectangle:
                                        pos: self.pos
                                        size: self.size

                                BoxLayout:
                                    size_hint_y: None
                                    height: 40
                                    BoxLayout:
                                        orientation: "vertical"
                                        size_hint_y: None
                                        height: 40
                                        MDLabel:
                                            text: "Current Song"
                                            color: rgba("#000000")
                                            font_size: 15

                                          
                                    Widget:


                                BoxLayout:
                                    Widget:
                                    Image:
                                        source: "legal.png"
                                        # source: "legal.png"
                                        id: pacture
                                    Widget:
                                    
                        
                                

                    MDBoxLayout:
                        adaptive_height: True
                        orientation: "vertical"
                        pos_hint: {"center_x": .5, "center_y": .05}
                        size_hint_x: None
                        width: 330
                    
                        Widget: 
                            size_hint_y: None
                            height: 10
                        BoxLayout:
                            size_hint_y: None
                            height: 40
                            Widget:
                                size_hint_x: None
                                width: 10
                            MDLabel:
                                text: "Musics"
                        MDBoxLayout:
                            adaptive_height: True
                            padding: 10
                            BoxLayout:
                                orientation: "vertical"
                                padding: 20
                                spacing: 10
                                size_hint_y: None
                                height: 390
                                canvas.before:
                                    Color:
                                        rgb: rgba("#2ac78b")
                                    RoundedRectangle:
                                        pos: self.pos
                                        size: self.size
                                BoxLayout:
                                    orientation: "vertical"
                                    size_hint_y: None
                                    height: 40
                                    MDLabel:
                                        text: "Your Songs"
                                        color: rgba("#ffffff")
                                        font_size: 15

                                    MDLabel:
                                        text: "Total Songs: 12 Songs"
                                        color: rgba("#d1e2dc")
                                        font_size: 12
                                        id: totalsongs


                                BoxLayout:
                                    orientation: "vertical"
                                    ScrollView:
                                        scroll_type: ['bars']
                                        bar_width: "15dp"
                                        bar_inactive_color: .55, .55, .55, 1 
                                        bar_color: .663, .663, .663, 1 
                                        MDList:
                                            id: content 
                                            padding: 10
                                            custom_divider: gch(colors[app.theme_cls.primary_palette]["50"])

                                            
        MDBoxLayout:
            
            BoxLayout: 
                orientation: 'vertical'
                size_hint_y: None
                height: 150
                canvas.before:
                    Color:
                        rgb: rgba("#87d87c")
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        
                
                

                MDLabel:
                    id: name_track
                    halign: "center"
                    text: "No Song Inputted"
                    font_style: "Caption"
                    size_hint_y: None
                    height: 35
                    color: rgba("#ffffff")

                Widget:
                    size_hint_y: None
                    height: "3dp"
                        
                MDBoxLayout:
                    adaptive_height: True
                    
                            

                    MDLabel:
                        halign: "center"
                        id: track_seconds1
                        text: "00:00"
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: rgba("#ffffff")
                        size_hint_x: None
                        width: 70

                    MDProgressBar:
                        id: progress_bar
                        value: 0
                        
                        
                        
                    MDLabel:
                        halign: "center"
                        id: track_seconds2
                        text: "00:00"
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: rgba("#ffffff")
                        size_hint_x: None
                        width: 70
                        
                MDBoxLayout:
                    adaptive_height: True
                    Widget:
                    MDIconButton:
                        icon: "skip-previous-outline"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon_size: "28sp"
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        on_press: app.previouss()
                        
                        
                        
                    MDIconButton:
                        icon: "skip-backward-outline"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon_size: "28sp"
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        on_press: app.backward()
                
                        
                        
                    MDIconButton:
                        icon: "play-circle-outline" if app.cuoostate == "pause" else "pause"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon_size: "35sp"
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        on_press: app.playaudio()
                        
                        
                    MDIconButton:
                        icon: "skip-forward-outline"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        icon_size: "28sp"
                        on_press: app.forward()
                        
                        
                    MDIconButton:
                        icon: "skip-next-outline"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        icon_size: "28sp"
                        on_press: app.nexts()
                        
                    Widget:
                        
                MDBoxLayout:
                    adaptive_height: True
                    Widget:
                    
                    MDIconButton:
                        icon: "shuffle-disabled" if app.cuoostateshuffle == "noshuffle" else "shuffle"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon_size: "22sp"
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        on_press: app.sssshuffle()
                    
                    Widget:
                    
                    MDIconButton:
                        icon: "volume-medium" if app.cuoostatemute == "unmuted" else "volume-mute"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon_size: "22sp"
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        on_press: app.mmmmuting()
                        

                    Widget:
                        
                    MDIconButton:
                        icon: "file"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon_size: "22sp"
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        
                    Widget:
                    
                    MDIconButton:
                        icon: "repeat" if app.cuoostateloop == "norepeat" else "repeat-once" 
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon_size: "22sp"
                        text_color:  rgba("#ffffff")
                        theme_text_color: "Custom"
                        on_press: app.lllloop()
                        
                    Widget:      


    MDScreen:
        name: "Rough screen"
               
        
        
        MDBoxLayout:
            
            orientation: 'vertical'
            
            padding: '20dp'
                   
                    
                    
           
            BoxLayout:
                size_hint_y: None
                height: 1 
                id: detailss
                orientation: 'vertical'
                BoxLayout:
                    
                    MDLabel:
                        id: t1album
                        italic: True
                        halign: "center"
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                    MDLabel:
                        id: t1artist
                        text: ""
                        italic: True
                        halign: "center"
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                    
                    MDLabel:
                        id: t1duration
                        text: ""
                        italic: True
                        halign: "center"
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                    
                    
                    MDLabel:
                        halign: "center"
                        id: shuffleds
                        text: ""
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                        
                    MDLabel:
                        halign: "center"
                        id: loops
                        text: ""
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                        
                    MDLabel:
                        halign: "center"
                        id: volumes
                        text: ""
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                        
                    MDLabel:
                        id: t1filesize
                        text: ""
                        halign: "center"
                        italic: True
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        
                    
                    MDLabel:
                        id: t1year
                        text: ""
                        italic: True
                        halign: "center"
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                      
                
                                       
"""

class MusicApp(MDApp):
    track_seconds = NumericProperty(480)
    app = ObjectProperty()
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    simple_dialog = None
    alert_dialog = None
    custom_dialog = None
    confirmation_dialog = None
    cuoostate = StringProperty("pause")
    cuoostateloop = StringProperty("norepeat")
    cuoostatemute = StringProperty("unmuted")
    cuoostateshuffle = StringProperty("noshuffle")
    dialog = None

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print ("working")
        self.title = 'CSNPlayer'
        self.icon = 'CSNPlayer.png'
        self.currentsong = ""
        self.lops = "once"
        self.volume = 1
        self.pauses = "play"
        self.shuffles = "off"
        self.datail = "close"
##        self.manager_open = False
##        self.manager = None

        # self.custate = 'play'
        
        
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        
        return Builder.load_string(kv)

    def imagemusic(self):
        try:
            file_path2 = str(Path.home()) + '\\'  + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)'
            os.chdir(file_path2)
            
            if str(os.getcwd()) == file_path2:
                print ("Exist")
                
        except:
            
            file_path = str(Path.home()) + '\\'  + r'Music'
            os.chdir(file_path)
            os.mkdir('CreateSphereNairaImage(CSN Player)')
        
    def on_start(self):

        # os.chdir(r'c:\Users\user\Desktop')
        # os.mkdir('note folders')
        # self.allsong()
        self.imagemusic()
        try:
            file_path = str(Path.home()) + '\\'  + r'Music' + '\\' + 'CreateSphereNairaMusic(CSN Player)'
            os.chdir(file_path)
            if str(os.getcwd()) == file_path:
                print ("Exist")
                
        except:
            
            file_path = str(Path.home()) + '\\'  + r'Music'
            os.chdir(file_path)
            os.mkdir('CreateSphereNairaMusic(CSN Player)')
            
            
        self.allsong()
        
    def allsong(self):
        self.imgfiles = []
        self.imgfiles2 = []
        for dirpath1, dirnames1, filenames1 in os.walk(str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)'): 
            self.imgfiles2 = filenames1

        for i in range(len(self.imgfiles2)):
            if self.imgfiles2[i].endswith('.jpg') or self.imgfiles2[i].endswith('.png'):
                if self.imgfiles2[i] not in self.imgfiles:
                    self.imgfiles.append(self.imgfiles2[i])

        print('ww', self.imgfiles)

        
##        self.root.ids.pacture.source = str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles)
##        print (str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles))


        
        self.files2 = []
        self.files = []
        for dirpath, dirnames, filenames in os.walk(str(Path.home()) + '\\'  + r'Music' + '\\' + 'CreateSphereNairaMusic(CSN Player)'): 
            self.files2 = filenames

        for i in range(len(self.files2)):
            if self.files2[i].endswith('.mp3') or self.files2[i].endswith('.wav') or self.files2[i].endswith('.oog'):
                if self.files2[i] not in self.files:
                    self.files.append(self.files2[i])

        loop = len(self.files)
        self.root.ids.totalsongs.text = "Total Songs: " + str(loop) + " Songs"

        self.root.ids.content.clear_widgets(self.root.ids.content.children[:])
        for i in range(loop):
            
            # print (r'C:\Users\user\Music\music' + '\\' + files[i])
            # if filename[0].endswith('.mp3') or filename[0].endswith('.wav') or filename[0].endswith('.aac') or filename[0].endswith('.oog') or filename[0].endswith('.wma'):
            if self.files[i].endswith('.mp3') or self.files[i].endswith('.wav') or self.files[i].endswith('.oog'):
                self.root.ids.content.add_widget(
                    Songlist(
                        musicname = self.files[i]
                    )
                )
            else:
                print (self.files[i])
            
    def action2(self):
        toast("opened the popup")
        
    def action1(self):
        toast("play song")
        
    
    def get_timer2(self, seconds):
        m = seconds // 60
        s = seconds - m * 60
        return "%02d:%02d" % (m, s)
        
    def get_timer(self):
        m = self.track_seconds // 60
        s = self.track_seconds - m * 60
        return "%02d:%02d" % (m, s)

  
        

    # def set_time(self,interval):
        # if self.action == "stop":
            # self.can = self.track_seconds + self.track_store
            # self.action = "start"
            # self.track_seconds = self.can
            # self.track_store = 0
            
           
        # self.track_seconds -= 1
        # self.track_store += 1
        
        
        # self.root.ids.track_seconds1.text =  self.get_timer()
        # if self.track_seconds <= 0:
            # self.root.ids.track_seconds1.text = self.states
            # Clock.unschedule(self.set_time)
            
            
    def set_time(self,interval):
        tag = TinyTag.get(self.currentsong)
        if self.action == "stop":
            self.can = self.track_seconds + self.track_store
            self.action = "start"
            self.track_seconds = self.can
            self.track_store = 0
            print ("house1")
            
        ## self.a is updated to current self.track_seconds for constant update
        ## self.a2 is also updated to current self.track_store
            
        self.a = self.track_seconds
        self.a2 = self.track_store
        
        self.track_seconds -= 1
        self.track_store += 1
        self.root.ids.progress_bar.max = tag.duration
        self.root.ids.progress_bar.value = self.track_store
        
        
        self.root.ids.track_seconds1.text = self.get_timer()
        
        if self.track_seconds <= 0:
            self.root.ids.track_seconds1.text = self.states
            Clock.unschedule(self.set_time)
            self.process = 'end'
            self.process2 = 'start'
            self.process3 = 'end'
            print ("1")
            if self.process == 'end' and self.process2 == "start":
                self.track_seconds = tag.duration
                self.track_store = 0
##                self.a = self.stage
                self.a = tag.duration
                self.a2 = 0
                print ("2")

            if self.lops == "loop":
                self.start_timer()
                print ("3")

            if self.lops == "once":

                print ("4")
                
            if self.process != "end" and self.process2 != "start" or self.lops != "loop" :
                leg = len(self.files)
                print (leg)
                print (self.files)
                print (len(self.files))
                print (self.currentsong2)
                print ("5")
                
                if '\\' in self.currentsong2:
                    collector = ""
                    r2 = len(self.currentsong2)

                    for i in range(r2):
                        v = self.currentsong2[r2 - 1 - i]
                        collector += v
                        if v == "\\":
                            break

                    songy = collector[::-1][1:]
                    
                    try:
                        if self.files.index(songy) <= leg-1:
                            if self.files.index(songy) == leg-1:
                                print ('finished')
                            else:
                                if self.shuffles == "off":
                                    leg2 = self.files[self.files.index(songy) + 1]
                                    self.playaudio2(leg2)
                                elif self.shuffles == "shuffle":
                                    if self.files.index(songy) <= 0 and leg == 5:
                                        leg2 = self.files[random.randrange(self.files.index(songy) + 4)]
                                        self.playaudio2(leg2)
                                        
                                        
                                    elif self.files.index(songy) <= 0 and leg == 6:
                                        leg2 = self.files[random.randrange(self.files.index(songy) + 5)]
                                        self.playaudio2(leg2)
                                        
                                    else:
                                        leg2 = self.files[random.randrange(self.files.index(songy))]
                                        self.playaudio2(leg2)
                                        
                    
                    except:
                        toast("Not in SongList")
                    
                        
                else:
                    try:
                        if self.files.index(self.currentsong2) <= leg-1:
                            if self.files.index(self.currentsong2) == leg-1:
                                print ('finished')
                                self.currentsong2 = self.files[0]
                                leg2 = self.files[self.files.index(self.currentsong2)]
                                self.playaudio2(leg2)

                            else:
                                if self.shuffles == "off":
                                    leg2 = self.files[self.files.index(self.currentsong2) + 1]
                                    self.playaudio2(leg2)
                                elif self.shuffles == "shuffle":
                                    # if self.files.index(self.currentsong2) <= 4 or leg <= 5:
                                        # print ('worrrking')
                                        # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 4)]
                                        # self.playaudio2(leg2)
                                        
                                    # elif self.files.index(self.currentsong2) >= 5 or leg >= 5:
                                        # print ('worrrking')
                                        # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 4)]
                                        # self.playaudio2(leg2)
                                        
                                    # else:
                                        # leg2 = self.files[random.randrange(self.files.index(songy))]
                                        # self.playaudio2(leg2)
                                        
                                    print ('worrrking1')
                                    if leg == 1:
                                        leg2 = self.files[random.randrange(leg)]
                                        self.playaudio2(leg2)
                                        
                                    elif leg == 2:
                                        leg2 = self.files[random.randrange(leg)]
                                        self.playaudio2(leg2)
                                        
                                    elif leg == 3:
                                
                                        leg2 = self.files[random.randrange(leg)]
                                        self.playaudio2(leg2)
                                        
                                    elif leg == 4:
                                        leg2 = self.files[random.randrange(leg)]
                                        self.playaudio2(leg2)
                                        
                                        
                                    elif leg == 5:
                                        leg2 = self.files[random.randrange(leg)]
                                        self.playaudio2(leg2)
                                        
                                    elif leg == 6:
                                        leg2 = self.files[random.randrange(leg)]
                                        self.playaudio2(leg2)
                                        
                                    elif leg >= 7:
                                        leg2 = self.files[random.randrange(leg)]
                                        self.playaudio2(leg2)
                    
                    except:
                        toast("Not in SongList")



        

    # def start_timer(self):
        # self.can = self.track_seconds + self.track_store
        # self.action = "start"
        # self.track_seconds = self.can
        # self.track_store = 0
        # Clock.schedule_interval(self.set_time, 1)
        
        
    # def start_timer2(self):
        # self.can = self.track_seconds + self.track_store
        # self.track_seconds = self.can
        # self.track_store = 0
        # Clock.schedule_interval(self.set_time, 1)
        
        
            
    def start_timer(self):
        self.can = self.track_seconds + self.track_store
        self.action = "start"
        self.track_seconds = self.can
        self.track_store = 0
        Clock.schedule_interval(self.set_time, 1)
        
        

    def start_timer2(self, value1, value2):
        self.can = value1
        self.action = "start"
        self.track_seconds = self.can
        self.track_store = value2
        Clock.schedule_interval(self.set_time, 1)        
            
            
        
        


    def playaudio(self):
        print ('processing')
        print (self.cuoostate)
        if self.cuoostate == "pause":
            self.cuoostate = "start"
            print (self.cuoostate)
              
        
            try:
                self.imgfiles = []
                self.imgfiles2 = []
                for dirpath1, dirnames1, filenames1 in os.walk(str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)'): 
                    self.imgfiles2 = filenames1

                for i in range(len(self.imgfiles2)):
                    if self.imgfiles2[i].endswith('.jpg') or self.imgfiles2[i].endswith('.png'):
                        self.imgfiles.append(self.imgfiles2[i])

                print('ww', self.imgfiles)

                
                # self.root.ids.pacture.source = str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles)
                print (str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles))

                
                #color
                    
                self.root.ids.t1album.color = (1,0,1,0)
                self.root.ids.t1artist.color = (1,0,1,0)
                self.root.ids.t1duration.color = (1,0,1,0)
                self.root.ids.t1filesize.color = (1,0,1,0)
                self.root.ids.t1year.color = (1,0,1,0)
                
                #color
                
                if self.pauses == "play":
                    self.states = "00:00"
                    self.action = "start"
                    self.process = "end"
                    self.process3 = "end"
                    self.track_store = 0
                    
                    self.a2 = 0
                    
                   
                    self.process2 = "start"
                    if self.process != 'step' and self.process2 != "stop" and self.process3 != "step":
                        try:
                            self.stopaudio()
                            self.sound = SoundLoader.load(self.currentsong)
                            tag = TinyTag.get(self.currentsong)

                            

                            self.root.ids.detailss.height = 0
                   
                            self.root.ids.t1album.text = 'album: ' + str(tag.album)
                            self.root.ids.t1artist.text ='artist: ' + str(tag.artist) 
                            self.root.ids.t1duration.text = 'duration: ' + str(self.get_timer2(tag.duration)) 
                            self.root.ids.t1filesize.text = 'filesize: ' + str(tag.filesize) + 'bytes'
                            self.root.ids.t1year.text = 'year: ' +  str(tag.year)
                            
                    
                            if '\\' in self.currentsong:
                                collector = ""
                                r2 = len(self.currentsong)

                                for i in range(r2):
                                    v = self.currentsong[r2 - 1 - i]
                                    collector += v
                                    if v == "\\":
                                        break

                                songy = collector[::-1][1:]
                                self.root.ids.name_track.text = songy
                            else:
                                self.root.ids.name_track.text = self.currentsong

                            
                            self.track_seconds = tag.duration
                            self.track_seconds2 = tag.duration
                            
                            self.stage = tag.duration
                            self.a = self.stage
                           
                            self.root.ids.track_seconds2.text = self.get_timer()
                            self.sound.play()
                            self.start_timer()
                            if self.root.ids.volumes.text == "":
                                self.sound.volume = self.volume
                            elif self.root.ids.volumes.text == "mute":
                                self.sound.volume = 0
                                
                            if self.lops == "loop":
                                self.sound.loop = True
                        
                        except:
                            toast("No song inputted")
                
                elif self.pauses == "pause":
                
                    tag = TinyTag.get(self.currentsong)
                    print (tag.duration)
                    if self.sound.length < 0:
                        toast('something wrong with song')
                        self.sound.play()
                        self.start_timer2(tag.duration, 0)
                    else:
                        self.sound.play()
                    
                        self.sound.seek(self.a2)
                        self.start_timer2(self.a, self.a2)
                        
                    if self.lops == "loop":
                        self.sound.loop = True
                        
                    print (self.a, self.a2)
                    
                   
            except:
                toast("No song Input")
        
        elif self.cuoostate == "start":
            print ('pause pause')
            self.pause()
            
    def playaudio2(self, song):
        self.cuoostate = "start"
        
    
        self.imgfiles = []
        self.imgfiles2 = []
        for dirpath1, dirnames1, filenames1 in os.walk(str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)'): 
            self.imgfiles2 = filenames1

        for i in range(len(self.imgfiles2)):
            if self.imgfiles2[i].endswith('.jpg') or self.imgfiles2[i].endswith('.png'):
                self.imgfiles.append(self.imgfiles2[i])

        print('ww', self.imgfiles)

        try:
            self.root.ids.pacture.source = str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles)
            print (str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles))
        
        except:
            self.root.ids.pacture.source = 'CSNPlayer.png'
            toast('No Image Gallery')


        self.states = "00:00"
        self.action = "start"
        self.process = "end"
        self.process3 = "end"
        self.pauses = "play"
        
        self.track_store = 0
        self.a2 = 0
        
        
        self.process2 = "start"
        self.currentsong2 = song
        if song.endswith('.jpg') or song.endswith('.png'):
            print ('image files present')            
        else:
        
        
            #color
                
            self.root.ids.t1album.color = (1,0,1,0)
            self.root.ids.t1artist.color = (1,0,1,0)
            self.root.ids.t1duration.color = (1,0,1,0)
            self.root.ids.t1filesize.color = (1,0,1,0)
            self.root.ids.t1year.color = (1,0,1,0)
            
            #color
            
           
            try:
                self.stopaudio()
                self.currentsong = r'C:\Users\user\Music\CreateSphereNairaMusic(CSN Player)' + '\\' + song
                tag = TinyTag.get(r'C:\Users\user\Music\CreateSphereNairaMusic(CSN Player)' + '\\' + song)
                self.sound = SoundLoader.load(r'C:\Users\user\Music\CreateSphereNairaMusic(CSN Player)' + '\\' + song)

                

                self.root.ids.detailss.height = 0
               
                self.root.ids.t1album.text = 'album: ' + str(tag.album)
                self.root.ids.t1artist.text ='artist: ' + str(tag.artist) 
                self.root.ids.t1duration.text = 'duration: ' + str(self.get_timer2(tag.duration)) 
                self.root.ids.t1filesize.text = 'filesize: ' + str(tag.filesize) + 'bytes'
                self.root.ids.t1year.text = 'year: ' +  str(tag.year)
                self.root.ids.name_track.text = song
                
                self.track_seconds = tag.duration
                self.track_seconds2 = tag.duration
                print (self.sound.length)
                print (tag.duration)
                self.stage = tag.duration
                self.a = self.stage
            
                self.root.ids.track_seconds2.text = self.get_timer()
                self.sound.play()
                self.start_timer()
                if self.root.ids.volumes.text == "":
                    self.sound.volume = self.volume
                elif self.root.ids.volumes.text == "mute":
                    self.sound.volume = 0
                
                if self.lops == "loop":
                    self.sound.loop = True
                        
                    
               
            except:
                
                self.currentsong = r'C:\Users\user\Music\CreateSphereNairaMusic(CSN Player)' + '\\' + song
                tag = TinyTag.get(r'C:\Users\user\Music\CreateSphereNairaMusic(CSN Player)' + '\\' + song)
                self.sound = SoundLoader.load(r'C:\Users\user\Music\CreateSphereNairaMusic(CSN Player)' + '\\' + song)
                self.root.ids.name_track.text = song
                
                

                
               
                self.root.ids.t1album.text = 'album: ' + str(tag.album)
                self.root.ids.t1artist.text ='artist: ' + str(tag.artist) 
                self.root.ids.t1duration.text = 'duration: ' + str(self.get_timer2(tag.duration)) 
                self.root.ids.t1filesize.text = 'filesize: ' + str(tag.filesize) + 'bytes'
                self.root.ids.t1year.text = 'year: ' +  str(tag.year)
               
                
                
                self.track_seconds = tag.duration
                self.track_seconds2 = tag.duration
              
                self.stage = tag.duration
                self.a = self.stage
            

                self.root.ids.track_seconds2.text = self.get_timer()
                self.sound.play()
                self.start_timer()
                if self.root.ids.volumes.text == "":
                    self.sound.volume = self.volume
                elif self.root.ids.volumes.text == "mute":
                    self.sound.volume = 0
                    
                if self.lops == "loop":
                    self.sound.loop = True
                   
        try:
            self.dialog.dismiss(force = True)
            self.dialog = None
        except:
            print ('Not Open')
            
    def stopaudio(self):
        

        self.custate = 'stop'
        self.process = 'end'
        self.process3 = 'end'
        self.process2 = 'start'
        self.action = "stop"
        self.action = "play"
        self.pauses = "play"
        try:
            tag = TinyTag.get(self.currentsong)
            self.track_seconds = tag.duration
            self.track_store = 0
            self.a = self.sound.length
            self.a2 = 0
            
            Clock.unschedule(self.set_time)
            
            self.sound.stop()
            
            self.root.ids.track_seconds1.text = self.states
        
        except:
            pass
        

    


    def volumeunmute(self):
        try:
            self.sound.volume = self.volume
            self.root.ids.valume.text = str(int((int(self.volume * 10)/10)*100)) + '%'

            self.root.ids.volumes.text = ""
        except:
            toast("No song")
        
    def volumemute(self):
        try:
            self.sound.volume = 0
            self.root.ids.valume.text =  '0%'

            self.root.ids.volumes.text = "mute"
            
        except:
            toast("No song")
        
        
    def pause(self):
        try:
            self.cuoostate = "pause"
            self.pauses = "pause"
            
            
            print (self.a, self.a2)
            Clock.unschedule(self.set_time)
            self.sound.stop()
            print (self.a, self.a2)
        
        except:
            toast("No song Inputted")



    def forward(self):
        try:
            tag = TinyTag.get(self.currentsong)
            print ('forward song')
            self.process = 'step'
            if self.a >= 0:
                self.a -= 10
                self.a2 += 10
                
                # @1 for continual forwarding self.track_seconds will be updated to  self.a
                # @2 for continual update self.track_store will be updated to self.a2
                
                print (self.a, self.stage)
                Clock.unschedule(self.set_time)
                
                # @1 and @2 shown below
        ##        self.track_seconds = self.a
        ##        self.track_store = self.a2
                
                self.sound.stop()
                self.sound.play()
                print ('house', self.a2)
                #self.sound.seek will be placed before self.start_timer2 for parallel sound update and timer update
                if self.sound.length < 0:
                    toast('Something wrong with song')
                    self.start_timer2(tag.duration, 0) 
                else:
                    self.sound.seek(self.a2)
                    self.start_timer2(self.a, self.a2)
                    
                if self.lops == "loop":
                    self.sound.loop = True
            
        except:
            toast("No song Inputted")


    def backward(self):
        try:
            print ('backward song')
            self.process3 = 'step'
            tag = TinyTag.get(self.currentsong)
            if self.a <= tag.duration:
                self.a += 10
                self.a2 -= 10

                # @1 for continual forwarding self.track_seconds will be updated to  self.a
                # @2 for continual update self.track_store will be updated to self.a2
                
                print (self.a, self.stage)
                Clock.unschedule(self.set_time)
                
                # @1 and @2 shown below
        ##        self.track_seconds = self.a
        ##        self.track_store = self.a2
                
                self.sound.stop()
                self.sound.play()
                
                #self.sound.seek will be placed before self.start_timer2 for parallel sound update and timer update
                if self.sound.length < 0:
                    toast('Something wrong with song')
                    self.start_timer2(tag.duration, 0) 
                else:
                    print ('working')
                    print (self.a2, tag.duration, type(self.a2), type(tag.duration))
                    if self.a >= tag.duration:
                        print ('exception')
                        self.start_timer2(tag.duration, 0)
                    else:
                        print ('execute')
                        self.sound.seek(self.a2)
                        self.start_timer2(self.a, self.a2) 

                if self.lops == "loop":
                    self.sound.loop = True
        
        except:
            toast("No song Inputted")
            
        
    def loopsong(self):
        if self.lops == "once":
            try:
                self.sound.loop = True
                self.root.ids.loops.text = "looped"
                
                self.lops = "loop"
            except:
                self.lops = "loop"
                self.root.ids.loops.text = "looped"
                
        elif self.lops == "loop":
            try:
                self.lops = "once"
                self.root.ids.loops.text = ""
                self.sound.loop = False
            except:
                self.lops = "once"
                self.root.ids.loops.text = ""
                
            
            
        

##    def volumemute(self, obj):
##
##        self.sound.loop = True

    def volumeup(self):
        try:
            if self.volume >= -0.1 and self.volume < 1:
                self.volume += 0.1
                self.sound.volume = self.volume
                print (self.volume)
                self.root.ids.valume.text = str(int((int(self.volume * 10)/10)*100)) + '%'

                self.root.ids.volumes.text = ""
                        
        except:
            toast("No song Inputted")

    def volumedown(self):
        try:
            if self.volume <= 1.1 and self.volume > 0:
                self.volume -= 0.1
                self.sound.volume = self.volume
                print (self.volume)
                self.root.ids.valume.text = str(int((int(self.volume * 10)/10)*100)) + '%'

                self.root.ids.volumes.text = ""
        
        except:
            toast("No song Inputted")
                
    
    def nexts(self):
        try:
            
            print ("next")
            leg = len(self.files)
            print (leg)
            print (self.files)
            print (len(self.files))
            print (self.currentsong2)
            print ("5")
            
            if '\\' in self.currentsong2:
                collector = ""
                r2 = len(self.currentsong2)

                for i in range(r2):
                    v = self.currentsong2[r2 - 1 - i]
                    collector += v
                    if v == "\\":
                        break

                songy = collector[::-1][1:]
                try:
                    if self.files.index(songy) <= leg-1:
                        if self.files.index(songy) == leg-1:
                            songy = self.files[0]
                            leg2 = self.files[self.files.index(songy)]
                            self.playaudio2(leg2)
                            print ('next 1', songy)
                        else:
                            if self.shuffles == "off":
                                leg2 = self.files[self.files.index(songy) + 1]
                                self.playaudio2(leg2)
                            elif self.shuffles == "shuffle":
                                print ('howling1')
                                if self.files.index(songy) <= 0 and leg == 5:
                                    leg2 = self.files[random.randrange(self.files.index(songy) + 4)]
                                    self.playaudio2(leg2)
                                    
                                    
                                elif self.files.index(songy) <= 0 and leg == 6:
                                    leg2 = self.files[random.randrange(self.files.index(songy) + 5)]
                                    self.playaudio2(leg2)
                                    
                                else:
                                    leg2 = self.files[random.randrange(self.files.index(songy))]
                                    self.playaudio2(leg2)
                                        
                except:
                    toast("Not in SongList")            
                    
            else:
                try:
                    if self.files.index(self.currentsong2) <= leg-1:
                        if self.files.index(self.currentsong2) == leg-1:
                            print ('first song')
                            self.currentsong2 = self.files[0]
                            leg2 = self.files[self.files.index(self.currentsong2)]
                            self.playaudio2(leg2)
                            print ('next 2', self.currentsong2)
                        else:
                            if self.shuffles == "off":
                                print (self.currentsong2)
                                leg2 = self.files[self.files.index(self.currentsong2) + 1]
                                self.playaudio2(leg2)
                            elif self.shuffles == "shuffle":
                                print ('howling1')
                                print (self.files.index(self.currentsong2))
                                print (leg)
                                

                                # if self.files.index(self.currentsong2) <= 0:
                                    # print ('worrrking')
                                    # if leg < 1:
                                        # leg2 = self.files[0]
                                        # self.playaudio2(leg2)
                                    # elif leg > 1:
                                        # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 1)]
                                        # self.playaudio2(leg2)
                                    # else:
                                        # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 1 )]
                                        # self.playaudio2(leg2)
                                    
                                # else:
                                    # print ('worrrking2')
                                    # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 1 )]
                                    # self.playaudio2(leg2)
                                    
                                print ('worrrking2')
                                if leg == 1:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                elif leg == 2:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg == 3:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg == 4:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                    
                                elif leg == 5:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg == 6:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg >= 7:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                
                
                except:
                    toast("Not in SongList")
          

            
                        
        except:
            toast("No song Inputted")
            
            
            
        


        
        
    def previouss(self):
        try:
            print ("previous")
            leg = len(self.files)
            print (leg)
            print (self.files)
            print (len(self.files))
            print (self.currentsong2)
            print ("6")
            
            if '\\' in self.currentsong2:
                collector = ""
                r2 = len(self.currentsong2)

                for i in range(r2):
                    v = self.currentsong2[r2 - 1 - i]
                    collector += v
                    if v == "\\":
                        break

                songy = collector[::-1][1:]
                try:
                    if self.files.index(songy) <= leg-1:
                        if self.files.index(songy) == leg-1:
                            songy = self.files[-1]
                            leg2 = self.files[self.files.index(songy)]
                            self.playaudio2(leg2)
                        else:
                            if self.shuffles == "off":
                                leg2 = self.files[self.files.index(songy) - 1]
                                self.playaudio2(leg2)
                            elif self.shuffles == "shuffle":
                                if self.files.index(songy) <= 0 and leg == 5:
                                    leg2 = self.files[random.randrange(self.files.index(songy) + 4)]
                                    self.playaudio2(leg2)
                                    
                                    
                                elif self.files.index(songy) <= 0 and leg == 6:
                                    leg2 = self.files[random.randrange(self.files.index(songy) + 5)]
                                    self.playaudio2(leg2)
                
                except:
                    toast("Not in SongList")
                        
                        
                    
            else:
                try:
                    if self.files.index(self.currentsong2) <= leg-1:
                        if self.files.index(self.currentsong2) == 0:
                            print ('last song')
                            self.currentsong2 = self.files[-1]
                            leg2 = self.files[self.files.index(self.currentsong2)]
                            self.playaudio2(leg2)
                            
                        else:
                            if self.shuffles == "off":
                                print ('previous go')
                                leg2 = self.files[self.files.index(self.currentsong2) - 1]
                                self.playaudio2(leg2)
                            elif self.shuffles == "shuffle":
                                # if self.files.index(self.currentsong2) <= 1:
                                    # print ('worrrking')
                                    # if leg < 1:
                                        # leg2 = self.files[0]
                                        # self.playaudio2(leg2)
                                    # elif leg > 1:
                                        # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 1)]
                                        # self.playaudio2(leg2)
                                    # else:
                                        # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 1 )]
                                        # self.playaudio2(leg2)
                                    
                                # else:
                                    # print ('worrrking2')
                                    # leg2 = self.files[random.randrange(self.files.index(self.currentsong2) + 1 )]
                                    # self.playaudio2(leg2)
                                    
                                
                                if leg == 1:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                elif leg == 2:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg == 3:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg == 4:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                    
                                elif leg == 5:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg == 6:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                                elif leg >= 7:
                                    leg2 = self.files[random.randrange(leg)]
                                    self.playaudio2(leg2)
                                    
                except:
                    toast("Not in SongList")
                                
        except:
            toast("No song Inputted") 
            
            
    def shuffling(self):
        if self.shuffles == "off":
            self.root.ids.shuffleds.text = "Shuffled"
            self.shuffles = "shuffle"
        elif self.shuffles == "shuffle":
            self.root.ids.shuffleds.text = ""
            self.shuffles = "off"
            
            
            
    def show_alert(self):
        try:
            if self.datail == "close":
                tag = TinyTag.get(self.currentsong)
                self.root.ids.t1album.text = 'album: ' + str(tag.album)
                self.root.ids.t1artist.text ='artist: ' + str(tag.artist) 
                self.root.ids.t1duration.text = 'duration: ' + str(self.get_timer2(tag.duration)) 
                self.root.ids.t1filesize.text = 'filesize: ' + str(tag.filesize) + 'bytes'
                self.root.ids.t1year.text = 'year: ' +  str(tag.year)
                        
                self.root.ids.t1album.color = (1,0,0,1)
                self.root.ids.t1artist.color = (1,0,0,1)
                self.root.ids.t1duration.color = (1,0,0,1)
                self.root.ids.t1filesize.color = (1,0,0,1)
                self.root.ids.t1year.color = (1,0,0,1)
                self.root.ids.detailss.height = 69
                self.datail = "open"
                
            elif self.datail == "open":
                self.root.ids.t1album.color = (1,0,1,0)
                self.root.ids.t1artist.color = (1,0,1,0)
                self.root.ids.t1duration.color = (1,0,1,0)
                self.root.ids.t1filesize.color = (1,0,1,0)
                self.root.ids.t1year.color = (1,0,1,0)
                
                self.root.ids.t1album.text = ''
                self.root.ids.t1artist.text =''
                self.root.ids.t1duration.text = '' 
                self.root.ids.t1filesize.text = ''
                self.root.ids.t1year.text = ''
                self.datail = "close"
                self.root.ids.detailss.height = 0
        except: 
            toast("No song inputted")
        
        
            
    def show_opendill(self):
        if True:
            content = LoadDialog(load=self.load22, cancel=self.dismiss_popup)
            self._popup = Popup(title="Load file", content=content,
                                size_hint=(0.9, 0.9))
            self._popup.open()
##        except:
##            print ('cool')
        
    def load22(self, path, filename):
        try:
            if filename[0].endswith('.mp3') or filename[0].endswith('.wav') or filename[0].endswith('.oog'):
                self.playaudio3(str(filename[0]))
                self.dismiss_popup()
                
            else:
                toast('File format not supportted')
                
        except:
            toast('Nothing selected')

    def dismiss_popup(self):
        self._popup.dismiss()


    def show_playlist(self):
        files = ['the gentle breeze.mp3', 'wild heart.mp3']
        loop = len(files)
        self.root.ids.content.clear_widgets(self.root.ids.content.children[:])
            
        for i in range(loop):
            
            # print (r'C:\Users\user\Music\music' + '\\' + files[i])
            # if filename[0].endswith('.mp3') or filename[0].endswith('.wav') or filename[0].endswith('.aac') or filename[0].endswith('.oog') or filename[0].endswith('.wma'):
            self.root.ids.content.add_widget(
                Songlist(
                    musicname = files[i]
                )
            )
        
        
    def playaudio3(self, song):
        self.imgfiles = []
        self.imgfiles2 = []
        for dirpath1, dirnames1, filenames1 in os.walk(str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)'): 
            self.imgfiles2 = filenames1

        for i in range(len(self.imgfiles2)):
            if self.imgfiles2[i].endswith('.jpg') or self.imgfiles2[i].endswith('.png'):
                self.imgfiles.append(self.imgfiles2[i])

        print('ww', self.imgfiles)

        
        self.root.ids.pacture.source = str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles)
        print (str(Path.home()) + '\\'   + r'Music' + '\\' + 'CreateSphereNairaImage(CSN Player)' + '\\' + random.choice(self.imgfiles))


        
        self.states = "00:00"
        self.action = "start"
        self.process = "end"
        self.process3 = "end"
        self.pauses = "play"
        
        self.track_store = 0
        self.a2 = 0
        
        
        self.process2 = "start"
        self.currentsong2 = song
        
        #color
            
        self.root.ids.t1album.color = (1,0,1,0)
        self.root.ids.t1artist.color = (1,0,1,0)
        self.root.ids.t1duration.color = (1,0,1,0)
        self.root.ids.t1filesize.color = (1,0,1,0)
        self.root.ids.t1year.color = (1,0,1,0)
        
        #color
        
       
        try:
            self.stopaudio()
            self.currentsong = song
            
            self.sound = SoundLoader.load(song)
            tag = TinyTag.get(song)

            self.root.ids.detailss.height = 0
           
            self.root.ids.t1album.text = 'album: ' + str(tag.album)
            self.root.ids.t1artist.text ='artist: ' + str(tag.artist) 
            self.root.ids.t1duration.text = 'duration: ' + str(self.get_timer2(tag.duration)) 
            self.root.ids.t1filesize.text = 'filesize: ' + str(tag.filesize) + 'bytes'
            self.root.ids.t1year.text = 'year: ' +  str(tag.year)
            # self.root.ids.name_track.text = song
            if '\\' in song:
                collector = ""
                r2 = len(song)

                for i in range(r2):
                    v = song[r2 - 1 - i]
                    collector += v
                    if v == "\\":
                        break

                songy = collector[::-1][1:]
                self.root.ids.name_track.text = songy
                
            self.track_seconds = tag.duration
            self.track_seconds2 = tag.duration
         
            self.stage = tag.duration
            self.a = self.stage
        
            self.root.ids.track_seconds2.text = self.get_timer()
            self.sound.play()
            self.start_timer()
            self.sound.volume = self.volume
            if self.lops == "loop":
                self.sound.loop = True
                    
                
           
        except:
            self.currentsong = song
            self.sound = SoundLoader.load(song)
            if '\\' in song:
                collector = ""
                r2 = len(song)

                for i in range(r2):
                    v = song[r2 - 1 - i]
                    collector += v
                    if v == "\\":
                        break

                songy = collector[::-1][1:]
                self.root.ids.name_track.text = songy
            
            tag = TinyTag.get(song)

            
           
            self.root.ids.t1album.text = 'album: ' + str(tag.album)
            self.root.ids.t1artist.text ='artist: ' + str(tag.artist) 
            self.root.ids.t1duration.text = 'duration: ' + str(self.get_timer2(tag.duration)) 
            self.root.ids.t1filesize.text = 'filesize: ' + str(tag.filesize) + 'bytes'
            self.root.ids.t1year.text = 'year: ' +  str(tag.year)
           
            
            
            self.track_seconds = tag.duration
            self.track_seconds2 = tag.duration
          
            self.stage = tag.duration
            self.a = self.stage
        

            self.root.ids.track_seconds2.text = self.get_timer()
            self.sound.play()
            self.start_timer()
            self.sound.volume = self.volume
            if self.lops == "loop":
                self.sound.loop = True

    def show_load(self):
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager = self.exit_manager,
            select_path = self.select_path,
            
            )
        self.file_manager.show('c:\\')
        self.manager_open = True


    def select_path(self, path):
        if path.endswith('.mp3') or path.endswith('.wav') or path.endswith('.oog'):
            self.playaudio3(str(path))
            
            self.exit_manager()
##            toast(path)
                
        else:
            toast('File format not supportted')
        

       
        
                
       

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
        
        
    def mmmmuting(self):
        if self.cuoostatemute == 'unmuted':
            self.cuoostatemute = 'muted'
            self.volumemute()
        
        elif self.cuoostatemute == 'muted':
            self.cuoostatemute = 'unmuted'
            self.volumeunmute()
            
            
    def lllloop(self):
        if self.cuoostateloop == 'norepeat':
            self.cuoostateloop = 'repeat'
            self.loopsong()
        
        elif self.cuoostateloop == 'repeat':
            self.cuoostateloop = 'norepeat'
            self.loopsong()
            
    
    def sssshuffle(self):
        if self.cuoostateshuffle == 'noshuffle':
            self.cuoostateshuffle = 'shuffle'
            self.shuffling()
        
        elif self.cuoostateshuffle == 'shuffle':
            self.cuoostateshuffle = 'noshuffle'
            self.shuffling()
            
    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Music Info",
                type="simple",
                items=[
                    Item(text= self.root.ids.t1album.text),
                    Item(text= self.root.ids.t1artist.text),
                    Item(text= self.root.ids.t1duration.text),
                    Item(text= self.root.ids.t1filesize.text),
                    Item(text= self.root.ids.t1year.text),
                ], buttons = [
                    MDFlatButton(text="CANCEL", on_release=self.dialog_close),
                ],
            )
            
        self.dialog.open()
        
        
    def dialog_close(self, *args):
        self.dialog.dismiss(force = True)
        self.dialog = None
        
    def markermain(self):
        self.root.ids.screen_manager.current = 'Home screen'





if __name__ == "__main__":
    MusicApp().run()



