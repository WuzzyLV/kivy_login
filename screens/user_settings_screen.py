from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from utils import user_utils
from utils.misc_utils import error_popup
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_file('screens/user_settings_screen.kv')

class UserSettingsScreen(Screen):
    current_user = ObjectProperty(None)

    def on_enter(self):
        self.ids.username_input.text = self.current_user['username']
        self.ids.password_input.text = self.current_user['password']
    def save_settings(self):
        new_username = self.ids.username_input.text
        new_password = self.ids.password_input.text
        if not new_username or not new_password:
            error_popup('Username and password cannot be empty.')
            self.on_enter()
            return

        if new_username != self.current_user['username']:
            existing_user = user_utils.get_user(self.current_user['username'])
            if existing_user:
                error_popup('User with this username already exists.')
                self.on_enter()
                return
            user_utils.change_username(self.current_user['uuid'], new_username)


        user_utils.change_password(self.current_user['uuid'], new_password)
        
        # Go back to the previous screen
        self.manager.current = 'main'

    def go_back(self):
        self.manager.current = 'main'