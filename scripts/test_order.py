from api.apiFactory import ApiFactory
import utils
import logging


class TestOrderApi:

    def test_order_list(self):
        """查看订单列表"""
        res = ApiFactory.get_order_api().order_list_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言 状态码
        utils.common_assert_code(res)
        # 断言是第一页
        assert res.json().get('current_page') == 1
        # 断言数据大于0
        assert len(res.json()) > 0

    def test_create_order(self):
        """创建订单"""
        res = ApiFactory.get_order_api().create_order_api(7, 3)
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言 状态码
        utils.common_assert_code(res)
        assert len(res.json().get('order_no')) > 0 and len(res.json().get('order_id')) > 0
        assert res.json().get('pass') is True

    def test_query_order(self):
        """查看订单详情"""
        res = ApiFactory.get_order_api().query_order_api(105)
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言 状态码
        utils.common_assert_code(res)
        # 断言 订单id
        assert res.json().get('id') == 105
        assert res.json().get('snap_address').get('name') == '里斯'
        assert res.json().get('snap_address').get('mobile') == '15878789898'



