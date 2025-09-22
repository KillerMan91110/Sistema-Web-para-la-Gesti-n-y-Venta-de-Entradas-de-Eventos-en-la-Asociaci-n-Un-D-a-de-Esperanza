from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="index"),  # esta será la portada "/"
]
