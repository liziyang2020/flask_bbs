from wtforms import Form,StringField,IntegerField
from wtforms.validators import InputRequired,Length,Email

class LoginForm(Form):
    email = StringField(validators=[Email(message='邮箱格式有误！'),InputRequired('请输入邮箱')])
    password = StringField(validators=[Length(min=6,max=20,message='密码必须在6-20位之间')])
    remember = IntegerField()