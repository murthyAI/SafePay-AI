import streamlit as st
import re

# 1. Page Setup
st.set_page_config(page_title="SafePay AI", page_icon="🛡️", layout="centered")

# 2. Branding & UI
st.title("🛡️ SafePay AI - Online Scam Shield")
st.markdown("### Mee bank account mariyu dabbulaki oka AI rakshana.")
st.info("Meeku vachina suspicious message or link ni kinda box lo paste chesi 'Scan' nokkandi.")

# 3. Input Section
user_message = st.text_area("SMS / WhatsApp Message / Link ikkada paste cheyandi:", height=150, placeholder="Example: You won a lottery! Click here to claim...")

# 4. Action Button & Logic
if st.button("Scan for Scams 🔍"):
    if user_message:
        # Simple AI Detection Logic
        scam_keywords = ["lottery", "win", "gift", "blocked", "kyc", "urgent", "paisa", "free recharge", "click here", "update", "customer care", "prize"]
        risk_score = 0
        findings = []

        # Keyword Check
        for word in scam_keywords:
            if word.lower() in user_message.lower():
                risk_score += 30
                findings.append(f"Anumanaspada padam (Suspicious word): *{word}*")

        # Link Analysis
        urls = re.findall(r'(https?://\S+)', user_message)
        if urls:
            risk_score += 20
            if any(s in urls[0] for s in ["bit.ly", "tinyurl", "t.co", "short", "click", "web.app"]):
                risk_score += 40
                findings.append("Danger: Idi oka hidden/short link. Hackers deenni ekkuvaga vadutharu.")

        # Display Results
        st.divider()
        if risk_score >= 70:
            st.error(f"🚨 DANGER! (Risk Score: {risk_score}%)")
            st.subheader("Idi kachithanga oka SCAM! Aa link click cheyakandi, evariki OTP cheppakandi.")
        elif risk_score >= 30:
            st.warning(f"⚠️ WARNING! (Risk Score: {risk_score}%)")
            st.write("Idi suspicious ga undi. Meeru kachithanga telisina valla thō verify cheyinchukondi.")
        else:
            st.success("✅ SAFE! Ee message safe ga unnattu gurtinchabadindi.")
            st.balloons()
            
        if findings:
            with st.expander("Detailed Analysis (Enduku idi scam?):"):
                for f in findings:
                    st.write(f"- {f}")
    else:
        st.warning("Daya chesi edaina message ni mundu enter cheyandi.")

# 5. The Mission & Support Section (Combined Option 1 & 2)
st.markdown("---")
with st.expander("🙏 SafePay AI: Oka chinna vinnapam - Ma Lakshyam"):
    st.write("""
    *Mithrulara,*
    
    Prathi roju entho mandhi samanyula kashtarjitham cyber neragalla palavthundi. Deenni addukovadame *SafePay AI* pradhana lakshyam. 

    Vyakthigathanga nenu konneilla kritham itharulaku sahayam chese kramamlo arthikanga ibbandhullo (appullo) chikkukunnanu. Aa samasyala nundi bayatapaduthune, samajamlo marevaru ilanti mosala barina padi kashtapadakudadhane uddheshamtho ee app ni rupondhinchanu.

    Evarini mosam cheyakunda, poorthi nijayithitho koodina oka sevanu meeku andhinche ee chinna prayathnanni prothsahinchandi. Mee vanthuga chese oka chinna sahayam (Donation), na arthika samasyalanu theerchukovadaniki mariyu ee app nu marinthaga shakthivanthanga marchadaniki naku kondantha andhaga untundi. 

    Mee sayam kevalam nake kadhu, mosapothunna vandhala mandhiki oka rakshana kavachamla maruthundi. Padhi mandhiki melu jarige ee prayanamlo meeru bhagaswamyulu avvandi.
    """)
    st.info("Support via UPI: *[8639471610@ybl]*") # Add your UPI ID here!

# 6. Sidebar
st.sidebar.title("SafePay AI")
st.sidebar.caption("© 2026 Protecting your money from hackers.")
