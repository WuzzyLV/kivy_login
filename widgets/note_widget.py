from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import StringProperty


# Load the KV file for the layout
Builder.load_file('widgets/note_widget.kv')

class NoteWidget(BoxLayout):
    note_text = StringProperty("")
    note_color = StringProperty("#FFFFFF")

    def __init__(self, note, delete_callback, edit_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.note = note
        self.note_uuid = note["uuid"]
        self.note_text = note["note"]
        self.note_color = note["color"]
        self.created_at = note["created_at"]
        self.category = note["category"]
        self.delete_callback = delete_callback
        self.edit_callback = edit_callback
        self.ids.note_image.source = f"assets/{self.category.lower()}.png"

    def on_delete(self):
        """Handle the delete button click."""
        self.delete_callback(self.note_uuid)

    def on_edit(self):
        """Handle the edit button click."""
        self.edit_callback(self.note )

    def save_edited_note(self, new_text):
        """Save the edited note text."""
        self.note_text = new_text
        self.ids.note_label.text = new_text
        self.edit_callback(self.note_uuid, new_text)

    def hex_to_rgb(self, hex_color):
        """Convert hex color string to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        return r, g, b
