from poium import Page, Element, Elements


class OfferPage(Page):
    offer_button = Element(
        xpath="//div[@class='table-responsive']/table/tbody[@id='content']/tr[1]/td[last()]/a[@id='pytestOfferBtn']",
        describe="报价按钮"
    )
    add_goods_price_btn = Element(id_='pytestAddGoodsPriceBtn', describe="添加货品价格按钮")
    client_id = Element(id_='client_id', describe="隐藏客户id")

    search_keyword = Element(id_='sea_keyword', describe="关键字搜索输入框")
    search_button = Element(xpath="//div[@class='input-group-append']/button[@type='submit']", describe='关键字搜索按钮')
    price_check = Element(xpath="//div[@class='table-responsive']/table/tbody/tr[1]/td[last()]/a", describe="阶梯价格查询按钮")
