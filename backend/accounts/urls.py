from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
    path('me/', views.UserMeView.as_view()),
    #path('customers/'),
    #path('customers/{id}'),
]