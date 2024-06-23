from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import requests
import cv2

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.username = TextInput(hint_text='Username')
        self.add_widget(self.username)
        self.face_image = Image()
        self.add_widget(self.face_image)
        self.capture_button = Button(text='Capture Face')
        self.capture_button.bind(on_press=self.capture_face)
        self.add_widget(self.capture_button)
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

    def capture_face(self, instance):
        # Capture face image code here
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imwrite('face_image.png', frame)
            self.face_image.source = 'face_image.png'
        cam.release()
        cv2.destroyAllWindows()

    def login(self, instance):
        data = {'username': self.username.text}
        files = {'face_image': open('face_image.png', 'rb')}
        response = requests.post('http://localhost:5000/login', data=data, files=files)
        print(response.json())

class RequestRideScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(RequestRideScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.username = TextInput(hint_text='Username')
        self.add_widget(self.username)
        self.destination = TextInput(hint_text='Destination')
        self.add_widget(self.destination)
        self.request_button = Button(text='Request Ride')
        self.request_button.bind(on_press=self.request_ride)
        self.add_widget(self.request_button)

    def request_ride(self, instance):
        data = {'username': self.username.text, 'destination': self.destination.text}
        response = requests.post('http://localhost:5000/request_ride', data=data)
        print(response.json())

class MobileApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(LoginScreen())
        main_layout.add_widget(RequestRideScreen())
        return main_layout

if __name__ == '__main__':
    MobileApp().run()

