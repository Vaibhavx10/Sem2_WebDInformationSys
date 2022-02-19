from contextlib import nullcontext
from traceback import print_tb
import requests
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration  

# Create your views here.
def displayHome(request):
    listofVidIDs = []
    listofVidResult = []
    if request.method == 'POST':
        yt_searching_url = 'https://www.googleapis.com/youtube/v3/search'
        yt_videos_url = 'https://www.googleapis.com/youtube/v3/videos'


        inputs = {
            'part':'snippet',
            'q':request.POST['ytsearch'],
            'key' : settings.YT_API_KEY,
            'safeSearch':'strict',
            'maxResults':9
        }



        searchresults = requests.get(yt_searching_url,params=inputs)

        
        
        fetchedresults = searchresults.json()['items']

        #Creating for loop to get all the video IDs
        #Need to fix the nothing found error
        for fr in fetchedresults:
             if(fr['id']['videoId'] != "" ):
                 listofVidIDs.append(fr['id']['videoId'])



        videos_input_param = {
            'part':'snippet,contentDetails',
            'key' : settings.YT_API_KEY,
            'id' : ','.join(listofVidIDs),
            'type':'video',
            'maxResults':9
        }



        videosresults = requests.get(yt_videos_url,params=videos_input_param)
        itemsofvideosresults = videosresults.json()['items']
        

        for data in itemsofvideosresults:
            v_dict = {
                'title' : data['snippet']['title'],
                'id': data['id'],
                'url':f'https://www.youtube.com/watch?v={ data["id"] }',
                'totaltimeinMinutes': parse_duration(data['contentDetails']['duration']).total_seconds() // 60,
                'thumbnails':data['snippet']['thumbnails']['high']['url']
            }

            listofVidResult.append(v_dict)
        


    passtoView = {
        'videos': listofVidResult   
    }


    return render(request,'searchingytvid/home.html',passtoView)
 

    