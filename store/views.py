from django.db.models import Q
from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from store.models import Product, Category
from store.serializers import ProductSerializer


def index(request):
    category = Category.objects.all()
    man_category = Category.objects.get(category_name="Man")
    woman_category = Category.objects.get(category_name="Woman")
    kids_category = Category.objects.get(category_name="Kids")
    context = {
        "category": category,
        "man_category": man_category,
        "woman_category": woman_category,
        "kids_category": kids_category,
    }
    return render(request=request, template_name="index.html", context=context)


def search(request):
    all_categories = Category.objects.all()
    products = Product.objects.all()
    is_search = False
    query = request.GET.get('search')
    if query:
        is_search = True
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    context = {
        "category": all_categories,
        "query": query,
        "products": products,
        "is_search": is_search,
    }

    return render(request=request, template_name='search.html', context=context)


class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
