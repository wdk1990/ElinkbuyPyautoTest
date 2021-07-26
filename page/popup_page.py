from poium import Page, Element, Elements


class PopupPage(Page):
    input_staff_name = Element(name='staff_name', describe="登录用户名")
    input_password = Element(name='password', describe="登录密码")
    login_button = Element(css=".card-body>form>div.form-group>button.btn", describe="登录按钮")

    message_button = Element(id_="message_warn", describe="信息图标按钮")
    layer_divs = Elements(class_name="layui-m-layer", describe="layer弹窗")
    layer_shades = Elements(class_name="layui-m-layershade", describe="layer弹窗蒙层")
    message_box = Element(id_="messageBox", describe="信息下拉菜单")
    wait_visit_count = Element(
        xpath="//a[@id='waitVisitCount']/span[@class='dropdown-item-desc']/span[@class='message-num']",
        describe="待回访数据总计"
    )
