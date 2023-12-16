import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.set_page_config(
      page_title="밀도 탐구",
      page_icon="./crown.png",
      layout="wide"
)
st.subheader("")
st.title(":magic_wand: 내가 아르키메데스였다면?")
st.header(':white_medium_square: 문제 상황', divider='rainbow')

# 영상 링크 : https://www.youtube.com/watch?v=StynfAWBxuU
video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


st.subheader(':white_medium_square: 왕에게 어떤 결론을 전달해야할까요?', divider='rainbow')
st.image('question.png')
st.subheader(":heavy_check_mark: 데이터로 문제상황 해결하기: 직접 수집한 데이터로 설명해보자!")

show_pages(
    [
        Page("app1.py", "1. 문제 상황 확인", ":magic_wand:"),
        Page("app2.py", "2. 데이터 수집", ":clipboard:"),
        Page("app3.py", "3. 데이터 해석", ":old_key:"),
        Page("app4.py", "4. 문제 해결", ":exclamation:"),
    ]
)





# contents 추가할 떄 마다 비율 나누기
# con1,con2 = st.columns([1.0,2.2])

# image = Image.open('갈릴레이 실험.jpg')
# con1.image(image, caption='자유 낙하에 대한 두 가지 생각')

# con2.subheader("자유 낙하 운동 논쟁: 아리스토텔레스 VS 갈릴레오")
# with con2:
#       st.markdown('질량이 다른 두 물체를 같은 높이에서 동시에 떨어뜨릴 때, 당시 대부분의 사람은 아리스토텔레스의 이론대로 질량이 큰 물체가 먼저 떨어진다고 생각했지만 갈릴레오는 물체에 작용하는 중력의 가속도는 물체의 질량과는 관계없이 일정하기 때문에 질량이 다른 두 물체는 같은 속도로 낙하하며 동시에 떨어질 것이라고 주장했다. 결과는 어땠을까?')
# st.divider()

# st.subheader(':brain: 생각해보기: 나의 예상은?', divider='violet')
# with st.form(key='my_form'):
#         st.markdown('##### :smile: 실험 결과를 예측해보자!')
#         prediction = st.radio(
#         "", 
#         ["**갈릴레오가 맞다(동시에 떨어진다)**", "**아리스토텔레스가 맞다(질량이 큰 물체가 먼저 떨어진다)**"],
#         captions = ["낙하하는데 걸리는 시간은 같으므로 중력 가속도는 질량에 관계 없이 같다.", "질량이 큰 물체의 낙하 시간이 짧으므로 중력 가속도는 질량이 큰 물체가 크다."])

#         submitted = st.form_submit_button("나의 예상은?")
# if submitted:
#     st.write("나는 질량이 다른 두 물체의 자유낙하 결과 ", prediction, "고 생각해!") 
# st.divider()
# st.subheader(":eyes: 눈으로 확인하기: 누가 맞았을까?", divider='violet')
# video_file = open('갈릴레이 실험3.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)

# st.markdown("#### **:bulb: 데이터로 검증하기: ':chart_with_upwards_trend: 프로젝트 1'로 가서 우리도 직접 확인해보자! :heavy_check_mark:**")

# # Specify what pages should be shown in the sidebar, and what their titles and icons
# # should be
