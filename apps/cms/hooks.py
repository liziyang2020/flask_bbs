import config
from flask import session, g
from .views import bp
from .models import CMSUser

#before_request
@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        current_cms_user_id = session.get(config.CMS_USER_ID)
        current_cms_user = CMSUser.query.get(current_cms_user_id)
        if current_cms_user:
            g.current_cms_user = current_cms_user