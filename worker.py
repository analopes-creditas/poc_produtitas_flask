from core.app import celery, create_app


app = create_app()
app.app_context().push()


# workers
from core.tasks.data_product import start_worker
start_worker()
