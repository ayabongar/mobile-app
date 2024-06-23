from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests

class DriverScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(DriverScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.name = TextInput(hint_text='Name')
        self.add_widget(self.name)
        self.vehicle = TextInput(hint_text='Vehicle')
        self.add_widget(self.vehicle)
        self.register_button = Button(text='Register as Driver')
        self.register_button.bind(on_press=self.register_driver)
        self.add_widget(self.register_button)
        self.status = TextInput(hint_text='Status', readonly=True)
        self.add_widget(self.status)

    def register_driver(self, instance):
        data = {'name': self.name.text, 'vehicle': self.vehicle.text}
        response = requests.post('http://localhost:5000/register_driver', data=data)
        self.status.text = response.json().get('message')

class DriverApp(App):
    def build(self):
        return DriverScreen()

if __name__ == '__main__':
    DriverApp().run()
