from rest_framework import serializers
from .models import productMainModel,productColourModel,productImageModel
# from .serializer import productColourModelSerailizer,productImageModelserializer

   
        
class productColourModelSerailizer(serializers.ModelSerializer):
    class Meta:
        model=productColourModel
        fields='__all__'
        
class productImageModelserializer(serializers.ModelSerializer):
    class Meta:
        model=productImageModel
        fields='__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    # color=serializers.PrimaryKeyRelatedField(queryset=productColourModel.objects.all())
    Colour = serializers.SerializerMethodField()
    Image = serializers.SerializerMethodField()
    class Meta:
        many=True
        model=productMainModel
        fields=('id','Title','Description','Price','unique_code','Size','Quality','Colour','Image')
    
    def get_Colour(self, user):
        colour = productColourModel.objects.all()
        return productColourModelSerailizer(colour, many=True, context=self.context).data
    
    def get_Image(self,user):
        image = productColourModel.objects.all()
        return productImageModelserializer(image, many=True, context=self.context).data
        

        