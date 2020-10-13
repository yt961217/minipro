def common_assert_code(res, code=200):
    """
    对状态码进行断言
    :param res:响应对象
    :param code:状态码
    :return:
    """

    assert res.status_code == code
