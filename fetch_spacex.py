import requests
import os


def fetch_spacex_last_launch(path_to_images):
    spacex_launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    spacex_images_urls = []
    response = requests.get(spacex_launch_url)
    if response.ok:
        spacex_images_urls = response.json()['links']['flickr_images']
    for img_number, url in enumerate(spacex_images_urls):
        download_image(url, f'{path_to_images}/spacex{img_number}.jpg')


def download_image(image_url, path_to_image):
    directory = './images/'
    os.makedirs(directory, exist_ok=True)

    response = requests.get(image_url)
    if response.ok:
        with open(path_to_image, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    path_to_images = './images'
    fetch_spacex_last_launch(path_to_images)
