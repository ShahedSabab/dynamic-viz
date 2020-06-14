from django.urls import path, include
from .views import wheatCanada_list, wheatCanada_detail, wheatCanada_modify
urlpatterns = [
    path('apiDetails/', wheatCanada_list),
    path('apiDetails/<int:pk>', wheatCanada_detail),
    path('apiDetails/modify/<token>', wheatCanada_modify)
]
