from django.urls import path
from . import views
from .views import addSubscriptionInDB
from .views import getUserSubscribedData
from .views import deleteVideoEntry
from .views import displatytsearchresultfor_home

urlpatterns = [
    path('',views.returnYTSearchPage,name='index'),
    path('displatytsearchresultfor_home',displatytsearchresultfor_home.as_view()),
    path('dashboard',views.callDashoardPage,name='dashboard'),
    path('moreInfo',views.moreInfo,name='moreInfo'),
    path('returnSubscriberDashboardPage',views.returnSubscriberDashboardPage,name='returnSubscriberDashboardPage'),
    path('addSubscriptionInDB',addSubscriptionInDB.as_view()),
    path('getUserSubscribedData',getUserSubscribedData.as_view()),
    path('deleteVideoEntry',deleteVideoEntry.as_view()),
    path('getDashboardPageonUserID',views.getDashboardPageonUserID,name='getDashboardPageonUserID'),
    path('displatytsearchresult',views.displatytsearchresult,name='displatytsearchresult'),
    
]
