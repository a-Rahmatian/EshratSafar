from django.urls import path
from EshartApp.api.views import travelRespond_api,travelDetail_api,passengerConfirmation_api,ticketRegistration_api,supporter_api
urlpatterns = [
    path("travelRespond/",travelRespond_api.as_view(),name="travel-respond"),
    path("travelRespond/<int:pk>/",travelDetail_api,name="travelDetail_api"),
    path("passengerConfirmation_api/",passengerConfirmation_api.as_view(),name="passengerConfirmation_api"),
    path("ticketRegistration_api/",ticketRegistration_api.as_view(),name="ticketRegistration_api"),
    path("supporter_api/",supporter_api.as_view(),name="supporter_api"),
    
]
 