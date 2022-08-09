from core.app import create_app
from core.tasks.data_product import create_product


# start workers
create_product()


app = create_app()
app.app_context().push()
