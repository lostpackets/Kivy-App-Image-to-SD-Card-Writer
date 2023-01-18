# from kivy.uix.boxlayout import BoxLayout
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# import shutil
# import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import shutil
import os

class ISO_Writer(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        self.iso_path = TextInput(text='/path/to/image.iso', multiline=False)
        self.sd_card = TextInput(text='/path/to/sdcard', multiline=False)
        self.status = Label(text='Enter the path of ISO file and SD card')
        self.write_button = Button(text='Write ISO', on_press=self.write_iso)
        root.add_widget(self.iso_path)
        root.add_widget(self.sd_card)
        root.add_widget(self.status)
        root.add_widget(self.write_button)
        Clock.schedule_interval(self.update, 1/60)
        return root

    def update(self, dt):
        pass

    def write_iso(self, instance):
        iso_path = self.iso_path.text
        sd_card = self.sd_card.text

        # Check if the ISO file and SD card exist
        if not os.path.exists(iso_path):
            self.status.text = "Error: ISO file not found."
            return
        if not os.path.exists(sd_card):
            self.status.text = "Error: SD card not found."
            return

        # Unmount the SD card
        if os.name == 'nt':
            os.system(f"dismount {sd_card}")
        else:
            os.system(f"umount {sd_card}")

        #

        # Write the ISO image to the SD card
        try:
            with open(iso_path, 'rb') as fsrc:
                with open(sd_card, 'wb') as fdst:
                    shutil.copyfileobj(fsrc, fdst, length=1024*1024*1024)
            self.status.text = "ISO image written to SD card successfully."
        except Exception as e:
            self.status.text = "Error writing ISO image to SD card:" + str(e)

if __name__ == '__main__':
    ISO_Writer().run()

# class ISO_Writer(App):
#     def build(self):
#         root = BoxLayout(orientation='vertical')
#         self.iso_path = TextInput(text='/path/to/image.iso', multiline=False)
#         self.sd_card = TextInput(text='/path/to/sdcard', multiline=False)
#         self.status = Label(text='Enter the path of ISO file and SD card')
#         self.write_button = Button(text='Write ISO', on_press=self.write_iso)
#         root.add_widget(self.iso_path)
#         root.add_widget(self.sd_card)
#         root.add_widget(self.status)
#         root.add_widget(self.write_button)
#         return root
