from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name="index"),                   #url for index view function.
    path('increment/',increment,name="increment"), #url for incriment view function.
    path('reset/',reset,name="reset"),             #url for reset view function.
    path('decrement/',decrement,name="decrement"), #url  for decriment view  function.

]
