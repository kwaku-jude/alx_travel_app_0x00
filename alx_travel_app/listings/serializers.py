from rest_framework import serializers
from .models import User, Listing, Booking, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


from rest_framework import serializers

from .models import Booking, Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['name','description','location','price_per_night']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['start_date','end_date','total_price','status']
