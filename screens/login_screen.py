from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from utils import user_utils
from utils.misc_utils import error_popup

class LoginWindow(Screen):
    user = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def verify_user(self, username, password):
        try:
            row = user_utils.get_user(username)
            if row is not None and row['password'] == password:
                self.user = row
                return True
            return False
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return False

    def login_button(self):
        if user_utils.check_password(self.username.text, self.password.text):
            self.user = user_utils.get_user(self.username.text)
            main_screen = self.manager.get_screen('main')
            print(f"Current user: {self.user}")
            main_screen.current_user = self.user
            main_screen.update_welcome_text()
            self.username.text = ''
            self.password.text = ''
            self.manager.current = 'main'
        else:
            error_popup('Login failed!')
            print("Login failed!")

    def register_button(self):
        settings_screen = self.manager.get_screen('settings')
        settings_screen.register_mode = True
        self.manager.current = 'settings'
        pass