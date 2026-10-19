import streamlit as st
import random
import string
import re

# إعدادات المتصفح الأساسية
st.set_page_config(page_title="منصة Panda Security التفاعلية", page_icon="🐼", layout="centered")

# تخصيص واجهة المستخدم وإضافة الباندا في الخلفية مع تدرج الأخضر والوردي النيون
st.markdown("""
    <style>
    /* خلفية متدرجة نيون مع دمج نمط الباندا الكرتوني المتكرر بشكل خفيف */
    .stApp {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.85) 0%, rgba(255, 0, 127, 0.85) 100%), 
                    url('https://freepik.com') !important;
        background-size: cover !important;
        background-blend-mode: multiply !important;
    }
    
    /* تنسيق اسم المنصة الداكن لزيادة التباين والوضوح فوق التدرج الفاتح */
    h1 {
        color: #120e2e !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: bold;
        font-size: 45px !important;
        text-shadow: 2px 2px 8px rgba(255, 255, 255, 0.6);
        margin-bottom: 5px;
    }
    
    /* تنسيق الوصف الفرعي */
    .subtitle {
        text-align: center; 
        color: #ffffff; 
        font-size: 19px; 
        font-weight: bold;
        text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
    }
    
    /* تنسيق التبويبات العلوية لتبرز بوضوح ممتع */
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        background-color: rgba(18, 14, 46, 0.85);
        border-radius: 12px 12px 0px 0px;
        padding: 10px 18px;
        margin: 0px 3px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #00ffcc;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #120e2e !important;
        color: #00ffcc !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }
    
    /* تنسيق حقول الإدخال لتكون واضحة وداكنة ومتباينة */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: rgba(18, 14, 46, 0.9) !important;
        border: 2px solid #120e2e !important;
        border-radius: 12px;
    }
    
    input, textarea {
        color: #ffffff !important;
    }
    
    /* تنسيق الخانات والبطاقات الداخلية */
    .stSelectbox, .stRadio {
        background-color: rgba(18, 14, 46, 0.85) !important;
        padding: 15px;
        border-radius: 12px;
        color: #ffffff !important;
    }
    
    label {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    
    /* تنسيق أزرار الفحص النيون التفاعلية */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #120e2e, #1a1540);
        color: #00ffcc;
        font-weight: bold;
        font-size: 18px;
        border-radius: 15px;
        border: 2px solid #00ffcc;
        padding: 12px 30px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
        transition: 0.3s;
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        background: #00ffcc;
        color: #120e2e;
        transform: scale(1.02);
        box-shadow: 0px 0px 20px #00ffcc;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة تطبيق Panda Security الرئيسية
st.markdown("<h1>🐼 Panda Security 🐼</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>منصة تفاعلية ممتعة ومرحة للتحقق من الأمان وفحص المخاطر السيبرانية</p>", unsafe_allow_html=True)

# لوحة معلومات توضيحية شفافة
st.markdown('<div style="background-color: rgba(18, 14, 46, 0.85); padding: 15px; border-radius: 12px; color: white; margin-bottom: 20px;">👾 <b>مختبر الباندا السيبراني:</b> اختبر أمانك الآن ودع الباندا الذكي يحتفل بنجاحك!</div>', unsafe_allow_html=True)

# دالة لعرض الباندا المتحرك عند النجاح بصورة ظريفة
def show_success_panda():
    st.markdown("<center><img src='https://giphy.com' width='200'></center>", unsafe_allow_html=True)
    st.balloons()

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
                    show_success_panda()
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
                    show_success_panda()
            else:
                st.warning("الرجاء لصق الكود البرمجي أولاً!")

# 2. قسم التحقق وفحص كلمة المرور
with tab2:
    st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🔍 مختبر قوة كلمات المرور</h3>", unsafe_allow_html=True)
    password = st.text_input("ادخل الكلمة المراد فحصها:", type="password", key="panda_pwd", placeholder="اكتب كلمتك السرية هنا...")
    
    if password:
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        if score <= 2:
            st.error("🚨 وضعية الخطر! كلمة المرور ضعيفة جداً وسهلة التخمين.")
            st.progress(20)
        elif score <= 4:
            st.warning("⚡ جيد ولكن! أمانك في المستوى المتوسط. أضف بعض الرموز والحروف الكبيرة.")
            st.progress(60)
        else:
            st.success("👑 بطل الحماية الخارق! حسابك آمن تماماً وجدار حمايتك صلب.")
            st.progress(100)
            show_success_panda()

# 3. قسم توليد كلمات المرور الآمنة
with tab3:
    st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🎲 مولد الرموز الآمنة الخارقة</h3>", unsafe_allow_html=True)
    length = st.slider("اختر طول كلمة المرور المطلوبة:", min_value=8, max_value=25, value=14)
    
    if st.button("🚀 اطلق درع الأمان الخاص بي"):
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_token = "".join(random.choice(characters) for _ in range(length))
        st.markdown("<p style='color: #120e2e; font-weight: bold;'>درع الحماية الجاهز هو:</p>", unsafe_allow_html=True)
        st.code(secure_token, language="")
        show_success_panda()

# 4. قسم تشفير وفك تشفير النصوص
with tab4:
    st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🕵️ آلة تشفير الرسائل الغامضة</h3>", unsafe_allow_html=True)
    text_to_process = st.text_input("اكتب الرسالة التي تريد معالجتها وتأمينها:", placeholder="مثلاً: سر الأمان الرقمي")
    action = st.radio("حدد نوع الحركة السيبرانية:", ["تشفير وحجب النص 🔒", "كسر الشيفرة وإظهار النص 🔓"])
    
    if st.button("✨ تشغيل آلة المعالجة"):
        if text_to_process:
            shift = 4
            result = "".join(chr(ord(char) + shift if "تشفير" in action else ord(char) - shift) for char in text_to_process)
            st.markdown("<p style='color: #120e2e; font-weight: bold;'>النتيجة المذهلة:</p>", unsafe_allow_html=True)
            st.code(result, language="")
            show_success_panda()
        else:
            st.error("أوه! يبدو أنك نسيت كتابة النص!")
