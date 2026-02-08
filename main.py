from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class HunterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        layout.add_widget(Label(text="My Hunter App - V1", font_size='20sp', size_hint_y=None, height=50))
        
        # Input URL/Username
        self.target_input = TextInput(hint_text="Masukkan Target (URL atau Username)", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.target_input)
        
        # Tombol Cek SQLi Dasar
        btn_sqli = Button(text="Cek Kerentanan SQLi", background_color=(0, 0.7, 0, 1))
        btn_sqli.bind(on_press=self.cek_sqli)
        layout.add_widget(btn_sqli)
        
        # Tombol Sherlock (OSINT)
        btn_osint = Button(text="Cari Jejak Digital (OSINT)", background_color=(0, 0, 0.7, 1))
        btn_osint.bind(on_press=self.cek_osint)
        layout.add_widget(btn_osint)
        
        # Area Log/Hasil
        self.result_label = Label(text="Hasil akan muncul di sini...", halign="center", valign="middle")
        self.result_label.bind(size=self.result_label.setter('text_size'))
        layout.add_widget(self.result_label)
        
        return layout

        def cek_sqli(self, instance):
        target = self.target_input.text
        if target:
            # Perintah yang bisa langsung kamu pakai di Termux
            command = f"sqlmap -u '{target}' --batch --dbs"
            self.result_label.text = f"SALIN PERINTAH INI KE TERMUX:\n\n{command}"
        else:
            self.result_label.text = "Error: Masukkan URL target dulu!"

    def cek_osint(self, instance):
        target = self.target_input.text
        if target:
            # Perintah Sherlock untuk Termux
            command = f"python3 ~/sherlock/sherlock_project {target}"
            self.result_label.text = f"SALIN PERINTAH INI KE TERMUX:\n\n{command}"
        else:
            self.result_label.text = "Error: Masukkan Username dulu!"

if __name__ == '__main__':
    HunterApp().run()
