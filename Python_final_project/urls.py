
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("resumesite.urls")),  # url of our main app/website (resumesite)

]
