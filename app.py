import streamlit as st
import random
import string
import re
import time

# إعدادات المتصفح الأساسية
st.set_page_config(page_title="منصة Panda Security التفاعلية", page_icon="🐼", layout="centered")

# إدارة حالة تسجيل الدخول باستخدام Session State في ستريمليت
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# تخصيص واجهة المستخدم برسم نيون للباندا في الخلفية مع تدرج الأخضر والوردي
st.markdown("""
    <style>
    /* تصميم خلفية متدرجة نيون مدمج معها رسمة باندا نيون متوهجة برمجياً */
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
    
    /* تنسيق الوصف الفرعي */
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
    
    /* تنسيق التبويبات العلوية لتبرز بوضوح نيون ممتع فوق الخلفية */
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        background-color: rgba(18, 14, 46, 0.9);
        border-radius: 12px 12px 0px 0px;
        padding: 10px 18px;
        margin: 0px 3px;
        border: 2px solid rgba(0, 255, 204, 0.3);
        position: relative;
        z-index: 1;
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
    
    /* منع الكتابة من أن تصبح بيضاء؛ وتثبيتها على لون أخضر نيون متوهج دائماً */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: rgba(18, 14, 46, 0.95) !important;
        border: 2px solid #120e2e !important;
        border-radius: 12px;
        box-shadow: inset 0 0 10px rgba(255, 0, 127, 0.2);
    }
    
    /* تثبيت لون إدخال النصوص للمتصفح لمنع تحوله للأبيض */
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
    
    /* تنسيق أزرار الفحص والتحقق والولوج فائقة التوهج */
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
        box-shadow: 0px 0px 25px #00ffcc, 0px 0px 10px #ff007f;
    }
    </style>
""", unsafe_allow_html=True)

# 1. شاشة تسجيل الدخول الرئيسية (إذا لم يسجل الطالب دخوله بعد)
if not st.session_state.logged_in:
    st.markdown("<h1>🐼 Panda Security 🐼</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>بوابة تسجيل الدخول الآمن للمنصة السيبرانية</p>", unsafe_allow_html=True)
    
    # بطاقة خيارات تسجيل الدخول داخل حاوية داكنة
    st.markdown('<div style="background-color: rgba(18, 14, 46, 0.9); padding: 25px; border-radius: 12px; color: white; border: 2px solid #ff007f; box-shadow: 0px 0px 15px #ff007f;">', unsafe_allow_html=True)
    st.subheader("🔒 يرجى اختيار طريقة تسجيل الدخول للبدء:")
    
    login_option = st.radio("اختر الوسيلة المعتمدة للتحقق:", ["التسجيل عبر البريد الإلكتروني (Email)", "التسجيل السريع عبر حساب Google"])
    
    if login_option == "التسجيل عبر البريد الإلكتروني (Email)":
        email_input = st.text_input("أدخل بريدك الإلكتروني التعليمي أو الشخصي:", placeholder="example@school.com")
        password_input = st.text_input("أدخل كلمة المرور الخاصة بك:", type="password", placeholder="********")
        
        if st.button("🚀 الدخول إلى النظام السيبراني"):
            if email_input and password_input:
                st.session_state.logged_in = True
                st.success("تم تسجيل الدخول بنجاح! جاري تحميل المنصة...")
                st.rerun()
            else:
                st.error("خطأ: يرجى كتابة البريد الإلكتروني وكلمة المرور أولاً!")
                
    else:
        st.info("💡 محاكاة تسجيل الدخول الذكي عبر Google")
        if st.button("🔴 تسجيل الدخول بواسطة حساب Google"):
            st.session_state.logged_in = True
            st.success("تم الاتصال بحساب Google بنجاح! جاري تحويلك للمختبر...")
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# 2. شاشة المنصة والأدوات السيبرانية الأربعة (تفتح فقط بعد نجاح تسجيل الدخول)
else:
    # واجهة تطبيق Panda Security بعد الولوج
    st.markdown("<h1>🐼 Panda Security 🐼</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>مختبر التحقق الذكي وفحص الروابط والأكواد والمخاطر السيبرانية</p>", unsafe_allow_html=True)

    # زر تسجيل الخروج متواجد بالأعلى للعودة للقائمة الرئيسية
    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button("🚪 خروج"):
            st.session_state.logged_in = False
            st.rerun()

    # لوحة معلومات توضيحية شفافة
    st.markdown('<div style="background-color: rgba(18, 14, 46, 0.9); padding: 15px; border-radius: 12px; color: white; margin-bottom: 20px; border-left: 5px solid #00ffcc;">👾 <b>مختبر الباندا السيبراني:</b> أهلاً بك يا بطل بعد التحقق من هويتك! حقول الإدخال مجهزة الآن بلون نيون فسفوري ثابت أثناء الكتابة.</div>', unsafe_allow_html=True)

    # دالة برمجية للاحتفال بنجاح الفحص
    def play_success_celebration():
        st.balloons()
        with st.spinner("الباندا يحلل النتيجة... 🐼⚡"):
            time.sleep(0.4)
        st.markdown("<h2 style='text-align: center; color: #120e2e; text-shadow: 0 0 10px #00ffcc;'>🐼 ✨ تـم التحقـق بـدرع نـيـون آمـن! ✨ 🐼</h2>", unsafe_allow_html=True)
        st.toast("بطل خارق! وعيك السيبراني يضيء كالأخضر الفسفوري! 🐼🛡️")

    # التبويبات التفاعلية الأربعة
    tab1, tab2, tab3, tab4 = st.tabs(["🛡️ فحص الروابط والأكواد", "🔍 فحص كلمات المرور", "🔑 مصنع الرموز", "🔒 نظام التشفير"])

    # 1. أداة فحص وتحليل الروابط والأكواد المشبوهة
    with tab1:
        st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🛡️ رادار فحص الروابط والأكواد المشبوهة</h3>", unsafe_allow_html=True)
        scan_type = st.radio("اختر نوع المادة المراد تحليلها:", ["رابط ويب (URL)", "كود برمجي (Code)"])
        
        if scan_type == "رابط ويب (URL)":
            user_url = st.text_input("أدخل رابط الموقع الإلكتروني لفحصه:", placeholder="مثال: http://free-gifts-claim.net")
            if st.button("🚨 ابدأ فحص الرابط سيبرانياً"):
                if user_url:
                    suspicious_words = ["free", "gift", "login-secure", "win", "money", "update-account", "prize", "claim"]
                    is_suspicious = any(word in user_url.lower() for word in suspicious_words) or "http://" in user_url.lower()
                    
                    if is_suspicious:
                        st.error("🚨 تحذير عالي الخطورة! هذا الرابط يحمل مؤشرات تصيد احتيالي أو برمجيات خبيثة!")
                    else:
                        st.success("✅ الرابط يبدو آمناً ونظيفاً تماماً!")
                        play_success_celebration()
                else:
                    st.warning("الرجاء إدخال الرابط أولاً!")
                    
        else:
            user_code = st.text_area("الصق الكود البرمجي هنا لتحليله:", placeholder="اكتب أو الصق الكود البرمجي هنا...", height=150)
            if st.button("⚙️ ابدأ التحليل البرمجي الخبير"):
                if user_code:
                    malicious_patterns = ["eval\(", "base64_decode", "os.system", "rm -rf", "subprocess", "keylogger", "steal_data"]
                    detected_threats = [pattern for pattern in malicious_patterns if re.search(pattern, user_code)]
                    
                    if detected_threats:
                        st.error(f"🚨 تم اكتشاف كود مشبوه! يحتوي الكود على أوامر قد تُستخدم لاختراق النظام.")
                    else:
                        st.success("✅ كود سليم ونظيف! تم فحص بنية الأوامر البرمجية بنجاح.")
                        play_success_celebration()
                else:
                    st.warning("الرجاء لصق الكود البرمجي أولاً!")

    # 2. قسم التحقق وفحص كلمة المرور
    with tab2:
