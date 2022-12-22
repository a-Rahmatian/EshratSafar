from dataclasses import fields
from rest_framework import serializers
from EshartApp.models import company,travel,passenger,ticket,terminal,admin1,supporter,city
class travelGet_serializer(serializers.ModelSerializer):
    class Meta:
        model =travel
        exclude=("id","company","travelTime","capacity","price","terminal")


class travelPost_serializer(serializers.ModelSerializer):
    class Meta:
        model=travel
        fields="__all__"


class passengerConfirmation_serializer(serializers.ModelSerializer):
    class Meta:
        model=passenger
        fields="__all__"  



class ticketRegistration_serializer(serializers.ModelSerializer):
    class Meta:
        model=ticket
        exclude=("id",)


class travelCreate_serializer(serializers.ModelSerializer):
    class Meta:
        model=travel
        exclude=("id",)

class supporter_serializer(serializers.ModelSerializer):
    class Meta:
        model=supporter
        exclude=("id",)

class adminLogin_serilizer(serializers.ModelSerializer):
    class Meta:
        model=admin1
        fields=("userAdmin","passAdmin",)

class adminRespond_serializer(serializers.ModelSerializer):
    class Meta:
        model=admin1
        fields="__all__"
    