from rest_framework import routers

from thread.views import ThreadView

router = routers.SimpleRouter()

router.register(r"threads", ThreadView)

thread_urlpatterns = []
thread_urlpatterns += router.urls
