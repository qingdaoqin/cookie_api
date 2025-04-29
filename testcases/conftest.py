import pytest
from common.requests_util import RequestsUtil

@pytest.fixture(scope="function") #每个用例独立Session
def api_client():
    client = RequestsUtil()
    client._force_login()
    yield client
    # 下方可做其它操作，比如清理测试数据