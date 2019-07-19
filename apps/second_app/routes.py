from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'$',views.index),
    url(r'generate$',views.generate),
    url(r'reset$',views.reset),
]