import requests
import app
import logging


class OrderApi:

    def __init__(self):
        # 获取订单列表url
        self.order_list_url = app.base_url + '/order/by_user'
        # 创建订单url
        self.create_order_url = app.base_url + '/order'
        # 查看订单url
        self.query_order_url = app.base_url + '/order/{}'

    def order_list_api(self, page=1):
        """
        订单列表
        :param page: 订单页数
        :return:
        """
        logging.info('订单 - 订单列表')
        data = {"page": page}
        logging.info('请求数据：{}'.format(data))
        return requests.get(self.order_list_url, params=data, headers=app.headers)

    def create_order_api(self, product_id, count):
        """
        创建订单
        :param product_id: 商品id
        :param count: 购买数量
        :return:
        """
        logging.info('订单 - 创建订单')
        # 请求体数据
        data = {"products": [{"product_id": product_id, "count": count}]}
        logging.info('请求数据：{}'.format(data))
        return requests.post(self.create_order_url, headers=app.headers, json=data)

    def query_order_api(self, order_id):
        """
        查看订单信息
        :param order_id: 订单编号
        :return:
        """
        logging.info('订单 - 查看订单信息')
        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
