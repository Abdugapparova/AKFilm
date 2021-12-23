from django.contrib import admin
from django.urls import path
from .views import index,regis, results,video,contacts,mainpage,vf,movies,cartoons
from .views_crud import Posts_list, addUser, deleteAccount, updateM


urlpatterns = [
    path('index/',index),
    path('',mainpage),
    path('regis/',addUser,name="Регистрация"), # 
    path('Город героев/',video), #мультик Город героев
    path('video/',video,name="Город героев мультик"),
    path('contacti/',contacts, name="О нас на навигационной панели"), 
    path('voenniyeFilmi/',vf, name="Военные фильмы на навигационной панели"), 
    path('voenniyeFilmi/movies/',movies),
    path('voenniyeFilmi/cartoons/',cartoons),
    path('regis/voenniyeFilmi/',vf),
    path('cartoons/voenniyeFilmi/',vf),
    path('movies/',movies,name="Фильмы на навигационной панели"),
    path('cartoons/movies/',movies),
    path('cartoons/',cartoons,name="Мультфильмы на навигационной панели"),
    path('movies/cartoons/',cartoons),
    path('results/',results),
    path('regis/logout/<pk>/',deleteAccount.as_view()), #нужно ввести свой ид чтобы выйти (ИД который вы указали во время регистрации)
    path('updateM/<pk>/',updateM.as_view(),name='updateM'),
    path('movies/listM/', Posts_list.as_view(), name="listM"), #на странице фильмы в конце ссылка 

]