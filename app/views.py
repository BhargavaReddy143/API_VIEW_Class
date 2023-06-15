from django.shortcuts import render
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

# Create your views here.


class Product_Apiview(APIView):
    def get(self, request, id):
        PO=Product.objects.all()

        PSD=Product_Serializer(PO, many=True)
        return Response(PSD.data)
    def post(self, request, id):
        PSD=Product_Serializer(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'Msg':'Data Is Inserted'})
        else:
            return Response({'Fail':'Data Is Not Valid'}) 
    def put(self, request, id):
        #id=request.data['id']
        PSO=Product.objects.get(id=id)
        PSD=Product_Serializer(PSO , data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'Msg':'Data Is Updated'})
        else:
            return Response({'Fail':'Updated Data Is Not Valid'})   

    def patch(self, request, id):
        #id=request.data['id']
        PSO=Product.objects.get(id=id)
        PSD=Product_Serializer(PSO , data=request.data, partial=True)
        if PSD.is_valid():
            PSD.save()
            return Response({'Msg':'Partial Update Is Done'})
        else:
            return Response({'Fail':'Updated Data Is Not Valid'}) 
    def delete(self, request, id):
        Product.objects.get(id=id).delete()
        return Response({'Msg':'Data Is Deleted!!'})         