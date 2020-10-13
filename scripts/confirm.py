from api.apiFactory import ApiFactory

# print("轮播图:{}".format(ApiFactory.get_home_api().banner_api().json()))
# print("专题栏：{}".format(ApiFactory.get_home_api().theme_api().json()))
# print("最近新品：{}".format(ApiFactory.get_home_api().product_recent_api().json()))

# print("商品分类：{}".format(ApiFactory.get_product_api().product_classify_api().json()))
# print("分类下商品:{}".format(ApiFactory.get_product_api().classify_product_api().json()))
# print("商品信息:{}".format(ApiFactory.get_product_api().product_detail_api().json()))

# print("token:{}".format(ApiFactory.get_user_api().get_token_api().json()))

print("订单列表:{}".format(ApiFactory.get_order_api().order_list_api().json()))
print("创建订单：{}".format(ApiFactory.get_order_api().create_order_api(12, 7).json()))
print("查看订单信息:{}".format(ApiFactory.get_order_api().query_order_api(109).json()))
