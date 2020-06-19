from flask_login import current_user, login_user
from .forms import LoginForm
from .models import User

from jinja2 import Markup

from flask_admin import expose
import flask_admin as Admin
from flask_admin import form
from flask_admin.form import rules
from flask_admin.contrib import sqla

from app import static_folder

from flask import render_template, redirect, url_for, request, flash
import os


file_path = os.path.join(static_folder, 'images')


# Writing own view for displaying start admin page
class MyAdminIndexView(Admin.AdminIndexView):

    @expose('/')
    def admin_panel(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('admin.login_view'))
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.admin_panel'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()


# This view will prevent access to the models if user isn't authenticated
class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


# This view for model "Model", designed specificaly for handling images
class ImageView(sqla.ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

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
