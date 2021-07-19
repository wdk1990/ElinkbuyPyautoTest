from poium import Page, Element


class LoginPage(Page):
    input_staff_name = Element(name='staff_name', describe="登录用户名")
    input_password = Element(name='password', describe="登录密码")
    login_button = Element(css=".card-body>form>div.form-group>button.btn", describe="登录按钮")
    user_error = Element(xpath="//div[@class='card-body']/form/div[1]/div[@class='invalid-feedback']", describe="用户名提示")
    pwd_error = Element(xpath="//div[@class='card-body']/form/div[2]/div[@class='invalid-feedback']", describe="密码提示")
    all_error = Element(xpath="//div[@class='card-body']/form/div[3]/span", describe="全部错误提示")
