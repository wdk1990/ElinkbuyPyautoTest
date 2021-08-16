from poium import Page, Element, Elements


class DataPage(Page):
    data_link = Element(partial_link_text='数据统计', describe="数据统计按钮")

    # 客户反馈统计
    fsc_link = Element(link_text='全部客户反馈类型统计', describe="全部客户反馈类型统计")
    fsci_link = Element(link_text='客户反馈类型统计', describe="客户反馈类型统计")
    fsq_link = Element(link_text='问题类型统计', describe="问题类型统计")
    fsb_link = Element(link_text='全部客户反馈次数统计', describe="全部客户反馈次数统计")
    fsbi_link = Element(link_text='客户反馈次数统计', describe="客户反馈次数统计")
    fsr_link = Element(link_text='全部责任人反馈类型统计', describe="全部责任人反馈类型统计")
    fsri_link = Element(link_text='责任人反馈类型统计', describe="责任人反馈类型统计")

    # 产品数据统计
    gsi_link = Element(link_text='热销产品统计', describe="热销产品统计")
    gss_link = Element(link_text='正式订单产品统计', describe="正式订单产品统计")
    gsg_link = Element(link_text='新产品排行榜设置', describe="新产品排行榜设置")

    # 客户回访统计
    vsc_link = Element(link_text='全部回访数/回头率客户统计', describe="全部回访数/回头率客户统计")
    vsci_link = Element(link_text='回访数/回头率客户统计', describe="回访数/回头率客户统计")
    vsi_link = Element(link_text='全部新客户有效回访统计', describe="全部新客户有效回访统计")
    vsa_link = Element(link_text='新客户有效回访统计', describe="新客户有效回访统计")
    vsr_link = Element(link_text='全部公共池客户有效回访统计', describe="全部公共池客户有效回访统计")
    vsal_link = Element(link_text='公共池客户有效回访统计', describe="公共池客户有效回访统计")
    vsp_link = Element(link_text='全部客户回访率统计', describe="全部客户回访率统计")
    vsall_link = Element(link_text='客户回访率统计', describe="客户回访率统计")
    vsvr_link = Element(link_text='客户行业统计', describe="客户行业统计")
    vsav_link = Element(link_text='24小时分配回访率统计', describe="24小时分配回访率统计")
    vsm_link = Element(link_text='维护客服回访统计', describe="维护客服回访统计")
    vsb_link = Element(link_text='客户回访与订单回购统计', describe="客户回访与订单回购统计")
    vsmr_link = Element(link_text='客服有效回访奖励统计', describe="客服有效回访奖励统计")
    vsn_link = Element(link_text='维护客服回访效果统计', describe="维护客服回访效果统计")
    vsrr_link = Element(link_text='维护客服回访回头率', describe="维护客服回访回头率")
    vsrv_link = Element(link_text='报备回访统计', describe="报备回访统计")
    vsq_link = Element(link_text='优质客户回访统计', describe="优质客户回访统计")

    menu_items = Elements(xpath="//*[@id='app']/div/div[7]/section/*[@class='ulBox']", describe="统计菜单列表")
