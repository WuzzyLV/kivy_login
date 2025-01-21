from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from utils import user_utils

class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def verify_user(self, username, password):
        try:
            row = user_utils.get_user(username)
            return row is not None and row['password'] == password
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return False

    def login_button(self):
        if self.verify_user(self.username.text, self.password.text):
            print("Login successful!")
            main_screen = self.manager.get_screen('main')
            main_screen.current_user = self.username.text
            main_screen.update_welcome_text()
            self.username.text = ''
            self.password.text = ''
            self.manager.current = 'main'
        else:
            print("Login failed!")
