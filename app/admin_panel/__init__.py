from .admin_view import MyAdminIndexView, ImageView, file_path, MyModelView
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.products.models import Model, Catalog, Category
from sqlalchemy.event import listens_for
from flask_admin import form
from app import db
import os


admin = Admin(index_view=MyAdminIndexView(), base_template='admin/master.html', template_mode='bootstrap3')


# Function will delete fiels from folder after model was deleted from admin panel.
@listens_for(Model, 'after_delete')
def del_image(mapper, connection, target):
    if target.logo and target.product_picture:
        # Delete image
        try:
            os.remove(os.path.join(file_path, target.logo))
            os.remove(os.path.join(file_path, target.product_picture))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(os.path.join(file_path,
                              form.thumbgen_filename(target.logo)))
            os.remove(os.path.join(file_path,
                              form.thumbgen_filename(target.product_picture)))
        except OSError:
            pass

# Ading views to admin panel.
admin.add_view(ImageView(Model, db.session))
admin.add_view(MyModelView(Catalog, db.session))
admin.add_view(MyModelView(Category, db.session))
