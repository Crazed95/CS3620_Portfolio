from django.urls import path
from. import views
urlpatterns = [
    path('',views.index, name= "index"),
    path('hobbie/',views.hobbie, name= "hobbie"),
    path('contact/',views.contact, name ="contact"),
    path('portfolio/',views.portfolio, name ="portfolio"),
]