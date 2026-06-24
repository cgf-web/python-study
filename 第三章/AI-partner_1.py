import streamlit as st
import os
from openai import OpenAI

#设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={},
)

st.title("AI智能伴侣")
st.logo("resources/AI_partner.png",)

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

system_prompt="You are a helpful assistant"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# 显示聊天信息
for message in st.session_state.messages:     #
    st.chat_message(message["role"]).write(message["content"])

prompt=st.chat_input("请输入您的问题")     # 获取用户输入的提示词
if prompt:#字符串自动转换为布尔值，非空字符串为True
    st.chat_message("user").write(prompt)      # 将用户提示词展示在输入框中
    print("用户输入：",prompt)      
    print("正在调用 DeepSeek API...")

    st.session_state.messages.append({"role": "user", "content": prompt})  # 将用户提示词添加到会话状态中

    #调用AI模型
    # 创建与DeepSeek AI大模型交互的客户端，使用OpenAI库
    try:
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
        )
        print("<------------ AI 回复 -------------->", response.choices[0].message.content)
        st.chat_message("assistant").write(response.choices[0].message.content)

        #保存大模型的结果
        st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})  # 将AI回复添加到会话状态中


    except Exception as e:
        print(f"\n 调用失败: {e}")
        print("可能的原因：")
        print("1. API Key 无效或过期")
        print("2. 网络连接问题")
        print("3. API 服务暂时不可用")
