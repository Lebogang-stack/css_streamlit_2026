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
