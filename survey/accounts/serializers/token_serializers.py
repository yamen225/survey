from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def create(self, validated_data):
        return super(MyTokenObtainPairSerializer).create(validated_data)

    def update(self, instance, validated_data):
        return super(MyTokenObtainPairSerializer).update(instance, validated_data)

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['fav_color'] = user.fav_color
        return token
