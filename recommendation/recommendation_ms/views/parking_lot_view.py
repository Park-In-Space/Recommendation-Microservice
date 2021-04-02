from recommendation_ms.models.parking_lot_model import Parking_lot    
from recommendation_ms.serializers.parking_lot_serializer import Parking_lotSerializer
from rest_framework import mixins
from rest_framework import generics

class Parking_lotList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    
    queryset = Parking_lot.objects.all()
    serializer_class = Parking_lotSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Parking_lotDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    
    queryset = Parking_lot.objects.all()
    serializer_class = Parking_lotSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
