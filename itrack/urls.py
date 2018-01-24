
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questionnaire/',  include('questionnaire.urls')),
    path('', include('main.urls') ),
    path('users/', include('users.urls')),
]
