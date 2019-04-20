import requests
import os


def download_image(image_url, path_to_image):
    directory = './images/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    response = requests.get(image_url)
    with open(path_to_image, 'wb') as file:
        file.write(response.content)


def fetch_hubble_image_by_id(id, path_to_image):
    hubble_image_urls = f'http://hubblesite.org/api/v3/image/{id}'
    hubble_image_url = requests.get(hubble_image_urls).json()['image_files'][-1:][0]['file_url']
    image_ext = get_image_ext(hubble_image_url)
    download_image(hubble_image_url, f'{path_to_image}/hubble{id}.{image_ext}')


def get_hubble_images_id_by_collection(collection_name):
    r = requests.get(f'http://hubblesite.org/api/v3/images?page=all&collection_name={collection_name}')
    image_ids = [x['id'] for x in r.json()]
    return image_ids


def get_image_ext(url):
    return str(url).split('.')[-1]


if __name__ == '__main__':
    path_to_images = './images'
    collection_name = "spacecraft"
    image_ids = get_hubble_images_id_by_collection(collection_name=collection_name)
    for id in image_ids:
        fetch_hubble_image_by_id(id, path_to_images)
