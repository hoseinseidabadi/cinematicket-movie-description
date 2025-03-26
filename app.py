import openai
import streamlit as st
from dotenv import load_dotenv
import os

# خواندن متغیرهای محیطی
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🎬 تولید توضیحات فیلم برای سینما تیکت")
st.write("یک ابزار برای تولید توضیحات فیلم و تئاتر جهت استفاده در سایت سینما تیکت.")

film_name = st.text_input("🎥 نام فیلم:")
film_type = st.selectbox("🎭 نوع:", ["فیلم سینمایی", "تئاتر"])

if st.button("📜 تولید توضیحات"):
    if film_name.strip():
        with st.spinner("⏳ در حال تولید توضیحات..."):
            prompt = f"یک یا دو پاراگراف درباره‌ی {film_type} «{film_name}» بنویس که در سایت سینما تیکت نمایش داده شود."
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "تو یک نویسنده محتوا برای سایت سینماتیکت هستی."},
                    {"role": "user", "content": prompt},
                ]
            )
        st.success("✅ توضیحات تولید شد!")
        st.write(response.choices[0].message.content)
    else:
        st.warning("⚠️ لطفاً نام فیلم را وارد کنید!")
