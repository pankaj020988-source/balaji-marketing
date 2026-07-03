import streamlit as st
from PIL import Image
import time

# 🌐 मुख्य पेज कॉन्फिगरेशन आणि डिझाईन सेटिंग्ज
st.set_page_config(page_title="बालाजी सायबर पॉईंट - अधिकृत पोर्टल", page_icon="💻", layout="wide")

# मूळ साईडबार आणि डिझाईन मॅनेजमेंट पूर्णपणे गायब करणे
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none !important;
        }
        [data-testid="collapsedControl"] {
            display: none !important;
        }
        div.stTabs [data-baseweb="tab-list"] {
            display: flex !important;
            justify-content: center !important;
        }
    </style>
""", unsafe_allow_html=True)

# मेमरीमध्ये ३ वेगवेगळ्या जाहिराती आणि त्यांचे फोटो साठवणे
if "ad1_text" not in st.session_state:
    st.session_state.ad1_text = "📌 **जाहिरात १ (नवीन महाभरती २०२६):** विविध शासकीय विभागांमध्ये बंपर जागा उपलब्ध! ऑनलाईन अर्ज अचूक भरण्यासाठी आजच सर्व आवश्यक कागदपत्रांसह दुकानात भेट द्या."
if "ad1_img" not in st.session_state: st.session_state.ad1_img = None

if "ad2_text" not in st.session_state:
    st.session_state.ad2_text = "📌 **जाहिरात २ (परीक्षा प्रवेशपत्र):** चालू महिन्यातील स्पर्धा परीक्षांचे हॉल तिकीट (Admit Card) डाऊनलोड करणे आणि परीक्षा केंद्र तपासणी सेवा सुरू आहे."
if "ad2_img" not in st.session_state: st.session_state.ad2_img = None

if "ad3_text" not in st.session_state:
    st.session_state.ad3_text = "📌 **जाहिरात ३ (ट्रॅव्हल बुकिंग ऑफर):** पावसाळी पर्यटनासाठी हॉटेल्स आणि मेकमायट्रिप (MakeMyTrip) टूर पॅकेजेसवर विशेष सवलत सुरू आहे! आजच आपले बुकिंग करा."
if "ad3_img" not in st.session_state: st.session_state.ad3_img = None

# ==========================================
# 📢 १. मुख्य डिजिटल होर्डिंग बॅनर
# ==========================================
st.markdown("""
<div style="background: linear-gradient(135deg, #002f6c 0%, #0056b3 100%); padding: 35px; border-radius: 12px; text-align: center; color: white; border: 3px solid #d4af37; box-shadow: 0px 4px 15px rgba(0,0,0,0.3); margin-bottom: 25px;">
    <h1 style="color: #e5be3b; font-size: 42px; font-weight: bold; margin-bottom: 5px; font-family: 'Arial';">बालाजी सायबर पॉईंट (माणगाव)</h1>
    <h3 style="font-size: 22px; font-weight: 500; margin-top: 0; opacity: 0.95;">तुमचे डिजिटल आणि ट्रॅव्हल सोल्यूशन पार्टनर!</h3>
    <hr style="border: 1px solid #d4af37; width: 60%; margin: 15px auto;">
    <div style="display: flex; justify-content: space-around; font-size: 18px; font-weight: bold; margin-top: 15px; flex-wrap: wrap;">
        <div style="margin: 5px;">💻 ऑनलाईन फॉर्म्स</div>
        <div style="margin: 5px;">📄 सरकारी योजना</div>
        <div style="margin: 5px;">✈️ ट्रॅव्हल बुकिंग</div>
        <div style="margin: 5px;">💰 कर आणि महसूल</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 🎯 २. मल्टिपल लाइव्ह डिजिटल नोटीस बोर्ड (३ जाहिरातींचे टॅब्स)
# ==========================================
st.markdown("### 📢 चालू घडामोडी आणि नवीन जाहिराती (Select Advertisement)")

# जाहिराती पाहण्यासाठी ग्राहकांना ३ सुंदर पर्याय दिले आहेत
ad_tab1, ad_tab2, ad_tab3 = st.tabs(["🔥 नोकर भरती (Ad 1)", "📄 हॉल तिकीट (Ad 2)", "✨ विशेष ऑफर्स (Ad 3)"])

with ad_tab1:
    col1, col2 = st.columns([3, 2])
    with col1: st.info(st.session_state.ad1_text)
    with col2:
        if st.session_state.ad1_img is not None: st.image(st.session_state.ad1_img, use_container_width=True)
        else: st.warning("📌 नोकर भरतीचे अधिकृत पत्रक पाहण्यासाठी दुकानात संपर्क करा.")

with ad_tab2:
    col1, col2 = st.columns([3, 2])
    with col1: st.info(st.session_state.ad2_text)
    with col2:
        if st.session_state.ad2_img is not None: st.image(st.session_state.ad2_img, use_container_width=True)
        else: st.warning("📌 परीक्षा प्रवेशपत्र डाऊनलोड करणे सुरू आहे.")

with ad_tab3:
    col1, col2 = st.columns([3, 2])
    with col1: st.info(st.session_state.ad3_text)
    with col2:
        if st.session_state.ad3_img is not None: st.image(st.session_state.ad3_img, use_container_width=True)
        else: st.warning("📌 मेकमायट्रिप टूर बुकिंग ऑफर्ससाठी आजच भेट द्या.")

st.write("---")

# ==========================================
# 🌟 ३. दुकानात उपलब्ध असलेल्या सेवांची यादी
# ==========================================
st.markdown("### 🌟 आमच्या प्रमुख डिजिटल सेवा:")
col_serv1, col_serv2 = st.columns(2)
with col_serv1:
    st.markdown("""
    **💻 ऑनलाईन फॉर्म्स आणि नोकरभरती सेवा:**
    * केंद्र व राज्य शासनाच्या सर्व प्रकारच्या नोकरभरतीचे ऑनलाईन अर्ज भरणे.
    * विविध स्पर्धा परीक्षांचे हॉल तिकीट (Admit Card) डाऊनलोड करणे.
    
    **✈️ ट्रॅव्हल आणि टूर बुकिंग सोल्यूशन्स:**
    * देश-विदेशातील विमानाची तिकिटे (Flight Tickets) झटपट बुक करणे.
    * कौटुंबिक आणि ग्रुप सहलींसाठी विशेष हॉटेल्स आणि मेकमायट्रिप (MakeMyTrip) टूर पॅकेजेस.
    """)
with col_serv2:
    st.markdown("""
    **📄 शासकीय योजना आणि दाखले:**
    * घरकुल योजना, शबरी आवास योजना आणि इतर महत्त्वाच्या शासकीय योजनांचे अर्ज.
    * उत्पन्न दाखला, रेशन कार्ड दुरुस्ती व नवीन रेशन कार्ड नोंदणी अर्ज.
    
    **💰 कर, महसूल आणि फोटो टूल्स:**
    * नगरपंचायत प्रॉपर्टी टॅक्स ऑनलाईन भरणे व वीज बिल भरणे.
    * पासपोर्ट साईझ फोटो तयार करणे आणि फोटो-सही अचूक रीसाईझ करणे.
    """)

st.write("")
st.markdown("<div style='background-color: #154c8c; color: white; padding: 12px; border-radius: 6px; text-align: center; font-size: 16px; font-weight: bold;'>📍 पत्ता: बालाजी कॉम्प्लेक्स, माणगाव, रायगड, महाराष्ट्र</div>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# ⚙️ ४. गुप्त ओनर कंट्रोल पॅनेल (३ जाहिराती बदलण्यासाठी)
# ==========================================
with st.expander("⚙️ सायबर ओनर कंट्रोल पॅनेल (लपविलेले विभाग)"):
    st.write("वेबसाईटवरील ३ वेगवेगळ्या जाहिराती आणि त्यांचे फोटो बदलण्यासाठी ओनर पासवर्ड टाका.")
    secret_pass = st.text_input("🔑 ओनर पासवर्ड प्रविष्ट करा:", type="password", key="mkt_pass")
    
    if secret_pass == "Balaji@123":
        st.success("🔓 कंट्रोल पॅनेल अनलॉक झाले!")
        
        # ३ स्वतंत्र जाहिराती एडिट करण्याचे सेक्शन
        st.markdown("#### 📝 जाहिरात १ बदला")
        new_ad1 = st.text_area("मजकूर (Ad 1):", value=st.session_state.ad1_text)
        new_file1 = st.file_uploader("फोटो (Ad 1):", type=["jpg", "png", "jpeg"], key="f1")
        
        st.markdown("#### 📝 जाहिरात २ बदला")
        new_ad2 = st.text_area("मजकूर (Ad 2):", value=st.session_state.ad2_text)
        new_file2 = st.file_uploader("फोटो (Ad 2):", type=["jpg", "png", "jpeg"], key="f2")
        
        st.markdown("#### 📝 जाहिरात ३ बदला")
        new_ad3 = st.text_area("मजकूर (Ad 3):", value=st.session_state.ad3_text)
        new_file3 = st.file_uploader("फोटो (Ad 3):", type=["jpg", "png", "jpeg"], key="f3")
        
        if st.button("🚀 सर्व जाहिराती एकत्र लाईव्ह करा", type="primary", use_container_width=True):
            st.session_state.ad1_text = new_ad1
            if new_file1 is not None: st.session_state.ad1_img = Image.open(new_file1)
                
            st.session_state.ad2_text = new_ad2
            if new_file2 is not None: st.session_state.ad2_img = Image.open(new_file2)
                
            st.session_state.ad3_text = new_ad3
            if new_file3 is not None: st.session_state.ad3_img = Image.open(new_file3)
                
            st.success("✅ सर्व जाहिराती यशस्वीरित्या अपडेट झाल्या आहेत! वर जाऊन तपासा.")
            st.rerun()
