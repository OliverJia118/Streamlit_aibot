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
        zhipuai.api_key = st.secrets['API_KEY']
        # st.write(st.secrets['API_KEY'])
        st.title('Welcome to DDM AI Chat box Version 1.0')
        st.write('')
    elif password == '':
        st.warning('Password is empty')
        st.stop()
    else:
        st.warning('Wrong password')
        st.stop()

else:
    api = st.sidebar.text_input('API', type='text')
    if api != '':
        zhipuai.api_key = api
        pass
    else:
        st.warning('API is empty')
        st.stop()

# test_prompt = st.text_input('担担面你好！')
#
#
# @st.cache_data
# def ai_test(prompt):
#     response = zhipuai.model_api.invoke(
#         model='chatglm_6b',
#         prompt=[{'role': 'user', 'content': prompt}],
#         temperature=0.9,
#         top_p=0.7,
#         incremental=True
#     )
#
#     return response
#
#
# if test_prompt != '':
#     response = ai_test(test_prompt)
# else:
#     st.warning('Text is empty')
#     st.stop()
# # response = ai_test(test_prompt)
# st.write(response['data']['choices'][0]['content'])


openai_api_key = st.secrets['OPENAI_KEY']
st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "担担面有何可为您效劳?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt+str(',请以担担面自称，并且回答问题开始加入:担担面跟你讲哦')})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=st.session_state.messages)
    msg = response.choices[0].message

    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)