from flask import Blueprint, render_template, views, request,session,redirect,url_for,g
from .decorators import *
from .forms import LoginForm
from .models import CMSUser

bp = Blueprint('cms', __name__, url_prefix='/cms')

# Index
@bp.route('/')
@cms_login_required
def index():
    return render_template('cms/index.html')

# Login
class LoginView(views.MethodView):
    def __init__(self):
        self.context = {}

    def get(self):
        return render_template('cms/login.html',**self.context)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            current_user = CMSUser.query.filter(email==email).first()
            if current_user and current_user.check_password(password):
                session[config.CMS_USER_ID] = current_user.id
                if remember:
                    # 如果设置session.permanent=True，那么过期时间默认31天,此处在配置文件中设置有效期为7天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                self.context['message'] = '邮箱或密码错误'
                return self.get()
        else:
            self.context['message'] = form.errors.popitem()[1][0]
            return self.get()

# Logout
@bp.route('/logout/')
@cms_login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

@bp.route('/profile/')
@cms_login_required
def profile():
    return render_template('cms/profile.html')

bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
