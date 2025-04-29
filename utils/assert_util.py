def assert_resp(resp, expected:dict):
    """增强断言：支持多字段校验"""
    for key, value in expected.items():
        assert resp.get(key) == value, f"断言失败：{key}应为{value}, 实际为[{resp.get(key)}]"