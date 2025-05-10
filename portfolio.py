import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="Prince Jindal | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
        /* Main color scheme */
        :root {
            --primary-color: #0A2647;
            --secondary-color: #144272;
            --accent-color: #2C74B3;
            --highlight-color: #205295;
            --text-color: #FFFFFF;
            --light-text: #EEEEEE;
            --dark-text: #333333;
            --bg-color: #F5F5F5;
        }
        
        /* Base styling */
        .main {
            background-color: #F8F9FA;
            color: var(--dark-text);
        }
        
        /* Custom headers */
        .header-style {
            color: var(--primary-color);
            font-weight: 600;
            letter-spacing: 0.5px;
            padding-bottom: 15px;
            border-bottom: 2px solid var(--accent-color);
            margin-bottom: 20px;
        }
        
        /* Hero section */
        .hero-container {
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .hero-name {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .hero-title {
            font-size: 1.5rem;
            font-weight: 400;
            margin-bottom: 1.5rem;
            opacity: 0.9;
        }
        
        .hero-contact {
            font-size: 1rem;
            opacity: 0.8;
        }
        
        /* Card styling */
        .card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            border-left: 5px solid var(--accent-color);
        }
        
        /* Skill badges */
        .badge {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background-color: var(--accent-color);
            color: white;
            border-radius: 30px;
            font-size: 0.85rem;
            margin: 0.25rem;
            font-weight: 500;
        }
        
        /* Project cards */
        .project-card {
            background-color: white;
            border-radius: 8px;
            padding: 1.2rem;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
            border-left: 4px solid var(--highlight-color);
            transition: transform 0.2s;
        }
        
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        .project-title {
            color: var(--secondary-color);
            font-weight: 600;
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }
        
        .tech-stack {
            color: var(--accent-color);
            font-size: 0.9rem;
            margin-bottom: 1rem;
            font-style: italic;
        }
        
        /* Contact form styling */
        .contact-form input, .contact-form textarea {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 15px;
            width: 100%;
        }
        
        .btn-primary {
            background-color: var(--accent-color);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 500;
            margin-top: 10px;
        }
        
        .btn-primary:hover {
            background-color: var(--highlight-color);
        }
        
        /* Timeline styling */
        .timeline-item {
            padding-left: 20px;
            border-left: 2px solid var(--accent-color);
            padding-bottom: 20px;
            position: relative;
        }
        
        .timeline-item:before {
            content: '';
            width: 12px;
            height: 12px;
            background: var(--accent-color);
            border-radius: 50%;
            position: absolute;
            left: -7px;
            top: 5px;
        }
        
        /* Chatbot styling */
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 10px;
            display: flex;
            flex-direction: column;
        }
        
        .ai-message {
            background-color: #e9ecef;
            border-left: 3px solid var(--secondary-color);
        }
        
        .user-message {
            background-color: #f8f9fa;
            border-right: 3px solid var(--accent-color);
            text-align: right;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .hero-name {
                font-size: 2.5rem;
            }
            
            .hero-title {
                font-size: 1.2rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# App layout
def main():
    local_css()
    
    # Sidebar
    with st.sidebar:
        st.markdown("### Navigation")
        nav_selection = st.radio("", ["Home", "Skills", "Projects", "AI Experience", "Contact"])
        
        st.markdown("---")
        st.markdown("### Let's Connect")
        st.markdown("[LinkedIn](https://linkedin.com/in/princejindal10)")
        st.markdown("[Email](mailto:j.prince0410@gmail.com)")
        st.markdown("[GitHub](https://github.com/princejindal)")  # Placeholder - update with your GitHub
        st.markdown("---")
        st.markdown("📞 (+91) 8307261678")
        st.markdown("📍 Gurgaon, India")

    # Main content based on navigation
    if nav_selection == "Home":
        display_home()
    elif nav_selection == "Skills":
        display_skills()
    elif nav_selection == "Projects":
        display_projects()
    elif nav_selection == "AI Experience":
        display_ai_experience()
    elif nav_selection == "Contact":
        display_contact()

# Home/Hero Section
def display_home():
    # Hero section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-name">Prince Jindal</div>
        <div class="hero-title">MERN/AI Fullstack Developer & DevOps Engineer</div>
        <div class="hero-contact">j.prince0410@gmail.com | (+91) 8307261678 | Gurgaon, India</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Summary
    st.markdown("<h2 class='header-style'>About Me</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        Passionate full-stack developer with hands-on experience in the MERN stack, RESTful APIs, and AI-powered systems. 
        Built real-time grade prediction and recommendation platforms using React, Node.js, Python, and MongoDB. 
        Adept in frontend optimization, API integration, and scalable backend design. 
        Eager to contribute to dynamic product teams with a startup mindset and strong DevOps practices.
    </div>
    """, unsafe_allow_html=True)
    
    # Education
    st.markdown("<h2 class='header-style'>Education</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        <div class="timeline-item">
            <strong>Manipal University Jaipur</strong><br>
            Bachelor's degree in Information Technology<br>
            <em>Relevant Coursework:</em> Data Structures and Algorithms, Design and Analysis of Algorithms, 
            Database Management Systems, Computer Organization & Architecture, Object-Oriented Programming, 
            Computer Networks, Operating System, Software Development.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: right;">
            <strong>September 2022 - Present</strong><br>
            CGPA 8.15
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        <div class="timeline-item">
            <strong>GD Goenka Signature School, Gurgaon</strong>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: right;">
            <strong>July 2022</strong><br>
            Class 12: 85%<br>
            Class 10: 85.2%
        </div>
        """, unsafe_allow_html=True)
    
    # Experience
    st.markdown("<h2 class='header-style'>Experience</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <strong>Front End Intern</strong> | Mistify AI Technologies<br>
        <em>June 2024 - August 2024 | Remote</em>
        <ul>
            <li>Constructed a library of 15+ modular React components (buttons, forms, tables) with a standardized API, enabling developers to build consistent user interfaces 50% faster and improving code reuse rates by 60%.</li>
            <li>Integrated RESTful APIs for seamless data retrieval and real-time updates, improving application responsiveness, and reducing data fetch errors by 40%.</li>
            <li>Optimized front-end performance by implementing lazy loading and code splitting, reducing page load time by 30% and improving user experience.</li>
            <li>Collaborated with the design team to implement UI/UX improvements, resulting in a 15% increase in user engagement and higher customer satisfaction.</li>
            <li>Conducted A/B testing for new features and iterated on the basis of user feedback, ensuring a user-centric design approach.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Achievements
    st.markdown("<h2 class='header-style'>Achievements & Extra-Curricular</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <strong>Operations Lead – Google for Startups, Startup Weekend Jaipur (2024)</strong>
        <p>Spearheaded event logistics for a high-profile startup event, ensuring an engaging experience for 200+ participants and 30+ mentors.</p>
        
        <strong>Production Lead – Under 25 Summit (2023)</strong>
        <p>Led a team of 50+ crew members to manage event logistics, crew coordination, and on-site production for one of India's largest youth events, attracting 10,000+ attendees, achieving a 90% on-time delivery rate.</p>
        
        <strong>Organizer – Blood Donation Camp (2023)</strong>
        <p>Organized and coordinated a highly successful blood donation camp in collaboration with medical teams and 50+ volunteers, increasing camp participation by 40% through strategic marketing and community outreach efforts.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("<h2 class='header-style'>Certifications</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <ul>
            <li>MERN Full-stack Guide by Maximilian Schwarzmüller</li>
            <li>AWS Academy Cloud Foundations</li>
            <li>Microsoft Azure Fundamentals: Describe Cloud Concepts</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Skills Section
def display_skills():
    st.markdown("<h1 class='header-style'>Technical Skills</h1>", unsafe_allow_html=True)
    
    # Skill categories
    skill_categories = {
        "Programming Languages": ["Python", "JavaScript", "TypeScript", "C", "C++", "Java", "SQL"],
        "Web Development": ["React.js", "Next.js", "TailwindCSS", "Node.js", "Express.js", "Flask", "HTML", "CSS"],
        "Databases": ["MongoDB", "PostgreSQL", "MySQL"],
        "AI/ML": ["Scikit-learn", "Pandas", "NumPy", "Flask APIs", "LLM experimentation (OpenAI)"],
        "DevOps & Cloud": ["GitHub Actions", "Docker (basic)", "GCP", "AWS"],
        "Tools": ["Git", "Power BI", "SAP/Oracle (Basic)", "Figma", "Microsoft Office"]
    }
    
    # Create tabs for skill categories
    tabs = st.tabs(skill_categories.keys())
    
    # Display skills in each tab
    for i, (category, skills) in enumerate(skill_categories.items()):
        with tabs[i]:
            st.markdown(f"<h3>{category}</h3>", unsafe_allow_html=True)
            
            # Display skill badges
            skill_html = ""
            for skill in skills:
                skill_html += f'<span class="badge">{skill}</span>'
            
            st.markdown(f'<div style="margin: 20px 0;">{skill_html}</div>', unsafe_allow_html=True)
            
            # Add toggle for more details
            with st.expander("Skill Details"):
                if category == "Programming Languages":
                    st.write("""
                    - **Python**: Used for AI/ML projects, including recommendation systems and grade prediction
                    - **JavaScript/TypeScript**: Core language for MERN stack development
                    - **C/C++**: Data structures and algorithm implementation
                    - **Java**: Object-oriented programming and application development
                    - **SQL**: Database queries and data manipulation
                    """)
                elif category == "Web Development":
                    st.write("""
                    - **React.js**: Component-based UI development with hooks and context API
                    - **Next.js**: Server-side rendering and static site generation
                    - **TailwindCSS**: Utility-first CSS framework for rapid UI development
                    - **Node.js**: Server-side JavaScript runtime
                    - **Express.js**: Web application framework for Node.js
                    - **Flask**: Lightweight Python web framework for API development
                    """)
                elif category == "Databases":
                    st.write("""
                    - **MongoDB**: NoSQL database used in MERN stack applications
                    - **PostgreSQL**: Relational database for structured data
                    - **MySQL**: Database management and query optimization
                    """)
                elif category == "AI/ML":
                    st.write("""
                    - **Scikit-learn**: Machine learning algorithms for predictive modeling
                    - **Pandas/NumPy**: Data manipulation and numerical computing
                    - **Flask APIs**: Deployment of machine learning models
                    - **LLM experimentation**: Theoretical knowledge of large language models
                    """)
                elif category == "DevOps & Cloud":
                    st.write("""
                    - **GitHub Actions**: CI/CD pipeline automation
                    - **Docker**: Containerization of applications (basic knowledge)
                    - **GCP/AWS**: Cloud deployment and service utilization
                    """)
                elif category == "Tools":
                    st.write("""
                    - **Git**: Version control and collaborative development
                    - **Power BI**: Data visualization and business intelligence
                    - **Figma**: UI/UX design and prototyping
                    """)
    
    # Skill proficiency visualization
    st.markdown("<h3 class='header-style'>Skill Proficiency</h3>", unsafe_allow_html=True)
    
    # Create a dictionary of skills and their proficiency levels
    skill_proficiency = {
        "MERN Stack": 85,
        "Python Development": 80,
        "AI/ML": 70,
        "DevOps": 65,
        "Database Management": 75,
        "UI/UX Design": 60
    }
    
    # Display proficiency bars
    for skill, proficiency in skill_proficiency.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(skill)
        with col2:
            st.progress(proficiency / 100)

# Projects Section
def display_projects():
    st.markdown("<h1 class='header-style'>Projects</h1>", unsafe_allow_html=True)
    
    # Create a 2-column layout for projects
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">Personalised YouTube Recommendation System</div>
            <div class="tech-stack">Python, Flask, JavaScript, Power BI, SQL, HTML, CSS</div>
            <p>An intelligent system that provides personalized video recommendations based on user preferences and viewing history.</p>
            <ul>
                <li>Created a scalable recommendation system using Python and YouTube Data API</li>
                <li>Integrated Power BI dashboards to visualize user engagement metrics</li>
                <li>Implemented OAuth 2.0 authentication for secure access</li>
                <li>Applied SQL for data storage and efficient query execution</li>
                <li>Developed a Flask API with 95% recommendation accuracy</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Project Details"):
            st.write("""
            ### Technical Implementation
            
            - **Data Collection**: Leveraged YouTube Data API for collecting video metadata and user interaction data
            - **Database Design**: SQL database structure for storing user preferences and video details
            - **Security**: OAuth 2.0 for secure authentication and API access
            - **API Development**: Flask-based RESTful API for serving recommendations to the frontend
            - **Performance Optimization**: Query optimization for faster data retrieval
            """)
            
            st.write("### Challenges & Solutions")
            st.write("""
            - **Challenge**: Managing API rate limits
              **Solution**: Implemented caching and batch processing
              
            - **Challenge**: Ensuring recommendation relevance
              **Solution**: Applied content-based filtering algorithms
              
            - **Challenge**: Handling large datasets
              **Solution**: Optimized database queries and implemented pagination
            """)
            
            # Demo button (placeholder)
            st.button("View Demo", key="demo_youtube")
        
    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">GradePro: AI-Powered University Grade Predictor & Advisor</div>
            <div class="tech-stack">React, Node.js, Python, Machine Learning, MongoDB, Express.js</div>
            <p>An intelligent system that helps students predict their grades and provides personalized academic advice.</p>
            <ul>
                <li>Built a scalable, real-time AI analytics system using MongoDB and Express.js</li>
                <li>Created interactive dashboards with React to visualize student performance</li>
                <li>Engineered a machine learning model in Python for grade prediction</li>
                <li>Automated data processing workflows for real-time updates</li>
                <li>Developed MongoDB-based data pipelines, improving retrieval speed by 40%</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Project Details"):
            st.write("""
            ### Technical Implementation
            
            - **Frontend**: React-based interactive dashboards with real-time updates
            - **Backend**: Node.js and Express.js for API management
            - **Database**: MongoDB for flexible data storage and retrieval
            - **ML Pipeline**: Python-based machine learning model for grade prediction
            - **Integration**: RESTful API connecting the ML model with the MERN stack
            """)
            
            st.write("### Features")
            st.write("""
            - Personalized grade predictions based on historical data
            - Course recommendations based on student strengths
            - Interactive visualization of academic performance
            - Customizable study plans and improvement strategies
            - Real-time updates and notifications
            """)
            
            # Demo button (placeholder)
            st.button("View Demo", key="demo_gradepro")
    
    # Additional Projects (collapsed by default)
    with st.expander("More Projects"):
        st.markdown("""
        <div class="project-card">
            <div class="project-title">Personal Portfolio Website</div>
            <div class="tech-stack">React, Next.js, TailwindCSS</div>
            <p>A modern, responsive portfolio website to showcase my projects and skills.</p>
            <ul>
                <li>Implemented responsive design using TailwindCSS</li>
                <li>Added dark/light mode toggle with theme persistence</li>
                <li>Optimized for SEO and performance</li>
            </ul>
        </div>
        
        <div class="project-card">
            <div class="project-title">Task Management API</div>
            <div class="tech-stack">Node.js, Express.js, MongoDB, JWT</div>
            <p>A RESTful API for task management with authentication and authorization.</p>
            <ul>
                <li>Implemented JWT-based authentication</li>
                <li>Created CRUD operations for task management</li>
                <li>Added role-based access control</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# AI Experience Section
def display_ai_experience():
    st.markdown("<h1 class='header-style'>AI Experience & Interests</h1>", unsafe_allow_html=True)
    
    # AI Skills and Interests
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>AI/ML Skills & Knowledge</h3>
            <ul>
                <li><strong>Libraries & Tools:</strong> Scikit-learn, Pandas, NumPy, Flask APIs</li>
                <li><strong>LLM Theory:</strong> Foundational understanding of transformer architecture, prompt engineering, and fine-tuning</li>
                <li><strong>Generative AI:</strong> Knowledge of text generation models, diffusion models, and their applications</li>
                <li><strong>Data Processing:</strong> Experience with data preparation, cleaning, and feature engineering</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # AI Interest areas
        st.markdown("""
        <div class="card">
            <h3>Areas of Interest</h3>
            <ul>
                <li>Large Language Models</li>
                <li>Multimodal AI Systems</li>
                <li>AI for Education</li>
                <li>Recommendation Systems</li>
                <li>AI Ethics & Safety</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Projects with AI component
    st.markdown("<h3 class='header-style'>AI-Focused Projects</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <div class="project-title">GradePro: AI-Powered Grade Prediction System</div>
        <p>Machine learning model that analyzes student performance data to predict future grades and provide personalized improvement recommendations.</p>
        <ul>
            <li>Developed predictive models using Python and scikit-learn</li>
            <li>Integrated ML pipeline with MERN stack application</li>
            <li>Implemented data processing workflows for continuous model improvement</li>
        </ul>
    </div>
    
    <div class="project-card">
        <div class="project-title">YouTube Recommendation Engine</div>
        <p>Content-based filtering algorithm that suggests videos based on user preferences and viewing history.</p>
        <ul>
            <li>Implemented recommendation algorithms with Python</li>
            <li>Integrated with YouTube Data API for content metadata</li>
            <li>Created visualization dashboards with Power BI</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Q&A Chatbot
    st.markdown("<h3 class='header-style'>Ask About My AI Experience</h3>", unsafe_allow_html=True)
    st.write("Select a question or type your own to learn more about my AI knowledge")
    
    # Predefined questions
    questions = [
        "What do you know about transformer architecture?",
        "How have you used machine learning in your projects?",
        "What's your understanding of prompt engineering?",
        "How would you explain the difference between supervised and unsupervised learning?",
        "What interests you about generative AI?"
    ]
    
    # Question selection or custom input
    question_option = st.selectbox("Select a question:", ["Select a question..."] + questions)
    custom_question = st.text_input("Or type your own question:")
    
    # Use either selected or custom question
    question = custom_question if custom_question else question_option if question_option != "Select a question..." else None
    
    if question and st.button("Ask"):
        # Display user question
        st.markdown(f"""
        <div class="chat-message user-message">
            <p>{question}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Simulate typing with a spinner
        with st.spinner("Thinking..."):
            time.sleep(1)  # Simulate processing time
        
        # Display response based on question
        response = ""
        
        if "transformer architecture" in question.lower():
            response = """
            While I'm still learning deeply about transformers, I understand they're the backbone of modern NLP models like GPT and BERT. 
            Transformers use self-attention mechanisms to weigh the importance of different words in context, which allows them to handle long-range 
            dependencies in text better than previous RNN or LSTM models. The architecture typically consists of encoders and decoders with multiple 
            attention heads, allowing the model to focus on different parts of the input sequence simultaneously.
            """
        elif "machine learning in your projects" in question.lower():
            response = """
            In my YouTube recommendation project, I implemented content-based filtering algorithms to suggest videos based on similarity metrics. 
            For GradePro, I used regression models to predict student grades based on historical performance data and attendance patterns. 
            I particularly enjoyed the challenge of feature engineering - determining which factors were most predictive of academic success.
            """
        elif "prompt engineering" in question.lower():
            response = """
            Prompt engineering is the process of crafting effective inputs to guide AI models (especially LLMs) toward desired outputs. 
            I understand it involves techniques like few-shot learning, chain-of-thought prompting, and carefully structuring inputs to 
            elicit more accurate, relevant, or creative responses from models. It's fascinating how the same model can produce dramatically 
            different results based solely on how you frame the prompt.
            """
        elif "supervised and unsupervised learning" in question.lower():
            response = """
            Supervised learning uses labeled data where the algorithm learns to map inputs to known outputs - like predicting house prices 
            based on features where you have historical price data. Unsupervised learning works with unlabeled data to find patterns or 
            structures - like clustering customers based on purchasing behavior without predefined groups. In my GradePro project, I used 
            supervised learning techniques since we had historical grade data to train on.
            """
        elif "generative ai" in question.lower():
            response = """
            I'm fascinated by generative AI's ability to create new content that feels authentic and creative. The applications span from 
            text generation to image creation and even code writing. What interests me most is the potential for generative AI to augment 
            human creativity rather than replace it - like how tools like GitHub Copilot can help developers write code faster while still 
            requiring human judgment and oversight.
            """
        else:
            response = """
            That's a great question about AI! While I have theoretical knowledge of AI concepts and have applied machine learning in my 
            projects like GradePro and the YouTube recommendation system, I'm continuously expanding my knowledge in this rapidly evolving 
            field. I'm particularly interested in the practical applications of AI in software development and creating intuitive user 
            experiences enhanced by intelligent systems.
            """
        
        # Display AI response
        st.markdown(f"""
        <div class="chat-message ai-message">
            <p>{response}</p>
        </div>
        """, unsafe_allow_html=True)

# Contact Form
def display_contact():
    st.markdown("<h1 class='header-style'>Get In Touch</h1>", unsafe_allow_html=True)
    
    # Contact information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Contact Information</h3>
            <p><strong>Email:</strong> j.prince0410@gmail.com</p>
            <p><strong>Phone:</strong> (+91) 8307261678</p>
            <p><strong>Location:</strong> Gurgaon, India</p>
            <p><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/princejindal10" target="_blank">linkedin.com/in/princejindal10</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Availability</h3>
            <p>I'm currently open to:</p>
            <ul>
                <li>Full-time positions in MERN Stack Development</li>
                <li>AI/ML Engineering opportunities</li>
                <li>DevOps Engineering roles</li>
                <li>Freelance projects</li>
                <li>Remote work opportunities</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Contact form
    st.markdown("<h3 class='header-style'>Send Me a Message</h3>", unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        name = st
