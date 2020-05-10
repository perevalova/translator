from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.config import Config

from googletrans import Translator

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '100')


class TranslateWindow(Screen):
    lg_from = ObjectProperty(None)
    lg_to = StringProperty('')

    def translate(self, *args):
        input_text = self.ids.lg_from.text
        translator = Translator()
        result = translator.translate(input_text, dest='uk')
        self.ids.lg_to.text = result.text


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("Translator.kv")

sm = WindowManager()

screens = [TranslateWindow(name="translator")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "translator"

class TranslatorApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    TranslatorApp().run()
