import utils
import logging
from api.apiFactory import ApiFactory


class TestProductApi:

    def test_product_classify_api(self):
        """商品分类"""
        res = ApiFactory.get_product_api().product_classify_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言
        utils.common_assert_code(res)
        assert len(res.json()) > 0
        assert False not in [i in res.text for i in ['id', 'name', 'topic_img_id']]

    def test_classify_product_api(self):
        """分类下商品"""
        res = ApiFactory.get_product_api().classify_product_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言
        utils.common_assert_code(res)
        assert len(res.json()) > 0
        assert False not in [i in res.text for i in ['id', 'name', 'price']]

    def test_product_det(self):
        """商品信息"""
        res = ApiFactory.get_product_api().product_detail_api(2)
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言
        utils.common_assert_code(res)
        assert res.json().get('id') == 2
        assert res.json().get('name') == '梨花带雨 3个'
