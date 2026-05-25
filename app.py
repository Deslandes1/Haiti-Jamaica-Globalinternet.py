import streamlit as st

# Set up page configurations with a clean responsive layout
st.set_page_config(
    page_title="GLOBALINTERNET.PY | JAMAICA",
    page_icon="🇯🇲",
    layout="centered"
)

# =========================================================================
# 🌟 POWERFUL CSS ANIMATION ENGINE (Shining Stars & Floating Balloons)
# =========================================================================
st.markdown(
    """
    <style>
    /* Main App Background Configuration */
    .stApp {
        background: linear-gradient(135deg, #060913 0%, #0d1527 100%);
        color: #ffffff;
        overflow-x: hidden;
    }

    /* --- Shining Star Animations --- */
    @keyframes flashStar {
        0%, 100% { opacity: 0.2; transform: scale(0.8) rotate(0deg); }
        50% { opacity: 1; transform: scale(1.2) rotate(180deg); filter: drop-shadow(0 0 10px #ffcc00); }
    }
    .star {
        position: absolute;
        width: 4px;
        height: 4px;
        background: #ffffff;
        border-radius: 50%;
        animation: flashStar 3s infinite ease-in-out;
    }

    /* --- Floating Balloon Animations --- */
    @keyframes floatUp {
        0% { transform: translateY(100vh) translateX(0); opacity: 0; }
        10% { opacity: 0.6; }
        90% { opacity: 0.6; }
        100% { transform: translateY(-20vh) translateX(50px); opacity: 0; }
    }
    .balloon {
        position: absolute;
        width: 25px;
        height: 32px;
        border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
        animation: floatUp 12s infinite linear;
        opacity: 0;
    }
    .balloon::after {
        content: "🎈";
        font-size: 28px;
        position: absolute;
        top: -10px;
        left: -5px;
    }

    /* --- Brand Header Layout --- */
    .brand-container {
        text-align: center;
        background: rgba(255, 255, 255, 0.03);
        border: 2px solid #00b060; /* Jamaican Green border accents */
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0, 176, 96, 0.15);
        margin-bottom: 35px;
    }
    .company-title {
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #febd11, #ffffff, #00b060); /* Gold, White, Green */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .flag-style {
        font-size: 5rem;
        line-height: 1;
        margin: 0;
        filter: drop-shadow(0 4px 10px rgba(0,0,0,0.5));
    }

    /* --- Interactive Action Buttons --- */
    .contact-btn {
        display: block;
        text-align: center;
        background: linear-gradient(90deg, #febd11, #00b060);
        color: #060913 !important;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 16px;
        border-radius: 10px;
        text-decoration: none;
        box-shadow: 0 4px 20px rgba(254, 189, 17, 0.4);
        transition: 0.3s ease;
        margin-top: 15px;
    }
    .contact-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 176, 96, 0.6);
    }
    </style>

    <!-- Background FX Injection Layer -->
    <div class="star" style="top: 15%; left: 10%; animation-delay: 0s;"></div>
    <div class="star" style="top: 25%; left: 80%; animation-delay: 1s;"></div>
    <div class="star" style="top: 60%; left: 15%; animation-delay: 0.5s;"></div>
    <div class="star" style="top: 75%; left: 85%; animation-delay: 1.8s;"></div>
    <div class="star" style="top: 45%; left: 50%; animation-delay: 2.2s;"></div>
    
    <div class="balloon" style="left: 15%; animation-delay: 0s; animation-duration: 14s;"></div>
    <div class="balloon" style="left: 45%; animation-delay: 3s; animation-duration: 11s;"></div>
    <div class="balloon" style="left: 75%; animation-delay: 6s; animation-duration: 16s;"></div>
    """,
    unsafe_allow_html=True
)

# =========================================================================
# 🇯🇲 FRONT-END BRAND UI HEADER
# =========================================================================
st.markdown(
    """
    <div class="brand-container">
        <p class="flag-style">🇯🇲</p>
        <h1 class="company-title">GLOBALINTERNET.PY</h1>
        <p style="color: #febd11; font-weight: bold; font-size: 1.1rem; letter-spacing: 1px;">
            BUILDING SOVEREIGN GLOBAL DIGITAL ECOSYSTEMS
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================================
# 👨‍💻 ABOUT THE COMPANY SECTION
# =========================================================================
st.subheader("👨‍💻 About the Company")
st.info(
    "**GlobalInternet.py** was founded by **GESNER DESLANDES** – owner, founder, and lead engineer. "
    "We build Python‑based software on demand for clients worldwide. Like Silicon Valley, but with a "
    "Haitian touch and outstanding outcomes."
)

st.markdown("---")

# =========================================================================
# 🛠️ SERVICE DISPLAY NODES
# =========================================================================
st.subheader("🚀 Services We Offer in Jamaica")

with st.expander("🧠 AI‑powered solutions", expanded=True):
    st.write("Advanced intelligent systems including smart conversational chatbots, automated data analysis structures, and streamlined business operations automation.")

with st.expander("🗳️ Complete election & voting systems", expanded=True):
    st.write("Highly secure, decentralized, multi‑language corporate or organizational voting frameworks with real‑time server verification matrices.")

with st.expander("🌐 Web applications", expanded=True):
    st.write("Custom interactive visual dashboards, optimized software internal tools, and robust cloud‑native online platforms built to scale.")

with st.expander("📦 Full package delivery", expanded=True):
    st.write("We email you the complete, raw source code directory and provide personalized guidance through your deployment installation pipelines. **We build it, you own it.**")

# =========================================================================
# 📞 SECURE CONTACT TERMINAL ZONE
# =========================================================================
st.markdown("---")
st.subheader("📲 Connect Directly With Our Deployment Desk")

col_phone, col_email = st.columns(2)

with col_phone:
    st.info("📞 Voice / WhatsApp Support")
    st.markdown(
        """
        <a class="contact-btn" href="https://wa.me/18768589428" target="_blank">
            💬 +1 (876) 858-9428
        </a>
        """,
        unsafe_allow_html=True
    )

with col_email:
    st.info("📧 Corporate Inquiries Email")
    st.markdown(
        """
        <a class="contact-btn" href="mailto:deslandes78@gmail.com">
            ✉️ deslandes78@gmail.com
        </a>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 GLOBALINTERNET.PY | Serving Sovereignty Across Jamaica. Powered by Streamlit Engine.")
