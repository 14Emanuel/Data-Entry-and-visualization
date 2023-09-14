# image_utils.py

import os
from django.conf import settings

def save_images(unique_id, image_files):
    for image_file in image_files:
        image_dir = os.path.join(settings.MEDIA_ROOT, 'images', unique_id)
        os.makedirs(image_dir, exist_ok=True)
        image_path = os.path.join(image_dir, image_file.name)
        with open(image_path, 'wb') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

def get_image_url(unique_id, image_file_name):
    return os.path.join(settings.MEDIA_URL, 'images', unique_id, image_file_name)
