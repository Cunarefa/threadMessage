from rest_framework import routers

from message.views import MessageView

router = routers.SimpleRouter()

router.register(r"messages", MessageView)

message_urlpatterns = []
message_urlpatterns += router.urls
