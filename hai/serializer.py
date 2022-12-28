from rest_framework import serializers
from .models import productMainModel,productColourModel,productImageModel
# from .serializer import productColourModelSerailizer,productImageModelserializer

   
        
class productColourModelSerailizer(serializers.ModelSerializer):
    class Meta:
        model=productColourModel
        fields='__all__'
        depth = 1
class productImageModelserializer(serializers.ModelSerializer):
    class Meta:
        model=productImageModel
        fields='__all__'
        depth = 1
        
class ProductSerializer(serializers.ModelSerializer):
    Colour =productColourModelSerailizer(many=True)
    Image = productImageModelserializer(many=True)
    class Meta:
        model=productMainModel
        fields='__all__'
        

        