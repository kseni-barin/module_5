from time import sleep

class UrTube:
    def __init__(self):
        self.users = [] # список объектов User
        self.videos = [] # список объектов Video
        self.current_user = None # текущий пользователь, User

    def log_in(self, nickname, password):
        for element in self.users:
           if element.nickname == nickname and element.password == hash(password):
               self.current_user = element

    def __contains__(self, item):
        if isinstance(item, User):
            return item in self.users
        elif isinstance(item, Video):
            return item in self.videos
        return False

    def register(self, nickname, password, age):
        other = User(nickname, password, age)
        if other in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(other)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, string):
        list_video = []
        for video in self.videos:
            if string.lower() in video.title.lower():
                list_video.append(video.title)
        return list_video

    def watch_video(self, name_film):
        for video in self.videos:
            if name_film == video.title:
                if self.current_user:
                    if self.current_user.age < 18 and video.adult_mode == True:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    else:
                        for i in range(1, video.duration + 1):
                            print(i, ' ', end='')
                            sleep(0.1)
                        print("Конец видео.")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео.")

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title # заголовок, строка
        self.duration = duration # продолжительность, секунды
        self.time_now = time_now # секунда остановки
        self.adult_mode = adult_mode # ограничение по возрасту, bool

    def __str__(self):
        return f'Видео {self.title} продолжительностью {self.duration}'

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname #имя пользователя, строка
        self.password = hash(password) #пароль в хэшированном виде, число
        self.age = age #возраст, число

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
