from poium import Page, Element, Elements


class Common(Page):
    input_staff_name = Element(name='staff_name', describe="登录用户名")
    input_password = Element(name='password', describe="登录密码")
    login_button = Element(css=".card-body>form>div.form-group>button.btn", describe="登录按钮")

    layer_divs = Elements(class_name="layui-m-layer", describe="layer弹窗")
    layer_shades = Elements(class_name="layui-m-layershade", describe="layer弹窗蒙层")

    avatar_warn = Element(id_='avatarWarn', describe="右上角用户头像")
    avatar_box = Element(id_='avatarBox', describe="右上角用户头像下拉框")
    logout_btn = Element(id_='logoutBtn', describe="退出登录按钮")

    customer_menu = Element(id_="pytestCustomerMenu", describe="客户管理菜单栏")
    customer_list = Element(id_="pytestCustomerList", describe="客户列表/我的客户菜单")

    customer_report_menu = Element(id_="pytestCustomerReportMenu", describe="报备报价合同栏")
    customer_report_list = Element(id_="pytestCustomerReportList", describe="客户报备列表")
