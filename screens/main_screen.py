from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
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
    sort_by = StringProperty(None)
    sort_order = BooleanProperty(True)  # True for asc, False for desc
    def on_enter(self):
        self.load_notes()
    
        
    def load_notes(self, sort_by=None):
        notes_container = self.ids.notes_container
        notes_container.clear_widgets()

        notes = notes_utils.get_notes_for_user(self.current_user["uuid"])

        if sort_by:
            self.sort_by = sort_by

        if self.sort_by == "name":
            notes = sorted(notes, key=lambda note: note["note"].lower(), reverse=not self.sort_order)
        elif self.sort_by == "date":
            notes = sorted(notes, key=lambda note: note["created_at"], reverse=not self.sort_order)  # Assuming notes have a "date" attribute

        for note in notes:
            note_widget = NoteWidget(
                note,
                delete_callback=self.delete_note,
                edit_callback=self.edit_note
            )
            notes_container.add_widget(note_widget)


    def update_welcome_text(self):
        self.welcome_text = f"{self.current_user["username"]}'s notes"

    def delete_note(self, note_uuid):
        notes_utils.delete_note_for_user(self.current_user["uuid"], note_uuid)
        self.load_notes()
        pass
    
    def new_note(self):
        screen = self.manager.get_screen('edit_create_note')
        screen.set_initial_values("", "Personal", "#000000")
        screen.note_uuid = str(uuid4())
        screen.save_callback = self.save_callback
        self.manager.current = 'edit_create_note'
        pass

    def edit_note(self, note):
        screen = self.manager.get_screen('edit_create_note')
        screen.set_initial_values(note["note"], note["category"], note["color"])
        screen.note_uuid = note["uuid"]
        screen.save_callback = self.save_callback
        self.manager.current = 'edit_create_note'
        pass

    def save_callback(self, note_uuid, note_text, category, color):
        notes_utils.edit_or_create_note(self.current_user["uuid"], note_uuid, note_text, color, category)
        print(f"Note saved: {note_text}")
        self.load_notes()
        self.manager.current = 'main'
        pass

    def name_sort(self):
        if self.sort_by == "name":
            self.sort_order = not self.sort_order
        else:
            self.sort_order = True

        self.ids.name_icon.source = "assets/up.png" if self.sort_order else "assets/down.png"
        self.load_notes(sort_by="name")

    def date_sort(self):
        if self.sort_by == "date":
            self.sort_order = not self.sort_order
        else:
            self.sort_order = True
        
        self.ids.date_icon.source = "assets/up.png" if self.sort_order else "assets/down.png"
        self.load_notes(sort_by="date")

    def logout_button(self):
        self.current_user = {}
        self.welcome_text = "Welcome!"
        self.manager.current = 'login'
