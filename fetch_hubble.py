import requests
from download_tools import download_image

def fetch_hubble_image_by_id(image_id, path_to_image):
    hubble_image_urls = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(hubble_image_urls)
    if not response.ok:
        return None
    hubble_image_url = response.json()['image_files'][-1:][0]['file_url']
    image_ext = get_image_ext(hubble_image_url)
    fetched_image_path = download_image(
        hubble_image_url,
        f'{path_to_image}/hubble{image_id}.{image_ext}'
    )
    return fetched_image_path


def get_hubble_images_id_by_collection(collection_name):
    params = {
        "collection_name": collection_name,
        "page": "all"
    }
    r = requests.get(
        url='http://hubblesite.org/api/v3/images',
        params=params
    )
    image_ids = [x['id'] for x in r.json()]
    return image_ids


def get_image_ext(url):
    return str(url).split('.')[-1]


if __name__ == '__main__':
    path_to_images = './images'
    collection_name = "spacecraft"
    image_ids = get_hubble_images_id_by_collection(collection_name=collection_name)
    for image_id in image_ids:
        fetch_hubble_image_by_id(image_id, path_to_images)
