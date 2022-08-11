from core.app import create_app
from core.tasks.create_data_product import start_task_create


# start workers
start_task_create()


app = create_app()
app.app_context().push()
