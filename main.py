from kivy.app import App
#kivymd
from kivymd.app import MDApp

from kivy.core.window import Window
from kivy.utils import platform
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from screens import UserSettingsScreen, EditCreateNoteScreen

Config.set('input', 'mouse', 'mouse, multitouch_on_demand')
Config.set('kivy', 'mouse cursor enable', 1)
Config.write()

class WindowManager(ScreenManager):
    pass

class LoginApp(MDApp):
    def build(self):
        if platform not in ('android', 'ios'):
            Window.size = (400, 600)
        if platform in ('android', 'ios'):
            Window.fullscreen = 'auto'
        manager = WindowManager()
        manager.add_widget(EditCreateNoteScreen(name='edit_create_note'))
        manager.add_widget(UserSettingsScreen(name='settings'))
        return manager
    


if __name__ == '__main__':
    LoginApp().run()
