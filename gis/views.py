from django.shortcuts import render, get_object_or_404
from .models import NavigationEntry
import base64
#from django.http import HttpResponse

def data_entry_view(request):
    if request.method == 'POST':
        # Process the form data
        sno = request.POST['sno']
        unique_id = request.POST['uniqueID']
        coordinates = request.POST['coordinates']
        gis = request.POST['gis']
        plus_code = request.POST['plusCode']
        nearby_railway_address = request.POST['nearbyRailwayAddress']
        nearby_railway_station = request.POST['nearbyRailwayStation']

        # Read photos and videos as base64-encoded strings
        photos_file = request.FILES.get('photos')
        videos_file = request.FILES.get('videos')

        photos_base64 = None
        if photos_file:
            photos_base64 = base64.b64encode(photos_file.read()).decode('utf-8')

        videos_base64 = None
        if videos_file:
            videos_base64 = base64.b64encode(videos_file.read()).decode('utf-8')

        type_of_item = request.POST['typeOfItem']
        status = request.POST['status']
        verified_scrap = request.POST['verifiedScrap']
        pending_department = request.POST['pendingDepartment']
        lot_no_engineering = request.POST['lotNoEngineering']
        lot_no_stores = request.POST['lotNoStores']
        auction_date_given = request.POST['auctionDate']
        fdp_date = request.POST['fdpEnds']
        phone_no = request.POST['phoneNo']
        custodian = request.POST['custodian']
        approx_weight = request.POST['approxWeight']
        approx_rate = request.POST['approxRate']

        # Create the NavigationEntry instance and save it to the database
        navigation_entry = NavigationEntry(
            sno=sno,
            unique_id=unique_id,
            coordinates=coordinates,
            gis=gis,
            plus_code=plus_code,
            nearby_railway_address=nearby_railway_address,
            nearby_railway_station=nearby_railway_station,
            photos=photos_base64,
            videos=videos_base64,
            type_of_item=type_of_item,
            status=status,
            verified_scrap=verified_scrap,
            pending_department=pending_department,
            lot_no_engineering=lot_no_engineering,
            lot_no_stores=lot_no_stores,
            auction_date_given=auction_date_given,
            fdp_date=fdp_date,
            phone_no=phone_no,
            custodian=custodian,
            approx_weight=approx_weight,
            approx_rate=approx_rate
        )
        navigation_entry.save()

        return render(request, 'data_entry_ui.html')
    else:
        return render(request, 'data_entry_ui.html')




def map_view(request):
    entries = NavigationEntry.objects.all()
    return render(request, 'map.html', {'entries': entries})


#function that render independent urls: status_update.html/
def status_update_view(request, unique_id):
    # Retrieve the specific navigation entry with the provided unique_id
    navigation_entry = get_object_or_404(NavigationEntry, unique_id=unique_id)
    return render(request, 'status_update.html', {'entry': navigation_entry})

