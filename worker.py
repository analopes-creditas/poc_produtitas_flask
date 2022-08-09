import tasks
from core.app import create_app

app = create_app()
app.app_context().push()

# # workers
from tasks.data_product import start_worker
start_worker()
