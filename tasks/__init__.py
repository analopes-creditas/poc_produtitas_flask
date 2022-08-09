import settings
from celery import Celery
from core.app import create_app


def make_celery():
   app = create_app()
   celery = Celery(app.import_name, broker=settings.BaseConfig.CELERY_BROKER)
   celery.conf.update(app.config)

   # class ContextTask(celery.Task):
   #    def __call__(self, *args, **kwargs):
   #       with app.app_context():
   #          return self.run(*args, **kwargs)

   # celery.Task = ContextTask
   return celery


celery = make_celery()