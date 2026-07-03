import streamlit as st
from PIL import Image
import io

# ==========================================
# 🌐 १. मुख्य पेज कॉन्फिगरेशन आणि कडक सिक्युरिटी CSS/JS
# ==========================================
st.set_page_config(page_title="बालाजी सायबर पॉईंट - अधिकृत पोर्टल", page_icon="💻", layout="wide")

st.markdown("""
    <style>
        /* 🔒 १. स्क्रीनशॉट, प्रिंट आणि कॉपीपासून संरक्षण करणारी कडक सिक्युरिटी */
        @media print {
            body { display: none !important; } /* प्रिंट काढण्याचा प्रयत्न केल्यास पूर्ण पेज गायब होईल */
        }
        
        body {
            -webkit-touch-callout: none !important;
            -webkit-user-select: none !important;
            -khtml-user-select: none !important;
            -moz-user-select: none !important;
            -ms-user-select: none !important;
            user-select: none !important; /* संपूर्ण पेजवरील टेक्स्ट किंवा इमेज सिलेक्ट/कॉपी बंद */
        }
        
        img {
            -webkit-user-drag: none !important; /* इमेज ओढून (Drag) डेस्कटॉपवर सेव्ह करणे बंद */
            pointer-events: none !important;    /* माऊसच्या क्लिक इव्हेंट्स ब्लॉक */
        }
        
        /* मूळ सेटिंग्ज पॅडिंग */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1.5rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 100% !important;
        }
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        div.stTabs [data-baseweb="tab-list"] { display: flex !important; justify-content: center !important; }
        
        /* 🔍 झूम इफेक्ट - फक्त पाहण्यासाठी, सेव्ह करण्यासाठी नाही */
        .zoom-effect img {
            transition: transform .2s;
            pointer-events: none !important;
        }
        .zoom-effect img:hover {
            transform: scale(1.08);
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
        
        .service-card {
            background: #ffffff; padding: 18px; border-radius: 10px;
            box-shadow: 0px 3px 10px rgba(0,0,0,0.08); border-left: 6px solid #0056b3;
            margin-bottom: 15px; transition: all 0.3s ease;
        }
        .service-card:hover { transform: translateY(-3px); box-shadow: 0px 6px 18px rgba(0,0,0,0.15); background: #f8faff; }
        .service-title { color: #002f6c; font-size: 18px; font-weight: bold; margin-bottom: 5px; }
        .service-desc { color: #444444; font-size: 14px; line-height: 1.4; }
    </style>
    
    <!-- 🔒 २. राईट क्लिक (Right-Click) आणि कीबोर्ड शॉर्टकट्स ब्लॉक करणारे स्क्रिप्ट -->
    <script>
        document.addEventListener('contextmenu', event => event.preventDefault()); /* राईट क्लिक बंद */
        document.onkeydown = function(e) {
            if (e.ctrlKey && 
                (e.keyCode === 67 || 
                 e.keyCode === 86 || 
                 e.keyCode === 85 || 
                 e.keyCode === 83 || 
                 e.keyCode === 80)) {
                return false; /* Ctrl+C, Ctrl+V, Ctrl+U (Source Code), Ctrl+S (Save), Ctrl+P (Print) पूर्ण बंद */
            }
        };
    </script>
""", unsafe_allow_html=True)

# मेमरी चालू ठेवणे
if "owner_password" not in st.session_state: st.session_state.owner_password = "Balaji@123"

for i in range(1, 4):
    for j in range(1, 6):
        state_key = f"ad{i}_img_{j}"
        if state_key not in st.session_state: st.session_state[state_key] = None

if "ad1_main_text" not in st.session_state: st.session_state.ad1_main_text = "🔥 **नोकर भरती व शैक्षणिक विशेष:** सर्व प्रकारचे ऑनलाईन जॉब फॉर्म्स, रेल्वे, पोलीस भरती आणि शाळा-कॉलेजचे ऑनलाईन प्रवेश अर्ज अचूक भरून मिळतील."
if "ad2_main_text" not in st.session_state: st.session_state.ad2_main_text = "📄 **हॉल तिकीट व प्रवेशपत्र अपडेट:** विविध चालू परीक्षांचे प्रवेशपत्र डाऊनलोड करून मिळतील."
if "ad3_main_text" not in st.session_state: st.session_state.ad3_main_text = "✈️ **विशेष प्रिंटिंग आणि बुकिंग सेवा:** फ्लाईट तिकीट बुकिंग, color झेरॉक्स आणि स्कॅनिंग जलद सेवा."

# ==========================================
# 📢 २. मुख्य जुना रॉयल् ब्लू बॅनर
# ==========================================
st.markdown("""
<div style="background: linear-gradient(135deg, #002f6c 0%, #0056b3 100%); padding: 35px; border-radius: 12px; text-align: center; color: white; border: 3px solid #d4af37; box-shadow: 0px 4px 15px rgba(0,0,0,0.3); margin-bottom: 25px;">
    <h1 style="color: #e5be3b; font-size: 44px; font-weight: bold; margin-bottom: 5px; font-family: 'Arial';">बालाजी सायबर पॉईंट</h1>
    <h3 style="font-size: 24px; font-weight: 500; margin-top: 0; opacity: 0.95;">डिजिटल क्रांती आणि शासकीय सेवा केंद्र</h3>
    <p style="font-size: 18px; color: #d4af37; font-weight: bold; margin-top: 5px;">सर्व ऑनलाईन सेवा एकाच छताखाली! | ☑ अचूक काम ☑ जलद सेवा ☑ वाजवी दर</p>
</div>
""", unsafe_allow_html=True)

# 🌟 ३ मुख्य टॅब्स 🌟
main_tab1, main_tab2, main_tab3 = st.tabs([
    "🔥 महाभरती व लाईव्ह ऑफर्स (Live Updates)", 
    "🏛️ डिजिटल ई-सेवा केंद्र (Services)", 
    "⚡ मोफत मोबाईल ऑटो-प्रिंट (Instant Print)"
])

# ------------------------------------------
# टॅब १: महाभरती व लाईव्ह ऑफर्स (🔒 सिक्युरिटी गॅलरी)
# ------------------------------------------
with main_tab1:
    st.markdown("### 📢 चालू घडामोडी आणि नवीन जाहिराती (🔒 सुरक्षेसाठी डाऊनलोड/स्क्रीनशॉट बंद केला आहे)")
    ad_tab1, ad_tab2, ad_tab3 = st.tabs(["🔥 नोकर भरती आणि शैक्षणिक (Ad 1)", "📄 हॉल तिकीट (Ad 2)", "✨ विशेष सेवा ऑफर्स (Ad 3)"])

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
                    # 🎯 डाऊनलोड बटन पूर्णपणे काढून टाकले आहे, फक्त कडक माऊस-प्रोटेक्टेड झूम दिसेल!
                    st.markdown('<div class="zoom-effect">', unsafe_allow_html=True)
                    st.image(img_data, use_container_width=True, caption=f"पत्रक {img_idx}")
                    st.markdown('</div>', unsafe_allow_html=True)
                else: st.write(f"ℹ️ पत्रक {img_idx} खाली")
        if not has_any_image: st.warning("📌 या विभागात सध्या कोणतेही अधिकृत पत्रक अपलोड केलेले नाही.")

    with ad_tab1: display_advertisement_gallery(1, st.session_state.ad1_main_text)
    with ad_tab2: display_advertisement_gallery(2, st.session_state.ad2_main_text)
    with ad_tab3: display_advertisement_gallery(3, st.session_state.ad3_main_text)

# ------------------------------------------
# टॅब २: डिजिटल ई-सेवा केंद्र
# ------------------------------------------
with main_tab2:
    st.markdown("<h3 style='color: #002f6c; margin-bottom: 20px;'>🌟 आमच्याकडील प्रमुख सेवा (Center Offerings)</h3>", unsafe_allow_html=True)
    col_grid1, col_grid2 = st.columns(2)
    with col_grid1:
        st.markdown("<h4 style='color: #0056b3; border-bottom: 2px solid #d4af37; padding-bottom: 5px;'>🏛️ महा-ई-सेवा केंद्र व शासकीय कामे</h4>", unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card" style="border-left-color: #e5be3b;">
            <div class="service-title">🏛️ महा-ई-सेवा केंद्र कामे</div>
            <div class="service-desc">सर्व प्रकारचे शासकीय दाखले, अधिकृत प्रपत्रे आणि सरकारी योजनांचे ऑनलाईन अर्ज अचूकपणे भरून मिळतील.</div>
        </div>
        <div class="service-card" style="border-left-color: #002f6c;">
            <div class="service-title">📄 डोमासिएल, उत्पन्न व जातीचे दाखले</div>
            <div class="service-desc">तहसीलदार कचेरीचे अधिकृत रहिवासी दाखले, वार्षिक उत्पन्नाचे प्रमाणपत्र आणि डिजिटल जातीचे दाखले जलद सेवा.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_grid2:
        st.markdown("<h4 style='color: #0056b3; border-bottom: 2px solid #d4af37; padding-bottom: 5px;'>🖨️ | स्पेशल प्रिंटिंग, झेरॉक्स आणि ट्रॅव्हल बुकिंग</h4>", unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card" style="border-left-color: #20c997;">
            <div class="service-title">💻 | सर्व प्रकारचे ऑनलाईन जॉब फॉर्म्स</div>
            <div class="service-desc">केंद्र व राज्य शासनाच्या सर्व मेगाभरती, पोलीस, आर्मी, रेल्वे व अर्ज १००% अचूक भरून मिळतील.</div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------
# टॅब ३: मोफत मोबाईल ऑटो-प्रिंट
# ------------------------------------------
with main_tab3:
    st.markdown("""
    <div style="text-align: center; margin-top: 20px; padding: 30px; background-color: #f8faff; border-radius: 12px; border: 2px dashed #0056b3;">
        <h2 style="color: #002f6c; margin-bottom: 5px;">👑 श्री बालाजी सायबर पॉईंट 👑</h2>
        <h4 style="color: #fd7e14; margin-top: 0; margin-bottom: 20px;">स्मार्ट मोबाईल ऑटो प्रिंट सिस्टीम</h4>
        <p style="font-size: 16px; color: #444; margin-bottom: 25px;">
            तुमच्या मोबाईलमधील फोटो, डॉक्युमेंट्स किंवा PDF फाईल्स थेट दुकानाच्या प्रिंटरवर पाठवण्यासाठी खालील बटनावर क्लिक करा.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 स्मार्ट ऑटो प्रिंट सिस्टीम उघडा (Open Print Portal)", "https://balaji-autoprint.onrender.com/", type="primary", use_container_width=True)

st.write("")
st.markdown("""<div style='background-color: #002f6c; color: white; padding: 15px; border-radius: 8px; text-align: center; font-size: 16px; font-weight: bold; border: 2px solid #d4af37;'>📍 पत्ताः बालाजी कॉम्प्लेक्स, माणगाव, रायगड, Maharashtra | 📞 संपर्क: 8007365051 | 🟢 व्हॉट्सॲप: 8806789013</div>""", unsafe_allow_html=True)
st.write("---")

# ==========================================
# ⚙️ ४. सायबर ओनर CONTROL PANEL
# ==========================================
col_foot1, col_foot2 = st.columns([5, 1])
with col_foot1: st.markdown("<p style='font-size: 13px; color: #555; margin-top: 10px; font-weight: bold;'>🙏 धन्यवाद ! पुन्हा भेट द्या! | Designed by Balaji Cyber Point</p>", unsafe_allow_html=True)
with col_foot2: show_admin = st.checkbox("⚙️ Settings", value=False, key="admin_check_box")

if show_admin:
    st.markdown("### ⚙️ सायबर ओनर CONTROL PANEL (🔐 Restricted Area)")
    secret_pass = st.text_input("🔑 ओनर पासवर्ड प्रविष्ट करा:", type="password", key="mkt_pass")
    if secret_pass == st.session_state.owner_password:
        st.success("🔓 Control पॅनेल यशस्वीरित्या अनलॉक झाले!")
        new_secure_password = st.text_input("🛡️ | नवीन सुरक्षित पासवर्ड टाईप करा:", type="password")
        if st.button("💾 नवीन पासवर्ड कायमचा सेव्ह करा"):
            if new_secure_password.strip() != "":
                st.session_state.owner_password = new_secure_password
                st.success("✅ पासवर्ड बदलला!")
                st.rerun()
        
        st.write("---")
        with st.form("master_ads_form"):
            st.markdown("#### 📁 विभाग १: नोकर भरती आणि शैक्षणिक (Ad 1)")
            t1 = st.text_input("मुख्य नोटीस ओळ १:", value=st.session_state.ad1_main_text)
            f1_1 = st.file_uploader("फोटो १ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_1")
            f1_2 = st.file_uploader("फोटो २ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_2")
            f1_3 = st.file_uploader("फोटो ३ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_3")
            f1_4 = st.file_uploader("फोटो ४ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_4")
            f1_5 = st.file_uploader("फोटो ५ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_5")
            
            submit_all = st.form_submit_button("🚀 सर्व जाहिराती आणि फोटो एकत्र लाईव्ह करा", use_container_width=True)
            if submit_all:
                st.session_state.ad1_main_text = t1
                if f1_1: st.session_state.ad1_img_1 = Image.open(f1_1)
                if f1_2: st.session_state.ad1_img_2 = Image.open(f1_2)
                if f1_3: st.session_state.ad1_img_3 = Image.open(f1_3)
                if f1_4: st.session_state.ad1_img_4 = Image.open(f1_4)
                if f1_5: st.session_state.ad1_img_5 = Image.open(f1_5)
                st.success("✅ यशस्वीरित्या अपडेट झाले!")
                st.rerun()
