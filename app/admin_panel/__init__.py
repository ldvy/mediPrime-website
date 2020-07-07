from .admin_views import MyAdminIndexView, MyModelView, file_path
from .views import ImageView, ReagentView, HomeView, BrandView, ServiceView

from flask_admin import Admin
from flask_admin import form
from flask_admin.menu import MenuLink

from flask_babel import lazy_gettext as _l

from app.products.models import Model, Catalog, Category, ReagentSubsection,\
                                Reagent
from app.home.models import Slider
from app.company.models import Job, Service, Brand
from app.news.models import NewsCategory, NewsOn

from sqlalchemy.event import listens_for
from app import db
import os


admin = Admin(index_view=MyAdminIndexView(name=_l('Home')), base_template='admin/master.html', template_mode='bootstrap3')


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
admin.add_link(MenuLink(name=_l('Home Page'), url='/', category=_l('Links')))
# Ading views to admin panel.
admin.add_views(ImageView(Model, db.session, category=_l("Products")),
                MyModelView(Catalog, db.session, category=_l("Products")),
                MyModelView(Category, db.session, category=_l("Products")),
                MyModelView(ReagentSubsection, db.session, category=_l("Products")),
                ReagentView(Reagent, db.session, category=_l("Products")),
                BrandView(Brand, db.session, category=_l("Company")),
                ServiceView(Service, db.session, category=_l("Company")),
                MyModelView(Job, db.session, category=_l("Company")),
                MyModelView(NewsCategory, db.session),
                HomeView(Slider, db.session))
                # NewsView(NewsOn, db.session))
