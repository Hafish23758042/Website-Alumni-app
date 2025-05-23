from django.contrib import admin
from django.urls import include, path  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumni_app.urls')),  
    path('about', include('about.urls')),
    path('contacts', include('contacts.urls'))
]
