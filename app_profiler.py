import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(
    page_title="Lebogang Ramotshela | Research & Data",
    page_icon="✳️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------- VISUAL IDENTITY -----------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
  --ink: #10251f;
  --paper: #f4f2eb;
  --lime: #d8ff65;
  --muted: #68766f;
  --line: rgba(16,37,31,.16);
}
html, body, [class*="css"] {
  font-family: 'Manrope', sans-serif;
}
.stApp {
  background:
    radial-gradient(circle at 90% 0%, rgba(216,255,101,.18), transparent 24rem),
    var(--paper);
  color: var(--ink);
}
.block-container {max-width: 1240px; padding-top: 1.6rem; padding-bottom: 3rem;}
[data-testid="stSidebar"] {
  background: #10251f;
}
[data-testid="stSidebar"] * {color: #f4f2eb;}
[data-testid="stSidebar"] [data-testid="stRadio"] label {font-weight: 600;}
[data-testid="stSidebar"] hr {border-color: rgba(255,255,255,.18);}
h1,h2,h3 {letter-spacing: -.045em; color: var(--ink);}
h1 {font-weight: 800; line-height: .98;}
h2 {font-weight: 800;}
p {line-height: 1.7;}
a {color: #315d3f !important; font-weight: 700;}
div[data-testid="stMetric"] {
  background: #fffef9;
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 1rem 1.1rem;
  box-shadow: 0 8px 24px rgba(16,37,31,.035);
}
.stButton > button, .stLinkButton > a {
  border-radius: 999px;
  border: 1px solid var(--ink);
  font-weight: 800;
}
.stButton > button[kind="primary"], .stLinkButton > a[kind="primary"] {
  background: var(--lime);
  color: var(--ink);
}
div[data-testid="stExpander"] {
  background: rgba(255,254,249,.75);
  border: 1px solid var(--line);
  border-radius: 14px;
}
div[data-testid="stSelectbox"] > div {border-radius: 12px;}
hr {border-color: var(--line);}
.eyebrow {
  font-family: 'DM Mono', monospace;
  font-size: .78rem; text-transform: uppercase; letter-spacing: .12em;
  color: #55715e; margin-bottom: .8rem;
}
.hero {
  background: #10251f; color: #f4f2eb; border-radius: 28px;
  padding: clamp(1.5rem, 4vw, 4rem); position: relative; overflow: hidden;
  border: 1px solid #10251f; margin: .6rem 0 1.2rem;
}
.hero:after {
  content: "∑"; position: absolute; right: 4%; top: -35%;
  font-size: clamp(13rem, 30vw, 25rem); line-height: 1;
  color: rgba(216,255,101,.10); font-weight: 800; pointer-events: none;
}
.hero h1 {color: #f4f2eb; font-size: clamp(2.7rem, 6vw, 5.8rem); max-width: 900px;}
.hero .sub {color: #d8ff65; font-size: clamp(1.05rem, 2vw, 1.45rem); font-weight: 700;}
.hero .intro {color: #d9e0d8; max-width: 720px; font-size: 1.02rem;}
.pill {
  display: inline-block; padding: .45rem .75rem; border-radius: 999px;
  border: 1px solid rgba(216,255,101,.45); color: #d8ff65;
  font-family: 'DM Mono', monospace; font-size: .73rem; margin: .2rem .3rem .2rem 0;
}
.section-kicker {font-family:'DM Mono',monospace;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;color:#55715e;}
.feature {
  background: #d8ff65; padding: 1.5rem; border-radius: 22px; height: 100%;
  border: 1px solid #c8ee5a;
}
.feature h3 {font-size: 1.4rem; margin-top: .6rem;}
.feature .num {font-family:'DM Mono',monospace;font-size:.8rem;}
.card {
  background: #fffef9; border: 1px solid var(--line); border-radius: 20px;
  padding: 1.35rem; height: 100%; box-shadow: 0 10px 30px rgba(16,37,31,.035);
}
.card h3 {margin:.4rem 0 .6rem;}
.card .meta {font-family:'DM Mono',monospace;font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:#55715e;}
.tag {
  display:inline-block;background:#e9eee4;color:#234632;padding:.35rem .6rem;
  border-radius:8px;font-size:.78rem;font-weight:700;margin:.2rem .2rem .2rem 0;
}
.big-quote {font-size:clamp(1.5rem,3vw,2.5rem);font-weight:800;line-height:1.2;letter-spacing:-.04em;}
.small-note {font-family:'DM Mono',monospace;font-size:.75rem;color:#68766f;}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ----------------------- CONTENT -----------------------
EMAIL = "francinahramotshela339@gmail.com"
PROFILE_PHOTO = Path(__file__).parent / "profile_photo.jpeg"
LINKEDIN = "https://www.linkedin.com/in/lebogang-francinah-ramotshela-702202244"

PAGES = [
    "✳ Overview",
    "⌁ Research lab",
    "▦ Toolkit",
    "↗ Journey",
    "✉ Say hello",
]
page = st.sidebar.radio("PORTFOLIO / 2026", PAGES, label_visibility="visible")
st.sidebar.markdown("---")
st.sidebar.markdown("### LFR")
st.sidebar.caption("Mathematical sciences · Statistics · Applied data")
st.sidebar.markdown("---")
st.sidebar.markdown(
    '<span style="font-family:DM Mono;color:#d8ff65;font-size:.72rem;">'
    'CURIOUS BY DESIGN<br>QUANTITATIVE BY TRAINING</span>',
    unsafe_allow_html=True
)

# ----------------------- OVERVIEW -----------------------
if page == "✳ Overview":
    hero_text, hero_photo = st.columns([1.65, 0.75], gap="large", vertical_alignment="center")
    with hero_text:
        st.markdown("""
        <div class="hero">
          <div class="eyebrow" style="color:#d8ff65;">RESEARCHER · MODELLER · DATA EXPLORER</div>
          <h1>Lebogang<br>Ramotshela<span style="color:#d8ff65;">.</span></h1>
          <div class="sub">Turning complex questions into clearer evidence.</div>
          <p class="intro">MSc Mathematical Sciences candidate at AIMS South Africa, with a background in Statistics. I use quantitative thinking, computational tools and data to explore questions across environmental and biological systems.</p>
          <span class="pill">MATHEMATICS</span><span class="pill">STATISTICS</span><span class="pill">DATA SCIENCE</span><span class="pill">MODELLING</span>
        </div>
        """, unsafe_allow_html=True)
    with hero_photo:
        if PROFILE_PHOTO.exists():
            st.image(str(PROFILE_PHOTO), use_container_width=True)
            st.markdown('<div class="small-note" style="text-align:center;">LEBOGANG RAMOTSHELA · CAPE TOWN, SOUTH AFRICA</div>', unsafe_allow_html=True)
        else:
            st.info("Add profile_photo.jpeg beside portfolio_app.py to display your portrait.")

    a, b, c = st.columns([1.1, 1, 1])
    with a:
        st.markdown('<div class="feature"><div class="num">01 / CURRENT FOCUS</div><h3>Climate extremes</h3><p>Exploring drought and heatwaves occurring together, and how these events relate to maize yields in South Africa.</p></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="card"><div class="meta">02 / METHODS</div><h3>Quantitative thinking</h3><p>Statistical inference, survival analysis, stochastic simulation and mathematical modelling.</p><span class="tag">R</span><span class="tag">Python</span></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="card"><div class="meta">03 / MOTIVATION</div><h3>Useful research</h3><p>Building analytical workflows that help turn complex datasets into interpretable findings.</p><span class="tag">Research</span><span class="tag">Evidence</span></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-kicker">A little about my approach</div>', unsafe_allow_html=True)
    st.markdown('<div class="big-quote">“Good analysis is more than running code. It is asking a precise question, choosing a defensible method, and explaining what the results mean.”</div>', unsafe_allow_html=True)
    st.write("")
    left, right = st.columns([1.2, .8])
    with left:
        st.subheader("What I’m curious about")
        st.write("Climate and environmental processes · Statistical inference · Biological transmission models · Complex systems · Applied data science")
    with right:
        st.subheader("Currently")
        st.markdown("""
        **AIMS South Africa**  
        MSc Mathematical Sciences  
        *Expected completion: November 2026*
        """)
        st.link_button("Connect on LinkedIn ↗", LINKEDIN)
    st.markdown("---")
    st.markdown('<div class="small-note">SCROLL LESS. EXPLORE MORE. USE THE MENU TO OPEN THE RESEARCH LAB.</div>', unsafe_allow_html=True)

# ----------------------- RESEARCH LAB -----------------------
elif page == "⌁ Research lab":
    st.markdown('<div class="eyebrow">SELECTED WORK / 01—03</div>', unsafe_allow_html=True)
    st.title("Research lab.")
    st.write("Three projects, three ways of using quantitative methods to investigate real-world questions.")

    projects = {
        "01 · Climate extremes & maize yields": {
            "discipline": "CLIMATE · ENVIRONMENTAL DATA",
            "title": "When drought meets heat",
            "description": "MSc research mapping the frequency, duration, severity and spatial distribution of compound drought–heatwave events across major maize-producing regions of South Africa. The project also examines how atmospheric water demand and soil-moisture deficits relate to maize-yield anomalies.",
            "questions": [
                "Where and when do compound events occur?",
                "How do soil moisture and atmospheric demand behave during critical maize-growth stages?",
                "How are climate indicators associated with yield anomalies?"
            ],
            "tools": ["Python", "Pandas", "NumPy", "Xarray", "ERA5-Land", "GLEAM"]
        },
        "02 · Measles transmission & missing data": {
            "discipline": "MATHEMATICAL BIOLOGY · STOCHASTIC MODELS",
            "title": "Modelling with incomplete observations",
            "description": "A team project completed during the AIMS Clinic on Meaningful Modelling of Epidemiological Data. Investigated how different missing-data mechanisms affect inference in a stochastic Chain Binomial SEIR model of within-household measles transmission.",
            "questions": [
                "How can household transmission be represented mathematically?",
                "How can missingness be introduced into simulated longitudinal data?",
                "How can epidemiological parameters be estimated from incomplete data?"
            ],
            "tools": ["R", "SEIR", "Stochastic simulation", "Likelihood-based estimation"]
        },
        "03 · Survival analysis": {
            "discipline": "STATISTICS · TIME-TO-EVENT ANALYSIS",
            "title": "Studying time to depression onset",
            "description": "BSc Honours research using survey data from 639 University of Limpopo students to investigate factors associated with depression onset. The work involved data cleaning and validation, Cox Proportional Hazards modelling, and interpretation of time-to-event results.",
            "questions": [
                "How can time-to-event data be analysed?",
                "Which measured factors are associated with the event of interest?",
                "How can survival models support interpretation of survey data?"
            ],
            "tools": ["R", "Survival analysis", "Cox Proportional Hazards", "Data preparation"]
        }
    }

    selected = st.selectbox("EXPLORE A PROJECT", list(projects.keys()))
    p = projects[selected]
    st.markdown("---")
    st.markdown(f'<div class="section-kicker">{p["discipline"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="big-quote">{p["title"]}</div>', unsafe_allow_html=True)
    st.write(p["description"])

    l, r = st.columns([1.1, .9])
    with l:
        st.subheader("Questions I investigate")
        for q in p["questions"]:
            st.markdown(f"- {q}")
    with r:
        st.subheader("Methods & tools")
        st.markdown("".join([f'<span class="tag">{x}</span>' for x in p["tools"]]), unsafe_allow_html=True)
        st.write("")
        st.info("Project reports, code repositories and visual results can be linked here as they are ready to share.")

    st.markdown("---")
    st.subheader("Make this section yours")
    st.write("For the climate project, the strongest next addition would be a real map, a yield-anomaly chart, or a carefully labelled figure from your analysis. Only publish figures you have checked and can explain.")

# ----------------------- TOOLKIT -----------------------
elif page == "▦ Toolkit":
    st.markdown('<div class="eyebrow">TOOLS ARE PART OF THE THINKING</div>', unsafe_allow_html=True)
    st.title("My toolkit.")
    st.write("A working set of programming, analytical and research skills developed through academic projects and research.")

    skill_groups = {
        "01 / Programming & computing": {
            "skills": ["Python", "R", "SAS", "SageMath", "Jupyter Notebook", "RStudio"],
            "note": "Implementing analytical workflows and computational experiments."
        },
        "02 / Data & scientific workflows": {
            "skills": ["Pandas", "NumPy", "Xarray", "Matplotlib", "NetCDF / GRIB"],
            "note": "Working with structured datasets, scientific arrays and gridded environmental data."
        },
        "03 / Statistics & inference": {
            "skills": ["Statistical inference", "Survival analysis", "Cox models", "Multivariate analysis", "Probability"],
            "note": "Analysing data, estimating relationships and interpreting uncertainty."
        },
        "04 / Mathematical modelling": {
            "skills": ["Stochastic simulation", "Chain Binomial / SEIR", "Model-based inference", "Linear algebra", "Optimisation"],
            "note": "Translating processes into quantitative models and exploring their behaviour."
        },
        "05 / Research practice": {
            "skills": ["Literature review", "Research design", "Quantitative analysis", "Technical reporting"],
            "note": "Connecting research questions, defensible methods and clear communication."
        },
    }
    for title, group in skill_groups.items():
        with st.expander(title, expanded=(title.startswith("01") or title.startswith("02"))):
            st.write(group["note"])
            st.markdown("".join([f'<span class="tag">{s}</span>' for s in group["skills"]]), unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="big-quote">Curiosity sets the question.<br>Methods give it structure.<br>Evidence moves it forward.</div>', unsafe_allow_html=True)

# ----------------------- JOURNEY -----------------------
elif page == "↗ Journey":
    st.markdown('<div class="eyebrow">EDUCATION · EXPERIENCE · COMMUNITY</div>', unsafe_allow_html=True)
    st.title("The journey so far.")
    st.write("A path shaped by mathematical training, research, teaching and student leadership.")

    st.subheader("Education")
    education = [
        ("2026 · IN PROGRESS", "MSc Mathematical Sciences", "African Institute for Mathematical Sciences (AIMS), South Africa", "Expected completion: November 2026. Research on compound drought–heatwave events and maize yields."),
        ("2025", "BSc Honours in Statistics", "University of Limpopo", "Average: 68%. Honours research in statistical modelling of depression among university students."),
        ("2024", "BSc in Mathematical Sciences", "University of Limpopo", "Average: 63%. Majors in Mathematics and Statistics.")
    ]
    for meta, degree, institution, detail in education:
        st.markdown(f"""
        <div class="card" style="margin-bottom:.8rem;">
          <div class="meta">{meta}</div><h3>{degree}</h3>
          <p><strong>{institution}</strong></p><p>{detail}</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Experience & leadership")
    roles = [
        ("2026", "Computational Thinking Tutor · Volunteer", "AIMS South Africa", "Facilitated computational-thinking and programming activities for high-school learners using TurtleStitch."),
        ("2025", "Student Assistant", "University of Limpopo · Department of Statistics and Operations Research", "Tutored first-year Statistics students, supported tutorials, invigilated assessments and marked assignments and quizzes."),
        ("2025", "Class Representative · Honours Statistics", "University of Limpopo", "Represented the cohort and facilitated communication between students and faculty."),
        ("2025", "Bursary Drive Volunteer", "Faculty of Science and Agriculture, University of Limpopo", "Assisted students with postgraduate funding applications."),
        ("2024", "Chairperson of Floor Representatives", "MBE Hall, University of Limpopo", "Led student representatives and supported communication with residence management.")
    ]
    for year, role, place, detail in roles:
        with st.expander(f"{year}  /  {role}"):
            st.markdown(f"**{place}**")
            st.write(detail)

    st.subheader("Scholarships & recognition")
    x, y, z = st.columns(3)
    with x:
        st.markdown('<div class="feature"><div class="num">2026</div><h3>Mastercard Foundation</h3><p>Full scholarship supporting MSc study at AIMS South Africa.</p></div>', unsafe_allow_html=True)
    with y:
        st.markdown('<div class="card"><div class="meta">2026</div><h3>Africa Scientifique</h3><p>Participant in a science communication and leadership programme for emerging African scientists.</p></div>', unsafe_allow_html=True)
    with z:
        st.markdown('<div class="card"><div class="meta">2025</div><h3>FirstRand Empowerment Foundation</h3><p>Postgraduate bursary supporting studies in Mathematical Sciences.</p></div>', unsafe_allow_html=True)

# ----------------------- CONTACT -----------------------
elif page == "✉ Say hello":
    st.markdown('<div class="eyebrow">COLLABORATION · RESEARCH · OPPORTUNITIES</div>', unsafe_allow_html=True)
    st.title("Have a question or an idea?")
    st.markdown('<div class="big-quote">Let’s connect the dots.</div>', unsafe_allow_html=True)
    st.write("I welcome conversations about research, mathematical modelling, data analysis and opportunities to learn and collaborate.")

    left, right = st.columns([1, 1])
    with left:
        st.markdown("""
        <div class="card">
          <div class="meta">EMAIL</div>
          <h3>Start a conversation</h3>
          <p>For research enquiries, collaboration or professional opportunities.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Email Lebogang ↗", f"mailto:{EMAIL}?subject=Portfolio%20Enquiry", type="primary")
    with right:
        st.markdown("""
        <div class="card">
          <div class="meta">LINKEDIN</div>
          <h3>Find me professionally</h3>
          <p>Connect to follow my academic and research journey.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Connect on LinkedIn ↗", LINKEDIN)

    st.markdown("---")
    st.caption("Based in Cape Town, South Africa.")

# ----------------------- FOOTER -----------------------
st.markdown("---")
st.markdown(
    '<div class="small-note">LEBOGANG FRANCINAH RAMOTSHELA · PORTFOLIO 2026 · '
    'BUILT WITH PYTHON + STREAMLIT</div>',
    unsafe_allow_html=True
)
