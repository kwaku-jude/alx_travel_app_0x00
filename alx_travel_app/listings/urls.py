from django.urls import path
from .views import (
    listing_list_create, listing_detail,
    booking_list_create, booking_detail,
    review_list_create, review_detail
)

urlpatterns = [
    # Listings API
    path('listings/', listing_list_create, name='listing-list-create'),
    path('listings/<uuid:pk>/', listing_detail, name='listing-detail'),

    # Bookings API
    path('bookings/', booking_list_create, name='booking-list-create'),
    path('bookings/<uuid:pk>/', booking_detail, name='booking-detail'),

    # Reviews API
    path('reviews/', review_list_create, name='review-list-create'),
    path('reviews/<uuid:pk>/', review_detail, name='review-detail'),
]