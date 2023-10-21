import speech_recognition as sr

class MicrophoneSettings:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def set_microphone_settings(self, energy_threshold=4000, dynamic_energy_threshold=True):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            if dynamic_energy_threshold:
                self.recognizer.dynamic_energy_threshold = True
            else:
                self.recognizer.energy_threshold = energy_threshold

    def get_audio(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        return audio