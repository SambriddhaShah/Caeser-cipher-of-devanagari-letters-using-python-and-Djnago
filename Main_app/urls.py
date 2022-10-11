from django.urls import path,include
from Main_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/',views.home),
    path('encrypt/',views.encrypt, name='encrypt'),
    path('decrypt/',views.decrypt, name='decrypt'),
    path('submit/',views.submit, name='submit'),
    path('process/<int:id>',views.process,name='process'),
    path('delete-all', views.delete_all, name= 'delete-all'),
    path('submitt/',views.submitt, name='submitt'),
    path('processs/<int:id>',views.processs,name='processs'),
]