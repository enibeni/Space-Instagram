import os
import requests


def download_image(image_url, path_to_image):
    directory = './images/'
    os.makedirs(directory, exist_ok=True)

    response = requests.get(image_url)
    if not response.ok:
        return None
    with open(path_to_image, 'wb') as file:
        file.write(response.content)
    return path_to_image
