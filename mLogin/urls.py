from django.urls import path
from django.conf.urls import url
from mLogin import views

urlpatterns = [
    path('',views.Index,name="login"),
    path('Register',views.Register,name="Register"),
    path('userHome/<str:pk>/',views.Home,name="Home"),
    path('logout',views.logout,name="logout"),
    path('google',views.google,name="google"),
    path('upload/<str:pk>/',views.upload,name="upload"),
    path('upload',views.upload,name="upload"),
    path('feature',views.feature,name="feature"),
    path('feature/<str:pk>',views.feature,name="feature"),
    path('seepost',views.seepost,name="seepost"),
    path('feature/seepost/<str:pk>',views.seepost,name="seepost"),
	path('seepost/<str:pk>',views.seepost,name="seepost"),
]