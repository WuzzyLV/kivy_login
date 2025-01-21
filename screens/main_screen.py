from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import csv
from utils import notes_utils
from uuid import uuid4
from widgets.note_widget import NoteWidget

class MainWindow(Screen):
    # 
    current_user = ObjectProperty(None)
    welcome_text = StringProperty("Welcome!")

    def on_enter(self):
        self.load_notes()
        
    def load_notes(self):
        notes_container = self.ids.notes_container
        notes_container.clear_widgets()

        notes = notes_utils.get_notes_for_user(self.current_user["uuid"])
        
        for note in notes:
            note_widget = NoteWidget(
                note,
                delete_callback=self.delete_note,
                edit_callback=self.edit_note
            )
            notes_container.add_widget(note_widget)


    def update_welcome_text(self):
        self.welcome_text = f"Hello, {self.current_user["username"]}!"

    def delete_note(self, note_uuid):
        print(f"Deleting note with UUID: {note_uuid}")
        pass
    def edit_note(self, note):
        screen = self.manager.get_screen('edit_create_note')
        screen.set_initial_values(note["note"], note["category"], note["color"])
        screen.note_uuid = note["uuid"]
        screen.save_callback = self.save_callback
        self.manager.current = 'edit_create_note'
        pass

    def save_callback(self, note_uuid, note_text, category, color):
        print(f"Saving note with UUID: {note_uuid}")
        print(f"Note text: {note_text}")
        pass

    def logout_button(self):
        self.current_user = {}
        self.welcome_text = "Welcome!"
        self.manager.current = 'login'
