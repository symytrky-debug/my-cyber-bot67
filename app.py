import streamlit as st
import random
import string

# إعدادات المتصفح الأساسية
st.set_page_config(page_title="منصة التفتيش والأمن الرقمي - Panda Security", page_icon="🐼", layout="centered")

# تخصيص واجهة المستخدم بألوان نيون وخلفية متناسقة وممتعة ومرحة للمرحلة المتوسطة
st.markdown("""
    <style>
    /* خلفية متناسقة ممتعة ومريحة بتدرج داكن ليبرز ألوان النيون */
    .stApp {
        background: linear-gradient(135deg, #120e2e 0%, #1a1540 100%);
    }
    
    /* تنسيق اسم المنصة الجديد Panda Security بخط عريض ونوافذ نيون متوهجة */
    h1 {
        color: #00ffcc !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-weight: bold;
        font-size: 40px !important;
        text-shadow: 0px 0px 15px #00ffcc, 0px 0px 30px #ff007f;
        margin-bottom: 5px;
    }
    
    /* تنسيق الوصف الفرعي */
    .subtitle {
        text-align: center; 
        color: #ff007f; 
        font-size: 18px; 
        font-weight: bold;
        text-shadow: 0px 0px 8px rgba(255, 0, 127, 0.4);
        margin-bottom: 25px;
    }
    
    /* تنسيق التبويبات العلوية بألوان ممتعة */
    .stTabs [data-baseweb="tab"] {
        color: #00ffcc;
        font-size: 18px;
        font-weight: bold;
        background-color: #1f1a4d;
        border-radius: 12px 12px 0px 0px;
        padding: 12px 24px;
        margin: 0px 6px;
        border: 1px solid #2d2673;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #ff007f;
        text-shadow: 0px 0px 10px #ff007f;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(45deg, #ff007f, #7928ca) !important;
        color: white !important;
        box-shadow: 0px 0px 15px rgba(255, 0, 127, 0.6);
    }
    
    /* تنسيق أزرار الفحص والتحقق النيون التفاعلية */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #00ffcc, #0099ff);
        color: #000000;
        font-weight: bold;
        font-size: 18px;
        border-radius: 15px;
        border: none;
        padding: 12px 30px;
        box-shadow: 0px 0px 15px #00ffcc;
        transition: 0.3s;
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        background: linear-gradient(45deg, #ff007f, #00ffcc);
        color: #ffffff;
        transform: scale(1.03);
        box-shadow: 0px 0px 25px #ff007f;
    }
    
    /* تنسيق حقول الإدخال لتتناسق مع الثيم الممتع */
    div[data-baseweb="input"] {
        background-color: #1f1a4d !important;
        border: 2px solid #2d2673 !important;
        border-radius: 12px;
    }
    
    input {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة تطبيق Panda Security الرئيسية
st.markdown("<h1>🐼 Panda Security 🐼</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>بوابتك التفاعلية الممتعة للتحقق من الأمان وفحص البيانات الرقمية</p>", unsafe_allow_html=True)

# رسالة ترحيبية حماسية
st.info("👾 **مرحباً بك في نظام الفحص والتحقق!** نحن هنا لنساعدك على حماية حساباتك ومعلوماتك من الأشرار الرقميين بطريقة تفاعلية وممتعة ومستعدين لإطلاق بالونات الأمان!")

# التبويبات التفاعلية للتحقق من الأمان
tab1, tab2, tab3 = st.tabs(["🔍 فحص أمان كلمات المرور", "🔑 مصنع الرموز القوية", "🔒 نظام تشفير البيانات"])

# 1. قسم التحقق وفحص كلمة المرور
with tab1:
    st.markdown("<h3 style='color: #00ffcc; margin-top: 15px;'>🛡️ مختبر القوة وتحليل الحسابات</h3>", unsafe_allow_html=True)
    st.write("اكتب كلمة مرور هنا ودع نظام التحقق يقيس مستوى حمايتها:")
    
    password = st.text_input("ادخل الكلمة المراد فحصها:", type="password", key="panda_pwd", placeholder="اكتب كلمتك السرية هنا...")
    
    if password:
        # حساب معايير الأمان وقوتها
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        # ردود فعل ملونة ومرحة حسب النتيجة
        if score <= 2:
            st.error("🚨 **وضعية الخطر!** كلمة المرور ضعيفة جداً وسهلة التخمين. أسرع وأضف أرقاماً ورموزاً لحماية حسابك.")
            st.progress(20)
        elif score <= 4:
            st.warning("⚡ **جيد ولكن!** أمانك في المستوى المتوسط. أنت قريب جداً من الحماية الكاملة، أضف بعض الرموز لتصبح بطلاً سيبرانياً.")
            st.progress(60)
        else:
            st.success("👑 **بطل الحماية الخارق!** حسابك آمن تماماً وجدار حمايتك صلب ومقاوم للاختراق.")
            st.progress(100)
            st.balloons()  # إطلاق مؤثر البالونات الاحتفالي التفاعلي

# 2. قسم توليد كلمات المرور الآمنة
with tab2:
    st.markdown("<h3 style='color: #00ffcc; margin-top: 15px;'>🎲 مولد الرموز الآمنة</h3>", unsafe_allow_html=True)
    st.write("إذا كانت كلمتك ضعيفة، دع مصنع الباندا يولد لك سلسلة أمان خارقة مستحيلة الاختراق:")
    
    length = st.slider("اختر طول كلمة المرور المطلوبة:", min_value=8, max_value=25, value=14)
    
    if st.button("🚀 اطلق درع الأمان الخاص بي"):
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_token = "".join(random.choice(characters) for _ in range(length))
        
        st.markdown("<p style='color: #ff007f; font-weight: bold;'>درع الحماية الجاهز للاستخدام هو:</p>", unsafe_allow_html=True)
        st.code(secure_token, language="")
        st.balloons()

# 3. قسم تشفير وفك تشفير النصوص
with tab3:
    st.markdown("<h3 style='color: #00ffcc; margin-top: 15px;'>🕵️ آلة تشفير الرسائل الغامضة</h3>", unsafe_allow_html=True)
    st.write("تعلم كيف يحمي الخبراء رسائلهم عبر الشبكة من خلال تشفيرها بلغة الباندا الغامضة:")
    
    text_to_process = st.text_input("اكتب الرسالة التي تريد معالجتها وتأمينها:", placeholder="مثلاً: سر الأمان الرقمي")
    action = st.radio("حدد نوع الحركة السيبرانية:", ["تشفير وحجب النص 🔒", "كسر الشيفرة وإظهار النص 🔓"])
    
    if st.button("✨ تشغيل آلة المعالجة"):
        if text_to_process:
            shift = 4
            result = "".join(chr(ord(char) + shift if "تشفير" in action else ord(char) - shift) for char in text_to_process)
            
            st.markdown("<p style='color: #00ffcc; font-weight: bold;'>النتيجة المذهلة بعد المعالجة البرمجية:</p>", unsafe_allow_html=True)
            st.code(result, language="")
        else:
            st.error("أوه! يبدو أنك نسيت كتابة النص المراد معالجته!")
