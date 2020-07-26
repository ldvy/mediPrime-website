from .admin_views import MyModelView, file_path
from .forms import BaseJsonForm
from .field import MultipalImagesField

from jinja2 import Markup
from flask import url_for
from flask_login import current_user
from flask_babelex import lazy_gettext as _l
from flask_admin import form
import sqlalchemy



# This view for model "Model", designed specificaly for handling images
class ImageView(MyModelView):
    # form_base_class = MultipleImagesForm
    def _list_thumbnail_logo(view, context, model, name):
        """
        `view` is current administrative view
        `context` is instance of jinja2.runtime.Context
        `model` is model instance
        `name` is property name

        """
        if not model.logo:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                        filename=f"images/{form.thumbgen_filename(model.logo)}"))

    def _list_thumbnail_product(view, context, model, name):
        markup = ''
        for filename in model.product_picture:
            thumb_filename = filename.split('.')[0] + '_thumb.jpeg'
            markup += '<img src="{}">'.format(url_for('static',
                        filename=f"images/{thumb_filename}"))
        return Markup(markup)

    column_labels = dict(model_name=_l('Model name'), model_name_ru=_l('Model name ru'),
        model_name_uk=_l('Model name uk'), logo=_l('Logo'), product_picture=_l('Product pictures'),
        description=_l('Description'), description_ru=_l('Description ru'),
        description_uk=_l('Description uk'), country=_l('Country'),
        country_ru=_l('Country ru'), country_uk=_l('Country uk'),
        brand=_l('Brand'), brand_ru=_l('Brand ru'), brand_uk=_l('Brand uk'),
        category=_l('Category'), video_link=_l('video_link'))

    # For displaing on main page | Prettifying
    column_formatters = {
            'logo': _list_thumbnail_logo,
            'product_picture': _list_thumbnail_product
        }


    form_create_rules  = ('model_name', 'model_name_ru', 'model_name_uk',
            'logo', 'product_picture', 'description', 'description_ru',
            'description_uk', 'country', 'country_ru', 'country_uk',
            'brand', 'brand_ru', 'brand_uk', 'category', 'video_link')

    # Overriding build-in fields with own
    form_extra_fields = {
        'logo': form.ImageUploadField(_l('Logo'), base_path=file_path,
                                      thumbnail_size=(100, 100, False)),
        'product_picture': MultipalImagesField(_l('Product pictures'), save_as_list=True) }

    column_searchable_list = ('model_name', 'description')


    column_descriptions = dict(
        model_name = _l("Name of the model"),
        description = _l("Description"),
    )


# This view designed specificaly for model "Reagent" for handling custom data
# type JsonDC
class ReagentView(MyModelView):
    form_base_class = BaseJsonForm

    def _formatJson(view, context, model, name):
        """
        `view` is current administrative view
        `context` is instance of jinja2.runtime.Context
        `model` is model instance
        `name` is property name

        """
        markup = '<br/>'.join([f'{k}&ensp;{v}' for k,v in model.json_dc.items()])
        return Markup(markup)

    # Dictionary of list view column formatters.
    # Prettifying look of json data on the main page
    column_formatters = {
        'json_dc': _formatJson
    }

    column_labels = dict(reagent_name=_l('reagent_name'), reagent_name_ru=_l('reagent_name_ru'),
        reagent_name_uk=_l('reagent_name_uk'), method=_l('method'), method_ru=_l('method_ru'),
        method_uk=_l('method_uk'), json_dc=_l('json_dc'), subsection=_l('subsection'))

    # Collection of excluded form field names.
    form_excluded_columns = ('json_dc')

    # Overriding fields
    form_extra_fields = {
        'packing' : form.Select2TagsField(_l("Packing")),
        'code' : form.Select2TagsField(_l("Code"))
    }

    def on_model_change(self, form, model, is_created):
        """
        Perform some actions before a model is created or updated.

        Called from create_model and update_model in the same transaction (if it has any meaning for a store backend).

        By default does nothing.

        Parameters:
        form – Form used to create/update model
        model – Model that will be created/updated
        is_created – Will be set to True if model was created and to False if edited
        """

        json_dict = {}
        packing_data = form.packing.data.split(',')
        code_data = form.code.data.split(',')
        for i in range(len(packing_data)):
            try:
                json_dict[packing_data[i]] = code_data[i]
            except IndexError:
                json_dict[packing_data[i]] = None

        model.json_dc = json_dict


# Custom view designed specificaly for handling background images in Slider model
class HomeView(MyModelView):

    def _thumbnail_image(view, context, model, name):
        """
        `view` is current administrative view
        `context` is instance of jinja2.runtime.Context
        `model` is model instance
        `name` is property name

        """
        return Markup('<img src="%s">' % url_for('static',
                    filename=f"images/{form.thumbgen_filename(model.bg_image)}"))

    column_labels = dict(bg_image=_l('bg_image'), title=_l('title'),
        title_ru=_l('title_ru'), title_uk=_l('title_uk'), text=_l('text'),
        text_ru=_l('text_ru'), text_uk=_l('text_uk'), btn_link=_l('btn_link'),
        slide_order_number=_l('slide_order_number'))

    # Dictionary of list view column formatters.
    # Prettifying the look of images on the main page
    column_formatters = {
            'bg_image': _thumbnail_image
        }

    # Overriding fields
    form_extra_fields = {
        'bg_image': form.ImageUploadField(_l('Background image'), base_path=file_path,
                                      thumbnail_size=(100, 100, True))
                }


class NovationView(HomeView):
    column_labels = dict(bg_image=_l('bg_image'), title=_l('title'),
        title_ru=_l('title_ru'), title_uk=_l('title_uk'), text=_l('text'),
        text_ru=_l('text_ru'), text_uk=_l('text_uk'))


class BrandView(MyModelView):

    def _thumbnail_image(view, context, model, name):
        """
        `view` is current administrative view
        `context` is instance of jinja2.runtime.Context
        `model` is model instance
        `name` is property name

        """
        return Markup('<img src="%s">' % url_for('static',
                    filename=f"images/{form.thumbgen_filename(model.logo)}"))

    column_labels = dict(name=_l('name'), name_ru=_l('name ru'), name_uk=_l('name uk'),
        description=_l('Description'), description_ru=_l('Description ru'),
        description_uk=_l('Description uk'), short_description=_l('short description'),
        short_description_ru=_l('short description ru'), short_description_uk=_l('short description uk'),
        country=_l('country'), country_ru=_l('country_ru'), country_uk=_l('country_uk'),
        brand_website=_l('brand_website'), logo=_l('logo'))

    # Dictionary of list view column formatters.
    # Prettifying the look of images on the main page
    column_formatters = {
            'logo': _thumbnail_image
        }

    # Overriding fields
    form_extra_fields = {
        'logo': form.ImageUploadField(_l('Background image'), base_path=file_path,
                                      thumbnail_size=(100, 100, True))
                        }

class ServiceView(MyModelView):

    def _thumbnail_image(view, context, model, name):
        """
        `view` is current administrative view
        `context` is instance of jinja2.runtime.Context
        `model` is model instance
        `name` is property name

        """
        return Markup('<img src="%s">' % url_for('static',
                    filename=f"images/{form.thumbgen_filename(model.icon)}"))

    column_labels = dict(title=_l('title'), title_ru=_l('title_ru'), title_uk=_l('title_uk'),
        icon=_l('icon'), text=_l('text'), text_ru=_l('text_ru'), text_uk=_l('text_uk'))

    # Dictionary of list view column formatters.
    # Prettifying the look of images on the main page
    column_formatters = {
            'icon': _thumbnail_image
        }

    # Overriding fields
    form_extra_fields = {
        'icon': form.ImageUploadField(_l('Icon'), base_path=file_path,
                                      thumbnail_size=(100, 100, True))
                        }


class NewsView(MyModelView):
    def _thumbnail_image(view, context, model, name):
        return Markup('<img src="%s">' % url_for('static',
                    filename=f"images/{form.thumbgen_filename(model.preview_image)}"))
    column_labels = dict(title=_l('title'), title_ru=_l('title_ru'), title_uk=_l('title_uk'),
        pub_date=_l('pub_date'), preview_image=_l('preview_image'),
        text=_l('text'), text_ru=_l('text_ru'), text_uk=_l('text_uk'))

    column_formatters = {
            'preview_image': _thumbnail_image
        }
    form_extra_fields = {
        'preview_image': form.ImageUploadField(_l('Preview imgage'), base_path=file_path,
                                      thumbnail_size=(100, 100, True))
                        }
