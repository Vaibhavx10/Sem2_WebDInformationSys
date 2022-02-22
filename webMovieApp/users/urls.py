
from django.urls import path
from .views import RegisterationPage
from .views import loginPage
from .views import getUserDetails
from .views import logoutPage

urlpatterns = [
    path('reg',RegisterationPage.as_view()),
    path('login',loginPage.as_view()),
    path('getUserDetails',getUserDetails.as_view()),
    path('logout',logoutPage.as_view())
]
