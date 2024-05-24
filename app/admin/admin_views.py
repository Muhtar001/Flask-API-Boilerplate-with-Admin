import os.path as op
from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, form
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask_login import current_user
from wtforms import TextAreaField, validators
from wtforms.widgets import TextArea
from app.models.user import User
from extensions import db


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()



class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.isAdmin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

class UserModelView(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    can_view_details = True
    column_exclude_list = ['password', 'about']
    column_details_exclude_list = ['password']
    column_searchable_list = ['first_name', 'last_name', 'email']
    column_filters = ['first_name', 'last_name']
    form_overrides = {
        'about': CKTextAreaField
    }
# TODO:change avatar field into image upload. until then, there would be no avatar

    def is_accessible(self):
        return current_user.is_authenticated and current_user.isAdmin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

admin = Admin(name='mysite', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(UserModelView(User, db.session))