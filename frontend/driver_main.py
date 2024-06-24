from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
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
        self.status = Label(text='Status')
        self.add_widget(self.status)
        self.accept_ride_button = Button(text='Accept Ride')
        self.accept_ride_button.bind(on_press=self.accept_ride)
        self.add_widget(self.accept_ride_button)
        self.ride_info = Label(text='No ride requests yet.')
        self.add_widget(self.ride_info)

    def register_driver(self, instance):
        data = {'name': self.name.text, 'vehicle': self.vehicle.text}
        response = requests.post('http://localhost:5000/register_driver', data=data)
        self.status.text = response.json().get('message')

    def accept_ride(self, instance):
        response = requests.get('http://localhost:5000/get_ride_request')  # Implement this route
        ride_request = response.json()
        if ride_request:
            self.ride_info.text = f"Ride request from {ride_request['username']} to {ride_request['destination']}.">
        else:
            self.ride_info.text = 'No ride requests yet.'

class DriverApp(App):
    def build(self):
        return DriverScreen()

if __name__ == '__main__':
    DriverApp().run()

