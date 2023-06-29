import streamlit as st
import zhipuai


st.sidebar.title('DDM AI Chatbox Version 1.0')

function = st.sidebar.selectbox('Function', ['Password', 'API'])
if function == 'Password':
    password = st.sidebar.text_input('Password', type='password')
    if password == '123456':
        st.title('DDM AI Chatbox Version 1.0')
        st.write('Welcome to DDM AI Chatbox Version 1.0')
        st.write('')
    elif password == '':
        st.warning('Password is empty')
        st.stop()
    else:
        st.warning('Wrong password')
        st.stop()


