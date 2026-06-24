#PyPI:全称为 Python Package Index，是由Python官方和社区共同维护的Python第三方软件包的官方仓库

#pip:pip是Python官方提供的Python包的管理工具，提供了对Python包的查找、下载、安装、卸载等功能


# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI


# 检查API密钥是否设置
if not os.environ.get('DEEPSEEK_API_KEY'):
    print("错误：未设置 DEEPSEEK_API_KEY 环境变量")
    print("请设置环境变量或在代码中直接指定 API Key")
    exit(1)

# 创建与DeepSeek AI大模型交互的客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

print("正在调用 DeepSeek API...")
try:
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "你是谁"},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    print("\n=== AI 回复 ===")
    print(response.choices[0].message.content)
    print("\n=== 调用成功 ===")

except Exception as e:
    print(f"\n 调用失败: {e}")
    print("可能的原因：")
    print("1. API Key 无效或过期")
    print("2. 网络连接问题")
    print("3. API 服务暂时不可用")

