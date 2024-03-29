from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose

from flask_login import current_user
from flask_ import redirect, url_for
from flask_admin.form import SecureForm

class AdminMixin:
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('user.login'))

class IndexAdmin(AdminMixin, AdminIndexView):
    pass


class MyAdminView(AdminMixin, ModelView):
    form_base_class = SecureForm

