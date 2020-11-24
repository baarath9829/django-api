from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChartData, chartModel, profileModel
from .serializers import ChartDataSerializers, ChartSerializers, ProfileSerializers
    

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def ChartDataView(request):
    if request.method == 'GET':
        resultset = ChartData.objects.all()
        serialized_data = ChartDataSerializers(resultset,many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ChartDataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        resultset = ChartData.objects.get(id=2)
        serializer = ChartDataSerializers(resultset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        resultset = ChartData.objects.get(id=4)
        resultset.delete()
        return Response(status=status.HTTP_200_OK)
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)   
@api_view(['GET'])
def chartdata(request,id):
    if request.method == 'GET':
        result = ChartData.objects.get(id=id)
        serializer = ChartDataSerializers(result)
        return Response(serializer.data,status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def test(request):
    chartresult = chartModel.objects.all()
    profileresult = profileModel.objects.all()
    serializer = ChartSerializers(chartresult,many=True) 
    print(chartresult)
    print(serializer.data)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def profile(request):
    if request.method == 'GET': 
        profileresult = profileModel.objects.all()
        serializer = ProfileSerializers(profileresult,many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','POST','PUT'])
def chart(request):
    if request.method == 'GET':
        name = request.GET.get('name','') 
        result = chartModel.objects.filter(name=name)
        serializer = ChartSerializers(result,many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = ChartSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        name = request.POST['name']
        day = request.POST['day']
        print(name)
        print(day)
        resultset = chartModel.objects.get(name=name,day=day) 
        serializer = ChartSerializers(resultset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)