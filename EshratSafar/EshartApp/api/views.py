from gc import get_objects
#from sys import ps1
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.db.models import Q

from EshartApp.models import terminal,ticket,travel,supporter,admin1,company,passenger
from EshartApp.api.serializers import travelGet_serializer,travelPost_serializer,passengerConfirmation_serializer,ticketRegistration_serializer,travelCreate_serializer,supporter_serializer,adminLogin_serilizer,adminRespond_serializer

class travelRespond_api(APIView):
    def get(self,request): #همه سفر ها را میگیرد
        Travels=travel.objects.all()
        serilizer=travelPost_serializer(Travels,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)

    def post(self,request): #مبدا مقصد تاریخ سفر و نوع سفر را میگرد و تمام سفر های با آن مشخصات را برمیگرداند
        serilizer=travelGet_serializer(data=request.data)
        if serilizer.is_valid():
            p1=serilizer.data["origin"]
            p2=serilizer.data["destination"]
            p3=serilizer.data["travelDate"]
            p4=serilizer.data["travelKind"]
           
            Travels1=travel.objects.filter(Q(origin=p1)&Q(destination=p2)&Q(travelDate=p3)&Q(travelKind=p4))
            serilizer1=travelPost_serializer(Travels1,many=True)
            
            return Response(serilizer1.data,status=status.HTTP_200_OK)

        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request): #تمام اطلاعات سفر را میگیرد و سفر را می سازد
        serilizer=travelCreate_serializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)

    def delete(self,request):
        #باید روی این کار شود
        pass
    
@api_view(["GET"])
def travelDetail_api(request,pk):
    
    try:
        Travel = travel.objects.get(pk=pk)
        serializer = travelPost_serializer(Travel)
        return Response(serializer.data,status=status.HTTP_200_OK)

    except travel.DoesNotExist:
        return Response({"error": {
                            "code": 404,
                            "message": "Article not found!"
                        }}, status=status.HTTP_404_NOT_FOUND)
   
class passengerConfirmation_api(APIView):
    def get(self,request):#لیست تمام مسافران را برمیگرداند
        Passenger=passenger.objects.all()
        serilizer=passengerConfirmation_serializer(Passenger,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    
    def put(self,request):# نام نام خوانوادگی کد ملی جنسیت و تاریخ تولد را میگیرد و مسافر را می سازد
        latest_id = passenger.objects.latest('id').id
        s=int(latest_id)
        serilizer=passengerConfirmation_serializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            s=s+1
            
            return Response(s,status=status.HTTP_201_CREATED)
       
        return Response(status=status.HTTP_404_NOT_FOUND)

class  ticketRegistration_api(APIView):
    def get(self,request):
        Ticket=ticket.objects.all()
        serilizer=ticketRegistration_serializer(Ticket,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serilizer=ticketRegistration_serializer(data=request.data) 
        if serilizer.is_valid():
            serilizer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)


class  supporter_api(APIView):
    def get(self,request):
        Supporter=supporter.objects.all()
        serializer=supporter_serializer(Supporter,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class adminLogin_api(APIView):
    def get(self,rerquest):
        Admin=admin1.objects.all()
        serilizer=adminRespond_serializer(Admin,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)

    def put(self,request):
        serilizer=adminLogin_serilizer(data=request.data)
        if serilizer.is_valid():
            pd=serilizer.data["userAdmin"]
            pf=serilizer.data["passAdmin"]
            f=admin1.objects.filter(Q(userAdmin=pd)&Q(passAdmin=pf))
            #serilizer1=adminRespond_serializer(data=f)
            #Admin=admin1.objects.all()
            serilizer1=adminRespond_serializer(data=f,many=True)
            if serilizer1.is_valid():
                return Response(serilizer1.data,status=status.HTTP_200_OK)

            return Response(data=serilizer1.data,status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_400_BAD_REQUEST)