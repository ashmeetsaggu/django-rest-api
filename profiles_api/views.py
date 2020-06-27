from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models




class HelloApiView(APIView) :
    """Test api view"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None) :
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete )' ,
            'Is similar to a traditional django view' ,
            'Gives you the most control over your applicatiin logic' ,
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})


    def post(self, request) :
        """create hello message that accepts name from serializer and does hello w our name"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({ 'message' : message })
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None) :
        """handle updating an object"""
        return Response({'method' : 'PUT'})


    def patch(self, request, pk=None) :
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})


    def delete(self, request, pk=None) :
        """delete an object"""
        return Response({ 'method' : 'DELETE' })



class HelloViewSet(viewsets.ViewSet) :
    """Test api viewset"""
    def list(self, request) :
        """return hello message with lists just like in page of apiview"""
        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more functionality with less code'
        ]
        return Response( { 'message' : 'Hello', 'a_viewset' : a_viewset })

    def create(self, request) :
        """create a new hello msg"""
        serializer = self.serializer_class(data=request.data)
        #retrieve data froms erializer class
        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response( {'message' : message })
        else :
            return Response( serializer.errrs, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None) :
        """handle getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None) :
        """handle updating an object"""
        return Respone({ 'http_method' : 'PUT'})

    def partial_update(self, request, pk=None) :
        """handle updating part of an object"""
        return Response({ 'http_method' : 'PATCH' })

    def destroy(self, request, pk=None) :
        """handle removing of an object"""
        return Response({ 'http_delete' : 'DELETE' })



class UserProfileViewSet(viewsets.ModelViewSet) :
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    
