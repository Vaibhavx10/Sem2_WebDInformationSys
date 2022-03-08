from django.urls import path
from . import views
from .views import addSubscriptionInDB
from .views import getUserSubscribedData
from .views import deleteVideoEntry

urlpatterns = [
    path('',views.returnYTSearchPage,name='index'),
    path('displatytsearchresult',views.displayHome,name='displatytsearchresult'),
    path('dashboard',views.callDashoardPage,name='dashboard'),
    path('moreInfo',views.moreInfo,name='moreInfo'),
    path('addSubscriptionInDB',addSubscriptionInDB.as_view()),
    path('getUserSubscribedData',getUserSubscribedData.as_view()),
    path('deleteVideoEntry',deleteVideoEntry.as_view()),
    path('getDashboardPageonUserID',views.getDashboardPageonUserID,name='getDashboardPageonUserID'),
]
