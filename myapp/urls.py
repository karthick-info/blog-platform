
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from myapp.views import custom_404

handler404 = 'myapp.views.custom_404'  # Update this line
urlpatterns = [
    path("blog/",include("blog.urls")),
    path('admin/', admin.site.urls),
]
