from django.shortcuts import render, redirect
from .models import NavigationEntry

def data_entry_view(request):
    if request.method == 'POST':
        sno = request.POST['sno']
        unique_id = request.POST['uniqueID']
        coordinates = request.POST['coordinates']
        gis = request.POST['gis']
        plus_code = request.POST['plusCode']
        nearby_location = request.POST['nearbyLocation']  # Add nearby_location field
        type_of_item = request.POST['typeOfItem']
        status = request.POST['status']
        
        navigation_entry = NavigationEntry(
            sno=sno,
            unique_id=unique_id,
            coordinates=coordinates,
            gis=gis,
            plus_code=plus_code,
            nearby_location=nearby_location,  # Assign the nearby_location field
            type_of_item=type_of_item,
            status=status
        )
        navigation_entry.save()
        
        return redirect('/')  # Replace '/' with the actual URL of the data entry page
    else:
        return render(request, 'data_entry_ui.html')
