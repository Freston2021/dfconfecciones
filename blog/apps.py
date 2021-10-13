from django.apps import AppConfig


#class BlogConfig(AppConfig):
#    name = 'blog'

################################################################################
#agregado

class UsersConfig(AppConfig):
    name = 'blog'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
