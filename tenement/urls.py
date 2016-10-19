from django.conf.urls import url
from tenement import views
urlpatterns = [
        url(r'^tenement/$', views.index,name='CarShopInfo'),
]
