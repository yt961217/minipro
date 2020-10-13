import requests
import app
import logging


class ProductApi:
    """商品api"""

    def __init__(self):
        # 商品分类
        self.product_classify_url = app.base_url + '/category/all'
        # 分类下商品
        self.classify_product_url = app.base_url + '/product/by_category'
        # 商品信息
        self.product_detail_url = app.base_url + '/product/{}'

    def product_classify_api(self):
        """商品分类"""
        logging.info('商品 - 商品分类')
        return requests.get(self.product_classify_url)

    def classify_product_api(self, id=2):
        """
        分类下商品
        :param id: 分类id
        :return:
        """
        logging.info('商品 - 分类下商品')
        # 请求数据
        data = {'id': id}
        logging.info('请求数据：{}'.format(data))
        return requests.get(self.classify_product_url, params=data)

    def product_detail_api(self, num=2):
        """
        商品信息
        :param num:商品id
        :return:
        """
        logging.info('商品 - 商品信息')
        return requests.get(self.product_detail_url.format(num))
