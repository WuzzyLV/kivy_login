from kivy.uix.image import Image
from kivy.properties import ObjectProperty

class ClickableImage(Image):
    callback = ObjectProperty(None) 
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.callback: 
                self.callback()
            else:
                print("Image clicked, but no callback set!")
            return True
        return super().on_touch_down(touch)
