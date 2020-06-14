# test_ihrm_login
import logging
import unittest
from api.login_api import LoginApi
# 创建unittest类
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        pass
    # def assert_common(self, http_code, success, code, message, response):
    #     self.assertEqual(http_code, response.status_code)
    #     self.assertEqual(success, response.json().get("success"))
    #     self.assertEqual(code, response.json().get("code"))
    #     self.assertIn(message, response.json().get("message"))
    # 编写登录成功的函数
    def test01_login_success(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,True,10000,"操作成功",response)

    def test02_mobile_is_empty(self):
        response = self.login_api.login({"mobile": "", "password": "1234567"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)

    def test03_mobile_is_not_exists(self):
        response = self.login_api.login({"mobile": "13900000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)

    def test04_password_is_error(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "1234567"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)

    def test05_params_is_none(self):
        response = self.login_api.login({},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)

    def test06_params_is_null(self):
        response = self.login_api.login(None,
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,99999,"抱歉，系统繁忙，请稍后重试！",response)

    def test07_more_params(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456","more_params": "1"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,True,10000,"操作成功",response)

    def test08_less_params_mobile(self):
        response = self.login_api.login({"password": "1234567"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)

    def test09_less_password(self):
        response = self.login_api.login({"mobile":"13800000002"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)

    def test10_params_is_error(self):
        response = self.login_api.login({"mobiles": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)

    def test11_password_is_empty(self):
        response = self.login_api.login({"mobiles": "13800000002", "password": ""},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self,200,False,20001,"用户名或密码错误",response)
