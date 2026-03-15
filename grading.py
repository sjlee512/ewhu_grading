import streamlit as st
import datetime

st.title("호구조사하기!")

if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# 페이지1
if st.session_state.page == 'page1':
    name = st.selectbox(label="이름을 선택하세요", options=['규잉', '갬', '승메'])

    if st.button("다음 페이지"):
        st.session_state['name'] = name
        st.session_state.page = 'page2'
        st.rerun()

# 페이지2
elif st.session_state.page == 'page2':
    career = st.text_input(label=f"{st.session_state['name']}님의 직업은 무엇입니까")

    if st.button("이전 페이지"):
        st.session_state.page = 'page1'
        st.rerun()

    if st.button("다음 페이지"):
        st.session_state['career'] = career
        st.session_state.page = 'page3' 
        st.rerun()

# 페이지3
elif st.session_state.page == 'page3':
    height = st.number_input(label=f"{st.session_state['name']}님의 키는 얼마입니까", value=160, step=1, min_value=150, max_value=200)
    weight = st.number_input(label=f"{st.session_state['name']}님의 몸무게는 얼마입니까", value=70, step=1, min_value=50, max_value=100)

    if st.button("이전 페이지"):
        st.session_state.page = 'page2'
        st.rerun()

    if st.button("다음 페이지"):
        st.session_state['height'] = height
        st.session_state['weight'] = weight
        st.session_state.page = 'page4' 
        st.rerun()

# 페이지4
elif st.session_state.page == 'page4':
    birth = st.date_input(label=f"{st.session_state['name']}님의 생일은 언제입니까", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(1999, 12,31))

    if st.button("이전 페이지"):
        st.session_state.page = 'page3'
        st.rerun()

    if st.button("다음 페이지"):
        st.session_state['birth'] = birth
        st.session_state.page = 'page5' 
        st.rerun()

# 페이지5
elif st.session_state.page == 'page5':
    marriage = st.checkbox(label="결혼하셨나요?")

    if st.button("이전 페이지"):
        st.session_state.page = 'page4'
        st.rerun()

    if st.button("다음 페이지"):
        st.session_state['marriage'] = marriage
        st.session_state.page = 'page_final' 
        st.rerun()

# 페이지6

elif st.session_state.page == 'page6':
    look = st.slider(label="본인의 외모점수를 매겨주세요", min_value=1, max_value=10)

    if st.button("이전 페이지"):
        st.session_state.page = 'page5'
        st.rerun()

    if st.button("다음 페이지"):
        st.session_state['look'] = look
        st.session_state.page = 'page_final' 
        st.rerun()

# 마지막페이지
if st.session_state.page == 'page_final':
    st.subheader(f"{st.session_state['name']}님")
    st.write(f"생일은 {st.session_state['birth']}이시군요.")
    st.write(f"키와 몸무게는 {st.session_state['height']}cm, {st.session_state['weight']}kg이시구요")
    st.write(f"직업은 {st.session_state['career']}이시네요")
    st.write(f"외모는 살짝아쉽네요")
    st.divider()
    st.write(f"{st.session_state['name']}님의 종합 점수는 C입니다.")
