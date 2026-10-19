import streamlit as st
import random
import string

# إعدادات المتصفح الأساسية
st.set_page_config(page_title="منصة Panda Security التفاعلية", page_icon="🐼", layout="centered")

# تخصيص واجهة المستخدم بتدرج نيون من الأخضر إلى الوردي
st.markdown("""
    <style>
    /* خلفية متدرجة نيون ممتعة من الأخضر إلى الوردي */
    .stApp {
        background: linear-gradient(135deg, #00ffcc 0%, #ff007f 100%) !important;
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
        font-size: 18px;
        font-weight: bold;
        background-color: rgba(18, 14, 46, 0.85);
        border-radius: 12px 12px 0px 0px;
        padding: 12px 24px;
        margin: 0px 4px;
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
    div[data-baseweb="input"] {
        background-color: rgba(18, 14, 46, 0.9) !important;
        border: 2px solid #120e2e !important;
        border-radius: 12px;
    }
    
    input {
        color: #ffffff !important;
    }
    
    /* تنسيق الخانات والبطاقات الداخلية لزيادة التباين العالي عن الخلفية الخارجية */
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
st.markdown("<p class='subtitle'>منصة تفاعلية ممتعة للتحقق من أمان وفحص البيانات الرقمية</p>", unsafe_allow_html=True)

# لوحة معلومات توضيحية شفافة
st.markdown('<div style="background-color: rgba(18, 14, 46, 0.85); padding: 15px; border-radius: 12px; color: white; margin-bottom: 20px;">👾 <b>مرحباً بك في نظام الفحص والتحقق!</b> استخدم التبويبات بالأسفل للتحقق من سلامة كلمات مرورك وتشفير بياناتك السرية.</div>', unsafe_allow_html=True)

# التبويبات التفاعلية للتحقق من الأمان
tab1, tab2, tab3 = st.tabs(["🔍 فحص أمان كلمات المرور", "🔑 مصنع الرموز القوية", "🔒 نظام تشفير البيانات"])

# 1. قسم التحقق وفحص كلمة المرور
with tab1:
    st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🛡️ مختبر القوة وتحليل الحسابات</h3>", unsafe_allow_html=True)
    st.write("اكتب كلمة مرور هنا ودع نظام التحقق يقيس مستوى حمايتها:")
    
    password = st.text_input("ادخل الكلمة المراد فحصها:", type="password", key="panda_gradient_pwd", placeholder="اكتب كلمتك السرية هنا...")
    
    if password:
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        if score <= 2:
            st.error("🚨 وضعية الخطر! كلمة المرور ضعيفة جداً وسهلة التخمين. أسرع وأضف أرقاماً ورموزاً لحماية حسابك.")
            st.progress(20)
        elif score <= 4:
            st.warning("⚡ جيد ولكن! أمانك في المستوى المتوسط. أنت قريب جداً من الحماية الكاملة، أضف بعض الرموز.")
            st.progress(60)
        else:
            st.success("👑 بطل الحماية الخارق! حسابك آمن تماماً وجدار حمايتك صلب ومقاوم للاختراق.")
            st.progress(100)
            st.balloons()

# 2. قسم توليد كلمات المرور الآمنة
with tab2:
    st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🎲 مولد الرموز الآمنة</h3>", unsafe_allow_html=True)
    st.write("إذا كانت كلمتك ضعيفة، دع مصنع الباندا يولد لك سلسلة أمان خارقة:")
    
    length = st.slider("اختر طول كلمة المرور المطلوبة:", min_value=8, max_value=25, value=14)
    
    if st.button("🚀 اطلق درع الأمان الخاص بي"):
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_token = "".join(random.choice(characters) for _ in range(length))
        
        st.markdown("<p style='color: #120e2e; font-weight: bold;'>درع الحماية الجاهز للاستخدام هو:</p>", unsafe_allow_html=True)
        st.code(secure_token, language="")
        st.balloons()

# 3. قسم تشفير وفك تشفير النصوص
with tab3:
    st.markdown("<h3 style='color: #120e2e; font-weight: bold;'>🕵️ آلة تشفير الرسائل الغامضة</h3>", unsafe_allow_html=True)
    st.write("تعلم كيف يحمي الخبراء رسائلهم عبر الشبكة من خلال تشفيرها بلغة الباندا الغامضة:")
    
    text_to_process = st.text_input("اكتب الرسالة التي تريد معالجتها وتأمينها:", placeholder="مثلاً: سر الأمان الرقمي")
    action = st.radio("حدد نوع الحركة السيبرانية:", ["تشفير وحجب النص 🔒", "كسر الشيفرة وإظهار النص 🔓"])
    
    if st.button("✨ تشغيل آلة المعالجة"):
        if text_to_process:
            shift = 4
            result = "".join(chr(ord(char) + shift if "تشفير" in action else ord(char) - shift) for char in text_to_process)
            
            st.markdown("<p style='color: #120e2e; font-weight: bold;'>النتيجة المذهلة بعد المعالجة البرمجية:</p>", unsafe_allow_html=True)
            st.code(result, language="")
        else:
            st.error("أوه! يبدو أنك نسيت كتابة النص المراد معالجته!")
