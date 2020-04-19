from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "medical.users"
    verbose_name = "用户管理"

    def ready(self):
        try:
            import medical.users.signals  # noqa F401
        except ImportError:
            pass
