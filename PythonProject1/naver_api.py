import urllib.request
import urllib.parse
import json
import datetime
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import Toplevel, Text, Scrollbar

def convert_to_power_link(mobile_link):
    # 모바일 링크를 데스크톱 링크로 변환
    try:
        if 'm.news.naver.com' in mobile_link:
            return mobile_link.replace('m.news.naver.com', 'n.news.naver.com')
        return mobile_link
    except:
        return mobile_link

def show_description(description):
    # 새 창 생성
    popup = Toplevel()
    popup.title("상세 내용")
    popup.geometry("600x400")

    # 텍스트 위젯과 스크롤바 생성
    text = Text(popup, wrap=tk.WORD, padx=10, pady=10)
    scrollbar = Scrollbar(popup, command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    # 내용 삽입
    text.insert(tk.END, description.replace('<b>', '').replace('</b>', ''))
    text.config(state='disabled')  # 읽기 전용으로 설정

    # 배치
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(expand=True, fill='both')


def on_double_click(event):
    # 선택된 항목 가져오기
    item = tree.selection()[0]
    description = tree.item(item)['values'][1]  # description은 두 번째 컬럼
    show_description(description)


def on_link_click(event):
    # 선택된 항목의 링크 열기
    item = tree.selection()[0]
    link = tree.item(item)['values'][3]  # link는 네 번째 컬럼
    power_link = convert_to_power_link(link)  # 파워링크로 변환
    webbrowser.open(power_link)


def fetch_news():
    search_keyword = '경제'
    client_id = "8mmT3X1UiUePVGgVQRad"
    client_secret = "PhAKCkU_8o"

    encText = urllib.parse.quote(str(search_keyword))
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "&start=" + str(1) + "&display=100"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)

    if response.getcode() == 200:
        response_body = response.read()
        json_data = json.loads(response_body.decode('utf-8'))
        print('request Success')
    else:
        print("Error Code:" + response.getcode())

    global root, tree
    root = tk.Tk()
    root.title("네이버 뉴스 검색 결과")
    root.geometry("1000x600")  # 창 크기 설정

    # 트리뷰 생성
    tree = ttk.Treeview(root)
    tree["columns"] = ("title", "description", "pubDate", "link")

    # 컬럼 설정
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("title", width=400)
    tree.column("description", width=300)
    tree.column("pubDate", width=100)
    tree.column("link", width=200)

    # 헤더 설정
    tree.heading("title", text="제목")
    tree.heading("description", text="내용")
    tree.heading("pubDate", text="작성일")
    tree.heading("link", text="링크")

    # 스크롤바
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    # 데이터 추가
    for item in json_data['items']:
        title = item['title'].replace('<b>', '').replace('</b>', '')
        description = item['description'].replace('<b>', '').replace('</b>', '')
        power_link = convert_to_power_link(item['link'])  # 파워링크로 변환
        tree.insert("", tk.END, values=(title, description, item['pubDate'], power_link))

    # 이벤트 바인딩
    tree.bind('<Double-1>', on_double_click)  # 더블클릭
    tree.bind('<Return>', on_link_click)  # 엔터 키

    tree.pack(expand=True, fill='both')

    # 도움말 레이블 추가
    help_text = "더블클릭: 본문 보기 / Enter: 링크 열기"
    help_label = tk.Label(root, text=help_text, pady=5)
    help_label.pack()

    root.mainloop()


fetch_news()