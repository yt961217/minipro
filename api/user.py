import requests
import app
import logging


class UserApi:

    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + '/token/user'
        # token验证
        self.token_verify_url = app.base_url + '/token/verify'
        # 获取地址信息
        self.user_address_url = app.base_url + '/address'

    def get_token_api(self):
        """获取token"""
        logging.info('用户 - 获取token')
        # 请求体数据
        data = {'code': app.code}
        logging.info('请求数据：{}'.format(data))
        return requests.post(self.get_token_url, headers=app.headers, json=data)

    def token_verify_api(self):
        """验证token"""
        logging.info('用户 - 验证token')
        # 请求体数据
        data = {"token": app.headers.get('token')}
        logging.info('请求数据：{}'.format(data))
        return requests.post(self.token_verify_url, headers=app.headers, json=data)

    def user_address_api(self):
        """获取地址信息"""
        logging.info('用户 - 获取地址信息')
        return requests.get(self.user_address_url, headers=app.headers)
