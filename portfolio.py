import streamlit as st
import json

# Configuration and theme setup
st.set_page_config(
    page_title="Prince Jindal | MERN/AI Developer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def load_css():
    st.markdown("""
    <style>
    /* Base styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header and section styling */
    .main-header {
        color: #f8f9fa;
        background-color: #0e1117;
        padding: 2.5rem 0;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 2rem;
        border-bottom: 4px solid #4361ee;
    }
    
    .section-header {
        color: #4361ee;
        font-weight: 600;
        font-size: 1.6rem;
        margin: 1.5rem 0 1rem 0;
        border-left: 4px solid #4361ee;
        padding-left: 0.8rem;
    }
    
    /* Card styling */
    .card {
        background-color: #1a1d24;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 3px solid #4361ee;
    }
    
    .card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    
    /* Skill tag styling */
    .skill-tag {
        background-color: #2e3440;
        color: #81a1c1;
        padding: 0.3rem 0.6rem;
        border-radius: 4px;
        display: inline-block;
        margin: 0.2rem;
        font-size: 0.85rem;
    }
    
    .skill-tag.mern {
        border-left: 3px solid #61dafb;
    }
    
    .skill-tag.ai {
        border-left: 3px solid #ff6b6b;
    }
    
    .skill-tag.devops {
        border-left: 3px solid #5cb85c;
    }
    
    .skill-tag.cyber {
        border-left: 3px solid #f0ad4e;
    }
    
    /* Terminal effect */
    .terminal {
        background-color: #1e1e1e;
        color: #f8f9fa;
        font-family: 'Courier New', monospace;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-top: 2px solid #4361ee;
    }
    
    .terminal-header {
        display: flex;
        align-items: center;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        color: #adb5bd;
    }
    
    .terminal-dot {
        height: 12px;
        width: 12px;
        background-color: #ff605c;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
    }
    
    .terminal-dot.yellow {
        background-color: #ffbd44;
    }
    
    .terminal-dot.green {
        background-color: #00ca4e;
    }
    
    .terminal-prompt {
        color: #4361ee;
        margin-right: 0.5rem;
    }
    
    .terminal-command {
        color: #f8f9fa;
    }
    
    /* Project cards */
    .project-card {
        background-color: #1a1d24;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #4361ee;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
        color: #f8f9fa;
    }
    
    .project-tech {
        margin-top: 0.8rem;
    }
    
    /* Animation for the blinking cursor */
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    
    .cursor {
        display: inline-block;
        width: 8px;
        height: 20px;
        background-color: #4361ee;
        animation: blink 1s infinite;
        vertical-align: middle;
    }
    
    /* Chatbot styles */
    .chat-message {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.8rem;
    }
    
    .chat-message.user {
        background-color: #2e3440;
        text-align: right;
    }
    
    .chat-message.bot {
        background-color: #1a1d24;
        border-left: 3px solid #4361ee;
    }

    /* Responsive adjustment for mobile */
    @media (max-width: 768px) {
        .main-header {
            padding: 1.5rem 0;
        }
        
        .section-header {
            font-size: 1.4rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Data for the portfolio
def load_portfolio_data():
    return {
        "name": "Prince Jindal",
        "title": "MERN/AI Fullstack Developer & DevOps Engineer",
        "about": "Passionate developer with expertise in MERN stack, AI/ML solutions, and DevOps practices. I build scalable applications with modern technologies and CI/CD pipelines.",
        "skills": {
            "MERN Stack": {
                "MongoDB": 90,
                "Express.js": 85,
                "React.js": 92,
                "Node.js": 88,
                "Redux": 82,
                "TypeScript": 80,
                "Next.js": 78
            },
            "AI/ML": {
                "Python": 85,
                "TensorFlow": 75,
                "PyTorch": 70,
                "LangChain": 80,
                "Hugging Face": 78,
                "OpenAI API": 85,
                "RAG Implementation": 82
            },
            "DevOps": {
                "Docker": 90,
                "Kubernetes": 80,
                "Jenkins": 85,
                "Terraform": 75,
                "AWS": 88,
                "Azure": 82,
                "CI/CD": 90
            },
            "Cybersecurity": {
                "OWASP": 85,
                "Penetration Testing": 75,
                "Security Auditing": 78,
                "Network Security": 80,
                "Authentication": 88,
                "Encryption": 82
            }
        },
        "projects": [
            {
                "title": "Personalised Youtube Recommendation System",
                "description": "A dynamic web application that recommends YouTube videos to users based on their viewing history and preferences. The system integrates YouTube Data API with Flask backend and SQL database for storage, using user authentication (OAuth 2.0) to fetch personalized data. Real-time metrics are visualized using Power BI, and an interactive prototype UI was developed in React.",
                "tech_stack": ["Python", "Flask", "JavaScript", "SQL", "Power BI", "OAuth 2.0", "HTML/CSS", "React"],
                "highlights": [
                    "Designed a Flask-based API to generate personalized video recommendations",
                    "Used OAuth 2.0 for secure access to user’s YouTube data",
                    "Processed user watch history and preferences to generate accurate suggestions",
                    "Developed a prototype React frontend to showcase recommended videos dynamically"
                ]            
            },
            {
                "title": "DevSecOps Pipeline Automation",
                "description": "GradePro is an intelligent web application designed to predict students’ semester grades based on academic performance metrics, attendance, past trends, and other behavioral inputs. The system combines a React-based UI, a Node.js/Express backend, and Python ML models to deliver real-time predictions and performance insights, stored and served via MongoDB pipelines.",
                "tech_stack": ["Jenkins", "Docker", "Kubernetes", "Terraform", "AWS", "OWASP ZAP", "SonarQube"],
                "highlights": [
                    "Developed a real-time grade prediction engine using Python ML models integrated into a Node.js backend",
                    "Designed an interactive React dashboard to help students track academic trends and receive personalized advice",
                    "Automated the data processing pipeline, enabling continuous learning and live prediction updates",
                    "UEnsured system scalability using Express.js API endpoints with structured data flow between frontend and backend"
                ]
            }
        ],
        "contact": {
            "email": "prince.jindal@example.com",
            "github": "github.com/princejindal",
            "linkedin": "linkedin.com/in/princejindal"
        }
    }

# Header Component
def render_header(data):
    st.markdown(f"""
    <div class="main-header">
        <h1>{data['name']}</h1>
        <h3>{data['title']}</h3>
        <p style="max-width: 700px; margin: 1rem auto; color: #adb5bd;">{data['about']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Terminal introduction effect
    st.markdown("""
    <div class="terminal">
        <div class="terminal-header">
            <span class="terminal-dot"></span>
            <span class="terminal-dot yellow"></span>
            <span class="terminal-dot green"></span>
            <span style="margin-left: 10px;">portfolio.sh</span>
        </div>
        <div>
            <span class="terminal-prompt">$</span>
            <span class="terminal-command">whoami</span>
        </div>
        <div style="margin-top: 0.5rem;">
    """, unsafe_allow_html=True)
    
    # Typing effect with JavaScript
    typing_text = data['name'] + ": " + data['title']
    st.markdown(f"""
        <div id="typing-text"></div>
        <span class="cursor"></span>
        
        <script>
            const text = "{typing_text}";
            let i = 0;
            const typingElement = document.getElementById('typing-text');
            
            function typeWriter() {{
                if (i < text.length) {{
                    typingElement.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 50);
                }}
            }}
            
            typeWriter();
        </script>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Skills Component
def render_skills(skills):
    st.markdown('<div class="section-header">Technical Skills</div>', unsafe_allow_html=True)
    
    tabs = st.tabs(list(skills.keys()))
    
    for i, category in enumerate(skills.keys()):
        with tabs[i]:
            st.markdown(f"<h4>My {category} Skills</h4>", unsafe_allow_html=True)
            
            cols = st.columns(2)
            skills_list = list(skills[category].items())
            mid_point = len(skills_list) // 2 + len(skills_list) % 2
            
            for col_idx, col in enumerate(cols):
                start_idx = col_idx * mid_point
                end_idx = start_idx + mid_point
                
                for skill, proficiency in skills_list[start_idx:end_idx]:
                    col.markdown(f"<div style='margin-bottom: 1rem;'><b>{skill}</b></div>", unsafe_allow_html=True)
                    col.progress(proficiency / 100)
            
            # Add code snippet for this category
            if category == "MERN Stack":
                st.markdown("""
                <div class="terminal">
                    <div class="terminal-header">
                        <span class="terminal-dot"></span>
                        <span class="terminal-dot yellow"></span>
                        <span class="terminal-dot green"></span>
                        <span style="margin-left: 10px;">mern-stack.js</span>
                    </div>
                    <pre style="color: #f8f9fa; margin: 0;">const app = express();
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log('MongoDB connected');
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
};

app.use(express.json());
app.use('/api/users', require('./routes/users'));
app.use('/api/auth', require('./routes/auth'));

if (process.env.NODE_ENV === 'production') {
  app.use(express.static('client/build'));
  app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'client', 'build', 'index.html'));
  });
}</pre>
                </div>
                """, unsafe_allow_html=True)
            elif category == "AI/ML":
                st.markdown("""
                <div class="terminal">
                    <div class="terminal-header">
                        <span class="terminal-dot"></span>
                        <span class="terminal-dot yellow"></span>
                        <span class="terminal-dot green"></span>
                        <span style="margin-left: 10px;">rag_system.py</span>
                    </div>
                    <pre style="color: #f8f9fa; margin: 0;">from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def create_rag_system():
    # Load documents and create embeddings
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=docs, 
        embedding=embeddings
    )
    
    # Create retriever and LLM
    retriever = vectorstore.as_retriever()
    llm = OpenAI(temperature=0)
    
    # Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    
    return qa_chain</pre>
                </div>
                """, unsafe_allow_html=True)
            elif category == "DevOps":
                st.markdown("""
                <div class="terminal">
                    <div class="terminal-header">
                        <span class="terminal-dot"></span>
                        <span class="terminal-dot yellow"></span>
                        <span class="terminal-dot green"></span>
                        <span style="margin-left: 10px;">Dockerfile</span>
                    </div>
                    <pre style="color: #f8f9fa; margin: 0;">FROM node:16-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]</pre>
                </div>
                """, unsafe_allow_html=True)
            elif category == "Cybersecurity":
                st.markdown("""
                <div class="terminal">
                    <div class="terminal-header">
                        <span class="terminal-dot"></span>
                        <span class="terminal-dot yellow"></span>
                        <span class="terminal-dot green"></span>
                        <span style="margin-left: 10px;">security_config.js</span>
                    </div>
                    <pre style="color: #f8f9fa; margin: 0;">// Set secure HTTP headers
const helmet = require('helmet');
app.use(helmet());

// Enable CORS with secure configuration
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS.split(','),
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,
  maxAge: 86400
}));

// Rate limiting to prevent brute force
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  standardHeaders: true,
  legacyHeaders: false
});
app.use('/api/auth', limiter);</pre>
                </div>
                """, unsafe_allow_html=True)

# Projects Component
def render_projects(projects):
    st.markdown('<div class="section-header">Featured Projects</div>', unsafe_allow_html=True)
    
    for idx, project in enumerate(projects):
        with st.expander(f"**{project['title']}**", expanded=(idx == 0)):
            cols = st.columns([2, 1])
            
            with cols[0]:
                st.markdown(f"<p>{project['description']}</p>", unsafe_allow_html=True)
                
                st.markdown("#### Key Highlights")
                for highlight in project['highlights']:
                    st.markdown(f"• {highlight}")
                
            with cols[1]:
                st.markdown("#### Tech Stack")
                tech_html = ""
                for tech in project['tech_stack']:
                    category = "mern" if tech in ["MongoDB", "Express.js", "React", "Node.js"] else \
                              "ai" if tech in ["Python", "TensorFlow", "PyTorch", "OpenAI API"] else \
                              "devops" if tech in ["Docker", "Kubernetes", "AWS", "Jenkins", "Terraform"] else "cyber"
                    tech_html += f"<span class='skill-tag {category}'>{tech}</span> "
                st.markdown(f"<div class='project-tech'>{tech_html}</div>", unsafe_allow_html=True)
            
            st.markdown("#### Sample Code")
            st.code(project['code_snippet'], language="python" if "def " in project['code_snippet'] else "javascript")

# AI Experience Component
def render_ai_experience(ai_experience):
    st.markdown('<div class="section-header">AI & Machine Learning Experience</div>', unsafe_allow_html=True)
    
    # DevOps pipeline visualization
    st.markdown("### AI Development Pipeline")
    
    pipeline_cols = st.columns(5)
    
    pipeline_steps = [
        {"icon": "📊", "title": "Data Collection", "color": "#4361ee"},
        {"icon": "🧹", "title": "Data Processing", "color": "#3a0ca3"},
        {"icon": "🧠", "title": "Model Training", "color": "#7209b7"},
        {"icon": "🔍", "title": "Evaluation", "color": "#f72585"},
        {"icon": "🚀", "title": "Deployment", "color": "#4cc9f0"}
    ]
    
    for idx, (col, step) in enumerate(zip(pipeline_cols, pipeline_steps)):
        col.markdown(f"""
        <div style="text-align: center; padding: 1rem; background-color: #1a1d24; border-radius: 8px; border-top: 3px solid {step['color']};">
            <div style="font-size: 2rem;">{step['icon']}</div>
            <div style="font-weight: 600; margin-top: 0.5rem;">{step['title']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add connecting arrow except for the last item
        if idx < len(pipeline_cols) - 1:
            col.markdown("""
            <div style="text-align: center; margin-top: 0.5rem;">
                <span style="font-size: 1.5rem; color: #4361ee;">→</span>
            </div>
            """, unsafe_allow_html=True)
    
    # AI Chatbot Q&A
    st.markdown("### Ask about my AI experience")
    
    # Initialize session state for chat
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Create dictionary for fast lookup of answers
    qa_dict = {item['question']: item['answer'] for item in ai_experience}
    
    # Display chat history
    for chat in st.session_state.chat_history:
        if chat['type'] == 'user':
            st.markdown(f"""
            <div class="chat-message user">
                <div style="font-weight: 600; margin-bottom: 0.3rem;">You</div>
                <div>{chat['message']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot">
                <div style="font-weight: 600; margin-bottom: 0.3rem;">Prince</div>
                <div>{chat['message']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Question selection or custom question
    question_options = ["Select a question..."] + [q['question'] for q in ai_experience] + ["Ask your own question"]
    selected_question = st.selectbox("", question_options)
    
    custom_question = ""
    if selected_question == "Ask your own question":
        custom_question = st.text_input("Type your question about my AI experience")
    
    # Submit button
    if st.button("Ask"):
        question = custom_question if selected_question == "Ask your own question" else selected_question
        
        if question and question != "Select a question...":
            # Add question to chat history
            st.session_state.chat_history.append({
                'type': 'user',
                'message': question
            })
            
            # Get answer
            if question in qa_dict:
                answer = qa_dict[question]
            else:
                # For custom questions, provide a generic response
                answer = "Thanks for your question! While this demo has limited responses, I'd be happy to discuss my AI experience in more detail during an interview. Please feel free to contact me to explore how my skills align with your needs."
            
            # Add answer to chat history
            st.session_state.chat_history.append({
                'type': 'bot',
                'message': answer
            })
            
            # Rerun to update UI
            st.experimental_rerun()

# Contact Form Component
def render_contact(contact_info):
    st.markdown('<div class="section-header">Get In Touch</div>', unsafe_allow_html=True)
    
    cols = st.columns([1, 1])
    
    with cols[0]:
        st.markdown("""
        <div class="card">
            <h4>Contact Information</h4>
            <div style="margin: 1.5rem 0;">
                <div style="margin-bottom: 1rem;">
                    <strong>Email:</strong> {0}
                </div>
                <div style="margin-bottom: 1rem;">
                    <strong>GitHub:</strong> <a href="https://{1}" target="_blank">{1}</a>
                </div>
                <div>
                    <strong>LinkedIn:</strong> <a href="https://{2}" target="_blank">{2}</a>
                </div>
            </div>
        </div>
        """.format(
            contact_info['email'],
            contact_info['github'],
            contact_info['linkedin']
        ), unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("<h4>Send me a message</h4>", unsafe_allow_html=True)
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        if st.button("Send Message", type="primary"):
            # This would normally connect to a backend
            st.success("Thank you for your message! I'll get back to you soon.")
            
            # For demo purposes, show a terminal effect
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="terminal-dot"></span>
                    <span class="terminal-dot yellow"></span>
                    <span class="terminal-dot green"></span>
                    <span style="margin-left: 10px;">message_sent.log</span>
                </div>
                <div>
                    <span class="terminal-prompt">$</span>
                    <span class="terminal-command">echo "Message sent successfully!"</span>
                </div>
                <div style="margin-top: 0.5rem; color: #5cb85c;">Message sent successfully!</div>
            </div>
            """, unsafe_allow_html=True)

# Main App
def main():
    # Load CSS and data
    load_css()
    data = load_portfolio_data()
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"<h2 style='text-align: center;'>{data['name']}</h2>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; margin-bottom: 2rem;'>👨‍💻 Developer Portfolio</div>", unsafe_allow_html=True)
        
        # Navigation
        st.markdown("### Navigation")
        nav_options = ["About", "Skills", "Projects", "AI Experience", "Contact"]
        selected_option = st.radio("", nav_options)
        
        # GitHub Stats
        st.markdown("### GitHub Activity")
        cols = st.columns(4)
        stats = [
            {"label": "Repos", "value": "32"},
            {"label": "Stars", "value": "218"},
            {"label": "PRs", "value": "148"},
            {"label": "Contribs", "value": "1.2k"}
        ]
        
        for i, (col, stat) in enumerate(zip(cols, stats)):
            col.markdown(f"""
            <div style='text-align: center;'>
                <div style='font-size: 1.2rem; font-weight: 600; color: #4361ee;'>{stat['value']}</div>
                <div style='font-size: 0.8rem;'>{stat['label']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Theme toggle (for demonstration)
        st.markdown("### Theme")
        theme = st.selectbox("", ["Dark (Default)", "Light"])
        
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; font-size: 0.8rem; color: #6c757d;'>
            Made with Streamlit<br>
            Last updated: May 2025
        </div>
        """, unsafe_allow_html=True)
    
    # Main content area
    render_header(data)
    
    # Conditional rendering based on navigation
    if selected_option == "Skills" or selected_option == "About":
        render_skills(data['skills'])
    
    if selected_option == "Projects" or selected_option == "About":
        render_projects(data['projects'])
    
    if selected_option == "AI Experience" or selected_option == "About":
        render_ai_experience(data['ai_experience'])
    
    if selected_option == "Contact" or selected_option == "About":
        render_contact(data['contact'])

if __name__ == "__main__":
    main()
