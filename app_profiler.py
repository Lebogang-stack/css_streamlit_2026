
import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Lebogang Ramotshela | Research Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #F7F9FC;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1150px;
    }

    h1, h2, h3 {
        color: #17365D;
    }

    .hero {
        background: linear-gradient(120deg, #17365D, #245A81);
        padding: 2.5rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 2rem;
    }

    .hero h1 {
        color: white;
        font-size: 2.7rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        color: #EAF2F8;
        font-size: 1.08rem;
    }

    .project-card {
        background: white;
        border: 1px solid #E1E8F0;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        min-height: 180px;
    }

    .tag {
        display: inline-block;
        background: #E5EEF8;
        color: #17365D;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.82rem;
        margin: 3px 3px 3px 0;
    }

    .muted {
        color: #607080;
    }

    a {
        color: #245A81 !important;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 1rem;
        border: 1px solid #E1E8F0;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROFILE INFORMATION
# --------------------------------------------------
NAME = "Lebogang Francinah Ramotshela"
EMAIL = "francinahramotshela339@gmail.com"
LINKEDIN = (
    "https://www.linkedin.com/in/"
    "lebogang-francinah-ramotshela-702202244"
)

ABOUT = """
I am an MSc Mathematical Sciences candidate at the African Institute
for Mathematical Sciences (AIMS) South Africa, with a background in
Statistics and Mathematical Sciences.

My work and research interests include applied data science,
statistical modelling, mathematical modelling and computational
analysis. I am particularly interested in using quantitative methods
to study climate and environmental processes, biological systems
and other complex real-world problems.

I use programming and statistical methods to translate research
questions into computational workflows and interpretable results.
"""


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("My Portfolio")
st.sidebar.caption("Mathematics | Statistics | Data Science")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Research Projects",
        "Technical Skills",
        "Education",
        "Experience & Leadership",
        "Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Lebogang Ramotshela**")
st.sidebar.caption("MSc Mathematical Sciences Candidate")


# --------------------------------------------------
# HOME
# --------------------------------------------------
if page == "Home":

    st.markdown(f"""
    <div class="hero">
        <h1>{NAME}</h1>
        <p>
            Mathematical Sciences | Statistics | Applied Data Science
        </p>
        <p>
            Using mathematical and statistical methods to investigate
            complex real-world problems.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.header("About Me")
    st.write(ABOUT)

    st.markdown("---")
    st.header("Research Interests")

    interests = [
        (
            "🌍 Climate and Environmental Data",
            "Spatiotemporal analysis, compound climate extremes "
            "and environmental impacts."
        ),
        (
            "📊 Statistical Modelling",
            "Statistical inference, survival analysis, "
            "regression and uncertainty."
        ),
        (
            "🧮 Mathematical Modelling",
            "Mathematical frameworks, stochastic simulation "
            "and model-based analysis."
        ),
        (
            "💻 Applied Data Science",
            "Data processing, computational workflows, "
            "visualisation and interpretation."
        ),
        (
            "🧬 Biological Systems",
            "Epidemiological modelling, transmission processes "
            "and inference under incomplete data."
        ),
        (
            "🔗 Complex Systems",
            "Interest in interacting processes, networks "
            "and system dynamics."
        )
    ]

    cols = st.columns(2)

    for i, (title, description) in enumerate(interests):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="project-card">
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        "Explore the navigation menu to learn about my research, "
        "technical skills, education and experience."
    )


# --------------------------------------------------
# RESEARCH PROJECTS
# --------------------------------------------------
elif page == "Research Projects":

    st.title("Research Projects")

    st.write(
        "My research experience brings together statistical "
        "inference, mathematical modelling and computational analysis."
    )

    projects = {
        "Climate Extremes and Maize Yields": {
            "area": "Climate and Environmental Data",
            "period": "2026",
            "description": """
            **Spatiotemporal Mapping of Compound Drought–Heatwave
            Events and Their Cascading Impacts on Maize Yields
            in South Africa**

            My MSc research investigates the frequency, duration,
            severity and spatial distribution of drought and
            heatwaves occurring together across major maize-producing
            regions of South Africa.

            The study also examines how atmospheric water demand
            and soil-moisture deficits relate to maize-yield anomalies.
            """,
            "methods": [
                "Python",
                "Pandas",
                "NumPy",
                "Xarray",
                "Climate data analysis",
                "Statistical modelling"
            ]
        },

        "Measles Transmission Modelling": {
            "area": "Mathematical Biology",
            "period": "2026",
            "description": """
            **Assessing the Impact of Missing Data for Within-Household
            Transmission Model of Measles**

            As part of a three-week modelling course and workshop
            at AIMS South Africa, I worked in an interdisciplinary
            team to investigate missing-data mechanisms in a
            stochastic Chain Binomial SEIR transmission model.

            The work involved simulating household transmission
            data and supporting likelihood-based estimation of
            epidemiological parameters.
            """,
            "methods": [
                "R",
                "Stochastic simulation",
                "SEIR models",
                "Missing-data mechanisms",
                "Likelihood-based estimation"
            ]
        },

        "Survival Analysis": {
            "area": "Statistical Modelling",
            "period": "2025",
            "description": """
            **Statistical Modelling of Depression Among University
            Students**

            My BSc Honours research analysed survey data from
            639 University of Limpopo students to investigate
            factors associated with the onset of depression.

            The analysis used time-to-event methods, including
            Cox Proportional Hazards modelling, and involved
            data cleaning, validation and interpretation.
            """,
            "methods": [
                "R",
                "Survival analysis",
                "Cox Proportional Hazards",
                "Data cleaning",
                "Statistical inference"
            ]
        }
    }

    selected_project = st.selectbox(
        "Select a research project",
        list(projects.keys())
    )

    project = projects[selected_project]

    st.markdown("---")
    st.subheader(selected_project)
    st.caption(
        f"{project['area']} · {project['period']}"
    )
    st.markdown(project["description"])

    st.markdown("**Methods and tools**")

    for method in project["methods"]:
        st.markdown(
            f'<span class="tag">{method}</span>',
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.subheader("Research Development")

    st.write(
        "This section can be expanded with project reports, "
        "GitHub repositories, research posters, code samples "
        "and published work as they become available."
    )


# --------------------------------------------------
# TECHNICAL SKILLS
# --------------------------------------------------
elif page == "Technical Skills":

    st.title("Technical Skills")

    st.write(
        "My technical background combines programming, statistical "
        "analysis and mathematical modelling."
    )

    skills = {
        "Programming Languages": [
            "Python", "R", "SAS", "SageMath"
        ],
        "Data Analysis and Scientific Computing": [
            "Pandas", "NumPy", "Xarray", "Matplotlib",
            "Jupyter Notebook", "RStudio", "NetCDF/GRIB workflows"
        ],
        "Statistical Methods": [
            "Statistical inference", "Survival analysis",
            "Cox Proportional Hazards", "Multivariate analysis",
            "Statistical modelling", "Probability"
        ],
        "Mathematical Modelling": [
            "Stochastic simulation", "Chain Binomial/SEIR models",
            "Model-based inference", "Linear algebra", "Optimisation"
        ],
        "Research Skills": [
            "Literature review", "Research design",
            "Computational experimentation", "Quantitative analysis",
            "Technical reporting"
        ]
    }

    for category, items in skills.items():
        with st.expander(category, expanded=True):
            st.write(" · ".join(items))

    st.markdown("---")
    st.subheader("Tools I Use")

    tool_cols = st.columns(4)

    tools = [
        ("Python", "Data analysis"),
        ("R", "Statistical computing"),
        ("SAS", "Statistical analysis"),
        ("Jupyter", "Computational research")
    ]

    for col, (tool, purpose) in zip(tool_cols, tools):
        with col:
            st.markdown(
                f"""
                <div class="project-card">
                    <h3>{tool}</h3>
                    <p>{purpose}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


# --------------------------------------------------
# EDUCATION
# --------------------------------------------------
elif page == "Education":

    st.title("Education")

    education = [
        {
            "qualification": "MSc Mathematical Sciences",
            "institution": "African Institute for Mathematical Sciences (AIMS), South Africa",
            "year": "Expected November 2026",
            "details": (
                "Research: Spatiotemporal Mapping of Compound "
                "Drought–Heatwave Events and Their Cascading "
                "Impacts on Maize Yields in South Africa."
            )
        },
        {
            "qualification": "BSc Honours in Statistics",
            "institution": "University of Limpopo, South Africa",
            "year": "2025",
            "details": (
                "Average: 68%. Research focused on statistical "
                "modelling of depression among university students."
            )
        },
        {
            "qualification": "BSc in Mathematical Sciences",
            "institution": "University of Limpopo, South Africa",
            "year": "2024",
            "details": (
                "Average: 63%. Majors in Mathematics and Statistics."
            )
        }
    ]

    for item in education:
        st.markdown(
            f"""
            <div class="project-card">
                <h3>{item['qualification']}</h3>
                <p><strong>{item['institution']}</strong></p>
                <p class="muted">{item['year']}</p>
                <p>{item['details']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Scholarships and Recognition")

    st.markdown("""
    - **Mastercard Foundation Scholarship (2026):**
      Full scholarship supporting MSc study at AIMS South Africa.
    - **Africa Scientifique Programme (2026):**
      Participant in a science communication and leadership
      programme for emerging African scientists.
    - **FirstRand Empowerment Foundation Postgraduate Bursary
      (2025):** Postgraduate funding supporting studies in
      Mathematical Sciences.
    """)


# --------------------------------------------------
# EXPERIENCE AND LEADERSHIP
# --------------------------------------------------
elif page == "Experience & Leadership":

    st.title("Experience & Leadership")

    experience = [
        (
            "Computational Thinking Tutor — Volunteer",
            "AIMS South Africa | April 2026",
            "Facilitated computational-thinking and programming "
            "activities for high-school learners using TurtleStitch."
        ),
        (
            "Student Assistant",
            "Department of Statistics and Operations Research, "
            "University of Limpopo | 2025",
            "Tutored first-year Statistics students, supported "
            "tutorial sessions, invigilated assessments and marked "
            "assignments and quizzes."
        ),
        (
            "Class Representative — Honours Statistics",
            "University of Limpopo | 2025",
            "Represented the Honours Statistics cohort and "
            "facilitated communication between students and faculty."
        ),
        (
            "Faculty of Science and Agriculture Bursary Drive Volunteer",
            "University of Limpopo | July–November 2025",
            "Assisted students with postgraduate funding applications "
            "and supported access-to-education initiatives."
        ),
        (
            "Chairperson of Floor Representatives",
            "MBE Hall, University of Limpopo | 2024",
            "Led student representatives and supported communication "
            "between residents and residence management."
        )
    ]

    for role, organisation, details in experience:
        st.markdown(
            f"""
            <div class="project-card">
                <h3>{role}</h3>
                <p><strong>{organisation}</strong></p>
                <p>{details}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# CONTACT
# --------------------------------------------------
elif page == "Contact":

    st.title("Get in Touch")

    st.write(
        "I welcome opportunities for research collaboration, "
        "academic engagement and applied data science projects."
    )

    st.markdown(f"**Email:** [{EMAIL}](mailto:{EMAIL})")
    st.markdown(
        f"**LinkedIn:** [Connect with me]({LINKEDIN})"
    )

    st.markdown("---")
    st.subheader("Send an Email")

    st.write(
        "Use the email link above to contact me directly "
        "about research or professional opportunities."
    )

    st.link_button(
        "Email Me",
        f"mailto:{EMAIL}?subject=Portfolio%20Enquiry",
        type="primary"
    )

    st.caption(
        "This portfolio presents my academic background, "
        "research interests and experience."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption(
    "© 2026 Lebogang Francinah Ramotshela | "
    "Mathematical Sciences, Statistics and Applied Data Science"
)
