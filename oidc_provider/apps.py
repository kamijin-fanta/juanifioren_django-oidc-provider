from django.apps import AppConfig


class OIDCProviderConfig(AppConfig):

    name = 'oidc_provider'
    verbose_name = u'OpenID Connect Provider'
    default_auto_field = 'django.db.models.AutoField'
