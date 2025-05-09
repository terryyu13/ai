# AI 作品集（免費部署版）

這個專案展示兩個 AI 應用案例，使用 Hugging Face 免費模型部署，無需付費 OpenAI 金鑰。

## 📌 專案一：社群內容生成器
輸入產品主題與特色，自動生成 Instagram 貼文與熱門 Hashtag。

## 🤖 專案二：社群互動 AI 助理
模擬回覆 IG 留言，支援不同語氣（幽默、專業、促銷）。

## 🚀 快速部署（使用 Streamlit Cloud）
1. Fork 本 repo
2. 建立 `.streamlit/secrets.toml` 檔案，填入：
```toml
HUGGINGFACE_API_TOKEN = "你的 Hugging Face API Token"
```
3. 在 [Streamlit Cloud](https://streamlit.io/cloud) 新建 App 並部署 `main.py`

## 🔧 需要安裝的套件
```bash
pip install -r requirements.txt
```
