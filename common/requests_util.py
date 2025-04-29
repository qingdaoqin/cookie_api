import requests
import time
from config.env_config import ENV
from requests.exceptions import RequestException

class RequestsUtil:
    def __init__(self):
        self.session = requests.Session()  # 重点：使用Session自动管理Cookie
        self.login_flag = False  # 标记是否已登录

    def _force_login(self):
        """Cookie失效时强制登录"""
        login_url = f"{ENV.BASE_URL}/login"
        resp = self.session.post(
            login_url,
            data={"username": ENV.TEST_USER, "password": ENV.TEST_PWD}
        )
        # 模拟检查登录成功（实际项目根据接口返回判断）
        assert resp.status_code == 200
        self.login_flag = True

    def request(self, method, path, **kwargs):
        """统一请求入口（自动处理Cookie）"""
        url = f"{ENV.BASE_URL}{path}"

        # 未登录时先登录（如首次请求）
        if not self.login_flag and "login" not in path:
            self._force_login()

        # 发送请求（Session会自动携带Cookie）
        response = self.session.request(
            method=method,
            url=url,
            **kwargs
        )

        # 检查Cookie失效（示例：返回302跳转到登录页）
        if response.status_code == 302 and "login" in response.headers.get("Location", ""):
            self._force_login()  # 重新登录
            return self.request(method, path, **kwargs)  # 重试请求

        return response

    def request_with_retry(self, method, url, **kwargs):
        """重试方法复用request"""
        for attempt in range(3):
            try:
                return self.request(method, url, **kwargs)  # 复用基础方法
            except Exception:
                if attempt == 2: raise
                time.sleep(1)

    def check_cookie_valid(self):
        """主动检查cookie是否还有效"""
        resp = self.session.get(f"{ENV.BASE_URL}/api/check_login")
        assert resp.status_code == 200

