# djngo db imports
from django.db.models import Q

# rest_framework imports for api views and response
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

# models and its searilizers for api viewsets
from recipe.models import Tag, Ingredient, Recipe
from recipe.serializers import (TagSerializer, IngredientSerializer,
                                RecipeSerializer, RecipeDetailSerializer)


class RecipeView(viewsets.ModelViewSet):
    """
    recipe viewsets which will resposible for all type of crud operations
    """
    permission_classes = (AllowAny, )
    serializer_class = RecipeSerializer
    serializer_action_classes = {
        'create': RecipeDetailSerializer,
        'update': RecipeDetailSerializer
    }
    paginate_by = 5
    queryset = Recipe.objects.all()

    @action(detail=False, methods=['get'], url_path='searchByName')
    def recipe_search_by_name(self, request):
        """
        This is custom function for search recipe by Name
        which will exceute when user pass query param in this url like   searchByName?q=Pizza
        """
        key = {}
        search_key = request.query_params.get("q").lower()
        if search_key:
            key['title__icontains'] = search_key

        results =RecipeSerializer( Recipe.objects.filter(
            **key).order_by('title'), many=True).data
        return Response(results, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='filterByMinPrice')
    def recipe_search_by_min_price(self, request):
        """
        This is custom function for filter recipe by min price
        which will exceute when user pass query param in this url like   filterByMinPrice?q=10
        """
        results = []
        search_key = request.query_params.get("q")
        if search_key:
            results =RecipeSerializer( Recipe.objects.filter(
                price__gte=int(search_key)).order_by('title'), many=True).data
        return Response(results, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='filterByMaxPrice')
    def recipe_search_by_max_name(self, request):
        """
        This is custom function for filter recipe by max price
        which will exceute when user pass query param in this url like   filterByMaxPrice?q=10
        """
        results = []
        search_key = request.query_params.get("q")
        if search_key:
            results =RecipeSerializer( Recipe.objects.filter(
                price__lte=int(search_key)).order_by('title'), many=True).data
        return Response(results, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='filterByTag')
    def recipe_search_by_tag(self, request):
        """
        This is custom function for filter recipe by Tag name
        which will exceute when user pass query param in this url like   filterByTag?q=Burger
        """
        search_key = request.query_params.get("q").lower()
        if search_key:
            cap_search = search_key.capitalize()
        try:
            find_tag = Tag.objects.filter(Q(name=search_key)| Q(name=cap_search)).first()
            data = Recipe.objects.filter(tags__in=[find_tag.id]).order_by('title')
        except:
            data = []
        results = RecipeSerializer(data, many=True).data
        return Response(results, status=status.HTTP_200_OK)


class TagView(viewsets.ModelViewSet):
    """
    TAG viewsets which will resposible for all type of crud operations
    """
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer
    paginate_by = 10
    queryset = Tag.objects.all()


class IngredientView(viewsets.ModelViewSet):
    """
    TAG viewsets which will resposible for all type of crud operations
    """
    permission_classes = (AllowAny, )
    paginate_by = 10
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
