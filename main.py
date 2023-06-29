from subprocess import run

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp


def download_from_url(url):
    run(f'yt-dlp.exe {url}', shell=True)


class MainScreen(Screen):
    def download(self):
        url = kv.screens[0].text_input.text
        print(f'Downloading the video located at the URL {url} ...')
        download_from_url(url)

class MyScreenManager(ScreenManager):
    pass

kv = Builder.load_file('kv.kv')

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        # self.theme_cls.primary_palette = 'Yellow'
        return kv

if __name__ == "__main__":
    MyApp().run()
    # download('https://fb.watch/ltP8OraWn4/')
