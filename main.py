import streamlit as st
import requests
import os

st.title("社群貼文自動生成器")

product = st.text_input("請輸入產品名稱或主題：")
feature = st.text_area("請輸入產品特色或推廣重點：")
language = st.selectbox("選擇輸出語言：", ["繁體中文", "英文"])

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

if st.button("生成貼文"):
    prompt = f"請用{language}撰寫一則 Instagram 貼文內容，主題為：{product}，產品特色如下：{feature}，並附上熱門 Hashtag。"
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }
    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
        headers=headers,
        json=payload
    )
    result = response.json()
    st.subheader("生成內容：")
    st.write(result[0]["generated_text"] if isinstance(result, list) else result)

st.title("留言回覆 AI 助理")
comment = st.text_input("輸入 IG 留言：")
tone = st.selectbox("選擇回覆語氣：", ["幽默", "專業", "促銷"])

if st.button("產生回覆"):
    reply_prompt = f"針對以下 IG 留言，用{tone}語氣撰寫一則友善的回覆：\n留言：{comment}"
    payload = {
        "inputs": reply_prompt,
        "parameters": {"max_new_tokens": 80}
    }
    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
        headers=headers,
        json=payload
    )
    result = response.json()
    st.subheader("AI 回覆內容：")
    st.write(result[0]["generated_text"] if isinstance(result, list) else result)
