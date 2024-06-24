from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import requests
import cv2

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.name = 'login'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.username = TextInput(hint_text='Username', size_hint_y=None, height=40)
        layout.add_widget(self.username)
        self.password = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40)
        layout.add_widget(self.password)
        self.face_image = Button(text='Capture Face', size_hint_y=None, height=50)
        self.face_image.bind(on_press=self.capture_face)
        layout.add_widget(self.face_image)
        self.login_button = Button(text='Login', size_hint_y=None, height=50)
        self.login_button.bind(on_press=self.login)
        layout.add_widget(self.login_button)
        self.status = Label(text='', size_hint_y=None, height=40)
        layout.add_widget(self.status)
        self.add_widget(layout)

    def capture_face(self, instance):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imwrite('face_image.png', frame)
        cam.release()
        cv2.destroyAllWindows()

    def login(self, instance):
        data = {'username': self.username.text, 'password': self.password.text}
        files = {'face_image': open('face_image.png', 'rb')}
        response = requests.post('http://localhost:5000/login', data=data, files=files)
        if response.status_code == 200:
            self.manager.current = 'request_ride'
        else:
            self.status.text = 'Login failed!'

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.name = 'register'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.username = TextInput(hint_text='Username', size_hint_y=None, height=40)
        layout.add_widget(self.username)
        self.password = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40)
        layout.add_widget(self.password)
        self.face_image = Button(text='Capture Face', size_hint_y=None, height=50)
        self.face_image.bind(on_press=self.capture_face)
        layout.add_widget(self.face_image)
        self.register_button = Button(text='Register', size_hint_y=None, height=50)
        self.register_button.bind(on_press=self.register)
        layout.add_widget(self.register_button)
        self.status = Label(text='', size_hint_y=None, height=40)
        layout.add_widget(self.status)
        self.add_widget(layout)

    def capture_face(self, instance):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imwrite('face_image.png', frame)
        cam.release()
        cv2.destroyAllWindows()

    def register(self, instance):
        data = {'username': self.username.text, 'password': self.password.text}
        files = {'face_image': open('face_image.png', 'rb')}
        response = requests.post('http://localhost:5000/register', data=data, files=files)
        if response.status_code == 201:
            self.status.text = 'Registration successful!'
        else:
            self.status.text = 'Registration failed!'

class RequestRideScreen(Screen):
    def __init__(self, **kwargs):
        super(RequestRideScreen, self).__init__(**kwargs)
        self.name = 'request_ride'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.username = TextInput(hint_text='Username', size_hint_y=None, height=40)
        layout.add_widget(self.username)
        self.destination = TextInput(hint_text='Destination', size_hint_y=None, height=40)
        layout.add_widget(self.destination)
        self.request_button = Button(text='Request Ride', size_hint_y=None, height=50)
        self.request_button.bind(on_press=self.request_ride)
        layout.add_widget(self.request_button)
        self.status = Label(text='', size_hint_y=None, height=40)
        layout.add_widget(self.status)
        self.add_widget(layout)

    def request_ride(self, instance):
        data = {'username': self.username.text, 'destination': self.destination.text}
        response = requests.post('http://localhost:5000/request_ride', data=data)
        self.status.text = response.json().get('message')

class MobileApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(RequestRideScreen())
        return sm

if __name__ == '__main__':
    MobileApp().run()

