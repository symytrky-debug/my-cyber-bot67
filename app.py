import streamlit as st
import random
import string

# إعدادات الصفحة
st.set_page_config(page_title="بوابة الأمن السيبراني", page_icon="🛡️", layout="centered")

# عنوان التطبيق
st.title("🛡️ المنصة السيبرانية التفاعلية")
st.subheader("تعلم وحماية وتشفير البيانات في مكان واحد")

# قسم تعريفي
st.info("""
**ما هو الأمن السيبراني؟**  
الأمن السيبراني هو ممارسة حماية الأنظمة والشبكات والبرامج من الهجمات الرقمية التي تهدف عادةً إلى الوصول إلى المعلومات الحساسة أو تغييرها أو تدميرها.
""")

# تقسيم الأدوات السيبرانية إلى تبويبات (Tabs)
tab1, tab2, tab3 = st.tabs(["🔍 فحص كلمة المرور", "🔑 مولد كلمات المرور", "🔒 مشفر النصوص"])

# 1. أداة فحص قوة كلمة المرور
with tab1:
    st.header("مختبر قوة كلمة المرور")
    password = st.text_input("أدخل كلمة المرور لاختبارها:", type="password", key="check_pwd")
    
    if password:
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        if score <= 2:
            st.error("❌ ضعيفة جداً (سهلة الاختراق هجوم التخمين)")
        elif score <= 4:
            st.warning("⚠️ متوسطة (ينصح بإضافة رموز وأرقام)")
        else:
            st.success("✅ قوية جداً (مقاومة للاختراق)")

# 2. أداة توليد كلمات المرور
with tab2:
    st.header("مولد كلمات المرور السيبرانية")
    length = st.slider("اختر طول كلمة المرور:", min_value=8, max_value=32, value=16)
    
    if st.button("توليد كلمة مرور آمنة"):
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = "".join(random.choice(characters) for _ in range(length))
        st.code(generated_password, language="")
        st.success("تم التوليد بنجاح! انسخ الكود أعلاه.")

# 3. أداة تشفير النصوص
with tab3:
    st.header("مشفر النصوص (خوارزمية الإزاحة)")
    text_to_process = st.text_input("أدخل النص المراد تشفيره أو فك تشفيره:")
    action = st.radio("اختر العملية:", ["تشفير 🔒", "فك التشفير 🔓"])
    
    if st.button("تنفيذ العملية السيبرانية"):
        if text_to_process:
            shift = 4
            result = ""
            for char in text_to_process:
                if action == "تشفير 🔒":
                    result += chr(ord(char) + shift)
                else:
                    result += chr(ord(char) - shift)
            st.success("النتيجة:")
            st.code(result, language="")
        else:
            st.error("الرجاء إدخال نص أولاً!")
