from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import userProfile
from .permissions import IsOwnerProfileOrAdminOrReadOnly
from .serializers import userProfileListSerializer
from django.db.models import Q

# Create your views here.

class UserProfileListAPIView(ListAPIView):
    queryset=userProfile.objects.all().filter(user__is_staff = False)
    serializer_class=userProfileListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()

        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = queryset.filter(
                Q(user__username__icontains=keyword) |
                Q(user__user_id__icontains=keyword) |
                Q(description__icontains=keyword))
        return queryset


class userProfileDetailView(RetrieveUpdateAPIView):
    queryset=userProfile.objects.all()
    serializer_class = userProfileListSerializer
    permission_classes = [IsOwnerProfileOrAdminOrReadOnly]

    lookup_field = "user_id"
