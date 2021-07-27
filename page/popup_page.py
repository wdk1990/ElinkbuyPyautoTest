from poium import Page, Element


class PopupPage(Page):
    message_button = Element(id_="message_warn", describe="信息图标按钮")
    message_box = Element(id_="messageBox", describe="信息下拉菜单")
    wait_visit_count = Element(
        xpath="//a[@id='waitVisitCount']/span[@class='dropdown-item-desc']/span[@class='message-num']",
        describe="待回访数据总计"
    )
    wait_visit_quality_count = Element(
        xpath="//a[@id='qualityVisitData']/span[@class='dropdown-item-desc']/span[@class='message-num']",
        describe="待回访优质客户"
    )
