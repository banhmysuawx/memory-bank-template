from rest_framework import serializers
from .models import Prompt
from django.conf import settings
import os

class PromptSerializer(serializers.ModelSerializer):
    # Write-only field for input
    content = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Prompt content in Markdown. Stored in a file, not DB."
    )
    # Read-only field for output
    content_read = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Prompt
        fields = ['id', 'title', 'content', 'content_read', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {'help_text': 'Prompt title (max 100 chars)'}
        }

    def get_content_read(self, instance):
        """Read content from markdown file."""
        content = ''
        if instance.markdown_path:
            abs_path = os.path.join(settings.BASE_DIR, instance.markdown_path)
            try:
                with open(abs_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                content = ''
        return content

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Rename 'content_read' to 'content' in output for API compatibility
        data['content'] = data.pop('content_read', '')
        return data

    def create(self, validated_data):
        content = validated_data.pop('content', '')
        prompt = Prompt.objects.create(**validated_data)
        # Save markdown file
        rel_path = os.path.join(
            getattr(settings, 'PROMPT_STORAGE_DIR', 'prompts'),
            f"{prompt.id}.md"
        )
        abs_path = os.path.join(settings.BASE_DIR, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(content)
        prompt.markdown_path = rel_path
        prompt.save(update_fields=['markdown_path'])
        return prompt

    def update(self, instance, validated_data):
        content = validated_data.pop('content', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if content is not None:
            abs_path = os.path.join(settings.BASE_DIR, instance.markdown_path)
            with open(abs_path, 'w', encoding='utf-8') as f:
                f.write(content)
        instance.save()
        return instance
