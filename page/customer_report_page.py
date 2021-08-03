from poium import Page, Element, Elements


class CustomerReportPage(Page):
    pagination = Elements(
        xpath="//td[@id='pytestReportListPage']/ul[@class='pagination']/li",
        describe="分页")
    last_page = Element(
        xpath="//td[@id='pytestReportListPage']/ul[@class='pagination']/li[last()-1]",
        describe="最后一页")
    last_sort = Element(
        xpath="//div[@class='table-responsive']/table[@id='report_tab save-stage']/tbody/tr[last()]/td[@id='pytestReportListSort']",
        describe="最后一页序号")

    report_button = Element(id_="pytestReportBtn", describe="报备按钮")

    report_name_input = Element(id_="cust_name", describe="报备名称输入框")
    report_search_button = Element(id_="subBtn", describe="报备检索按钮")
