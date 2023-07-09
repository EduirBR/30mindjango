from django.urls import path
from .views import home, create_post, post
urlpatterns = [
    path('', home, name='home'),
    path('newpost/', create_post, name='create_post'),
    path('<int:id>/', post, name='post')
]
