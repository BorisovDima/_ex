from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'chat.apps.chat'

    def ready(self):
        import chat.apps.chat.signals


