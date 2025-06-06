
import unittest


# 自动发现 test 文件夹下所有 test_*.py 文件里的测试用例
loader = unittest.TestLoader()
suite = loader.discover(start_dir='tests', pattern='test_*.py')

# 执行测试
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)


