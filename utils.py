

# 通用断言函数
import json


def assert_common(httpcode, success, code, message, response, self):
    self.assertEqual(httpcode, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言message

# 读取登录数据的函数
# 1 定义读取数据的函数，并从外界接收文件名
def read_login_data(filename):

    # 2 使用内置函数open打开外界传入的文件名
    with open(filename, mode='r', encoding='utf-8') as f:

        # 3 使用内置模块json加载文件
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = list()
        # 4 读取每一组数据，并按照parameterized的要求，拼接数据成一个嵌套元组的形式
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
        # 5 打印结果，并return 返回
        print("提取的结果为：",result_list)
        return result_list

if __name__ == '__main__':
    import app
    filename = app.BASE_DIR + "/data/login_data.json"
    print("filename的路径为：", filename)
    read_login_data(filename)