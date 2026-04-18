import streamlit as st
import re
import urllib.parse

# 1. Page Setup
st.set_page_config(page_title="SafePay AI", page_icon="🛡️", layout="centered")

# 2. Branding & UI
st.title("🛡️ SafePay AI - Online Scam Shield")
st.markdown("### Mee bank account mariyu dabbulaki oka AI rakshana.")

# Save Link Tip
st.success("💡 *Tip:* Ee link ni ventane vadukovadaniki, browser options lo *'Add to Home Screen'* cheసుకోండి.")

st.info("Meeku vachina suspicious message or link ni kinda box lo paste chesi 'Scan' nokkandi.")

# 3. Input Section
user_message = st.text_area("SMS / WhatsApp Message / Link ikkada paste cheyandi:", height=150, placeholder="Example: You won a lottery! Click here to claim...")

# App Link for Sharing
app_url = "https://safepay-ai-check.streamlit.app"

# 4. Action Button & Logic
if st.button("Scan for Scams 🔍"):
    if user_message:
        scam_keywords = ["lottery", "win", "gift", "blocked", "kyc", "urgent", "paisa", "free recharge", "click here", "update", "customer care", "prize"]
        risk_score = 0
        findings = []

        for word in scam_keywords:
            if word.lower() in user_message.lower():
                risk_score += 30
                findings.append(f"Suspicious word: *{word}*")

        urls = re.findall(r'(https?://\S+)', user_message)
        if urls:
            risk_score += 20
            if any(s in urls[0] for s in ["bit.ly", "tinyurl", "t.co", "short", "click", "web.app"]):
                risk_score += 40
                findings.append("Danger: Hidden/Short link detected.")

        st.divider()
        result_text = ""
        if risk_score >= 70:
            st.error(f"🚨 DANGER! (Risk Score: {risk_score}%)")
            result_text = "Idi kachithanga oka SCAM! Beware."
            st.subheader(result_text)
        elif risk_score >= 30:
            st.warning(f"⚠️ WARNING! (Risk Score: {risk_score}%)")
            result_text = "Idi suspicious ga undi. Be careful."
            st.write(result_text)
        else:
            st.success("✅ SAFE! Ee message safe ga unnattu gurtinchabadindi.")
            result_text = "Ee message safe ga undi."
            st.balloons()
            
        # WhatsApp Share Button
        share_msg = f"SafePay AI Results: {result_text}\n\nMeeku vachina messages ni kuda ikkada check chesukondi: {app_url}"
        encoded_msg = urllib.parse.quote(share_msg)
        whatsapp_url = f"https://wa.me/?text={encoded_msg}"
        
        st.link_button("Share this Result on WhatsApp 🟢", whatsapp_url)
    else:
        st.warning("Daya chesi edaina message ni mundu enter cheyandi.")

# 5. The Mission & Support Section (Fully Visible)
st.markdown("---")
st.markdown("### 🙏 SafePay AI: మా లక్ష్యం & మీ చిన్న సాయం")
st.write("""
ప్రతి రోజూ ఎంతో మంది సామాన్యుల కష్టార్జితం సైబర్ నేరగాళ్ల పాలవుతోంది. దీన్ని అడ్డుకోవడమే *SafePay AI* ప్రధాన లక్ష్యం. 

వ్యక్తిగతంగా నేను కొన్నేళ్ల క్రితం ఇతరులకు సహాయం చేసే క్రమంలో ఆర్థిక ఇబ్బందుల్లో (అప్పుల్లో) చిక్కుకున్నాను. ఆ సమస్యల నుండి బయటపడుతూనే, సమాజానికి మేలు చేయాలని ఈ యాప్‌ని రూపొందించాను.

ఎవరినీ మోసం చేయకుండా, నిజాయితీగా నేను చేస్తున్న ఈ చిన్న ప్రయత్నాన్ని ప్రోత్సహించండి. మీరు అందించే *కేవలం ₹20* సహాయం, నా బాధ్యతలను తీర్చుకోవడానికి మరియు ఈ యాప్‌ను మరింత మెరుగ్గా మార్చడానికి నాకు కొండంత అండగా ఉంటుంది.
""")

# UPI Details & QR Code display
col1, col2 = st.columns([1, 1])
with col1:
    st.info("Support Amount: *₹20*")
    # IKKADA MEE CORRECT UPI ID IVVANDI
    st.success("UPI ID: **8639471410@ybl**")
with col2:
    try:
        st.image("qr_code.png", caption="Scan & Pay ₹20", width=180)
    except:
    st.image("https://raw.githubusercontent.com/murthyAI/SafePay-AI/main/qr.png", caption="Scan & Pay ₹20", width=180)

# 6. Sidebar
st.sidebar.title("SafePay AI")
st.sidebar.info("💡 Ee app ni save cheyandi: browser options (three dots) loki velli 'Add to Home Screen' click cheyandi.")
st.sidebar.caption("© 2026 Protecting your money.")
