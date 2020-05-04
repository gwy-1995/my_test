import unittest
import logging
from HTMLTestRunner import HTMLTestRunner
import os



def jia(a,b):

    return (a + b)



class Test2_2(unittest.TestCase):
    """测试加减法"""
    def setUp(self):
        print("测试开始")


    def test_3(self):
        """测试加法"""
        self.a = 1
        self.b = 2
        self.c = jia(self.a,self.b)
        self.assertEqual(self.c,3,"计算错误")






    def test_4(self):
        """测试等于"""
        value = 3
        self.assertEqual(value,4,"计算错误")



    def test_5(self):
        value = 5
        self.assertEqual(value,5,"计算错误")


    def tearDown(self):
        print("测试结束")

if __name__ == '__main__':


    suite = unittest.TestSuite()
    suite.addTest(Test2_2("test_3"))
    suite.addTest(Test2_2("test_4"))
    suite.addTest(Test2_2("test_5"))
    filename = open("//root//test.html", "w",encoding='utf-8')  # "wb"新建或者打开一个二进制文件，写入执行完的数据
    runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title="测试报告",description =u"测试用例明细")
    runner.run(suite)
    filename.close()
    unittest.main()
