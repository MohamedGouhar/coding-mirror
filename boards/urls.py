from django.urls import path
from . import views
import boards
urlpatterns = [
path('',views.boards,name='boards'),
path('boards/<int:board_id>/',views.board_topics,name='board_topics')
]
