import streamlit as st
from PIL import Image

# 🌐 मुख्य पेज कॉन्फिगरेशन आणि डिझाईन सेटिंग्ज
st.set_page_config(page_title="बालाजी सायबर पॉईंट - अधिकृत पोर्टल", page_icon="💻", layout="centered")

# मेमरीमध्ये चालू नोकरभरतीचा मजकूर आणि बॅनर साठवणे
if "live_ad_text" not in st.session_state:
    st.session_state.live_ad_text = "📌 **नवीन महाभरती २०२६:** विविध शासकीय विभागांमध्ये बंपर जागा उपलब्ध! ऑनलाईन अर्ज अचूक भरण्यासाठी आजच सर्व आवश्यक कागदपत्रांसह दुकानात भेट द्या."
if "live_ad_banner" not in st.session_state:
    st.session_state.live_ad_banner = None

# ==========================================
# 📢 १. मुख्य डिजिटल होर्डिंग बॅनर (HTML/CSS)
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

st.write("")

# ==========================================
# 🎯 २. लाइव्ह डिजिटल नोटीस बोर्ड (जाहिराती प्रदर्शन)
# ==========================================
st.markdown("### 📢 नवीन सरकारी नोकर भरती व महत्त्वाच्या जाहिराती")
col_ad1, col_ad2 = st.columns([3, 2])

with col_ad1:
    st.info(st.session_state.live_ad_text)
with col_ad2:
    if st.session_state.live_ad_banner is not None:
        st.image(st.session_state.live_ad_banner, caption="अधिकृत जाहिरात पत्रक", use_container_width=True)
    else:
        st.warning("📌 **परीक्षा प्रवेशपत्र (Admit Card):** चालू महिन्यातील विविध स्पर्धा परीक्षांचे हॉल तिकीट डाऊनलोड करणे आणि परीक्षा केंद्र तपासणी सेवा सुरू आहे.")

st.write("---")

# ==========================================
# 🌟 ३. दुकानात उपलब्ध असलेल्या सर्व डिजिटल सेवांची यादी
# ==========================================
st.markdown("### 🌟 आमच्या प्रमुख डिजिटल सेवा:")

col_serv1, col_serv2 = st.columns(2)
with col_serv1:
    st.markdown("""
    **💻 ऑनलाईन फॉर्म्स आणि नोकरभरती सेवा:**
    * केंद्र व राज्य शासनाच्या सर्व प्रकारच्या नोकरभरतीचे ऑनलाईन अर्ज भरणे.
    * विविध स्पर्धा परीक्षांचे हॉल तिकीट (Admit Card) डाऊनलोड करणे.
    * निकाल पाहणे आणि गुणवत्ता यादी तपासणे.
    
    **✈️ ट्रॅव्हल आणि टूर बुकिंग सोल्यूशन्स:**
    * देश-विदेशातील विमानाची तिकिटे (Flight Tickets) झटपट बुक करणे.
    * रेल्वे आणि बस प्रवासाचे आरक्षित तिकिटे मिळणे.
    * कौटुंबिक आणि ग्रुप सहलींसाठी विशेष हॉटेल्स आणि मेकमायट्रिप (MakeMyTrip) टूर पॅकेजेस.
    """)

with col_serv2:
    st.markdown("""
    **📄 शासकीय योजना आणि दाखले:**
    * घरकुल योजना, शबरी आवास योजना आणि इतर महत्त्वाच्या शासकीय योजनांचे अर्ज.
    * उत्पन्न दाखला, रेशन कार्ड दुरुस्ती व नवीन रेशन कार्ड नोंदणी अर्ज.
    * पॅन कार्ड काढणे आणि आधार कार्ड अपडेट संबंधित सेवा.
    
    **💰 कर, महसूल आणि फोटो टूल्स:**
    * नगरपंचायत प्रॉपर्टी टॅक्स ऑनलाईन भरणे.
    * महावितरण (MSEDCL) घरगुती व व्यावसायिक वीज बिल भरणे.
    * पासपोर्ट साईझ फोटो तयार करणे, फोटो व सही योग्य पिक्सेलमध्ये रीसाईझ करणे.
    """)

st.write("")

# ==========================================
# 📍 ४. दुकानाचा अधिकृत पत्ता
# ==========================================
st.markdown("""
<div style="background-color: #154c8c; color: white; padding: 12px; border-radius: 6px; text-align: center; font-size: 16px; font-weight: bold; box-shadow: 0px 2px 8px rgba(0,0,0,0.15);">
    📍 पत्ता: बालाजी कॉम्प्लेक्स, माणगाव, रायगड, महाराष्ट्र
</div>
""", unsafe_allow_html=True)

st.write("---")

# ==========================================
# ⚙️ ५. चोरून जाहिरात बदलणारा गुप्त ॲडमीन कंट्रोल (केवळ तुमच्यासाठी)
# ==========================================
with st.expander("⚙️ सायबर ओनर कंट्रोल पॅनेल (लपविलेले विभाग)"):
    st.write("होम पेजवरील चालू भरतीचा मजकूर आणि बॅनर बदलण्यासाठी पासवर्ड टाका.")
    secret_pass = st.text_input("🔑 ओनर पासवर्ड प्रविष्ट करा:", type="password", key="mkt_pass")
    
    if secret_pass == "Balaji@123":
        st.success("🔓 कंट्रोल पॅनेल अनलॉक झाले!")
        new_text = st.text_area("📝 नवीन भरतीचा मजकूर लिहा:", value=st.session_state.live_ad_text)
        new_file = st.file_uploader("🖼️ जाहिरातीचा नवीन फोटो अपलोड करा (JPG/PNG):", type=["jpg", "png", "jpeg"])
        
        if st.button("🚀 नवीन जाहिरात वेबसाईटवर लाईव्ह करा", type="primary", use_container_width=True):
            st.session_state.live_ad_text = new_text
            if new_file is not None:
                st.session_state.live_ad_banner = Image.open(new_file)
            st.success("✅ जाहिरात यशस्वीरित्या बदलली आहे! वर जाऊन पेज तपासा.")
            st.rerun()
