import streamlit as st
from PIL import Image
import io

# ==========================================
# 🌐 १. मुख्य पेज कॉन्फिगरेशन आणि थीम सेटिंग्ज
# ==========================================
st.set_page_config(page_title="बालाजी सायबर पॉईंट - अधिकृत पोर्टल", page_icon="💻", layout="wide")

# संपूर्ण साईट १००% फुल स्क्रीन रुंदीला सेट करणे आणि मूळ मेनू लपवणे (CSS मॅजिक)
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1.5rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 100% !important;
        }
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
        .zoom-effect img {
            transition: transform .2s;
        }
        .zoom-effect img:hover {
            transform: scale(1.03);
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 💾 २. कायमस्वरूपी डेटा स्टोरेज मेमरी (प्रत्येक विभागात ५ फोटो)
# ==========================================
if "owner_password" not in st.session_state: st.session_state.owner_password = "Balaji@123"

# ३ विभागांसाठी ५-५ फोटोंचे मेमरी कप्पे तयार करणे
for i in range(1, 4):
    for j in range(1, 6):
        state_key = f"ad{i}_img_{j}"
        if state_key not in st.session_state:
            st.session_state[state_key] = None

# मूळ टेक्स्ट नोटीस
if "ad1_main_text" not in st.session_state: st.session_state.ad1_main_text = "🔥 **नोकर भरती विशेष:** रेल्वे, पोलीस आणि बँक भरतीचे अर्ज सुरू आहेत."
if "ad2_main_text" not in st.session_state: st.session_state.ad2_main_text = "📄 **हॉल तिकीट अपडेट:** विविध परीक्षांचे प्रवेशपत्र डाऊनलोड करून मिळतील."
if "ad3_main_text" not in st.session_state: st.session_state.ad3_main_text = "✨ **विशेष ट्रॅव्हल बुकिंग ऑफर्स:** हॉटेल्स आणि फ्लाईट्सवर आकर्षक डिस्काउंट!"

# ==========================================
# 📢 ३. मुख्य डिजिटल होर्डिंग बॅनर
# ==========================================
st.markdown("""
<div style="background: linear-gradient(135deg, #002f6c 0%, #0056b3 100%); padding: 35px; border-radius: 12px; text-align: center; color: white; border: 3px solid #d4af37; box-shadow: 0px 4px 15px rgba(0,0,0,0.3); margin-bottom: 25px;">
    <h1 style="color: #e5be3b; font-size: 44px; font-weight: bold; margin-bottom: 5px; font-family: 'Arial';">बालाजी सायबर पॉईंट (माणगाव)</h1>
    <h3 style="font-size: 22px; font-weight: 500; margin-top: 0; opacity: 0.95;">तुमचे डिजिटल आणि ट्रॅव्हल सोल्यूशन पार्टनर!</h3>
    <hr style="border: 1px solid #d4af37; width: 50%; margin: 15px auto;">
    <div style="display: flex; justify-content: space-around; font-size: 18px; font-weight: bold; margin-top: 15px; flex-wrap: wrap;">
        <div style="margin: 5px;">💻 ऑनलाईन फॉर्म्स</div>
        <div style="margin: 5px;">📄 सरकारी योजना</div>
        <div style="margin: 5px;">✈️ ट्रॅव्हल बुकिंग</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 🎯 ४. डिजिटल नोटीस बोर्ड (प्रत्येक विभागात ५ फोटो झूम सुविधेसह)
# ==========================================
st.markdown("### 📢 चालू घडामोडी आणि नवीन जाहिराती (फोटोवर क्लिक करून मोठे करा)")

ad_tab1, ad_tab2, ad_tab3 = st.tabs(["🔥 नोकर भरती (Ad 1)", "📄 हॉल तिकीट (Ad 2)", "✨ विशेष ऑफर्स (Ad 3)"])

# --- फंक्शन: ५ फोटो ग्रीडमध्ये सुंदर दाखवणे आणि झूम सुविधा देणे ---
def display_advertisement_gallery(tab_index, main_text):
    st.info(main_text)
    
    cols = st.columns(5)
    has_any_image = False
    
    for img_idx in range(1, 6):
        img_key = f"ad{tab_index}_img_{img_idx}"
        img_data = st.session_state[img_key]
        
        with cols[img_idx - 1]:
            if img_data is not None:
                has_any_image = True
                st.markdown('<div class="zoom-effect">', unsafe_allow_html=True)
                st.image(img_data, use_container_width=True, caption=f"पत्रक {img_idx}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                img_buffer = io.BytesIO()
                img_data.save(img_buffer, format="PNG")
                st.download_button(label=f"🔍 सेपरेट झूम करा ({img_idx})", data=img_buffer.getvalue(), file_name=f"balaji_ad_{tab_index}_{img_idx}.png", mime="image/png", key=f"dl_{tab_index}_{img_idx}", use_container_width=True)
            else:
                st.write(f"ℹ️ पत्रक {img_idx} रिकामे")
                
    if not has_any_image:
        st.warning("📌 या विभागात सध्या कोणतेही अधिकृत पत्रक अपलोड केलेले नाही. माहितीसाठी दुकानात संपर्क करा.")

with ad_tab1:
    display_advertisement_gallery(1, st.session_state.ad1_main_text)

with ad_tab2:
    display_advertisement_gallery(2, st.session_state.ad2_main_text)

with ad_tab3:
    display_advertisement_gallery(3, st.session_state.ad3_main_text)

st.write("---")

# ==========================================
# 🌟 ५. दुकानात उपलब्ध असलेल्या सेवांची यादी
# ==========================================
st.markdown("### 🌟 आमच्या प्रमुख डिजिटल सेवा:")
col_serv1, col_serv2 = st.columns(2)
with col_serv1:
    st.markdown("""
    **💻 On-line फॉर्म्स आणि नोकरभरती सेवा:**
    * केंद्र व राज्य शासनाच्या सर्व प्रकारच्या नोकरभरतीचे ऑनलाईन अर्ज भरणे.
    * विविध स्पर्धा परीक्षांचे हॉल तिकीट (Admit Card) डाऊनलोड करणे.
    
    **✈️ ट्रॅव्हल आणि टूर बुकिंग सोल्यूशन्स:**
    * देश-विदेशातील विमानाची तिकिटे (Flight Tickets) आणि हॉटेल्स झटपट बुक करणे.
    * कौटुंबिक आणि ग्रुप सहलींसाठी विशेष मेकमायट्रिप (MakeMyTrip) टूर पॅकेजेस.
    """)
with col_serv2:
    st.markdown("""
    **📄 शासकीय योजना आणि दाखले:**
    * घरकुल योजना, शबरी आवास योजना आणि इतर महत्त्वाच्या शासकीय योजनांचे अर्ज.
    * उत्पन्न दाखला, रेशन कार्ड दुरुस्ती व नवीन रेशन कार्ड नोंदणी अर्ज.
    
    **💰 डिजिटल फोटो टूल्स:**
    * पासपोर्ट साईझ फोटो तयार करणे.
    * सरकारी फॉर्म्ससाठी फोटो आणि सही अचूक रीसाईझ करणे.
    """)

st.write("---")

# ==========================================
# ⚙️ ६. चोरून जाहिरात बदलणारी सुंदर सेटिंग सिस्टीम (फूटर्सच्या आत)
# ==========================================
col_foot1, col_foot2 = st.columns([5, 1])

with col_foot1:
    st.markdown("<p style='font-size: 11px; color: #aaa; margin-top: 10px;'>© 2026 Balaji Cyber Point. All Rights Reserved.</p>", unsafe_allow_html=True)

with col_foot2:
    # ⚙️ हा तो गुप्त ओनर सेटिंग पर्याय आहे!
    show_admin = st.checkbox("⚙️ Settings", value=False, key="admin_check_box")

# ग्राहक चेकबॉक्सवर टिक करणार नाहीत, पण तुम्ही क्लिक करताच खाली पासवर्ड बॉक्स उघडेल
if show_admin:
    st.markdown("### ⚙️ सायबर ओनर कंट्रोल पॅनेल (🔐 Restricted Area)")
    secret_pass = st.text_input("🔑 ओनर पासवर्ड प्रविष्ट करा:", type="password", key="mkt_pass")
    
    if secret_pass == st.session_state.owner_password:
        st.success("🔓 कंट्रोल पॅनेल यशस्वीरित्या अनलॉक झाले!")
        
        # अ) पासवर्ड बदलणे
        st.markdown("#### 🔑 ओनर पासवर्ड मॅनेजमेंट (Change Password)")
        new_secure_password = st.text_input("🛡️ नवीन सुरक्षित पासवर्ड टाईप करा:", type="password", key="change_pwd_box")
        if st.button("💾 नवीन पासवर्ड कायमचा सेव्ह करा"):
            if new_secure_password.strip() != "":
                st.session_state.owner_password = new_secure_password
                st.success(f"✅ पासवर्ड बदलला! नवीन पासवर्ड: '{new_secure_password}'")
                st.rerun()
        
        st.write("---")
        st.markdown("### 📝 प्रत्येक विभागातील ५-५ फोटो मॅनेजमेंट")
        
        with st.form("master_ads_form"):
            # विभाग १
            st.markdown("#### 📁 विभाग १: नोकर भरती (Ad 1)")
            t1 = st.text_input("मुख्य नोटीस ओळ १:", value=st.session_state.ad1_main_text)
            f1_1 = st.file_uploader("फोटो १ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_1")
            f1_2 = st.file_uploader("फोटो २ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_2")
            f1_3 = st.file_uploader("फोटो ३ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_3")
            f1_4 = st.file_uploader("फोटो ४ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_4")
            f1_5 = st.file_uploader("फोटो ५ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_5")
            
            st.write("---")
            # विभाग २
            st.markdown("#### 📁 विभाग २: हॉल तिकीट (Ad 2)")
            t2 = st.text_input("मुख्य नोटीस ओळ २:", value=st.session_state.ad2_main_text)
            f2_1 = st.file_uploader("फोटो १ (Ad 2):", type=["jpg", "png", "jpeg"], key="fu_2_1")
            f2_2 = st.file_uploader("फोटो २ (Ad 2):", type=["jpg", "png", "jpeg"], key="fu_2_2")
            f2_3 = st.file_uploader("फोटो ३ (Ad 2):", type=["jpg", "png", "jpeg"], key="fu_2_3")
            f2_4 = st.file_uploader("फोटो ४ (Ad 2):", type=["jpg", "png", "jpeg"], key="fu_2_4")
            f2_5 = st.file_uploader("फोटो ५ (Ad 2):", type=["jpg", "png", "jpeg"], key="fu_2_5")
            
            st.write("---")
            # विभाग ३
            st.markdown("#### 📁 विभाग ३: विशेष ऑफर्स (Ad 3)")
            t3 = st.text_input("मुख्य नोटीस ओळ ३:", value=st.session_state.ad3_main_text)
            f3_1 = st.file_uploader("फोटो १ (Ad 3):", type=["jpg", "png", "jpeg"], key="fu_3_1")
            f3_2 = st.file_uploader("फोटो २ (Ad 3):", type=["jpg", "png", "jpeg"], key="fu_3_2")
            f3_3 = st.file_uploader("फोटो ३ (Ad 3):", type=["jpg", "png", "jpeg"], key="fu_3_3")
            f3_4 = st.file_uploader("फोटो ४ (Ad 3):", type=["jpg", "png", "jpeg"], key="fu_3_4")
            f3_5 = st.file_uploader("फोटो ५ (Ad 3):", type=["jpg", "png", "jpeg"], key="fu_3_5")
            
            submit_all = st.form_submit_button("🚀 सर्व जाहिराती आणि फोटो एकत्र लाईव्ह करा", use_container_width=True)
            
            if submit_all:
                st.session_state.ad1_main_text = t1
                if f1_1: st.session_state.ad1_img_1 = Image.open(f1_1)
                if f1_2: st.session_state.ad1_img_2 = Image.open(f1_2)
                if f1_3: st.session_state.ad1_img_3 = Image.open(f1_3)
                if f1_4: st.session_state.ad1_img_4 = Image.open(f1_4)
                if f1_5: st.session_state.ad1_img_5 = Image.open(f1_5)
                    
                st.session_state.ad2_main_text = t2
                if f2_1: st.session_state.ad2_img_1 = Image.open(f2_1)
                if f2_2: st.session_state.ad2_img_2 = Image.open(f2_2)
                if f2_3: st.session_state.ad2_img_3 = Image.open(f2_3)
                if f2_4: st.session_state.ad2_img_4 = Image.open(f2_4)
                if f2_5: st.session_state.ad2_img_5 = Image.open(f2_5)
                    
                st.session_state.ad3_main_text = t3
                if f3_1: st.session_state.ad3_img_1 = Image.open(f3_1)
                if f3_2: st.session_state.ad3_img_2 = Image.open(f3_2)
                if f3_3: st.session_state.ad3_img_3 = Image.open(f3_3)
                if f3_4: st.session_state.ad3_img_4 = Image.open(f3_4)
                if f3_5: st.session_state.ad3_img_5 = Image.open(f3_5)
                
                st.success("✅ सर्व १५ जाहिरातींचे फोटो सिस्टीम मेमरीत यशस्वीरित्या लाईव्ह झाले आहेत!")
                st.rerun()
    elif secret_pass != "":
        st.error("❌ चुकीचा पासवर्ड!")
