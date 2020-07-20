from app import create_app, db
from app.products.models import Catalog, Category, Model, Reagent, ReagentSubsection
from app.admin_panel.models import User
from app.company.models import Job
from cli import register

# Main application instance
app = create_app()
register(app)

# Using decorator to make pre-import to command providen by flask CLI (flask shell)
# Make it easy for testing models
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Catalog': Catalog, 'Category': Category, 'Model': Model,
            'User': User, 'Reagent': Reagent, "ReagentSubsection": ReagentSubsection,
            'Job': Job}
