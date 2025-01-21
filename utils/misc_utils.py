from kivy.uix.popup import Popup
from kivy.uix.label import Label

def error_popup( message):
    popup = Popup(
        title='Error',
        content=Label(text=message),
        size_hint=(None, None),
        size=(300, 200)
    )
    popup.open()