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

    def __init__(self, note_uuid, note_text, note_color, delete_callback, edit_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.note_uuid = note_uuid
        self.note_text = note_text
        self.note_color = note_color
        self.delete_callback = delete_callback
        self.edit_callback = edit_callback

    def on_delete(self):
        """Handle the delete button click."""
        self.delete_callback(self.note_uuid)

    def on_edit(self):
        """Handle the edit button click."""
        self.show_edit_popup()

    def show_edit_popup(self):
        """Show a popup for editing the note."""
        content = FloatLayout()

        note_input = TextInput(
            text=self.note_text,
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.6}
        )
        save_button = Button(
            text="Save",
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            on_press=lambda x: self.save_edited_note(note_input.text)
        )

        content.add_widget(note_input)
        content.add_widget(save_button)

        self.popup = Popup(
            title="Edit Note",
            content=content,
            size_hint=(0.6, 0.4),
            auto_dismiss=True
        )
        self.popup.open()

    def save_edited_note(self, new_text):
        """Save the edited note text."""
        self.note_text = new_text
        self.ids.note_label.text = new_text
        self.edit_callback(self.note_uuid, new_text)
        self.popup.dismiss()

    def hex_to_rgb(self, hex_color):
        """Convert hex color string to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        return r, g, b
