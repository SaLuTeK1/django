from rest_framework.views import APIView
from rest_framework.response import Response

class CarListView(APIView):
    def get(self, *args, **kwargs):
        return Response('Hello World get!')

    def post(self, *args, **kwargs):
        data = self.request.data
        prms = self.request.query_params.dict()
        print(data)
        print(prms)
        return Response('Hello World post!')

    def put(self, *args, **kwargs):
        return Response('Hello World put!')

    def patch(self, *args, **kwargs):
        return Response('Hello World patch!')

    def delete(self, *args, **kwargs):
        return Response('Hello World delete!')

class CarDetailView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response('Hello World')