import streamlit as st
import random
import string

# إعدادات الصفحة
st.set_page_config(page_title="مخيم الحماية السيبرانية الرقمي", page_icon="🚀", layout="centered")

# تصميم الألوان الممتعة والخلفية باستخدام CSS مخصص للمرحلة المتوسطة
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #251c3d 100%);
    }
    h1 {
        color: #ff007f !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-shadow: 2px 2px 10px rgba(255, 0, 127, 0.5);
    }
    .stTabs [data-baseweb="tab"] {
        color: #00d2ff;
        font-size: 18px;
        font-weight: bold;
        background-color: #1a1a2e;
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
        margin: 0px 4px;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #ff007f;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #ff007f !important;
        color: white !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #00ffcc, #0099ff);
        color: #000;
        font-weight: bold;
        font-size: 18px;
        border-radius: 20px;
        border: none;
        padding: 10px 30px;
        box-shadow: 0px 4px 15px rgba(0, 255, 204, 0.4);
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(45deg, #0099ff, #00ffcc);
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي الملون
st.markdown("<h1>🎮🎮 منصة الأبطال السيبرانيين 🎮🎮</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00ffcc; font-size: 20px; font-weight: bold;'>اكتشف أسرار الهاكرز الأخلاقيين وحصّن بياناتك بنقرة زر!</p>", unsafe_allow_html=True)

# بطاقة ترحيبية كرتونية ممتعة
st.info("👾 **مرحباً بك يا بطل!** الأمن السيبراني هو قوتك الخارقة لحماية أجهزتك وحساباتك من الأشرار الرقميين على الإنترنت. هل أنت مستعد للتحدي؟")

# تبويبات تفاعلية ملونة
tab1, tab2, tab3 = st.tabs(["⚡ فاحص كلمات المرور السرية", "🎲 مولّد الرموز الخارقة", "🔐 شيفرة الرسائل الغامضة"])

# 1. تحدي وفحص قوة كلمة المرور
with tab1:
    st.markdown("<h3 style='color: #00ffcc;'>🔍 مختبر القوة الرقمي</h3>", unsafe_allow_html=True)
    st.write("اكتب كلمة مرورك السرية وشاهد المؤشر الملون كيف يتفاعل مع قوتها!")
    
    password = st.text_input("جرب كلمة مرور هنا:", type="password", key="fun_pwd", placeholder="اكتب هنا مثلاً: Cyber@2026")
    
    if password:
        # حساب النقاط بطريقة برمجية مرحة
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        # تغيير الألوان والرسائل بناءً على النتيجة لتكون حماسية وممتعة
        if score <= 2:
            st.error("🚨 **وضعية الخطر!** كلمة مرورك ضعيفة جداً ويمكن للهاكرز تخمينها في ثوانٍ! أضف رموزاً وأرقاماً فوراً.")
            st.progress(20)
        elif score <= 4:
            st.warning("⚡ **جيد ولكن!** حمايتك متوسطة. أنت في طريقك لتصبح بطلاً، لكن أضف بعض الحروف الكبيرة لتجعلها أقوى.")
            st.progress(60)
        else:
            st.success("👑 **مستوى الملك الخارق!** كلمة مرورك أسطورية ومستحيلة الاختراق!")
            st.progress(100)
            st.balloons() # إطلاق بالونات احتفالية عند النجاح الكامل!

# 2. مولد كلمات المرور الممتع
with tab2:
    st.markdown("<h3 style='color: #00ffcc;'>🎲 مصنع الرموز الحصينة</h3>", unsafe_allow_html=True)
    st.write("اختر طول رداء الحماية الخاص بك ودعنا نطلق لك رمزاً غير قابل للكسر!")
    
    length = st.slider("اختر مستوى تعقيد الطول:", min_value=8, max_value=25, value=14)
    
    if st.button("🚀 توليد درع الحماية"):
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = "".join(random.choice(characters) for _ in range(length))
        
        st.markdown("<p style='color: #ff007f; font-weight: bold;'>درعك السري الجاهز للاستخدام هو:</p>", unsafe_allow_html=True)
        st.code(generated_password, language="")
        st.balloons()

# 3. صندوق التشفير السري الممتع
with tab3:
    st.markdown("<h3 style='color: #00ffcc;'>🕵️ كاشف الرسائل والمخبر السري</h3>", unsafe_allow_html=True)
    st.write("اكتب رسالة سرية لأصدقائك وقم بتشفيرها بلغة الهاكرز الغامضة لكي لا يفهمها أحد غيركم!")
    
    text_to_process = st.text_input("اكتب رسالتك السرية هنا:", placeholder="مثلاً: التقي بكم في معمل الحاسب")
    action = st.radio("اختر الحركة السيبرانية:", ["تشفير القفل 🔒", "كسر الشيفرة وفك القفل 🔓"])
    
    if st.button("✨ تشغيل آلة التشفير"):
        if text_to_process:
            shift = 4  # إزاحة الأحرف والرموز بطريقة ممتعة
            result = "".join(chr(ord(char) + shift if "تشفير" in action else ord(char) - shift) for char in text_to_process)
            
            st.markdown("<p style='color: #00ffcc; font-weight: bold;'>النتيجة المذهلة:</p>", unsafe_allow_html=True)
            st.code(result, language="")
        else:
            st.error("أوه! لقد نسيت كتابة الرسالة المراد تشفيرها!")
