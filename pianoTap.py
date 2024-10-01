'''
Created on 2024/09/11

@author: ナズ
'''
from kivy.app import App
from kivy.core.audio import SoundLoader 


class PianoTapApp(App):
    def build(self):
        self.sounds = {
            'C': SoundLoader.load('key08.mp3'),
            'D': SoundLoader.load('key10.mp3'),
            'E': SoundLoader.load('key12.mp3'),
            'F': SoundLoader.load('key13.mp3'),
            'G': SoundLoader.load('key15.mp3'),
            'A': SoundLoader.load('key17.mp3'),
            'B': SoundLoader.load('key19.mp3'),
            'C2': SoundLoader.load('key20.mp3')
        }
         
        return self.root
    
    def play_sound(self, letter):
        self.sounds[letter].play()

app = PianoTapApp()
app.run()

#An app where u can play sounds by pressing the buttons. Clicking a button for example mght make the sound of the note C