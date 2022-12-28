from hai import views
from django.urls import path
urlpatterns = [
    path('allproduct/',views.ProductList.as_view(),name="allproduct"),
    path('singleproduct/<int:pk>/',views.prodProductDetailWithId,name = 'employee-detail'),
    # path('ProductColor/',views.ProductColor.as_view(),name="allproduct"),
    # path('ProductImage/',views.ProductImage.as_view(),name="allproduct"),

]
