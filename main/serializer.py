from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class ProductinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productinfo
        fields = '__all__'



class AboutusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus
        fields = '__all__'


class ProductfaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productfaq
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class FaktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakt
        fields = '__all__'

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = '__all__'


class AboutteaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abouttea
        fields = '__all__'

class IjtimoiySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ijtimoiy
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"
