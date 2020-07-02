from .admin_views import MyModelView, file_path
from jinja2 import Markup
from flask_admin import form
from app.products.models import Reagent
from flask import url_for
from .forms import BaseJsonForm
from app import db


# This view for model "Model", designed specificaly for handling images
class ImageView(MyModelView):

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
        if not model.product_picture:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                        filename=f"images/{form.thumbgen_filename(model.product_picture)}"))

    # For displaing on main page | Prettifying
    column_formatters = {
            'logo': _list_thumbnail_logo,
            'product_picture' : _list_thumbnail_product
        }
    # Overriding build-in fields with own
    form_extra_fields = {
        'logo': form.ImageUploadField('Logo', base_path=file_path,
                                      thumbnail_size=(100, 100, False)),
        'product_picture': form.ImageUploadField('Product Picture',
                                      base_path=file_path,
                                      thumbnail_size=(100, 100, True))
    }
    column_searchable_list = ('model_name', 'description')


    column_descriptions = dict(
        model_name = "Name of the model",
        description = "Description"
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

    # Collection of excluded form field names.
    form_excluded_columns = ('json_dc')

    # Overriding fields
    form_extra_fields = {
        'packing' : form.Select2TagsField("Packing"),
        'code' : form.Select2TagsField("Code")
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

    # Dictionary of list view column formatters.
    # Prettifying the look of images on the main page
    column_formatters = {
            'bg_image': _thumbnail_image
        }

    # Overriding fields
    form_extra_fields = {
        'bg_image': form.ImageUploadField('Background image', base_path=file_path,
                                      thumbnail_size=(100, 100, True))
                        }


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

    # Dictionary of list view column formatters.
    # Prettifying the look of images on the main page
    column_formatters = {
            'logo': _thumbnail_image
        }

    # Overriding fields
    form_extra_fields = {
        'logo': form.ImageUploadField('Background image', base_path=file_path,
                                      thumbnail_size=(100, 100, True))
                        }


# ISSUE: Handling array of images
# class NewsView(MyModelView):
#     def _thumbnail_image(view, context, model, name):
#         for image in model.images:
#             yield Markup('<img src="%s">' % url_for('static',
#                         filename=f"images/{form.thumbgen_filename(image)}"))
#     column_formatters = {
#             'images': _thumbnail_image
#         }
#     form_extra_fields = {
#         'images': form.ImageUploadField('Background image', base_path=file_path,
#                                       thumbnail_size=(100, 100, True))
#                         }
