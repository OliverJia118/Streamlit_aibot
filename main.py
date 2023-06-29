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
        pass
    else:
        st.warning('API is empty')
        st.stop()







