import utils
from api.apiFactory import ApiFactory
import app
import logging
import pytest

@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        """获取token"""
        res = ApiFactory.get_user_api().get_token_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言
        utils.common_assert_code(res)
        assert len(res.json().get('token')) > 0
        # 保存 token 到 app 配置文件中
        app.headers['token'] = res.json().get('token')
        print(app.headers)

    def test_token_verify(self):
        """验证token"""
        res = ApiFactory.get_user_api().token_verify_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言
        utils.common_assert_code(res)
        assert res.json().get('isValid') is True

    def test_user_address(self):
        """获取地址信息"""
        res = ApiFactory.get_user_api().user_address_api()
        # 打印 请求地址，响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言
        utils.common_assert_code(res)
        # 断言信息
        assert False not in [i in res.text for i in ['里斯', '上海市', '123号']]

