from api.apiFactory import ApiFactory
import utils
import logging


class TestHomeApi:

    def test_banner_api(self):
        """轮播图"""
        # 请求返回对象
        res = ApiFactory.get_home_api().banner_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))

        # 断言状态码
        utils.common_assert_code(res)
        # 断言id 和 name
        assert res.json().get('id') == 1 and res.json().get('name') == '首页置顶'
        # 断言items长度大于0
        assert len(res.json().get('items')) > 0

    def test_theme_api(self):
        """专题栏"""
        # 请求返回对象
        res = ApiFactory.get_home_api().theme_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言三个id
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        # 断言关键字段 description, topic_img, head_img
        assert False not in [i in res.text for i in ['description', 'topic_img', 'head_img']]

    def test_recent_product_api(self):
        """最近新品"""
        # 请求返回对象
        res = ApiFactory.get_home_api().product_recent_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言新品数量大于0
        assert len(res.json()) > 0
        # 断言关键字段 id， name， price
        assert False not in [i in res.text for i in ['id', 'name', 'price']]

