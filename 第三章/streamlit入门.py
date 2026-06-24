# Streamlit
# Streamlit是一个开源的Python库，专为数据工程web网站(无需掌握前端技术)及机器学习工程师设计，用来快速基于Python代码构建交互式的web应用。
# 官方网站:https://streamlit.io

# Streamlit是一个开源的Python库，专为数据工程web网站(无需掌握前端技术)设计，用来快速基于Python代码构建交互式的Web应用。
# 1. 安装streamlit: pip install streamlit
# 2.在python文件中引入streamlit模块
# 3.基于streamlit中提供的API来构建Web应用
# 4.运行程序:streamlit run xxxx.py


import streamlit as st


st.set_page_config(
    page_title="streamlit 入门演示",
    page_icon=":cat2:",

    #页面布局，可选值有："wide"、"centered"
    layout="wide",
    #侧边栏初始状态，可选值有："open"、"closed"、"expanded"
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help':'https://www.extremelycoolapp.com/help',
        'Report a bug':"https://www.extremelycoolapp.com/bug",
        'About': "# 这是一个Streamlit入门演示"
    }
)



#大标题
st.title('Streamlit 入门演示')
st.header('Streamlit 一级标题')
st.subheader('Streamlit 二级标题')

st.write("布偶猫，被誉为“猫中仙女”，以其优雅的外表和温顺的性格成为最受欢迎的宠物猫之一。")
st.write("它们体型较大，成年后可达10-20斤，拥有深邃的蓝色眼眸和柔顺的中长毛，毛色多为双色、手套色或重点色，宛如戴着一副可爱的面具。最迷人的是其松弛柔软的体态，当你抱起它时，它会像布偶一样全身放松，信赖地偎依在主人怀中，‘布偶’之名便由此而来。")
st.write("性格是布偶猫最大的魅力。它们极度温顺、安静且粘人，被称为”小狗猫“，喜欢跟随主人走动，享受陪伴。它们通常脾气极好，忍耐力强，能与儿童和其他宠物友好相处，是理想的家庭伴侣。其轻柔的叫声和爱撒娇的天性，能带给主人无尽的温暖与治愈。")
st.write("养护方面，需要定期梳理其丰厚毛发以防止打结，并提供足够的关注与互动。拥有一只布偶猫，就如同拥有了一位温柔优雅、终生依恋的毛茸茸家人。")

st.logo('resources/cat.jpg')
st.image('resources/布偶猫.jpg', width=400)

st.video('resources/布偶猫.mp4')


student_data = {
    "姓名":["王林","贝罗","莫厉海","石萧","李慕婉"],
    "学号":["20260001","20260002","20260003","20260004","20260005"],
    "语文": [98,90,59,29,80],
    "数学":[88,78,65,70,39],
    "英语": [99,89,87,59,62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(student_data)


#文本输入
name=st.text_input("请输入你的名字")
st.write(f"您输入的姓名为：{name}")

#密码输入
password=st.text_input("请输入你的密码",type="password")#type设置为password，表示输入的内容为密码形式，不会显示在屏幕上
st.write(f"您输入的密码为：{password}")

#单选按钮
gender=st.radio("请选择你的性别",["男","女","其他"],index=0)
st.write(f"您选择的性别为：{gender}")

