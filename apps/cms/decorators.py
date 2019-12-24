from functools import wraps
from flask import session,redirect,url_for
import config


def cms_login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if session.get(config.CMS_USER_ID):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('cms.login'))
    return inner