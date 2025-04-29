# 运行测试+生成Allure报告
pytest && allure serve reports/
开箱即用 ：直接克隆代码，修改config.yaml即可适配新项目
企业级特性 ：
Token自动管理
线程安全的请求封装
多环境一键切换
低维护成本 ：
用例与数据分离（YAML参数化）
公共方法统一维护
如果需要扩展（如数据库校验、Mock服务），可以继续在此基础上添加模块。