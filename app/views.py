from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer


# FoodType ViewSet
class FoodTypeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = "__all__"
    ordering_fields = "__all__"
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # Throttling qo'shildi


# Food ViewSet
class FoodViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = "__all__"
    ordering_fields = "__all__"
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # Throttling qo'shildi


# Comment ViewSet
class CommentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["text", "author__username"]
    ordering_fields = ["created"]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # Throttling qo'shildi


# Email Sending View
class SendEmailView(APIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # Throttling qo'shildi

    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject', 'Django Email Subject')
        message = request.data.get('message', 'Default Message Content')
        recipient_email = request.data.get('recipient_email', None)

        if not recipient_email:
            return Response(
                {"error": "Recipient email is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            send_mail(
                subject,
                message,
                'sizning_email@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            return Response(
                {"success": "Email muvaffaqiyatli yuborildi!"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": f"Email yuborishda xatolik: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
