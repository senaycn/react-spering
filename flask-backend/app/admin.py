from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import User, About, Contact, Experience
admin = Admin(app, name="Admin", template_mode="bootstrap3")


class UserAdminView(ModelView):
    # User modeli ile ilgili özel ayarları burada yapabilirsiniz
    pass


class AboutAdminView(ModelView):
    # About modeli ile ilgili özel ayarları burada yapabilirsiniz
    pass

class ContactAdminView(ModelView):
    # Contact modeli ile ilgili özel ayarları burada yapabilirsiniz
    pass


class ExperienceAdminView(ModelView):
    # Services modeli ile ilgili özel ayarları burada yapabilirsiniz
    pass


admin.add_view(UserAdminView(User, db.session))
admin.add_view(AboutAdminView(About, db.session))
admin.add_view(ContactAdminView(Contact, db.session))
admin.add_view(ExperienceAdminView(Contact, db.session))
