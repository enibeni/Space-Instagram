from os import listdir
from instabot import Bot
from os.path import join as joinpath


if __name__ == '__main__':
    path_to_images = './images'

    bot = Bot()
    bot.login()

    for image in listdir(path_to_images):
        bot.upload_photo(joinpath(path_to_images, image))





