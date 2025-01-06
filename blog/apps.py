from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    This class is the configuration class for the blog app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
