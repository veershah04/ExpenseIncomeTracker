from django.apps import AppConfig


class UserincomeConfig(AppConfig):
    name = 'userincome'

    def ready(self):
        import userincome.signals
