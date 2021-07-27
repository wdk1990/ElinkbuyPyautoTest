from poium import Page, Element


class LoginPage(Page):
    user_error = Element(xpath="//div[@class='card-body']/form/div[1]/div[@class='invalid-feedback']", describe="用户名提示")
    pwd_error = Element(xpath="//div[@class='card-body']/form/div[2]/div[@class='invalid-feedback']", describe="密码提示")
    all_error = Element(xpath="//div[@class='card-body']/form/div[3]/span", describe="全部错误提示")
