"""
AI智能伴侣 - 分步练习模板
使用方法：每次只完成一个步骤，确保能运行后再进行下一步
"""

import streamlit as st
import os
from openai import OpenAI

# ==================== 第1步：基础页面配置 ====================
# 任务：运行程序，确认能看到标题和图标
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI智能伴侣")
# st.logo("resources/AI_partner.png")  # 暂时注释掉，避免路径问题

# ==================== 第2步：API客户端配置 ====================
# 任务：确认API密钥已正确设置（可以先跳过，后面再测试）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

system_prompt = "You are a helpful assistant"

# ==================== 第3步：会话状态初始化 ====================
# 任务：理解为什么需要session_state
# 提示：Streamlit每次交互都会重新执行整个脚本
if "messages" not in st.session_state:
    st.session_state.messages = []
    print("✅ 初始化了空的聊天历史")
else:
    print(f"📝 当前有 {len(st.session_state.messages)} 条聊天记录")

# ==================== 第4步：显示历史消息 ====================
# 任务：手动添加几条测试数据，看看能否显示
# 取消下面注释来测试：
# st.session_state.messages = [
#     {"role": "user", "content": "你好"},
#     {"role": "assistant", "content": "你好！有什么可以帮助你的？"}
# ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ==================== 第5步：获取用户输入 ====================
# 任务：在页面上输入文字，确认能在控制台看到输出
prompt = st.chat_input("请输入您的问题")

if prompt:
    print(f"👤 用户输入：{prompt}")
    
    # 5.1 显示用户消息
    st.chat_message("user").write(prompt)
    
    # 5.2 保存用户消息到历史记录
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # ==================== 第6步：调用AI API ====================
    # 任务：先注释掉try-except，直接调用API测试
    print("🔄 正在调用 DeepSeek API...")
    
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
        
        ai_response = response.choices[0].message.content
        print(f"🤖 AI回复：{ai_response}")
        
        # 6.1 显示AI回复
        st.chat_message("assistant").write(ai_response)
        
        # 6.2 保存AI回复到历史记录
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
    except Exception as e:
        print(f"❌ 调用失败：{e}")
        st.error(f"API调用失败：{str(e)}")

# ==================== 练习建议 ====================
# 1. 先完成第1-4步，确保能正常运行并显示测试消息
# 2. 然后添加第5步，测试用户输入功能
# 3. 最后添加第6步，测试API调用
# 4. 每一步都要理解代码的作用，不要只是复制粘贴
# 5. 尝试修改一些参数，看看效果如何变化
