from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.index, name='index'),
    path('universities', views.universities, name='universities'),
    path('profile/<id>', views.profile, name='profile'),
    path('notification', views.notification, name='notification'),
    path('additional', views.additional, name='additional'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('admission/<category>', views.admission, name='admission'),
    path('login', views.login, name='login')
]