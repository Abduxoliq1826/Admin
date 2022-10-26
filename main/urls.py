from django.urls import path
from .views import *

urlpatterns = [
    path("", Login, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path('is_admin/', ProductFilter, name='productfilter'),
    path('about/<int:pk>/', About, name='about'),
    path('logins/', Logins, name='logins'),
    path('log-out/', LogOut, name='logout'),
    path('user/', All_User, name='users'),

    path('ads/', AllAds, name='ads'),
    path('isacepted/', IsAcepted, name='isacepted'),
    path('isrejected/', IsRejected, name='isrejected'),
    path('sort/', Sold, name='sold'),

    path('info/', InformationViews, name='info'),

    path('users/<int:pk>/', Users, name='users'),

    path('ads/<int:pk>/', AdsSingle, name='single-ads'),
    path('accepted/<int:pk>/', Accepted, name='accept'),
    path('rejected/<int:pk>/', Rejected, name='reject'),
    path('reset/', Reset, name='reset'),
    path('reset-user/', UpdateUser, name='reset_user'),

    path('category/', AddCategory, name='category'),
    path('single-category/<int:pk>/', SingleCategory, name='single_category'),
    path('delete-category/<int:pk>/', DeleteCategory, name='delete_category'),

    path('subcategory/', SubCategory, name='subcategory'),
    path('single-subcategory/<int:pk>/', SingleSubCategory, name='single_subcategory'),
    path('delete-sub-category/<int:pk>/', DeleteSubCategory, name='delete_category'),

    path('regions/', Regions, name='regions'),
    path('single-region/<int:pk>/', SingleRegion, name='single_region'),
    path('delete-region/<int:pk>/', DeleteRegion, name='delete_region'),
]