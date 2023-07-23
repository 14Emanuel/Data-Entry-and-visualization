from django.shortcuts import render, redirect
from .models import NavigationEntry
import base64

def data_entry_view(request):
    if request.method == 'POST':
        sno = request.POST['sno']
        unique_id = request.POST['uniqueID']
        coordinates = request.POST['coordinates']
        gis = request.POST['gis']
        plus_code = request.POST['plusCode']
        nearby_location = request.POST['nearbyLocation']

        # Read photos and videos as base64-encoded strings
        photos_file = request.FILES.get('photos')
        videos_file = request.FILES.get('videos')

        if photos_file:
            photos_base64 = base64.b64encode(photos_file.read()).decode('utf-8')
        else:
            photos_base64 = None

        if videos_file:
            videos_base64 = base64.b64encode(videos_file.read()).decode('utf-8')
        else:
            videos_base64 = None

        type_of_item = request.POST['typeOfItem']
        status = request.POST['status']


        # Create the NavigationEntry instance and save it to the database
        navigation_entry = NavigationEntry(
            sno=sno,
            unique_id=unique_id,
            coordinates=coordinates,
            gis=gis,
            plus_code=plus_code,
            nearby_location=nearby_location,
            photos=photos_base64,
            videos=videos_base64,
            type_of_item=type_of_item,
            status=status
        )
        navigation_entry.save()

        return redirect('/')  # Replace '/' with the actual URL of the data entry page
    else:
        return render(request, 'data_entry_ui.html')
