import streamlit as st
import requests
import os

st.set_page_config(page_title="AI 社群內容生成器", layout="centered")
st.title("📱 社群貼文自動生成器")

product = st.text_input("請輸入產品名稱或主題：")
feature = st.text_area("請輸入產品特色或推廣重點：")
language = st.selectbox("選擇輸出語言：", ["繁體中文", "英文"])

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_text(prompt, max_tokens=100):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": max_tokens}
    }
    response = requests.post(
        ""https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        try:
            result = response.json()
            if isinstance(result, list) and "generated_text" in result[0]:
                return result[0]["generated_text"]
            else:
                return "⚠️ 回傳格式異常，無法擷取內容。"
        except Exception as e:
            return f"⚠️ JSON 解碼失敗：{str(e)}"
    else:
        return f"❌ API 錯誤（狀態碼 {response.status_code}）：\n{response.text}"

if st.button("生成貼文"):
    if not HUGGINGFACE_API_TOKEN:
        st.error("請先設定 HUGGINGFACE_API_TOKEN")
    elif not product or not feature:
        st.warning("請輸入完整的主題與特色")
    else:
        prompt = f"請用{language}撰寫一則 Instagram 貼文內容，主題為：{product}，產品特色如下：{feature}，並附上熱門 Hashtag。"
        result = generate_text(prompt, max_tokens=100)
        st.subheader("生成內容：")
        st.write(result)

# 第二段：留言回覆 AI 助理
st.markdown("---")
st.title("💬 留言回覆 AI 助理")

comment = st.text_input("輸入 IG 留言：")
tone = st.selectbox("選擇回覆語氣：", ["幽默", "專業", "促銷"])

if st.button("產生回覆"):
    if not comment:
        st.warning("請輸入留言內容")
    else:
        reply_prompt = f"針對以下 IG 留言，用{tone}語氣撰寫一則友善的回覆：\n留言：{comment}"
        result = generate_text(reply_prompt, max_tokens=80)
        st.subheader("AI 回覆內容：")
        st.write(result)
