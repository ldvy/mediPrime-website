from .admin_views import MyAdminIndexView, MyModelView, file_path
from .views import ImageView, ReagentView, HomeView, BrandView
 # NewsView

from flask_admin import Admin
from flask_admin import form
from flask_admin.menu import MenuLink

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
admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))
# Ading views to admin panel.
admin.add_views(ImageView(Model, db.session, category="Products"),
                MyModelView(Catalog, db.session, category="Products"),
                MyModelView(Category, db.session, category="Products"),
                MyModelView(ReagentSubsection, db.session, category="Products"),
                ReagentView(Reagent, db.session, category="Products"),
                HomeView(Slider, db.session),
                BrandView(Brand, db.session, category="Company"),
                MyModelView(Service, db.session, category="Company"),
                MyModelView(Job, db.session, category="Company"), MyModelView(NewsCategory, db.session))
                # NewsView(NewsOn, db.session))
