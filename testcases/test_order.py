import pytest
from utils.yaml_util import read_test_data
from utils.assert_util import assert_resp

# 读取参数化数据
test_data = read_test_data("tesr_order.yaml")

class TestOrder:
    @pytest.mark.parametrize("cases", test_data["create_order"])
    def test_create_order(self, api_client, cases):
        """创建订单"""
        resp = api_client.request(
            method="POST",
            path="/order/create",
            json=cases["params"],
        ).json()
        assert_resp(resp, cases["expected"])