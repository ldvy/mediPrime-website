from flask_admin.form.fields import Select2TagsField
from wtforms.widgets import FileInput
from werkzeug.utils import secure_filename
from .admin_views import file_path, images, ALOWED_EXTENSIONS
from flask import redirect, url_for, flash
from flask_babelex import lazy_gettext as _l
from PIL import Image
import os


class MultipalImagesField(Select2TagsField):
    widget = FileInput(multiple=True)

    def process_formdata(self, valuelist):
        if self.save_as_list:
            filenames = []
            for file in valuelist:
                filename = secure_filename(file.filename)
                if filename.split('.')[1] not in ALOWED_EXTENSIONS:
                    flash(_l('This file \"{filename}\" extension is not a picture. Please check allowed extensions') + " ,".join(ALOWED_EXTENSIONS))
                    return redirect(url_for('.create_view'))
                filenames.append(filename)
                if filename not in images:
                    image_path = os.path.join(file_path, filename)
                    file.save(image_path)
                    file_thumb, ext = os.path.splitext(image_path)
                    image = Image.open(image_path)
                    image.thumbnail((100, 100), Image.ANTIALIAS)
                    image.save(file_thumb + '_thumb.jpeg', "JPEG")

            self.data = [u"{}".format(f) for f in filenames]
        else:
            self.data = self.coerce(valuelist[0])
