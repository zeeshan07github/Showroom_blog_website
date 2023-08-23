from django.urls import path 
from . import views

app_name = 'Showroom'
urlpatterns = [
    path("" , views.brand_list , name ='brand_list'),
    path("<int:profile_id>" , views.brand_detail , name ='brand_detail'),
    path("<int:profile_id>/delete/" , views.brand_delete , name ='brand_delete'),
    path('delete_brand/<int:brand_id>/', views.delete_brand, name='delete_brand'),

    path("team/" , views.our_team , name ='our_team'),
    path("Showrooms.html/" , views.showroomss , name ='showroomss'),
    path("contactus/" , views.contactview , name ='contactus'),
    path("newprofile/" , views.Newprofile , name ='newprofile'),
    path("newmodel/" , views.Newmodel , name ='newmodel'),
    path("filter/" , views.filters , name ='filter'),

]
