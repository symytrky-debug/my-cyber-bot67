import streamlit as st
import random
import string
import re
import time

# إعدادات المتصفح الأساسية
st.set_page_config(page_title="منصة Panda Security التفاعلية", page_icon="🐼", layout="centered")

# إدارة حالة تسجيل الدخول باستخدام Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# تخصيص واجهة المستخدم بالألوان النيون وتثبيت لون الخط الأخضر الفسفوري
st.markdown("""
    <style>
    /* تصميم خلفية متدرجة نيون ممتعة من الأخضر إلى الوردي */
    .stApp {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.9) 0%, rgba(255, 0, 127, 0.9) 100%),
                    radial-gradient(circle at 50% 30%, #00ffcc 0%, transparent 60%) !important;
        position: relative;
    }

    /* إضافة تأثير نيون للباندا يظهر بشكل فني في خلفية المنصة */
    .stApp::before {
        content: "🐼";
        position: fixed;
        top: 20%;
        left: 50%;
        transform: translate(-50%, -20%);
        font-size: 180px;
        opacity: 0.15;
        filter: drop-shadow(0 0 20px #00ffcc) drop-shadow(0 0 40px #ff007f);
        z-index: 0;
        pointer-events: none;
    }
    
    /* تنسيق اسم المنصة الداكن مع توهج نيون مزدوج */
    h1 {
        color: #120e2e !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: bold;
        font-size: 48px !important;
        text-shadow: 0px 0px 10px #00ffcc, 0px 0px 20px #ff007f;
        margin-bottom: 5px;
        position: relative;
        z-index: 1;
    }
    
    /* تنسيق الوصف الفرعي والمطلعة الترحيبية */
    .subtitle {
        text-align: center; 
        color: #ffffff; 
        font-size: 19px; 
        font-weight: bold;
        text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.6);
        margin-bottom: 25px;
        position: relative;
        z-index: 1;
    }

    .welcome-intro {
        background-color: rgba(18, 14, 46, 0.95);
        color: #00ffcc;
        padding: 20px;
        border-radius: 12px;
        border-right: 5px solid #00ffcc;
        border-left: 5px solid #ff007f;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
    }
    
    /* تنسيق التبويبات العلوية لتبرز بوضوح نيون ممتع */
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        background-color: rgba(18, 14, 46, 0.9);
        border-radius: 12px 12px 0px 0px;
        padding: 10px 18px;
        margin: 0px 3px;
        border: 2px solid rgba(0, 255, 204, 0.3);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #00ffcc;
        text-shadow: 0px 0px 10px #00ffcc;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #120e2e !important;
        color: #00ffcc !important;
        box-shadow: 0px 4px 15px rgba(0, 255, 204, 0.4);
        border: 2px solid #00ffcc;
    }
    
    /* تثبيت لون إدخال النصوص لمنع تحوله للأبيض أثناء الكتابة نهائياً */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: rgba(18, 14, 46, 0.95) !important;
        border: 2px solid #120e2e !important;
        border-radius: 12px;
    }
    
    input, textarea, input:focus, textarea:focus {
        color: #00ffcc !important;
        -webkit-text-fill-color: #00ffcc !important;
        font-family: monospace;
        font-weight: bold;
    }
    
    /* تنسيق الخانات والبطاقات الداخلية */
    .stSelectbox, .stRadio {
        background-color: rgba(18, 14, 46, 0.9) !important;
        padding: 15px;
        border-radius: 12px;
        color: #ffffff !important;
        border: 1px solid rgba(255, 0, 127, 0.2);
    }
    
    label {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    
    /* تنسيق أزرار النيون التفاعلية */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #120e2e, #1a1540);
        color: #00ffcc;
        font-weight: bold;
        font-size: 18px;
        border-radius: 15px;
        border: 2px solid #00ffcc;
        padding: 12px 30px;
        box-shadow: 0px 4px 20px rgba(0, 255, 204, 0.4);
        transition: 0.3s;
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        background: #00ffcc;
        color: #120e2e;
        transform: scale(1.02);
        box-shadow: 0px 0px 25px #00ffcc;
    }
    </style>
""", unsafe_allow_html=True)

# 1. شاشة تسجيل الدخول الرئيسية + المطلعة الخارجية المضافة
if not st.session_state.logged_in:
    st.markdown("<h1>🐼 Panda Security 🐼</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>بوابة الولوج والتحقق الرقمي للمرحلة المتوسطة</p>", unsafe_allow_html=True)
    
    # 📌 المطلعة المضافة برا (مقدمة المنصة الترحيبية للطلاب):
    st.markdown("""
        <div class="welcome-intro">
            🚀 مرحباً بكم في معمل الأبطال السيبرانيين! <br>
            إنترنت اليوم مليء بالتحديات، وهنا في Panda Security سنتعلم معاً كيف نكشف الروابط المشبوهة، 
            ونفحص قوة كلمات مرورنا، ونشفر رسائلنا السرية كالمحترفين. <br>
            🔒 سجل دخولك الآن لتبدأ التحدي الخارق!
        </div>
    """, unsafe_allow_html=True)
    
    # بطاقة خيارات تسجيل الدخول
    st.markdown('<div style="background-color: rgba(18, 14, 46, 0.9); padding: 25px; border-radius: 12px; border: 2px solid #ff007f; box-shadow: 0px 0px 15px rgba(255, 0, 127, 0.4);">', unsafe_allow_html=True)
    st.subheader("🔑 اختر وسيلة الدخول للتحقق:")
    
    login_option = st.radio("وسيلة التحقق:", ["البريد الإلكتروني (Email)", "حساب Google السريع"])
    
    if login_option == "البريد الإلكتروني (Email)":
        email_input = st.text_input("أدخل البريد الإلكتروني:", placeholder="example@school.com")
        password_input = st.text_input("أدخل كلمة المرور:", type="password", placeholder="********")
        
        if st.button("🚀 الدخول إلى نظام الباندا"):
            if email_input and password_input:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("الرجاء كتابة البريد وكلمة المرور أولاً!")
                
    else:
        st.info("💡 محاكاة الدخول الذكي والآمن")
        if st.button("🔴 الدخول الفوري بواسطة حساب Google"):
            st.session_state.logged_in = True
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# 2. شاشة الأدوات السيبرانية الأربعة (تفتح بعد تسجيل الدخول)
else:
    st.markdown("<h1>🐼 Panda Security 🐼</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>مختبر التحقق وفحص المخاطر السيبرانية</p>", unsafe_allow_html=True)

    if st.button("🚪 تسجيل الخروج من المختبر"):
        st.session_state.logged_in = False
        st.rerun()

    def play_success_celebration():
        st.balloons()
        with st.spinner("الباندا يحلل النتيجة... 🐼⚡"):
            time.sleep(0.4)
        st.markdown("<h2 style='text-align: center; color: #120e2e; text-shadow: 0 0 10px #00ffcc;'>🐼 ✨ تـم التحقـق بـدرع نـيـون آمـن! ✨ 🐼</h2>", unsafe_allow_html=True)
        st.toast("بطل خارق! وعيك السيبراني يضيء كالأخضر الفسفوري! 🐼🛡️")

    tab1, tab2, tab3, tab4 = st.tabs(["🛡️ فحص الروابط والأكواد", "🔍 فحص كلمات المرور", "🔑 مصنع الرموز", "🔒 نظام التشفير"])

    # [باقي أدوات الفحص والتشفير تعمل بكفاءة عالية وبنفس الألوان والخصائص المضمونة]
    with tab1:
        st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🛡️ رادار فحص الروابط والأكواد المشبوهة</h3>", unsafe_allow_html=True)
        scan_type = st.radio("اختر المادة المراد تحليلها:", ["رابط ويب (URL)", "كود برمجي (Code)"])
        if scan_type == "رابط ويب (URL)":
            user_url = st.text_input("أدخل رابط الموقع الإلكتروني لفحصه:", placeholder="http://free-gifts-claim.net")
            if st.button("🚨 ابدأ فحص الرابط سيبرانياً"):
                if user_url and ("free" in user_url.lower() or "http://" in user_url.lower()):
                    st.error("🚨 تحذير! هذا الرابط يحمل مؤشرات تصيد احتيالي!")
                elif user_url:
                    st.success("✅ الرابط آمن تماماً!")
                    play_success_celebration()
        else:
            user_code = st.text_area("الصق الكود البرمجي هنا لتفتيشه:")
            if st.button("⚙️ ابدأ التحليل البرمجي"):
                if user_code and "eval" in user_code:
                    st.error("🚨 تم اكتشاف كود مشبوه وضار!")
                elif user_code:
                    st.success("✅ كود سليم ونظيف!")
                    play_success_celebration()

    with tab2:
        st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🔍 مختبر قوة كلمات المرور</h3>", unsafe_allow_html=True)
        password = st.text_input("ادخل الكلمة المراد فحصها:", type="password", placeholder="اكتب كلمتك السرية هنا...")
        if password:
            if len(password) >= 10:
                st.success("👑 بطل الحماية الخارق! حسابك آمن وجدار حمايتك صلب.")
                st.progress(100)
                play_success_celebration()
            else:
                st.error("🚨 وضعية الخطر! كلمة المرور ضعيفة جداً وسهلة التخمين.")
                st.progress(30)

    with tab3:
        st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🎲 مولد الرموز الآمنة الخارقة</h3>", unsafe_allow_html=True)
        length = st.slider("اختر طول الكلمة المطلوبة:", 8, 25, 14)
        if st.button("🚀 اطلق درع الأمان الخاصة بي"):
            token = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            st.code(token, language="")
            play_success_celebration()

    with tab4:
        st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🕵️ آلة تشفير الرسائل الغامضة</h3>", unsafe_allow_html=True)
        text_to_process = st.text_input("اكتب الرسالة لتأمينها:")
action = st.radio("حدد نوع الإجراء السري:", ["تشفير وحجب النص 🔒", "كسر الشيفرة وإظهار النص 🔓"])
if st.button("✨ تشغيل آلة المعالجة"):
if text_to_process:
result = "".join(chr(ord(char) + 4 if "تشفير" in action else ord(char) - 4) for char in text_to_process)
st.code(result, language="")
play_success_celebration()
