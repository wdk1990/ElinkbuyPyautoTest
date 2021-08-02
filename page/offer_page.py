from poium import Page, Element, Elements


class OfferPage(Page):
    offer_button = Element(
        xpath="//div[@class='table-responsive']/table/tbody[@id='content']/tr[1]/td[last()]/a[@id='pytestOfferBtn']",
        describe="报价按钮"
    )


