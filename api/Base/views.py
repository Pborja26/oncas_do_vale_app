from rest_framework.response import Response
from rest_framework.views import APIView
from Base import models as basemodels
from Base import serializers as baseserializers
# Create your views here.
class ThemeView(APIView):
   def get(self, request, *args, **kwargs):
        themes = basemodels.theme.objects.all()
        serialized_data = baseserializers.ThemeSerializer(themes, many=True).data

        # Organizando os temas por tipo
        organized_data = {}
        for theme_item in serialized_data:
            theme_type_name = theme_item['theme_type']['name']
            if theme_type_name not in organized_data:
                organized_data[theme_type_name] = []
            organized_data[theme_type_name].append({
                "id": theme_item['id'],
                "name": theme_item['name'],
                "color": theme_item['color'],
            })

        return Response(organized_data)