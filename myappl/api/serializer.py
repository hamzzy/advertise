from rest_framework.serializers import ModelSerializer
from myappl.models import Ads,Category,UserProfile,User

class CatSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','slug']
class AdsSerializer(ModelSerializer):
        class Meta:
          model = Ads
          fields = [ 'name','text','phone','price','picture','location','category','user','timestamp']


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user','location','picture']
class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
