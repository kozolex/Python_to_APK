import kivy
import sys
print("python:")
print(sys.version)
print("kivy:")
print(kivy.__version__)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        return MyBoxLayout()

class MyBoxLayout(BoxLayout):
    def on_button_click(self):
        user_input = self.ids.text_input.text
        self.ids.output_label.text = f'Wprowadzono: {user_input}'

if __name__ == '__main__':
    MyApp().run()
