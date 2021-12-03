from django.conf.urls import url
from . import views



urlpatterns = [
#url(r'^gallery',views.collection,name='gallery'),
url(r'^submitassignment',views.submitassignment,name='assignment'),
url(r'^addquery',views.addquery,name='query')

    
]

