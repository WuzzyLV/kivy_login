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
    register_mode = ObjectProperty(False)

    def on_enter(self):
        if not self.register_mode:
            self.ids.username_input.text = self.current_user['username']
            self.ids.password_input.text = self.current_user['password']
        else:
            self.ids.username_input.text = ''
            self.ids.password_input.text = ''
    def save_settings(self):
        new_username = self.ids.username_input.text
        new_password = self.ids.password_input.text
        if self.register_mode:
            self.register_logic(new_username, new_password)
            return
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

    def register_logic(self, username, password):
        if not username or not password:
            error_popup('Username and password cannot be empty.')
            return
        try:
            try:
                user_utils.create_user(username, password)
            except ValueError as e:
                error_popup(f'User with this username already exists')
                return
            self.manager.current = 'login'
        except Exception as e:
            error_popup(f'Error creating user: {e}')

    def go_back(self):
        if self.register_mode:
            self.manager.current = 'login'
        else:
            self.manager.current = 'main'