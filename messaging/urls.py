from django.urls import path
from .views import MessageListCreateView
from .consumers import MessageConsumer

websocket_urlpatterns = [
    path("ws/messages/", MessageConsumer.as_asgi()),
]

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
]
