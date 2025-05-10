import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Prince Jindal | MERN/AI Fullstack Developer & DevOps Engineer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS (you'll need to create this file or embed the CSS directly)
# local_css("style.css")

# Instead of external CSS, we'll use inline styles
custom_css = """
<style>
    /* Main colors */
    :root {
        --primary: #2563eb;
        --primary-dark: #1e40af;
        --secondary: #0ea5e9;
        --dark: #1e293b;
        --light: #f8fafc;
        --accent: #10b981;
    }
    
    /* General styling */
    .stApp {
        background-color: #f8fafc;
    }
    
    .header {
        color: var(--dark);
        border-bottom: 2px solid var(--primary);
        padding-bottom: 0.5rem;
    }
    
    .card {
        background-color: black;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        border-left: 4px solid var(--primary);
    }
    
    .skill-card {
        background-color: black;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .skill-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .skill-title {
        color: var(--primary-dark);
        font-weight: 600;
    }
    
    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .tech-pill {
        display: inline-block;
        background-color: var(--secondary);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .contact-form {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        max-width: 80%;
    }
    
    .user-message {
        background-color: var(--primary);
        color: white;
        margin-left: auto;
    }
    
    .bot-message {
        background-color: #e2e8f0;
        margin-right: auto;
    }
    
    .highlight {
        color: var(--primary);
        font-weight: 600;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# State management
if 'expanded_project' not in st.session_state:
    st.session_state.expanded_project = None

if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "bot", "content": "Hi! I'm here to answer questions about Prince's AI experience. Ask me anything about LLMs, Generative AI, or his projects."}
    ]

# Hero Section
st.title("Prince Jindal")
st.markdown("""
    <h2 style='color: #2563eb; margin-top: -1rem;'>MERN/AI Fullstack Developer & DevOps Engineer</h2>
    <p style='font-size: 1.1rem;'>
        Passionate full-stack developer with hands-on experience in the MERN stack, RESTful APIs, and AI-powered systems. 
        Adept in frontend optimization, API integration, and scalable backend design.
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# Skills Section
st.header("🛠 Skills & Expertise")
st.markdown("""
    <p style='font-size: 1.1rem; margin-bottom: 1.5rem;'>
        Here's a quick overview of my technical skills and areas of expertise.
    </p>
""", unsafe_allow_html=True)

# Skills columns
col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("**MERN Stack**", expanded=True):
        st.markdown("""
            - **React.js** (Next.js, Redux)
            - **Node.js** (Express.js)
            - **MongoDB** (Mongoose)
            - Modern CSS (TailwindCSS)
            - RESTful API design
        """)

with col2:
    with st.expander("**AI/ML & Data**", expanded=True):
        st.markdown("""
            - Python for ML (Scikit-learn)
            - LLM experimentation (OpenAI)
            - Data analysis & visualization
            - Recommendation systems
            - Predictive modeling
        """)

with col3:
    with st.expander("**DevOps & Cloud**", expanded=True):
        st.markdown("""
            - CI/CD (GitHub Actions)
            - Containerization (Docker)
            - Cloud platforms (AWS, GCP)
            - Infrastructure as Code
            - Monitoring & logging
        """)

st.markdown("---")

# Projects Section
st.header("🚀 Project Highlights")

# Project 1
with st.container():
    st.markdown("""
        <div class='card'>
            <div class='project-header'>
                <h3>Personalised YouTube Recommendation System</h3>
                <div>
                    <span class='tech-pill'>Python</span>
                    <span class='tech-pill'>Flask</span>
                    <span class='tech-pill'>JavaScript</span>
                    <span class='tech-pill'>Power BI</span>
                </div>
            </div>
            <ul>
                <li>Created a scalable recommendation system using the Python and YouTube Data API, optimizing query execution and API response times.</li>
                <li>Integrated Power BI dashboards to visualize user engagement metrics and recommendation accuracy.</li>
                <li>Implemented OAuth 2.0 authentication for secure access and data retrieval.</li>
                <li>Applied SQL for data storage and retrieval, ensuring data integrity and efficient query execution.</li>
                <li>Developed a Flask API to process video recommendations, ensuring a 95% accuracy rate.</li>
                <li>Prototyped a React-based user interface for seamless user interaction with recommended videos.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Project 2
with st.container():
    st.markdown("""
        <div class='card'>
            <div class='project-header'>
                <h3>GradePro: AI-Powered University Grade Predictor & Advisor</h3>
                <div>
                    <span class='tech-pill'>React</span>
                    <span class='tech-pill'>Node.js</span>
                    <span class='tech-pill'>Python</span>
                    <span class='tech-pill'>MongoDB</span>
                </div>
            </div>
            <ul>
                <li>Built a scalable, real-time AI analytics system using MongoDB and Express.js, ensuring fast data processing and retrieval.</li>
                <li>Interactive dashboards created using React to visualize student performance trends.</li>
                <li>Engineered a machine learning model in Python, integrated with the Node.js backend for real-time predictions.</li>
                <li>Automated data processing workflows for real-time grade prediction updates.</li>
                <li>Developed MongoDB-based data pipelines, improving data retrieval speed by 40%.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# AI Interest Section
st.header("🤖 AI Interests & Theoretical Knowledge")
st.markdown("""
    <div class='card'>
        <h3>Large Language Models & Generative AI</h3>
        <p>
            While my practical experience with AI focuses on predictive modeling and recommendation systems,
            I maintain a strong theoretical understanding of cutting-edge AI technologies:
        </p>
        <ul>
            <li><span class='highlight'>Transformer Architecture</span>: Understanding of self-attention mechanisms and encoder-decoder structures</li>
            <li><span class='highlight'>LLM Training</span>: Knowledge of pre-training, fine-tuning, and RLHF processes</li>
            <li><span class='highlight'>Prompt Engineering</span>: Techniques for effective interaction with models like GPT</li>
            <li><span class='highlight'>Ethical Considerations</span>: Awareness of bias, fairness, and responsible AI development</li>
            <li><span class='highlight'>Emergent Capabilities</span>: Understanding of how scale affects model behavior</li>
        </ul>
        <p>
            I'm particularly interested in exploring how LLMs can be integrated with traditional software systems
            to create more intelligent applications.
        </p>
    </div>
""", unsafe_allow_html=True)

# Chatbot Section
st.markdown("---")
st.header("💬 Ask About My AI Knowledge")

# Chat container
chat_container = st.container()

# Display chat messages
for message in st.session_state.chat_messages:
    with chat_container:
        if message["role"] == "user":
            st.markdown(f"""
                <div class='chat-message user-message'>
                    {message["content"]}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='chat-message bot-message'>
                    {message["content"]}
                </div>
            """, unsafe_allow_html=True)

# Chat input
user_input = st.text_input("Ask a question about my AI experience:", key="user_input", placeholder="E.g., What do you know about transformer models?")

# Chat logic
if user_input:
    # Add user message to chat
    st.session_state.chat_messages.append({"role": "user", "content": user_input})
    
    # Simple response logic
    user_input_lower = user_input.lower()
    response = ""
    
    if "transformer" in user_input_lower:
        response = """
            Transformer models are a type of neural network architecture that relies on self-attention mechanisms 
            rather than recurrent or convolutional layers. The key components are:
            
            1. <span class='highlight'>Self-Attention</span>: Allows the model to weigh the importance of different words in a sequence
            2. <span class='highlight'>Encoder-Decoder Structure</span>: Used in models like BERT (encoder-only) and GPT (decoder-only)
            3. <span class='highlight'>Positional Encoding</span>: Adds information about the position of each word in the sequence
            
            Transformers have revolutionized NLP due to their parallel processing capabilities and ability to capture long-range dependencies.
        """
    elif "llm" in user_input_lower or "large language model" in user_input_lower:
        response = """
            Large Language Models (LLMs) are AI systems trained on vast amounts of text data that can understand 
            and generate human-like text. Key aspects include:
            
            1. <span class='highlight'>Scale</span>: Typically have billions of parameters and require massive compute resources
            2. <span class='highlight'>Training Process</span>: Involves pre-training on general text and fine-tuning for specific tasks
            3. <span class='highlight'>Emergent Abilities</span>: Capabilities that appear only in larger models (e.g., complex reasoning)
            4. <span class='highlight'>Applications</span>: Chatbots, content generation, code assistance, and more
            
            While I haven't trained LLMs from scratch, I understand their architecture and have experimented with API-based implementations.
        """
    elif "generative" in user_input_lower:
        response = """
            Generative AI refers to models that can create new content (text, images, code, etc.). Important concepts:
            
            1. <span class='highlight'>Diffusion Models</span>: Used in image generation (e.g., Stable Diffusion)
            2. <span class='highlight'>GANs</span>: Generative Adversarial Networks that pit two networks against each other
            3. <span class='highlight'>Autoregressive Models</span>: Generate output one piece at a time (like GPT does with text)
            4. <span class='highlight'>Control Mechanisms</span>: Techniques to guide generation (temperature, top-k sampling)
            
            My experience with generative AI is primarily theoretical, though I've built recommendation systems that share some conceptual similarities.
        """
    else:
        response = """
            I'm happy to discuss my AI knowledge! Could you clarify your question? 
            I can speak about transformer architectures, LLM capabilities, generative AI concepts, 
            or how AI can be integrated into full-stack applications.
        """
    
    st.session_state.chat_messages.append({"role": "bot", "content": response})
    st.rerun()

st.markdown("---")

# Contact Section
st.header("📬 Get In Touch")
with st.form("contact_form"):
    st.markdown("""
        <div class='contact-form'>
            <p>Have a question or opportunity? Send me a message!</p>
    """, unsafe_allow_html=True)
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message", height=150)
    
    submitted = st.form_submit_button("Send Message")
    if submitted:
        if name and email and message:
            st.success("Message sent successfully! I'll get back to you soon.")
            # In a real app, you would add code here to actually send the message
        else:
            st.error("Please fill in all fields.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 1rem; color: #64748b;'>
        <p>© 2024 Prince Jindal. All rights reserved.</p>
        <p>j.prince0410@gmail.com | (+91) 8307261678 | Gurgaon, India</p>
    </div>
""", unsafe_allow_html=True)
