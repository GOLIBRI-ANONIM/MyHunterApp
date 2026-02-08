from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard  # Fitur untuk copy otomatis

class HunterApp(App):
    def build(self):
        # Layout utama dengan warna background gelap (Dark Mode)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)

        # Header
        layout.add_widget(Label(text="My Hunter App - V2 (Pro)", font_size='24sp', color=(0, 1, 0, 1), size_hint_y=None, height=60))

        # Input Target
        self.target_input = TextInput(hint_text="Masukkan Target (URL/User)", multiline=False, size_hint_y=None, height=50, background_color=(1,1,1,1))
        layout.add_widget(self.target_input)

        # Tombol SQLi
        btn_sqli = Button(text="CEK SQLi", background_color=(0, 0.5, 0, 1), bold=True)
        btn_sqli.bind(on_press=self.cek_sqli)
        layout.add_widget(btn_sqli)

        # Tombol OSINT
        btn_osint = Button(text="CEK OSINT", background_color=(0, 0, 0.5, 1), bold=True)
        btn_osint.bind(on_press=self.cek_osint)
        layout.add_widget(btn_osint)

        # Area Hasil (Sekarang pakai TextInput agar BISA DI-COPY)
        layout.add_widget(Label(text="Hasil Perintah:", size_hint_y=None, height=30))
        self.result_display = TextInput(text="", readonly=True, background_color=(0.1, 0.1, 0.1, 1), foreground_color=(0, 1, 0, 1), font_name="Roboto")
        layout.add_widget(self.result_display)

        # Tombol Copy Otomatis
        btn_copy = Button(text="SALIN KE CLIPBOARD", size_hint_y=None, height=60, background_color=(0.7, 0.7, 0, 1))
        btn_copy.bind(on_press=self.copy_ke_clipboard)
        layout.add_widget(btn_copy)

        return layout

    def cek_sqli(self, instance):
        target = self.target_input.text
        if target:
            command = f"sqlmap -u '{target}' --batch --dbs"
            self.result_display.text = command
        else:
            self.result_display.text = "Error: Target kosong!"

    def cek_osint(self, instance):
        target = self.target_input.text
        if target:
            command = f"python3 ~/sherlock/sherlock_project {target}"
            self.result_display.text = command
        else:
            self.result_display.text = "Error: Target kosong!"

    def copy_ke_clipboard(self, instance):
        if self.result_display.text:
            Clipboard.copy(self.result_display.text)
            # Opsional: ubah teks tombol sebentar untuk tanda sukses
            instance.text = "TERTULIS! (BERHASIL DI-COPY)"
        else:
            self.result_display.text = "Gak ada yang bisa di-copy, BRI!"

if __name__ == '__main__':
    HunterApp().run()

