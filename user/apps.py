from django.apps import AppConfig

"""
Method ready() is used to ensure that the signal handlers defined in the user.signals module are
registered and executed correctly when the app is loaded.
"""


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals
