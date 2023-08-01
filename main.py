import streamlit as st
import warnings
import openai

warnings.filterwarnings("ignore")
st.set_page_config(page_icon=':robot:', page_title='担担面AI')

st.sidebar.title('DDM AI Chat box Version 1.0')

function = st.sidebar.selectbox('Function', ['Openai', '智谱AI'])  # 创建一个侧边栏选择框，用户可以选择功能，包括Openai和智谱AI
if function == 'Openai':  # 如果用户选择了Openai功能
    password = st.sidebar.text_input('Password', type='password')  # 要求用户输入密码
    if password == st.secrets['PASSWORD']:  # 如果输入的密码与存储的密码匹配
        openai_api_key = st.secrets['OPENAI_KEY']  # 显示Openai的API密钥
    elif password == '':  # 如果密码为空
        st.warning('Password is empty')  # 显示警告信息：密码为空
        openai_api_key = ''  # 设置Openai的API密钥为空
        st.stop()  # 停止执行后续代码
    else:  # 如果密码错误
        st.warning('Wrong password')  # 显示警告信息：密码错误
        openai_api_key = ''  # 设置Openai的API密钥为空
        st.stop()  # 停止执行后续代码


    st.header("💬欢迎呀，这里是OpenAI担担面")
    style = st.selectbox('你希望担担面是什么性格呢？', ['严肃认真', '诙谐幽默', '学术专业', '悲观', '乐观'])

    personality = '。回答问题时要求如下：将自己模仿成一个名字叫 ”担担面“ 的人来回答， 回答风格要求：' + str(style)
    temperature = st.slider('离谱程度（越高越离谱）', min_value=0.0, max_value=2.0,step=0.1, value=0.9)
    top_p = st.slider('靠谱程度（越高越靠谱）', min_value=0.0, max_value=1.0, step=0.1, value=0.95)

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "担担面有何可为您效劳?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"].replace(personality,''))

    if prompt := st.chat_input():

        openai.api_key = openai_api_key
        st.session_state.messages.append({"role": "user", "content": prompt+str(personality)})
        st.chat_message("user").write(prompt)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=st.session_state.messages,
                                                temperature=temperature)
        msg = response.choices[0].message
        st.write(msg)
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

else:
    st.write('智谱AI')