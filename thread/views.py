from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from thread.models import Thread
from thread.serializers import ThreadSerializer


class ThreadView(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        user = request.query_params.get("user")
        queryset = self.queryset.filter(participants__in=[user])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)





