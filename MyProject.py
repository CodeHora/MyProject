### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
### ㅡㅡㅡㅡㅡㅡㅡ< 프로젝트 Dev Logs App> ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


# excel_file_path = 'D:\\foldername\\filename.xlsm'
# st.title('이것은 타이틀 입니다')
# st.markdown("Text can be **bold**, _italic_, or ~~strikethrough~~.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
#🐀🐂🐅🐇  🐉🐍🐎🐏   🐒🐓🐕‍🦺🐖
#자축인묘 진사오미 신유술해



import streamlit as st
import pandas as pd
import random


'''메인 표지'''
st.divider()
#input image right sort
# st.image('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', width=30)
st.image('./images/[bing_dalle]main.jpg', width=400, caption='My Private Project 2023', use_column_width=False)
st.title('Dvelopment TimeLine')
st.markdown("본 페이지는 '홍지호'님의 개인 프로젝트 입니다.")
#사이트 내용에대한 설명문
st.markdown("-년도별 개발작업물 List")
st.divider()

'''년도별 작업내용'''


#### <빈 데이터 프레임>ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


#### 빈 프로젝트 데이터프레임 생성


# df23 = pd.DataFrame(
#     {
#         "Category" : ["Dev", "Work", "Work"],
#         "name": ["-", "-", "-"],
#         "url": ["-", "-", "-"],
#         "stars": ["0", "0", "0"], #[random.randint(0, 5) for _ in range(3)],
#         "Complite volume": ["0", "0", "0"], #[[random.randint(0, 100) for _ in range(30)] for _ in range(3)],
#         "Info" : ["-", "-", "-"]
#     }

# )
    
    
# st.dataframe(
#     df23,
#     column_config={
#         "Category" : st.column_config.Column(
#             "Category",
#             help="프로젝트의 분류를 표시합니다.",
#             width=30,
#         ),
#         "name": st.column_config.Column(
#             "Project name",
#             help="담당 프로젝트명",
#             width=100,
#         ),
#         "stars": st.column_config.NumberColumn(
#             "Difficult",
#             width=30,
#             help="주관적인 프로젝트의 작업 난이도를 표시합니다.",
#             format="%d ⭐",
#         ),
#         "url": st.column_config.LinkColumn(
#             "App URL",
#             width=100,
#         ),
#         "Complite volume": st.column_config.ProgressColumn(
#             "Complite volume",
#             width=80,
#             help="프로젝트의 작업 진행도를 표시합니다.",
#             format="%f%%",
#             min_value=0,
#             max_value=100,
#         ),
#         "Info" : st.column_config.LinkColumn(
#             "Info",
#             width=100,
#             help="프로젝트에 대한 설명을 표시합니다.",
#         ),
    
#     },
#     hide_index=True,
#     use_container_width = True,    
# )










###[ 2022년 작업물 ]ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

st.markdown("##### [ - 2022 🐅 ]")
# df_url = ["https://roadmap.streamlit.app", "-", "https://issues.streamlit.app"]

df = pd.DataFrame(
    {   
        "Category" : ["Dev", "Work", "Work"],
        "name": ["정사영상편집", "데이터관리", "QGIS 수치지도작업"],
        "url": ["https://roadmap.streamlit.app", "-", "-"],
        "stars": ["3","1","1"], #[random.randint(0, 5) for _ in range(3)],
        "Complite volume": ["80", "100", "100"], #[[random.randint(0, 100) for _ in range(30)] for _ in range(3)],
        "Info" : ["국토정보플랫폼 정사영상 편집.",
                  "이미지 파일관리",
                  "QGIS를 Shp생성 및 데이터 입력"]
    }
)

# function(df_url[0]) { return '<a href=' + df_url[0].value + '> 🖱️ </a>' }
# st.markdown(df.url[0])
st.dataframe(
    df,
    column_config={
        
        "Category" : st.column_config.Column(
            "Category",
            help="프로젝트의 분류를 표시합니다.",
            width=30,
        ),
        "name": st.column_config.Column(
            "Project name",
            help="담당 프로젝트명",       
        ),            
        "stars": st.column_config.NumberColumn(
            "Difficult",
            width=30,
            help="주관적인 프로젝트의 작업 난이도를 표시합니다.",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn(
            "App URL",                                              
            width=100,
        ),
        "Complite volume": st.column_config.ProgressColumn(
            "Complite volume",
            width=80,
            help="프로젝트의 작업 진행도를 표시합니다.",
            format="%f%%",
            min_value=0,
            max_value=100,
        ),
        "Info" : st.column_config.LinkColumn(
            "Info",                                                      
            width=100,
            help="프로젝트에 대한 설명을 표시합니다.",
        ),
    },
    hide_index=True,
    use_container_width = True,
    
)



###[ 2023년 작업물 ]ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

st.markdown("##### [ - 2023 🐇 ]")

Info_2023 = '''기계설비 성능점검 및 보고서 작성 \n
보고서 자동화
'''
st.markdown(Info_2023)

#### 빈 프로젝트 데이터프레임 생성
df23 = pd.DataFrame(
    {
        "Category" : ["Dev", "Work", "Work"],
        "name": ["-", "-", "-"],
        "url": ["-", "-", "-"],
        "stars": ["0", "0", "0"], #[random.randint(0, 5) for _ in range(3)],
        "Complite volume": ["0", "0", "0"], #[[random.randint(0, 100) for _ in range(30)] for _ in range(3)],
        "Info" : ["-", "-", "-"]
    }

)
    
    
st.dataframe(
    df23,
    column_config={
        "Category" : st.column_config.Column(
            "Category",
            help="프로젝트의 분류를 표시합니다.",
            width=30,
        ),
        "name": st.column_config.Column(
            "Project name",
            help="담당 프로젝트명",
            width=100,
        ),
        "stars": st.column_config.NumberColumn(
            "Difficult",
            width=30,
            help="주관적인 프로젝트의 작업 난이도를 표시합니다.",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn(
            "App URL",
            width=100,
        ),
        "Complite volume": st.column_config.ProgressColumn(
            "Complite volume",
            width=80,
            help="프로젝트의 작업 진행도를 표시합니다.",
            format="%f%%",
            min_value=0,
            max_value=100,
        ),
        "Info" : st.column_config.LinkColumn(
            "Info",
            width=100,
            help="프로젝트에 대한 설명을 표시합니다.",
        ),
    
    },
    hide_index=True,
    use_container_width = True,    
)
