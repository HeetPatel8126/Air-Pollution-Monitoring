from django.urls import path
from .views import home, live_data

urlpatterns = [
    path('', home, name='home'),
    path('live_data/', live_data, name='live_data'),
]
