from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from message.models import Message
from message.serializers import MessageSerializer
from thread.models import Thread


class MessageView(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        """Create Message instance for Thread instance by 'thread_id' request arg."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        thread = Thread.objects.get(id=request.data["thread_id"])
        message = Message(**serializer.validated_data, sender=request.user, thread=thread)
        message.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """Return messages list for any thread. URL: v1/messages/?thread=21"""
        thread = request.query_params.get("thread")
        if thread:
            queryset = self.queryset.filter(thread_id=thread)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response({"message": "Set an id of a Thread."})

    @action(methods=["get"], detail=False)
    def unread_for_user(self, request, pk=None):
        """Return all unread messages for particular User by URL: v1/messages/unread_for_user/?user=1"""
        user = request.query_params.get("user")
        if user:
            unread_messages = Message.objects.select_related("sender").filter(is_read=False)
            count_unread_messages = unread_messages.filter(sender_id=user).count()
            return Response({"message": count_unread_messages}, status=status.HTTP_200_OK)
        return Response({"Unread messages": "Set the User's id."})

    @action(methods=["post"], detail=True)
    def mark_as_read(self, request, pk=None):
        """Mark message as read by URL: v1/messages/1/mark_as_read"""
        message = self.get_object()
        serializer = self.get_serializer(context={"request": request}, data=request.data, instance=message)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Message marked as read."}, status=status.HTTP_200_OK)


