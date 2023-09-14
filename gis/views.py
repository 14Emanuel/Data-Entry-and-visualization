from django.shortcuts import render, get_object_or_404
from .models import NavigationEntry, Image  # Import the Image model
import logging  # Import the logging module
from django.http import HttpResponse, HttpResponseNotFound  # Import HttpResponse and HttpResponseNotFound
from django.conf import settings

import os

def save_images(unique_id, image_files):
    # Define the directory where images will be saved
    image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images', unique_id)

    # Create the directory if it doesn't exist
    os.makedirs(image_dir, exist_ok=True)

    # Iterate over image files and save them
    for image_file in image_files:
        # Generate a unique filename for each image
        image_filename = f"{unique_id}_{image_file.name}"

        # Build the full file path
        image_path = os.path.join(image_dir, image_filename)

        # Open and write the image file
        with open(image_path, 'wb') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

# You can now call this function in your `data_entry_view` to save the uploaded images.

logger = logging.getLogger(__name__)

from django.template import loader

def data_entry_view(request):
    if request.method == 'POST':
        # Process the form data
        unique_id = request.POST['uniqueID']
        surveyor_id = request.POST['surveyorID']
        coordinates = request.POST['coordinates']
        nearby_station = request.POST['nearbyStation']
        scrap_location = request.POST['scrapLocation']
        scrap_category = request.POST['categoryDropdown']
        sub_category = request.POST['subCategory']
        scrap_status = request.POST['scrapStatus']
        verified_scrap = request.POST['verifiedScrap']
        pending_department = request.POST['pendingDepartment']
        custodian = request.POST['custodian']
        custodian_contact = request.POST['custodianContact']
        approx_weight = request.POST['approxWeight']
        approx_rate = request.POST['approxRate']
        remarks = request.POST['remarks']

        try:
            # Create the NavigationEntry instance and save it to the database
            navigation_entry = NavigationEntry(
                mongo_id=None,  # You can set this to None since it will be generated automatically
                unique_id=unique_id,
                surveyor_id=surveyor_id,
                coordinates=coordinates,
                nearby_station=nearby_station,
                scrap_location=scrap_location,
                scrap_category=scrap_category,
                sub_category=sub_category,
                scrap_status=scrap_status,
                verified_scrap=verified_scrap,
                pending_department=pending_department,
                custodian=custodian,
                custodian_contact=custodian_contact,
                approx_weight=approx_weight,
                approx_rate=approx_rate,
                remarks=remarks
            )
            navigation_entry.save()

            # Process and save images
            scrap_pictures_files = request.FILES.getlist('scrapPictures')
            print("List of uploaded image files:")  # Add this line to print the list
            for photo_file in scrap_pictures_files:
                print(photo_file)  # Print each uploaded file
                # Save the images using the utility function
                save_images(unique_id, [photo_file])

            # Add a log entry for successful submission
            logger = logging.getLogger(__name__)
            logger.info(f"Form submitted successfully for unique_id: {unique_id}")

            return render(request, 'data_entry_ui.html')
        except Exception as e:
            # Handle any exceptions here, like validation errors or database issues
            logger = logging.getLogger(__name__)
            logger.error(f"Error processing form for unique_id: {unique_id}, Error: {str(e)}")
            return render(request, 'data_entry_ui.html', {'error_message': str(e)})
    else:
        return render(request, 'data_entry_ui.html')

def map_view(request):
    entries = NavigationEntry.objects.all()
    return render(request, 'map.html', {'entries': entries})



# pop_up vies functions
def popup_view(request, unique_id):
    try:
        entry = NavigationEntry.objects.get(unique_id=unique_id)
        images_folder = os.path.join(settings.STATIC_ROOT, 'images', unique_id)
        image_filenames = os.listdir(images_folder)
        image_urls = []

        for filename in image_filenames:
            if filename.lower().endswith('.jpg'):
                # Create the image URL with the correct format
                image_url = os.path.join('images', unique_id, filename)
                image_urls.append(image_url)

        logger.info("Image URLs: %s", image_urls)

        context = {
            'unique_id': entry.unique_id,
            'surveyor_id': entry.surveyor_id,
            'coordinates': entry.coordinates,
            'nearby_station': entry.nearby_station,
            'scrap_location': entry.scrap_location,
            'image_urls': image_urls,
        }

        # Load the template using loader
        template = loader.get_template('popup_template.html')

        # Render the template with the context
        rendered_html = template.render(context)

        return HttpResponse(rendered_html)

    except NavigationEntry.DoesNotExist:
        return render(request, 'error.html', {'message': 'Navigation entry not found'})


#navigation pane functions:
def navigation_pane_view(request, unique_id):
    try:
        entry = NavigationEntry.objects.get(unique_id=unique_id)
        images_folder = os.path.join(settings.STATIC_ROOT, 'images', unique_id)
        image_filenames = os.listdir(images_folder)
        image_urls = []

        for filename in image_filenames:
            if filename.lower().endswith('.jpg'):
                # Create the image URL with the correct format
                image_url = os.path.join('images', unique_id, filename)
                image_urls.append(image_url)

        logger.info("Image URLs: %s", image_urls)

        context = {
            'unique_id': entry.unique_id,
            'surveyor_id': entry.surveyor_id,
            'coordinates': entry.coordinates,
            'nearby_station': entry.nearby_station,
            'scrap_location': entry.scrap_location,
            'scrap_category': entry.scrap_category,
            'sub_category': entry.sub_category,
            'scrap_status': entry.scrap_status,
            'verified_scrap': entry.verified_scrap,
            'pending_department': entry.pending_department,
            'custodian': entry.custodian,
            'custodian_contact': entry.custodian_contact,
            'approx_weight': entry.approx_weight,
            'approx_rate': entry.approx_rate,
            'remarks': entry.remarks,
            'image_urls': image_urls,  # Add image URLs to the context
            # You can add other fields as needed
        }

        # Load the template using loader
        template = loader.get_template('navigation_ui.html')

        # Render the template with the context
        rendered_html = template.render(context)

        return HttpResponse(rendered_html)

    except NavigationEntry.DoesNotExist:
        return render(request, 'error.html', {'message': 'Navigation entry not found'})


#status_update
logger = logging.getLogger(__name__)

def status_update_view(request, unique_id):
    try:
        entry = NavigationEntry.objects.get(unique_id=unique_id)
        images_folder = os.path.join(settings.STATIC_ROOT, 'images', unique_id)
        image_filenames = os.listdir(images_folder)
        image_urls = []

        for filename in image_filenames:
            if filename.lower().endswith('.jpg'):
                # Create the image URL with the correct format
                image_url = os.path.join('images', unique_id, filename)
                image_urls.append(image_url)

        logger.info("Image URLs: %s", image_urls)

        context = {
            'unique_id': entry.unique_id,
            'surveyor_id': entry.surveyor_id,
            'coordinates': entry.coordinates,
            'nearby_station': entry.nearby_station,
            'scrap_location': entry.scrap_location,
            'scrap_category': entry.scrap_category,
            'sub_category': entry.sub_category,
            'scrap_status': entry.scrap_status,
            'verified_scrap': entry.verified_scrap,
            'pending_department': entry.pending_department,
            'custodian': entry.custodian,
            'custodian_contact': entry.custodian_contact,
            'approx_weight': entry.approx_weight,
            'approx_rate': entry.approx_rate,
            'remarks': entry.remarks,
            'image_urls': image_urls,  # Add image URLs to the context
            # You can add other fields as needed
        }

        # Load the template using loader
        template = loader.get_template('status_update.html')

        # Render the template with the context
        rendered_html = template.render(context)

        return HttpResponse(rendered_html)

    except NavigationEntry.DoesNotExist:
        return render(request, 'error.html', {'message': 'Status update entry not found'})


#update_navigation_entry
from django.http import JsonResponse

def update_navigation_entry(request, navigation_entry_id):
    if request.method == 'POST':
        updated_data = request.POST.get('updated_data')
        try:
            navigation_entry = NavigationEntry.objects.get(id=navigation_entry_id)
            navigation_entry.remarks = updated_data
            navigation_entry.save()
            return JsonResponse({'message': 'Data updated successfully'})
        except NavigationEntry.DoesNotExist:
            return JsonResponse({'error': 'NavigationEntry not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


