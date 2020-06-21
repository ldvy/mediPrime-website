from app import create_app, db
from app.products.models import Catalog, Category, Model, Reagent, ReagentSubsection
from app.admin_panel.models import  User


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Catalog': Catalog, 'Category': Category, 'Model': Model,
            'User': User, 'Reagent': Reagent, "ReagentSubsection": ReagentSubsection}
