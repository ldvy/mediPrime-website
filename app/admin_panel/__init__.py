from .admin_views import MyAdminIndexView, MyModelView, file_path
from .views import ImageView, ReagentView, HomeView, BrandView
 # NewsView

from flask_admin import Admin
from flask_admin import form

from app.products.models import Model, Catalog, Category, ReagentSubsection,\
                                Reagent
from app.home.models import Slider
from app.jobs.models import Job, Service, Brand
from app.news.models import NewsCategory, NewsOn

from sqlalchemy.event import listens_for
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
admin.add_views(ImageView(Model, db.session), MyModelView(Catalog, db.session),
                MyModelView(Category, db.session), MyModelView(ReagentSubsection, db.session),
                ReagentView(Reagent, db.session), HomeView(Slider, db.session),
                BrandView(Brand, db.session), MyModelView(Service, db.session),
                MyModelView(Job, db.session), MyModelView(NewsCategory, db.session))
                # NewsView(NewsOn, db.session))
