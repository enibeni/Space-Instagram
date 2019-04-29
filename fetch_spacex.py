import requests
from download_tools import download_image


def fetch_spacex_last_launch(path_to_images):
    spacex_launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    fetched_image_paths = []
    response = requests.get(spacex_launch_url)
    if not response.ok:
        return None
    spacex_images_urls = response.json()['links']['flickr_images']
    for img_number, url in enumerate(spacex_images_urls):
        fetched_image_path = download_image(
            url,
            f'{path_to_images}/spacex{img_number}.jpg'
        )
        fetched_image_paths.append(fetched_image_path)
    return fetched_image_paths


if __name__ == '__main__':
    path_to_images = './images'
    fetch_spacex_last_launch(path_to_images)
