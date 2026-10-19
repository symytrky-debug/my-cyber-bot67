import streamlit as st
import random
import string

# إعدادات المتصفح الأساسية
st.set_page_config(page_title="منصة التدقيق والتحقق السيبراني", page_icon="🛡️", layout="centered")

# تخصيص واجهة المستخدم بالألوان المتناسقة لتقليل الإيموجيز وزيادة التباين
st.markdown("""
    <style>
    /* تغيير لون خلفية التطبيق بالكامل إلى تدرج أزرق داكن محايد */
    .stApp {
        background: linear-gradient(135deg, #0a1128 0%, #101f42 100%);
    }
    
    /* تنسيق العنوان الرئيسي المتخصص */
    h1 {
        color: #00d2ff !important;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        text-shadow: 0px 0px 12px rgba(0, 210, 255, 0.3);
        margin-bottom: 5px;
    }
    
    /* تنسيق التبويبات العلوية */
    .stTabs [data-baseweb="tab"] {
        color: #8a99ad;
        font-size: 16px;
        font-weight: 600;
        background-color: #132247;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        margin: 0px 4px;
        border: 1px solid #1c356a;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #00d2ff;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #00d2ff !important;
        color: #0a1128 !important;
    }
    
    /* تنسيق خانات الإدخال لزيادة التباين والتناسق */
    div[data-baseweb="input"] {
        background-color: #132247 !important;
        border: 1px solid #1c356a !important;
        border-radius: 8px;
    }
    
    input {
        color: #ffffff !important;
    }
    
    /* تنسيق أزرار الفحص والتحقق */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #00d2ff, #0072ff);
        color: #ffffff;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        padding: 12px 30px;
        box-shadow: 0px 4px 15px rgba(0, 114, 255, 0.3);
        transition: 0.3s;
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        background: linear-gradient(45deg, #0072ff, #00d2ff);
        box-shadow: 0px 4px 20px rgba(0, 210, 255, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# واجهة المنصة الرئيسية
st.markdown("<h1>منصة التدقيق والتحقق السيبراني</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a99ad; font-size: 16px;'>أنظمة ذكية تفاعلية لفحص مستوى الأمان والتحقق من سلامة البيانات الرقمية للمرحلة المتوسطة</p>", unsafe_allow_html=True)

# لوحة معلومات مركزية
st.info("مرحباً بك في نظام الفحص. استخدم التبويبات المتاحة بالأسفل لإجراء اختبارات الأمان والتحقق من أدوات الحماية الخاصة بك.")

# إنشاء تبويبات الفحص المتخصصة
tab1, tab2, tab3 = st.tabs(["فحص أمان كلمة المرور", "أداة التوليد الآمن", "نظام تشفير البيانات"])

# 1. نظام فحص وتحليل مستوى أمان كلمة المرور
with tab1:
    st.markdown("<h3 style='color: #00d2ff; margin-top: 15px;'>وحدة فحص وقوة الحسابات</h3>", unsafe_allow_html=True)
    st.write("أدخل كلمة المرور في الحقل أدناه ليقوم النظام بتحليلها والتحقق من مدى صمودها ضد هجمات التخمين السيبرانية:")
    
    password = st.text_input("كلمة المرور المراد فحصها:", type="password", key="secure_inspect_pwd", placeholder="أدخل الكلمة هنا للبدء في التحليل...")
    
    if password:
        # خوارزمية قياس معايير الأمان
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        # استجابة النظام بناءً على التحليل الرقمي
        if score <= 2:
            st.error("النتيجة: غير آمنة مخترقة برمجياً. كلمة المرور ضعيفة للغاية وسهلة التخمين.")
            st.progress(20)
        elif score <= 4:
            st.warning("النتيجة: أمان متوسط. الخصائص جيدة ولكن يفضل تدعيمها برموز إضافية وحروف كبيرة لحماية أقوى.")
            st.progress(60)
        else:
            st.success("النتيجة: أمان عالي جدار حماية قوي ومقاوم لمحاولات الاختراق الرقمي.")
            st.progress(100)
            st.balloons()  # تأثير تفاعلي للاحتفال بتحقيق معايير الأمان الكاملة

# 2. وحدة توليد الرموز العشوائية المشفرة
with tab2:
    st.markdown("<h3 style='color: #00d2ff; margin-top: 15px;'>وحدة توليد معايير الحماية المعقدة</h3>", unsafe_allow_html=True)
    st.write("إذا كانت كلمتك الحالية ضعيفة، يمكنك استخدام هذا النظام لإنشاء سلسلة نصية عشوائية مطابقة لمعايير الأمن السيبراني العالمي:")
    
    length = st.slider("حدد عدد خانات الطول المطلوبة للتحقق:", min_value=8, max_value=25, value=14)
    
    if st.button("بدء توليد السلسلة الآمنة"):
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_token = "".join(random.choice(characters) for _ in range(length))
        
        st.markdown("<p style='color: #00d2ff; font-weight: 600;'>تم إنشاء الرمز بنجاح وفقاً لمعايير الفحص:</p>", unsafe_allow_html=True)
        st.code(secure_token, language="")
        st.balloons()

# 3. نظام محاكاة تشفير وفك تشفير الرسائل
with tab3:
    st.markdown("<h3 style='color: #00d2ff; margin-top: 15px;'>نظام تشفير وحماية سلامة النصوص</h3>", unsafe_allow_html=True)
    st.write("تساعد هذه الأداة على فهم كيفية حماية البيانات أثناء انتقالها عبر الشبكة باستخدام خوارزميات الإزاحة الرياضية:")
    
    text_to_process = st.text_input("أدخل النص المطلوب معالجته سيبرانياً:", placeholder="اكتب النص المراد حمايته هنا...")
    action = st.radio("حدد نوع الإجراء المطلوب:", ["تشفير وحجب النص", "فك التشفير وإظهار النص"])
    
    if st.button("معالجة البيانات"):
        if text_to_process:
            shift = 4
            result = "".join(chr(ord(char) + shift if "تشفير" in action else ord(char) - shift) for char in text_to_process)
            
            st.markdown("<p style='color: #00d2ff; font-weight: 600;'>مخرجات النظام بعد المعالجة البرمجية:</p>", unsafe_allow_html=True)
            st.code(result, language="")
        else:
            st.error("فشل الإجراء: حقل النص فارغ. يرجى كتابة البيانات أولاً.")
