import streamlit as st

# Force wide, full-screen layout and page configurations
st.set_page_config(
    page_title="GLOBALINTERNET.PY | JAMAICA",
    page_icon="🇯🇲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# 🌟 COMPACT ANIMATION & FULL-SCREEN LAYOUT ENGINE (CSS)
# =========================================================================
st.markdown(
    """
    <style>
    /* Force application to eliminate margins and scrolling */
    .stApp {
        background: linear-gradient(135deg, #060913 0%, #0d1527 100%);
        color: #ffffff;
        overflow: hidden;
        height: 100vh;
    }
    
    /* Clean block paddings */
    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0rem !important;
        max-width: 95% !important;
    }

    /* --- Shining Star Animations --- */
    @keyframes flashStar {
        0%, 100% { opacity: 0.2; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); filter: drop-shadow(0 0 8px #ffcc00); }
    }
    .star {
        position: absolute;
        width: 3px;
        height: 3px;
        background: #ffffff;
        border-radius: 50%;
        animation: flashStar 3s infinite ease-in-out;
    }

    /* --- Floating Balloon Animations --- */
    @keyframes floatUp {
        0% { transform: translateY(100vh); opacity: 0; }
        10% { opacity: 0.5; }
        90% { opacity: 0.5; }
        100% { transform: translateY(-10vh); opacity: 0; }
    }
    .balloon {
        position: absolute;
        animation: floatUp 10s infinite linear;
        opacity: 0;
        font-size: 24px;
    }

    /* --- Top-Left Flex Header Layout --- */
    .header-flex-container {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 20px;
        margin-bottom: 15px;
        padding-bottom: 5px;
        border-bottom: 1px solid rgba(0, 176, 96, 0.2);
    }
    .large-flag-left {
        font-size: 4rem;
        line-height: 1;
        margin: 0;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));
    }
    .company-title-right {
        font-size: 2.5rem;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #febd11, #ffffff, #00b060);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    /* --- Strong White Copy Headings --- */
    .strong-white-heading {
        color: #ffffff !important;
        font-size: 1.25rem;
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 3px;
        border-left: 4px solid #00b060;
        padding-left: 8px;
    }
    
    .about-text {
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.4;
    }

    /* --- Compact Feature Service Block Cards --- */
    .service-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 176, 96, 0.2);
        border-radius: 8px;
        padding: 8px 12px;
        margin-bottom: 6px;
        height: 100%;
    }
    .service-title {
        font-size: 0.95rem;
        font-weight: bold;
        color: #febd11;
        margin: 0 0 2px 0;
    }
    .service-desc {
        font-size: 0.85rem;
        color: #cbd5e1;
        margin: 0;
        line-height: 1.3;
    }

    /* --- Ultra-Compact Action Call Buttons --- */
    .contact-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(90deg, #febd11, #00b060);
        color: #060913 !important;
        font-weight: bold;
        font-size: 0.95rem;
        padding: 8px;
        border-radius: 6px;
        text-decoration: none;
        box-shadow: 0 4px 12px rgba(254, 189, 17, 0.2);
        margin-top: 2px;
    }
    
    .contact-label {
        font-size: 0.85rem;
        color: #94a3b8;
        margin-bottom: 1px;
        font-weight: 500;
    }
    </style>

    <!-- Background Decoration Node Injections -->
    <div class="star" style="top: 15%; left: 35%; animation-delay: 0s;"></div>
    <div class="star" style="top: 25%; left: 80%; animation-delay: 1s;"></div>
    <div class="star" style="top: 50%; left: 75%; animation-delay: 0.5s;"></div>
    <div class="star" style="top: 75%; left: 20%; animation-delay: 1.5s;"></div>
    
    <div class="balloon" style="left: 45%; animation-delay: 0s; animation-duration: 9s;">🎈</div>
    <div class="balloon" style="left: 90%; animation-delay: 4s; animation-duration: 11s;">🎈</div>
    """,
    unsafe_allow_html=True
)

# =========================================================================
# 🇯🇲 TOP-LEFT FLAG & COMPANY TITLE ROW HEADER
# =========================================================================
st.markdown(
    """
    <div class="header-flex-container">
        <p class="large-flag-left">🇯🇲</p>
        <h1 class="company-title-right">GLOBALINTERNET.PY</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================================
# 🏢 ABOUT THE COMPANY (STRONG WHITE)
# =========================================================================
st.markdown('<div class="strong-white-heading">👨‍💻 About the Company</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="about-text">
        <strong>GlobalInternet.py</strong> was founded by <strong>GESNER DESLANDES</strong> – owner, founder, and lead engineer. 
        We build Python‑based software on demand for clients worldwide. Like Silicon Valley, but with a Haitian touch and outstanding outcomes.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================================
# 🚀 SERVICES MATRIX (GRID ROW)
# =========================================================================
st.markdown('<div class="strong-white-heading">🚀 Services We Offer in Jamaica</div>', unsafe_allow_html=True)

# Generate a 4-column balanced configuration layer
serv_col1, serv_col2, serv_col3, serv_col4 = st.columns(4)

with serv_col1:
    st.markdown(
        """
        <div class="service-card">
            <p class="service-title">🧠 AI‑powered solutions</p>
            <p class="service-desc">Advanced intelligent systems including smart conversational chatbots, automated data analysis structures, and streamlined business automation.</p>
        </div>
        """, unsafe_allow_html=True
    )

with serv_col2:
    st.markdown(
        """
        <div class="service-card">
            <p class="service-title">🗳️ Complete election & voting systems</p>
            <p class="service-desc">Highly secure, decentralized, multi‑language corporate or organizational voting frameworks with real‑time server verification matrices.</p>
        </div>
        """, unsafe_allow_html=True
    )

with serv_col3:
    st.markdown(
        """
        <div class="service-card">
            <p class="service-title">🌐 Web applications</p>
            <p class="service-desc">Custom interactive visual dashboards, optimized software internal tools, and robust cloud‑native online platforms built to scale.</p>
        </div>
        """, unsafe_allow_html=True
    )

with serv_col4:
    st.markdown(
        """
        <div class="service-card">
            <p class="service-title">📦 Full package delivery</p>
            <p class="service-desc">We email you the complete, raw source code directory and provide personalized guidance through your deployment installation pipelines. We build it, you own it.</p>
        </div>
        """, unsafe_allow_html=True
    )

# =========================================================================
# 📞 CONNECT DIRECTLY HUB (STRONG WHITE)
# =========================================================================
st.markdown('<div class="strong-white-heading">📲 Connect Directly With Our Deployment Desk</div>', unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    st.markdown('<div class="contact-label">📞 Voice / WhatsApp Support</div>', unsafe_allow_html=True)
    st.markdown(
        '<a class="contact-btn" href="https://wa.me/18768589428" target="_blank">💬 +1 (876) 858-9428</a>',
        unsafe_allow_html=True
    )

with btn_col2:
    st.markdown('<div class="contact-label">📧 Corporate Inquiries Email</div>', unsafe_allow_html=True)
    st.markdown(
        '<a class="contact-btn" href="mailto:deslandes78@gmail.com">✉️ deslandes78@gmail.com</a>',
        unsafe_allow_html=True
    )

# =========================================================================
# 📜 FOOTER BASE NODE
# =========================================================================
st.markdown(
    """
    <div style="text-align: center; margin-top: 15px; font-size: 0.75rem; color: #64748b; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 5px;">
        © 2026 GLOBALINTERNET.PY | Serving Sovereignty Across Jamaica. Powered by Streamlit Engine.
    </div>
    """,
    unsafe_allow_html=True
)
