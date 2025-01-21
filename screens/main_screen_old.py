from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import csv

class MainWindow(Screen):
    current_user = StringProperty("")
    welcome_text = StringProperty("Welcome!")

    def update_welcome_text(self):
        self.welcome_text = f"Hello, {self.current_user}!"

    def change_password(self):
        try:
            new_password = self.ids.new_password.text
            if not new_password:
                self.show_popup("Error", "Please enter a new password")
                return
            users_data = []
            with open('users.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    if row['username'] == self.current_user:
                        row['password'] = new_password
                    users_data.append(row)
                self.ids.new_password.text = ""
            with open('users.csv', 'w', encoding='utf-8', newline='') as file:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                writer.writerows(users_data)
            self.show_popup("Success", "Password changed successfully!")
        except Exception as e:
            self.show_popup("Error", f"Failed to change password: {str(e)}")

    def show_popup(self, title, text):
        popup = Popup(title=title,
                      content=Label(text=text),
                      size_hint=(None, None),
                      size=(400, 200))
        popup.open()

    def logout_button(self):
        self.current_user = ""
        self.welcome_text = "Welcome!"
        self.manager.current = 'login'
