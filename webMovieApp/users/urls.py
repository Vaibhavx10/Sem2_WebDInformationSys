
from django.urls import path
from .views import RegisterationPage
from .views import InsertRegisterationInfoToDB
from .views import loginAPIAuthentication
from .views import getUserDetails
from .views import logoutPage
from .views import returnLoginPage,returnRegisterationPage


urlpatterns = [
    path('reg',RegisterationPage.as_view()),
    path('loginApi',loginAPIAuthentication.as_view()),
    path('getUserDetails',getUserDetails.as_view()),
    path('logout',logoutPage.as_view()),
    path('loginPage',returnLoginPage,name='loginPage'),
    path('registerationPage',returnRegisterationPage,name='RegisterationPage'),
    path('regInfoToDB',InsertRegisterationInfoToDB.as_view()),
]
