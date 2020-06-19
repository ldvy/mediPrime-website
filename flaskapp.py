from app import create_app, db
from app.products.models import Catalog, Category, Model
from app.admin_panel.models import  User


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Catalog': Catalog, 'Category': Category, 'Model': Model,
            'User': User}
