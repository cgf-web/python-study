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
st.logo("resources/AI_partner.png")


system_prompt = """
    你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。规则：
    1. 每次只回1条消息
    2. 禁止任何场景或状态描述性文字，匹配用户的语言
    3. 回复简短，像微信聊天一样
    4. 有需要的话可以用emoji表情，像微信聊天一样
    5. 用符合伴侣性格的方式对话，
    6. 回复的内容，要充分体现伴侣的性格特征
    伴侣性格：
    %s
    你必须严格遵守上述规则来回复用户。
    """

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"

    
# 显示聊天信息
for message in st.session_state.messages:     # 遍历会话状态中的消息    
    st.chat_message(message["role"]).write(message["content"])


client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


#左侧的侧边栏  -with  streamlit中上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    nature=st.text_area("性格",placeholder="请输入性格",value=st.session_state.nature)
    if nick_name and nature:
        st.session_state.nick_name = nick_name
        st.session_state.nature = nature


prompt=st.chat_input("请输入您的问题")     # 获取用户输入的提示词
if prompt:#字符串自动转换为布尔值，非空字符串为True
    st.chat_message("user").write(prompt)      # 将用户提示词展示在输入框中
    print("用户输入：",prompt)      
    print("正在调用 DeepSeek API...")

    st.session_state.messages.append({"role": "user", "content": prompt})  # 将用户提示词添加到会话状态中

    #调用AI模型
    # 创建与DeepSeek AI大模型交互的客户端，使用OpenAI库
    try:
        print([
                {"role": "system", "content": system_prompt%(st.session_state.nick_name, st.session_state.nature)},
                *st.session_state.messages,   # 打印会话状态中的消息到控制台
            ])
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
                *st.session_state.messages,   # 解包会话状态中的消息
            ],
            stream=True,  # 启用流式输出
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
        )
        
        #流式输出
        with st.chat_message("assistant"):
            response_message = st.empty()  # 创建一个空的聊天消息容器
            full_response = ""

            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    response_message.write(full_response)

        #保存大模型的结果
        st.session_state.messages.append({"role": "assistant", "content": full_response})  # 将AI回复添加到会话状态中


    except Exception as e:
        print(f"\n 调用失败: {e}")
        print("可能的原因：")
        print("1. API Key 无效或过期")
        print("2. 网络连接问题")
        print("3. API 服务暂时不可用")
