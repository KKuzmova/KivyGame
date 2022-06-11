from kivy.core.audio import SoundLoader


class ButtonSound:

    def btn_pressed(self):
        sound = SoundLoader.load('sounds/click_btn.wav')
        sound.volume = .02

        sound.play()
