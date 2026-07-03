import streamlit as st
from PIL import Image
import io

# ==========================================
# 🌐 १. मुख्य पेज कॉन्फिगरेशन आणि थीम सेटिंग्ज
# ==========================================
st.set_page_config(page_title="बालाजी सायबर पॉईंट - अधिकृत पोर्टल", page_icon="💻", layout="wide")

st.markdown("""
    <style>
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
        .zoom-effect img { transition: transform .2s; }
        .zoom-effect img:hover { transform: scale(1.03); box-shadow: 0px 4px 15px rgba(0,0,0,0.3); }
        .service-card {
            background: #ffffff; padding: 18px; border-radius: 10px;
            box-shadow: 0px 3px 10px rgba(0,0,0,0.08); border-left: 6px solid #0056b3;
            margin-bottom: 15px; transition: all 0.3s ease;
        }
        .service-card:hover { transform: translateY(-3px); box-shadow: 0px 6px 18px rgba(0,0,0,0.15); background: #f8faff; }
        .service-title { color: #002f6c; font-size: 18px; font-weight: bold; margin-bottom: 5px; }
        .service-desc { color: #444444; font-size: 14px; line-height: 1.4; }
    </style>
""", unsafe_allow_html=True)

# मेमरी चालू ठेवणे
if "owner_password" not in st.session_state: st.session_state.owner_password = "Balaji@123"

for i in range(1, 4):
    for j in range(1, 6):
        state_key = f"ad{i}_img_{j}"
        if state_key not in st.session_state: st.session_state[state_key] = None

if "ad1_main_text" not in st.session_state: st.session_state.ad1_main_text = "🔥 **नोकर भरती विशेष:** सर्व प्रकारचे ऑनलाईन जॉब फॉर्म्स, रेल्वे, पोलीस आणि बँक भरतीचे अर्ज अचूक भरून मिळतील."
if "ad2_main_text" not in st.session_state: st.session_state.ad2_main_text = "📄 **हॉल तिकीट व प्रवेशपत्र अपडेट:** विविध चालू परीक्षांचे प्रवेशपत्र डाऊनलोड करून मिळतील."
if "ad3_main_text" not in st.session_state: st.session_state.ad3_main_text = "✈️ **विशेष प्रिंटिंग आणि बुकिंग सेवा:** फ्लाईट तिकीट बुकिंग, कलर झेरॉक्स आणि स्कॅनिंग जलद सेवा."

# मुख्य होर्डिंग बॅनर
st.markdown("""
<div style="background: linear-gradient(135deg, #002f6c 0%, #0056b3 100%); padding: 35px; border-radius: 12px; text-align: center; color: white; border: 3px solid #d4af37; box-shadow: 0px 4px 15px rgba(0,0,0,0.3); margin-bottom: 25px;">
    <h1 style="color: #e5be3b; font-size: 44px; font-weight: bold; margin-bottom: 5px; font-family: 'Arial';">बालाजी सायबर पॉईंट</h1>
    <h3 style="font-size: 24px; font-weight: 500; margin-top: 0; opacity: 0.95;">डिजिटल क्रांती आणि शासकीय सेवा केंद्र</h3>
    <p style="font-size: 18px; color: #d4af37; font-weight: bold; margin-top: 5px;">सर्व ऑनलाईन सेवा एकाच छताखाली! | ☑ अचूक काम ☑ जलद सेवा ☑ वाजवी दर</p>
</div>
""", unsafe_allow_html=True)

# 🌟 स्क्रीनवर ३ नवीन आकर्षक बदललेले VIP टॅब्स 🌟
main_tab1, main_tab2, main_tab3 = st.tabs([
    "🔥 महाभरती व लाईव्ह ऑफर्स (Live Updates)", 
    "🏛️ डिजिटल ई-सेवा केंद्र (VIP Services)", 
    "⚡ मोफत मोबाईल ऑटो-प्रिंट (Instant Print)"
])

# ------------------------------------------
# टॅब १: महाभरती व लाईव्ह ऑफर्स
# ------------------------------------------
with main_tab1:
    st.markdown("### 📢 चालू घडामोडी आणि नवीन जाहिराती (फोटोवर क्लिक करून मोठे करा)")
    ad_tab1, ad_tab2, ad_tab3 = st.tabs(["🔥 नोकर भरती (Ad 1)", "📄 हॉल तिकीट (Ad 2)", "✨ विशेष सेवा ऑफर्स (Ad 3)"])

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
                    st.download_button(label=f"🔍 सेपरेट झूम ({img_idx})", data=img_buffer.getvalue(), file_name=f"balaji_ad_{tab_index}_{img_idx}.png", mime="image/png", key=f"dl_{tab_index}_{img_idx}", use_container_width=True)
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
            <div class="service-desc">सर्व प्रकारचे शासकीय दाखले, अधिकृत प्रपत्रे आणि सरकारी योजनांचे ऑनलाईन अर्ज अचूकपणे भरून मिळतील.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #002f6c;">
            <div class="service-title">📄 डोमासिएल, उत्पन्न व जातीचे दाखले</div>
            <div class="service-desc">तहसीलदार कचेरीचे अधिकृत रहिवासी दाखले, वार्षिक उत्पन्नाचे प्रमाणपत्र आणि डिजिटल जातीचे दाखले जलद सेवा.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #28a745;">
            <div class="service-title">💳 नवीन पॅन CARD / दुरुस्ती</div>
            <div class="service-desc">नवीन पॅन कार्ड काढणे, हरवलेले पॅन कार्ड मिळवणे किंवा जुन्या पॅन कार्डमधील नाव, जन्मतारीख व फोटो दुरुस्ती.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #dc3545;">
            <div class="service-title">🗳️ मतदार कार्ड आणि आधार लिंक</div>
            <div class="service-desc">नवीन मतदार यादीत नाव नोंदवणे, मतदार कार्ड (Voter ID) डिजिटल करणे आणि आधार कार्ड लिंक करण्याची कामे.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #17a2b8;">
            <div class="service-title">📜 गॅझेट गॅरंटी सुविधा (नाव/धर्म बदलणे)</div>
            <div class="service-desc">शासकीय राजपत्रात (Gazette) अधिकृत नाव बदलणे, विवाहांतर नाव बदलणे किंवा कायदेशीर धर्म बदलण्याची संपूर्ण प्रक्रिया.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #6f42c1;">
            <div class="service-title">👮 पोलीस व्हेरिफिकेशन (Police Verification)</div>
            <div class="service-desc">नोकरी, चारित्र्य प्रमाणपत्र किंवा पासपोर्टसाठी लागणारे अधिकृत ऑनलाईन पोलीस व्हेरिफिकेशन अर्ज सुविधा.[cite: 1]</div>
        </div>
        """, unsafe_allow_html=True)

    with col_grid2:
        st.markdown("<h4 style='color: #0056b3; border-bottom: 2px solid #d4af37; padding-bottom: 5px;'>🖨️ | स्पेशल प्रिंटिंग, झेरॉक्स आणि ट्रॅव्हल बुकिंग</h4>", unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card" style="border-left-color: #20c997;">
            <div class="service-title">💻 | सर्व प्रकारचे ऑनलाईन जॉब फॉर्म्स</div>
            <div class="service-desc">केंद्र व राज्य शासनाच्या सर्व मेगाभरती, पोलीस, आर्मी, रेल्वे व अर्ज १००% अचूक भरून मिळतील.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #007bff;">
            <div class="service-title">✈️ | फ्लाईट बुकिंग केंद्र (Flight Tickets)</div>
            <div class="service-desc">विमान प्रवासाचे तिकिट बुकिंग, हॉटेल्स आणि प्रवासाचे झटपट व खात्रीशीर आरक्षण सोल्यूशन्स.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #ffc107;">
            <div class="service-title">📐 A3 | हाय-क्वालिटी प्रिंटिंग सेवा</div>
            <div class="service-desc">मोठ्या आकाराचे दस्तऐवज, नकाशा, अधिकृत पत्रके आणि विशेष दस्तऐवजांची हाय-क्वालिटी डिजिटल प्रिंटिंग सुविधा.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #343a40;">
            <div class="service-title">🎨 कलर झेरॉक्स (Xerox) व स्कॅनिंग</div>
            <div class="service-desc">कागदपत्रांची कडक लेझर कलर झेरॉक्स आणि स्कॅनिंग सेवा.[cite: 1]</div>
        </div>
        <div class="service-card" style="border-left-color: #6c757d;">
            <div class="service-title">🔒 A3 आणि A4 कडक लॅमिनेशन</div>
            <div class="service-desc">तुमची महत्त्वाची प्रमाणपत्रे सुरक्षित ठेवण्यासाठी कडक वॉटरप्रूफ लॅमिनेशन.[cite: 1]</div>
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
            तुमच्या मोबाईलमधील फोटो, डॉक्युमेंट्स किंवा PDF फाईल्स थेट दुकानाच्या प्रिंटरवर पाठवण्यासाठी खालील बटनेवर क्लिक करा.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button(
        "🚀 स्मार्ट ऑटो प्रिंट सिस्टीम उघडा (Open Print Portal)", 
        "https://balaji-autoprint.onrender.com/", 
        type="primary", 
        use_container_width=True
    )

st.write("")
st.markdown("""<div style='background-color: #002f6c; color: white; padding: 15px; border-radius: 8px; text-align: center; font-size: 16px; font-weight: bold; border: 2px solid #d4af37;'>📍 पत्ताः बालाजी कॉम्प्लेक्स, माणगाव, रायगड, Maharashtra[cite: 1] | 📞 संपर्क: 8007365051[cite: 1] | 🟢 व्हॉट्सॲप: 8806789013[cite: 1]</div>""", unsafe_allow_html=True)
st.write("---")

# जाहिरात सेटिंग्ज
col_foot1, col_foot2 = st.columns([5, 1])
with col_foot1: st.markdown("<p style='font-size: 13px; color: #555; margin-top: 10px; font-weight: bold;'>🙏 धन्यवाद ! पुन्हा भेट द्या![cite: 1] | Designed by Balaji Cyber Point</p>", unsafe_allow_html=True)
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
            t1 = st.text_input("मुख्य नोटीस ओळ १:", value=st.session_state.ad1_main_text)
            f1_1 = st.file_uploader("फोटो १ (Ad 1):", type=["jpg", "png", "jpeg"], key="fu_1_1")
            submit_all = st.form_submit_button("🚀 सर्व जाहिराती आणि फोटो एकत्र लाईव्ह करा", use_container_width=True)
            if submit_all:
                st.session_state.ad1_main_text = t1
                if f1_1: st.session_state.ad1_img_1 = Image.open(f1_1)
                st.success("✅ अपडेट झाले!")
                st.rerun()
