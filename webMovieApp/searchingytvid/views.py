import requests
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration
from pprint import PrettyPrinter
import jwt
from rest_framework.exceptions import AuthenticationFailed
from searchingytvid.models import UsersSubscription
from searchingytvid.serializers import userssubscriptionSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UsersSubscription

# Calling API using
# Documentation https://medium.com/daily-python/python-script-to-consume-the-omdb-api-daily-python-15-aa9457f6d090

#https://api.tvmaze.com/show This will show all the info that we need to display on dashboard
#including imdb ID
#More info on this can be found on https://www.tvmaze.com/api


# For More info Refer http://www.omdbapi.com/

def callingimdbAPI(searchquery):
    printer = PrettyPrinter()

    url = 'http://www.omdbapi.com/?apikey='+settings.OMDB_API_KEY
    year = ''
    movietitle = searchquery
    inputData = {
        's':movietitle,
        'type':'movie',
        'y':year
    }

    response = requests.get(url,params=inputData).json()
    #print(response['Search'][0]['imdbID'])

    imdbID = response['Search'][0]['imdbID']
    #Call API Based on IMDB ID
    getDataOnImdbID(imdbID)

def getDataOnImdbID(imdbID):
    printer = PrettyPrinter()
    url = 'http://www.omdbapi.com/?apikey='+settings.OMDB_API_KEY
    inputData = {
        'i':imdbID
    }
    response = requests.get(url,params=inputData).json()
    return response



def returnYTSearchPage(request):
    return render(request,'searchingytvid/home.html')




def getYoutubeResultsOnSearch(ytsearch):
    listofVidIDs = []
    listofVidResult = []
    yt_searching_url = 'https://www.googleapis.com/youtube/v3/search'
    yt_videos_url = 'https://www.googleapis.com/youtube/v3/videos'


    inputs = {
            'part':'snippet',
            'q':ytsearch,
            'key' : settings.YT_API_KEY,
            'safeSearch':'strict',
            'maxResults':9
            }



    searchresults = requests.get(yt_searching_url,params=inputs)



    fetchedresults = searchresults.json()['items']
    print("\n \n fetchedresults >> ",fetchedresults)

    #Creating for loop to get all the video IDs
    
    for fr in fetchedresults:
                    listofVidIDs.append(fr['id'].get('videoId',''))





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

    if len(listofVidResult) > 1:
        passtoView = {
            'videos': listofVidResult
        }
    else:
        passtoView = {
            'videos': "FAIL"
        }
    return passtoView


class displatytsearchresultfor_home(APIView):
    def post(self,request):    
        passtoView = getYoutubeResultsOnSearch(request.POST['ytsearch'])
        return Response(passtoView,status=status.HTTP_200_OK)

def displatytsearchresult(request):
    passtoView = getYoutubeResultsOnSearch(request.POST['ytsearch'])
    return render(request,'searchingytvid/home.html',passtoView)


def callDashoardPage(request):
    
    displayShowsAPIURL = requests.get('https://api.tvmaze.com/show').json()
    customResult = []
    for i in range(20):
         customResult.append(displayShowsAPIURL[i])



    passtoView = {
        'videos': customResult
    }

    return render(request,'searchingytvid/dashboard.html',passtoView)

def getDashboardPageonUserID(request):
        uname = request.POST['dash_uname']
        userid = request.POST['dash_userid']
        print('getDashboardPageonUserID >> uname ',uname)
        print('getDashboardPageonUserID >> userid ',userid)


        displayShowsAPIURL = requests.get('https://api.tvmaze.com/show').json()
        customResult = []
        for i in range(20):
            customResult.append(displayShowsAPIURL[i])



        passtoView = {
            'videos': customResult,
            'uemail':uname,
            'userid':userid
        }
        return render(request,'searchingytvid/dashboard.html',passtoView)







def moreInfo(request):
    #Need to call moreInfo Page
    imdbid = request.POST['moreInfo_imdbid']
    vidname = request.POST['moreInfo_vidname']
    uemail = request.POST['moreInfo_uemail']
    userid = request.POST['moreInfo_userid']



    #Calling api based on imdbID to get additional information

    passtoView = {
        'meta': getDataOnImdbID(imdbid),
        'userID':userid,
        'uemail':uemail,
        'vidname':vidname
    }

    print("moreInfo passtoView >> ",passtoView)
    return render(request,'searchingytvid/moreInfo.html',passtoView)


def returnSubscriberDashboardPage(request):
    #jwttoken = request.POST['jwtcookie']
    uemail = request.POST['sub_uname']
    userid = request.POST['sub_userid']
    passtoView = {
            'jwtcookie':"dummy",
            'uemail':uemail,
            'userid':userid
         }
    return render(request, 'searchingytvid/subscribeddashboard.html',passtoView)         


class addSubscriptionInDB(APIView):
    def post(self,request):
        #Check if user is signed and jwt token is present 
        token = request.COOKIES.get('jwtcookie')

        if not token:
            print('Unauthenticated User !!!')
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            print('Token Expired !!')   
            return Response(status=status.HTTP_404_NOT_FOUND)

        requserID = int(request.data['userid'])
        jwtuserID = int(payload['id'])

        if requserID == jwtuserID:
            data = UsersSubscription.objects.filter(userid=request.data['userid'],imdbid=request.data['imdbid']) 
            usrandimdbCount = userssubscriptionSerializers(data,many=True)
            
            if len(usrandimdbCount.data) < 1:
                serializer = userssubscriptionSerializers(data=request.data)
                if serializer.is_valid():
                    serializer.is_valid(raise_exception=True)
                    print(serializer.errors)
                    serializer.save()
                    return Response(request.data, status=status.HTTP_200_OK)
                else:
                        print("PRINTED ERROR ", serializer.errors)
                        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
            else:
                 return Response(request.data, status=status.HTTP_404_NOT_FOUND)       
        else:
            print("New Error !! ")
        
        
        

# using userId get list of imdbIDs which he has subscribed and from that list get
# all meta data of that imdbID
class getUserSubscribedData(APIView):
    def post(self,request):
        userid = request.data['userid']
        userInfo = UsersSubscription.objects.filter(userid_id=userid)
        serializer = userssubscriptionSerializers(userInfo,many=True)
        listofsubscribedVideos = []
        # print(serializer.data)
        for fr in serializer.data:
             imdbInfo = getDataOnImdbID(fr['imdbid'])
             listofsubscribedVideos.append(imdbInfo)

        return Response(listofsubscribedVideos,status=status.HTTP_200_OK)


class deleteVideoEntry(APIView):
    def post(self,request):
        userid = request.data["userid"]
        deleteimdbID = request.data["deleteimdbID"]
        print("deleteVideoEntry | deleteimdbID >> ",deleteimdbID)
        deletethisVid = UsersSubscription.objects.filter(imdbid=deleteimdbID)
        info = deletethisVid.delete()
        return Response(info,status=status.HTTP_200_OK)

