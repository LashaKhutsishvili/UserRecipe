from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        recipes = self.request.user.recipes.all()
        return recipes

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
