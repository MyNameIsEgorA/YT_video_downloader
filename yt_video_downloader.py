from pytube import YouTube
import shutil
import os.path


class Downloader:

    def __init__(self, url: str, quality: str):
        self.url = url
        self.quality = quality
        self.yt = self.donwloader(url=self.url)

    @staticmethod
    def donwloader(url):
        return YouTube(url)

    def file_creator(self):
        print('Ваше видео скачивается, пожалуйста, подождите, это может занять некоторое время')
        self.yt.streams.filter(res=self.quality).first().download()


class NormalName:
    def __init__(self, filename):
        self.filename = filename
        self.answer = ''

    def transform(self):
        for x in self.filename:
            if x not in ['|', '#', ':', '~']:
                self.answer += x
        return self.answer

class Relocator:
    def __init__(self, filename: str, directory_name: str):
        self.filename = os.path.normpath(filename)
        self.directory_name = os.path.normpath(directory_name)

    def act(self):
        shutil.move(self.filename, self.directory_name)


input_url = input("Введите url вашего видео с ютуба: ")
if 'youtube.com' not in input_url:
    raise ValueError("Нужна ссылка с официального сайта или приложения youtube")

input_quality = input("Введите качество, в котором вы хотите скачать видео с ютуба в формате '720p': ")
if input_quality not in ['144p', '240p', '360p', '480p', '720p', '1080p']:
    raise ValueError("Вы ввели неправильное качество видео")

input_dirname = input('Введите имя папки, в которую вы хотите добавить ваше видео: ')


if __name__ == '__main__':
    try:
        down = Downloader(input_url, input_quality)
        down.file_creator()
        normal_name = NormalName(down.yt.title).transform()
        relocator = Relocator(normal_name + '.mp4', input_dirname)
        relocator.act()
    except Exception:
        print('\nВозможно, вы сделали что-то не так, попробуйте еще раз и проверьте, что вы взяли ссылку именно с ютуба, \n'
              'что вы указали правильное разрешение (p - английская буква) \n'
              'и что программа имеет доступ к директории, в которую вы хотели поместить файл')
        print("\nЕсли вы все сделали правильно, но у вас все равно не получилось, то свяжитесь с автором"
              " данного скрипта, информация об этом в файле readme.txt")
