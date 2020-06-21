from .admin_views import MyModelView, file_path
from jinja2 import Markup
from flask_admin import form
from app.products.models import Reagent
from flask import url_for


# This view for model "Model", designed specificaly for handling images
class ImageView(MyModelView):

    def _list_thumbnail(view, context, model, name):
        if not model.logo and not model.product_picture:
            return ''
        if model.logo:
            return Markup('<img src="%s">' % url_for('static',
                        filename=f"images/{form.thumbgen_filename(model.logo)}"))
        else:
            return Markup('<img src="%s">' % url_for('static',
                        filename=f"images/{form.thumbgen_filename(model.product_picture)}"))
    # For displaing on main page
    column_formatters = {
            'logo': _list_thumbnail,
            'product_picture' : _list_thumbnail
        }
    # Overriding build-in fields with own
    form_extra_fields = {
        'logo': form.ImageUploadField('Logo', base_path=file_path,
                                      thumbnail_size=(100, 100, False)),
        'product_picture': form.ImageUploadField('Product Picture',
                                      base_path=file_path,
                                      thumbnail_size=(100, 100, True))
    }


# This view designed specificaly for model "Reagent" for handling custom data
# type JsonDC
class ReagentView(MyModelView):

    def _formatJson(view, context, model, name):
        markup = '<br/>'.join([f'{k}&ensp;{v}' for k,v in model.json_dc.items()])
        return Markup(markup)

    column_formatters = {
        'json_dc': _formatJson
    }

    # ISSUE: Flask-Admin cannot handle custom data type in collumn of the models
    # Need to create custum field to represent json data in form.
    # form_rules = [
    #     form.rules.FieldSet(('reagent_name', 'method', 'json_dc'), "Reagent")
    # ]


# Custom view designed specificaly for handling background images in Slider model
class HomeView(MyModelView):

    def _thumbnail_image(view, context, model, name):
        return Markup('<img src="%s">' % url_for('static',
                    filename=f"images/{form.thumbgen_filename(model.bg_image)}"))

    column_formatters = {
            'bg_image': _thumbnail_image
        }

    form_extra_fields = {
        'bg_image': form.ImageUploadField('Background image', base_path=file_path,
                                      thumbnail_size=(100, 100, True))
                        }


class BrandView(MyModelView):

    def _thumbnail_image(view, context, model, name):
        return Markup('<img src="%s">' % url_for('static',
                    filename=f"images/{form.thumbgen_filename(model.logo)}"))

    column_formatters = {
            'logo': _thumbnail_image
        }

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
