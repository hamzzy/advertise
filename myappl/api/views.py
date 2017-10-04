from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from ..models import Category,Ads,UserProfile,User
from .serializer import CatSerializer,AdsSerializer,UserSerializer,userSerializer



class CatListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
class CatDetailView(RetrieveAPIView):
   queryset = Category.objects.all()
   serializer_class = CatSerializer

class AdsListView(ListCreateAPIView):
   queryset = Ads.objects.all()
   serializer_class = AdsSerializer

class UsersListView(ListCreateAPIView):
   queryset = UserProfile.objects.all()
   serializer_class = UserSerializer
class userListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer


