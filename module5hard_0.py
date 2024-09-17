from time import sleep

class UrTube:
    def __init__(self):
        self.users = [] # список объектов User
        self.videos = [] # список объектов Video
        self.current_user = None # текущий пользователь, User

    def log_in(self, nickname, password):
        '''
        Метод log_in пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        '''
        for element in self.users:
           if element.nickname == nickname and element.password == hash(password):
               self.current_user = element

    def register(self, nickname, password, age):
        '''
        Добавляет пользователя в список, если пользователя не существует (с таким
        же nickname). Если существует, выводит на экран: "Пользователь {nickname}
        уже существует". После регистрации, вход выполняется автоматически.
        '''
        if self.users:
            existence = False
            for element in self.users:
                if element.nickname == nickname:
                    existence = True
                    break
            if existence:
                print(f'Пользователь {nickname} уже существует')
            else:
                self.users.append(User(nickname, hash(password), age))
        else:
            self.users.append(User(nickname, hash(password), age))
        self.log_in(nickname, password)

    def log_out(self):
        '''
        сброс текущего пользователя на None
        '''
        self.current_user = None

    def add(self, *args):
        if self.videos:
            for elem in args:
                existence2 = False
                for video in self.videos:
                    if video.title == elem.title:
                        existence2 = True
                        break
                if existence2:
                    pass
                else:
                    self.videos.append(elem)
        else:
            for elem in args:
                self.videos.append(elem)

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
                    if self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    else:
                        for i in range(1, video.duration + 1):
                            print(i, ' ', end='')
                            sleep(0.5)
                        print("Конец видео.")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео.")
        else:
            pass

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title # заголовок, строка
        self.duration = duration # продолжительность, секунды
        self.time_now = time_now # секунда остановки
        self.adult_mode = adult_mode # ограничение по возрасту, bool

    def __str__(self):
        return f'Видео {self.title} продолжительностью {self.duration}'

    def __eq__(self, other):
        return self.title == other.title and self.duration == other.duration and self.time_now == other.time_now and self.adult_mode == other.adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname #имя пользователя, строка
        self.password = password #пароль в хэшированном виде, число
        self.age = age #возраст, число

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password and self.age == other.age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)


