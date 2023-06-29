import streamlit as st
import zhipuai
import warnings


warnings.filterwarnings("ignore")
st.set_page_config(layout='wide', page_icon='🐶', page_title='担担面AI Chat box')


st.sidebar.title('DDM AI Chat box Version 1.0')

function = st.sidebar.selectbox('Function', ['Password', 'API'])
if function == 'Password':
    password = st.sidebar.text_input('Password', type='password')
    if password == 'dandanzuibang':
        zhipuai.api_key = '14c95ca09607c9c512335cb8f14bce9f.hiDwX89fjf04hpwM'
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


test_prompt = st.text_input('Test prompt')

@st.cache_data
def ai_test(prompt):
    response = zhipuai.model_api.invoke(
        model = 'chatglm_6b',
        prompt = [{'role':'user', 'content':prompt}]
    )

    return response

response = ai_test(test_prompt)
st.write(response['data']['choices'][0]['content'])

