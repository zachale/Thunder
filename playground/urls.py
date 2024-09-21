#map the url to the view functions!

from django.urls import path
from . import views


#URLConfiguration!
#because we included playground in the main urls file, now we specify the sub URL
urlpatterns = [
    path('hi/',views.say_hello)
]