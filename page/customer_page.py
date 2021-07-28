from poium import Page, Element,Elements


class CustomerPage(Page):
    customer_menu = Element(id_="pytestCustomerMenu", describe="客户管理菜单栏")
    customer_list = Element(id_="pytestCustomerList", describe="客户列表/我的客户菜单")
    pagings=Elements()