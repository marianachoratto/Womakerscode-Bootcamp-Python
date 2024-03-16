from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #Aqui é o nome da tabela que vai aparecer no site
    verbose_name = 'Módulo geral'
    name = 'base'
