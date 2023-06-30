import streamlit as st
import zhipuai
import warnings
import openai

warnings.filterwarnings("ignore")
st.set_page_config(page_icon='🐶', page_title='担担面AI')

st.sidebar.title('DDM AI Chat box Version 1.0')

function = st.sidebar.selectbox('Function', ['Password', 'API'])
if function == 'Password':
    password = st.sidebar.text_input('Password', type='password')
    if password == st.secrets['PASSWORD']:
        openai_api_key = st.secrets['OPENAI_KEY']
        # st.write(st.secrets['API_KEY'])

    elif password == '':
        st.warning('Password is empty')
        st.stop()
    else:
        st.warning('Wrong password')
        st.stop()

else:
    api = st.sidebar.text_input('API', type='text')
    if api != '':
        openai_api_key = api
        pass
    else:
        st.warning('API is empty')
        st.stop()


st.header("💬欢迎呀，这里是AI担担面")
style = st.selectbox('你希望担担面是什么性格呢？', ['诙谐幽默', '严肃认真', '学术专业', '悲观','乐观'])

personality = '。回答问题时要求如下：将自己模仿成一个名字叫 ”担担面“ 的人来回答， 回答风格要求：' + str(style)
temperature = st.radio_slider('离谱程度（越高越离谱）', min_value=0.0, max_value=2, value=0.9)

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

    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)