from flask_login import current_user, login_user, logout_user
from .forms import LoginForm
from .models import User

from flask_admin import expose
import flask_admin as Admin
from flask_admin import form
from flask_admin.form import rules
from flask_admin.contrib import sqla

from flask_babelex import lazy_gettext as _l

from app import static_folder

from flask import render_template, redirect, url_for, request, flash
import os


# Path for storing image data, based in static_folder
file_path = os.path.join(static_folder, 'media')

# Images in 'static/images'
images = os.listdir(file_path)

# Alowed images extensions
ALOWED_EXTENSIONS = ['gif', 'jpg', 'jpeg', 'png', 'tiff']


# Writing own view for displaying start admin page
class MyAdminIndexView(Admin.AdminIndexView):

    @expose('/')
    def admin_panel(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()


    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        """
        Login view for authentification
        """
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash(_l('Invalid username or password'))
                return redirect(url_for('admin.login_view'))
            login_user(user, remember=form.remember_me.data)

        if current_user.is_authenticated:
            return redirect(url_for('.admin_panel'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()
    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('home.home_view'))


# This is base view from Flask-Admin package
# View specifically designet for authentification validation and base template
# initializing
class MyModelView(sqla.ModelView):
    list_template = 'admin/list.html'
    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    def search_placeholder(self):
        if self.column_searchable_list:
            return ", ".join(
                str(self.column_labels.get(col, col))
                for col in self.column_searchable_list
            )

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('admin.login_view'))
