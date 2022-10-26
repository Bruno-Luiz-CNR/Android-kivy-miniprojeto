from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from pytube import YouTube, Playlist
from kivymd.app import MDApp


Window.size = (300, 580)

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class BruTha(MDApp):
    def build(self):
        self.icon = "play.ico"
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.accent_palette = 'DeepOrange'
        return Builder.load_file("main.kv")
    def baixar(self):
        condicao = (self.root.ids.tx.text)
        if condicao == '':
            erro = 'Insira a URL !'
            self.root.ids.box.text = (erro)
        else:
            YouTube(self.root.ids.tx.text).streams.get_highest_resolution().download('~/Downloads')
            nome = 'Concluido !!'
            self.root.ids.box.text = (nome)

    def downloadaudio(self):
        condicao = (self.root.ids.tx.text)
        if condicao == '':
            erro = 'Insira a URL !'
            self.root.ids.box.text = (erro)
        else:
            YouTube(self.root.ids.tx.text).streams.get_audio_only().download('~/Downloads')
            nome = 'Concluido !!'
            self.root.ids.box.text = (nome)

    def varios(self):
        condicao = (self.root.ids.tx2.text)
        if condicao == '':
            erro = 'Insira a URL !'
            self.root.ids.box2.text = (erro)
        else:
            url = self.root.ids.tx2.text
            get_video = Playlist(url)
            for video in get_video.videos:
                video.streams.get_highest_resolution().download('~/Downloads')
                nome = 'Concluido !!'
                self.root.ids.box2.text = (nome)

    def variosaudios(self):
        condicao = self.root.ids.tx2.text
        if condicao == '':
            erro = 'Insira a URL !'
            self.root.ids.box2.text = (erro)
        else:
            url = self.root.ids.tx2.text
            audio = Playlist(url)
            for audios in audio.videos:
                audios.streams.get_audio_only().download('~/Downloads')
                nome = 'Concluido !!'
                self.root.ids.box2.text = (nome)



if __name__ == "__main__":
    BruTha().run()