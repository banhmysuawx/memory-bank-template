from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db import transaction
from django.conf import settings
from .models import Prompt
from .serializers import PromptSerializer
import os
import shutil


class PromptViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing prompts.
    list:
        List all prompts (paginated).
    retrieve:
        Get prompt details by ID.
    create:
        Create a new prompt.
    update:
        Update a prompt.
    partial_update:
        Partially update a prompt.
    destroy:
        Delete a prompt.
    clone:
        Clone a prompt (custom action).
    """
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None  # Use global pagination

    @action(detail=True, methods=['post'], url_path='clone', url_name='clone')
    @transaction.atomic
    def clone(self, request, pk=None):
        """
        Clone a prompt by ID. Returns the new prompt.
        This endpoint does NOT require a request body.
        """
        try:
            original = self.get_object()
        except Prompt.DoesNotExist:
            return Response({'detail': 'Prompt not found.'}, status=status.HTTP_404_NOT_FOUND)
        # Read original content
        abs_path = os.path.join(settings.BASE_DIR, original.markdown_path)
        try:
            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            return Response({'detail': 'Failed to read original prompt content.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # Create new prompt (do not require request body)
        serializer = self.get_serializer(data={
            'title': f"{original.title} (Clone)",
            'content': content
        })
        serializer.is_valid(raise_exception=True)
        new_prompt = serializer.save()
        return Response(self.get_serializer(new_prompt).data, status=status.HTTP_201_CREATED)
