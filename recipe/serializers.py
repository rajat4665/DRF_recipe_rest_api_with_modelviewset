from rest_framework import serializers
from recipe.models import Tag , Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'grams')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe for a list view"""
    # ingredients = IngredientSerializer(many=True, read_only=True)
    # tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'time_minutes', 'price',
             # 'tags', 'ingredients'
        )
        read_only_fields = ('id',)


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serialize a recipe detail view"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        read_only_fields = ('id',)
