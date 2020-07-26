from .admin_views import MyAdminIndexView, MyModelView, file_path
from .views import ImageView, ReagentView, HomeView, BrandView, ServiceView,\
    NewsView, NovationView

from flask_admin import Admin
from flask_admin import form
from flask_admin.menu import MenuLink

from flask_babelex import lazy_gettext as _l

from app.products.models import Model, Catalog, Category, ReagentSubsection,\
                                Reagent
from app.home.models import Slider, Novation
from app.company.models import Job, Service, Brand
from app.news.models import NewsOn

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
            for image_path in target.product_picture:
                os.remove(os.path.join(file_path, image_path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(os.path.join(file_path,
                              form.thumbgen_filename(target.logo)))
            for thumb_picture in [image.split('.')[0] + '_thumb.jpeg' for image in target.product_picture]:
                os.remove(os.path.join(file_path, thumb_picture))
        except OSError:
            pass

@listens_for(Novation, 'after_delete')
def del_image(mapper, connection, target):
    if target.bg_image:
        try:
            os.remove(os.path.join(file_path, target.bg_image))
        except OSError:
            pass
        try:
            os.remove(os.path.join(file_path, form.thumbgen_filename(target.bg_image)))
        except OSError:
            pass
 

@listens_for(Slider, 'after_delete')
def del_image(mapper, connection, target):
    if target.bg_image:
        try:
            os.remove(os.path.join(file_path, target.bg_image))
        except OSError:
            pass
        try:
            os.remove(os.path.join(file_path, form.thumbgen_filename(target.bg_image)))
        except OSError:
            pass


admin.add_link(MenuLink(name=_l('Home Page'), url='/', category=_l('Links')))

# Custom views

class CatalogView(MyModelView):
    column_labels = dict(name=_l('name'), name_ru=_l('name ru'), name_uk=_l('name uk'), categories=_l('categories'))

class CategoryView(MyModelView):
    column_labels = dict(name=_l('name'), name_ru=_l('name ru'), name_uk=_l('name uk'), catalog=_l('catalog'), models=_l('models'))

class ReagentSubsectionView(MyModelView):
    column_labels = dict(section_name=_l('section_name'), section_name_ru=_l('section_name_ru'), section_name_uk=_l('section_name_uk'), reagents=_l('reagents'))

class JobView(MyModelView):
    column_labels = dict(position=_l('position'), position_ru=_l('position_ru'),
        position_uk=_l('position_uk'), requirements=_l('requirements'),
        requirements_ru=_l('requirements_ru'), requirements_uk=_l('requirements_uk'),
        responsibilities=_l('responsibilities'), responsibilities_ru=_l('responsibilities_ru'),
        responsibilities_uk=_l('responsibilities_uk'), conditions=_l('conditions'),
        conditions_ru=_l('conditions_ru'), conditions_uk=_l('conditions_uk'))

catalog = CatalogView(Catalog, name=_l('Catalog'), session=db.session, category=_l("Products"))
category = CategoryView(Category, name=_l('Category'), session=db.session, category=_l("Products"))
reagentSubsection = ReagentSubsectionView(ReagentSubsection, name=_l('Reagent Subsection'), session=db.session, category=_l("Products"))
job = JobView(Job, name=_l('Job'), session=db.session, category=_l("Company"))

# Ading views to admin panel.
admin.add_views(ImageView(Model, name=_l('Model'), session=db.session, category=_l("Products")),
                catalog, category, reagentSubsection,
                ReagentView(Reagent, name=_l('Reagent'), session=db.session, category=_l("Products")),
                BrandView(Brand, name=_l('Brand'), session=db.session, category=_l("Company")),
                ServiceView(Service, name=_l('Service'), session=db.session, category=_l("Company")),
                job,
                HomeView(Slider, name=_l('Slider'), session=db.session, category=_l('Home')),
                NovationView(Novation, name=_l('Novation'), session=db.session, category=_l('Home')),
                NewsView(NewsOn, name=_l('News'), session=db.session))
