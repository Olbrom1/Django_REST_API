from rest_framework import viewsets
from .serializers import FilmSerializer
from .models import Film
from .serializers import FilmFullSerializer
from rest_framework.response import Response


class FilmViewset(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmFullSerializer(instance)
        return Response(serializer.data)


