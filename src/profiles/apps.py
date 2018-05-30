from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
    verbose_name = 'User Profiles'

    def ready(self):
        from . import signals
