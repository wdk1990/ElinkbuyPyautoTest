from poium import Page, Element, Elements


class CustomerPage(Page):
    customer_menu = Element(id_="pytestCustomerMenu", describe="客户管理菜单栏")
    customer_list = Element(id_="pytestCustomerList", describe="客户列表/我的客户菜单")

    last_page = Element(xpath="//td[@id='pytestCustomerListPage']/ul[@class='pagination']/li[last()-1]",describe="最后一页")
    last_sort = Element(xpath="//div[@class='table-responsive']/table/tbody[@id='content']/tr[last()]/td[@id='pytestCustomerListSort']",describe="最后一页序号")

    search_client_rank = Element(name='search_client_rank', describe="客户等级下拉框")
    search_btn = Element(id_='pytestCustomerSearchBtn', describe="搜索按钮")

    pagination = Elements(xpath="//td[@id='pytestCustomerListPage']/ul[@class='pagination']/li", describe="分页")






