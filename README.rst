=====================
robot car wash server
=====================

`Robot Framework`_ is a generic open source test automation framework.

.. _Robot Framework: http://robotframework.org/

Running
-------

::
    # 依赖安装
    pip install -r requirements.txt

    # 测试所有
    robot -d results --pythonpath . -v VERSION:d tests/

    # 测试所有--除了login
    robot -d results --pythonpath . -v VERSION:d -e login tests/

    # 测试所有--除了login和错误用例
    robot -d results --pythonpath . -v VERSION:d -e login -e wrong tests/

    # 测试所有--除了login,错误用例,不登录
    robot -d results --pythonpath . -v VERSION:d -e login -e wrong -e WithoutLogin tests/

    # 测试login
    robot -d results --pythonpath . -v VERSION:d -i login tests/

    # 测试错误用例
    robot -d results --pythonpath . -v VERSION:d -i wrong tests/

    # 测试不登录
    robot -d results --pythonpath . -v VERSION:d -i WithoutLogin tests/
