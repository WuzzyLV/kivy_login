from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.pickers import MDColorPicker
from utils.misc_utils import error_popup

Builder.load_file('screens/edit_create_note_screen.kv')

class EditCreateNoteScreen(Screen):
    note_uuid = StringProperty("")
    note_text = ObjectProperty(None)
    category = ObjectProperty(None)
    color = ObjectProperty(None)
    save_callback = ObjectProperty(None)

    def set_initial_values(self, note_text="", category="", color="#FFFFFF"):
        self.ids.note_input.text = note_text
        self.ids.color_picker.text = color
        self.ids.category_spinner.text = category


    def change_color(self):
        color = self.ids.color_picker.text
        if not color.startswith('#') or len(color) != 7:
            return
        self.color = color
        self.ids.color_box.canvas.before.children[0].rgba = self.hex_to_rgb(color)

    def validate_color_input(self, instance, value):
        if not value.startswith('#'):
            value = '#' + value
        if len(value) > 7:
            value = value[:7]
        self.ids.color_picker.text = value
        self.change_color()

    def open_category_menu(self):
        self.ids.category_dropdown.open()

    def save_note(self):
        note_text = self.ids.note_input.text
        category = self.ids.category_spinner.text
        color = self.color

        if not note_text or not category or not color:
            error_popup("All fields are required!")
            return
        self.save_callback(self.note_uuid, note_text, category, color)
    
    def close(self):
        self.manager.current = 'main'

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
        return r, g, b, 1

    def rgb_to_hex(self, rgb_color):
        return '#' + ''.join(f'{int(c * 255):02x}' for c in rgb_color)
