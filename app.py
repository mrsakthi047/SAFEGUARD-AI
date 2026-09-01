
import streamlit as st
from PIL import Image

# ============================================================
# SAFEGUARD AI — UI CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SAFEGUARD AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(80, 120, 255, 0.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(170, 80, 255, 0.10),
            transparent 30%
        ),
        #080A12;
    color: #F5F7FF;
}

/* Main title */

.hero-title {
    text-align: center;
    font-size: 58px;
    font-weight: 800;
    letter-spacing: -2px;
    margin-top: 35px;
    margin-bottom: 8px;
}

.hero-title span {
    background: linear-gradient(
        90deg,
        #7C8CFF,
        #C084FC,
        #60A5FA
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    text-align: center;
    color: #AAB2C8;
    font-size: 19px;
    margin-bottom: 45px;
}

/* Cards */

.feature-card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 22px;
    padding: 25px;
    min-height: 170px;
    transition: 0.3s;
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: rgba(140,150,255,0.45);
}

.feature-icon {
    font-size: 35px;
}

.feature-title {
    font-size: 21px;
    font-weight: 700;
    margin-top: 12px;
}

.feature-text {
    color: #AAB2C8;
    font-size: 14px;
    line-height: 1.6;
}

/* Section */

.section-title {
    text-align: center;
    font-size: 32px;
    font-weight: 750;
    margin-top: 65px;
    margin-bottom: 25px;
}

/* Buttons */

.stButton > button {
    border-radius: 14px;
    min-height: 48px;
    font-weight: 700;
}

/* Footer */

.footer {
    text-align: center;
    color: #7E879E;
    margin-top: 70px;
    padding: 30px;
    border-top: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""
<div class="hero-title">
    🛡️ <span>SAFEGUARD AI</span>
</div>

<div class="hero-subtitle">
    Think. Detect. Protect.
    <br>
    AI-powered content safety for text and images.
</div>
""", unsafe_allow_html=True)


# ============================================================
# FEATURE CARDS
# ============================================================

st.markdown(
    '<div class="section-title">Intelligent Protection</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-icon">💬</div>

    <div class="feature-title">
    Smart Text Safety
    </div>

    <div class="feature-text">
    Analyze messages for potentially harmful,
    toxic and abusive language.
    </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-icon">🌍</div>

    <div class="feature-title">
    Multilingual Analysis
    </div>

    <div class="feature-text">
    Detect supported languages and prepare
    multilingual content for safety analysis.
    </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-icon">👁️</div>

    <div class="feature-title">
    Vision Protection
    </div>

    <div class="feature-text">
    Analyze visual content and protect
    potentially sensitive images.
    </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# TEXT SAFETY
# ============================================================

st.markdown(
    '<div class="section-title">💬 Text Safety Scanner</div>',
    unsafe_allow_html=True
)

text_input = st.text_area(
    "Enter a message to analyze",
    height=150,
    placeholder="Type a message here..."
)


if st.button(
    "🛡️ Analyze Message",
    use_container_width=True
):

    if not text_input.strip():

        st.warning(
            "Please enter a message first."
        )

    else:

        # ----------------------------------------------------
        # Try to use our analysis engine if available
        # ----------------------------------------------------

        try:

            result = analyze_message(
                text_input
            )

            risk = result["risk_level"]

            if risk == "Low":

                st.success(
                    "✅ Message appears safe."
                )

            elif risk == "Medium":

                st.warning(
                    "⚠️ Potentially harmful content detected."
                )

            else:

                st.error(
                    "🚨 High-risk content detected."
                )

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Language",
                    result["language"]
                )

            with c2:
                st.metric(
                    "Toxicity",
                    result["toxicity_label"]
                )

            with c3:
                st.metric(
                    "Risk",
                    result["risk_level"]
                )

            st.subheader(
                "🔒 Protected Message"
            )

            st.info(
                result["protected_text"]
            )

        except Exception as e:

            st.error(
                "Safety engine is not connected yet."
            )

            st.caption(
                f"Technical information: {e}"
            )


# ============================================================
# IMAGE SAFETY
# ============================================================

st.markdown(
    '<div class="section-title">🖼️ Image Safety</div>',
    unsafe_allow_html=True
)

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp"]
)


if uploaded_image is not None:

    image = Image.open(
        uploaded_image
    ).convert("RGB")

    st.image(
        image,
        caption="Uploaded image",
        use_container_width=True
    )

    st.info(
        "🛡️ Image received. "
        "The production safety classifier will "
        "evaluate the image before displaying it."
    )


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown(
    '<div class="section-title">⚙️ How It Works</div>',
    unsafe_allow_html=True
)

steps = [
    ("01", "Input", "Text or image enters the system."),
    ("02", "Analyze", "AI models inspect the content."),
    ("03", "Assess", "Safety signals are combined."),
    ("04", "Protect", "Unsafe content is masked or protected."),
    ("05", "Notify", "The user receives a clear safety notice.")
]

for number, title, description in steps:

    st.markdown(
        f"""
        <div class="feature-card"
             style="margin-bottom:14px; min-height:auto;">

        <b>{number} — {title}</b>

        <br>

        <span style="color:#AAB2C8;">
        {description}
        </span>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PRIVACY
# ============================================================

st.markdown(
    '<div class="section-title">🔐 Privacy First</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="feature-card">

<b>🛡️ Protection by design</b>

<br><br>

SAFEGUARD AI is designed around a simple principle:
potentially harmful content should be protected
before it reaches another person's screen.

<br><br>

<strong>Design goal:</strong>

Original sensitive content should not be unnecessarily
redisplayed, stored or exposed.

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

🛡️ <b>SAFEGUARD AI</b>

<br><br>

AI • Deep Learning • NLP • Computer Vision

<br><br>

Built as an educational AI/ML project.

</div>
""", unsafe_allow_html=True)
          
