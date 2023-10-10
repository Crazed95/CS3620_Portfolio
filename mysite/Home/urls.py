from django.urls import path
from. import views
urlpatterns = [
    path('',views.index, name= "home"),
    path('hobbie/',views.hobbie, name= "hobbie"),
    path('contact/',views.contact, name ="contact"),
    path('portfolio/',views.portfolio, name ="portfolio"),
    path('hobbie/<int:hobbie_id>', views.h_details, name="detail"),
    path('portfolio/<int:portfolio_id>', views.p_details, name="p_detail"),
]

