"""
facade
сложная система
разделяем клиентский код и внутренности
api проще
единый интерфейс к разным классам

клиент
подсистемы
фасад

adapter
proxy
mediator

os
pandas numpy matplotlib
flask
subprocess.run()
"""

class DVDPlayer:
    def on(self):
        print('DVD вкл')

    def play(self):
        print("DVD play")

    def off(self):
        print("DVD выкл")

class Projector:
    def on(self):
        print('проектор вкл')

    def set_input(self, source):
        print(f"проектор источник {source}")

    def off(self):
        print("проектор выкл")

class AudioSystem:
    def on(self):
        print('аудиосистема вкл')

    def set_voulme(self, level):
        print(f"громкость установлена {level}")

    def off(self):
        print("аудиосистема выкл")

class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, audio: AudioSystem):
        self.dvd = dvd
        self.projector = projector
        self.audio = audio

    def watch_movie(self):
        print("начало")
        self.projector.on()
        self.projector.set_input("DVD")
        self.audio.on()
        self.audio.set_voulme(100)
        self.dvd.on()
        self.dvd.play()
        print("готово")

    def end_movie(self):
        print("завершаем")
        self.dvd.off()
        self.audio.off()
        self.projector.off()

dvd = DVDPlayer()
projector = Projector()
audio = AudioSystem()

cinema = HomeTheaterFacade(dvd, projector, audio)

cinema.watch_movie()
cinema.end_movie()