from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.username = TextInput(hint_text='Username')
        self.add_widget(self.username)
        self.face_image = Button(text='Capture Face')
        self.face_image.bind(on_press=self.capture_face)
        self.add_widget(self.face_image)
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

    def capture_face(self, instance):
        # Capture face image code here
        pass

    def login(self, instance):
        data = {'username': self.username.text}
        files = {'face_image': open('path_to_face_image', 'rb')}
        response = requests.post('http://localhost:5000/login', data=data, files=files)
        print(response.json())

class MobileApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MobileApp().run()
