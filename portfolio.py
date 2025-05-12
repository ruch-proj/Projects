from flask import Flask, render_template_string

app = Flask(__name__)

# Portfolio data with image
portfolio_data = {
    "name": "Ruchika Mahajan",
    "tagline": "Student | Web Developer | AI Developer | Tech Enthusiast",
    "about": "Creative tech enthusiast with a strong foundation in Mathematics and Electrical Engineering, passionate about building secure, scalable, and user-centric digital experiences. I bridge deep learning, embedded systems, and full-stack development to deliver impactful, real-time solutions.",
    "image_url": "https://drive.google.com/thumbnail?id=19o1zgF8yV5UxDQoVlNmHe08wpKk_aLrc",  # Added image URL (replace with your actual image)
    "skills": {
        "Programming Languages": ["Python (Advanced)", "C/C++", "R"],
        "Machine Learning": ["TensorFlow", "PyTorch", "scikit-learn", "OpenCV"],
        "Web Development": ["Flask", "HTML/CSS", "Firebase"],
        "Data Science": ["Pandas", "NumPy", "Matplotlib"],
        "Hardware Technologies": ["Cadence", "Verilog", "TCAD", "Pspice"],
        "Database Management": ["MySQL"]
    },
    "experience": [
        {
            "title": "Gimbal Space | Embedded Systems Intern",
            "description": [
                "Developed and tested embedded C/C++ firmware for microcontroller-based systems, improving hardware response time by 15%.",
                "Designed and executed 10+ real-time simulations using hardware-in-the-loop (HIL) setups.",
                "Collaborated with a cross-functional team to debug and document system issues."
            ],
            "icon": "microchip"
        },
        {
            "title": "Girl Power Talk | AI Research Intern",
            "description": [
                "Built a real-time document scanning system using OpenCV and Tesseract OCR with 92%+ accuracy.",
                "Designed automated data pipelines with Firebase & Firestore, reducing manual handling by 60%.",
                "Developed backend using Python and Flask, reducing API response time by 30%."
            ],
            "icon": "robot"
        },
        {
            "title": "I Care Foundation | Software/Web Developer",
            "description": [
                "Developed cross-platform solutions integrating data from 5+ third-party APIs.",
                "Automated reporting pipelines using cloud tools, reducing manual time by 70%.",
                "Increased digital reach by 40% through automation-driven SEO strategies."
            ],
            "icon": "globe"
        }
    ],
    "projects": [
        {
            "title": "Gesture Recognition for Prosthetic Arm",
            "description": [
                "Developed ML-based system using EMG signals from 8 subjects (44,000+ data points).",
                "Achieved 95%+ classification accuracy for 8 distinct gestures.",
                "Technologies: Python, MATLAB, EMG sensors"
            ],
            "color": "#4e79a7",
            "icon": "hand-paper"
        },
        {
            "title": "Fraud Detection Application",
            "description": [
                "Detects fraudulent transactions using Isolation Forest algorithm.",
                "Utilizes synthetic data generation and preprocessing.",
                "Technologies: Python, scikit-learn, Pandas"
            ],
            "color": "#e15759",
            "icon": "shield-alt"
        },
        {
            "title": "Sign Language Recognition",
            "description": [
                "Real-time system using webcam input with CNN-LSTM model (90%+ accuracy).",
                "Reduced raw video data by 80% through landmark extraction.",
                "Technologies: Python, TensorFlow, MediaPipe"
            ],
            "color": "#76b7b2",
            "icon": "sign-language"
        },
        {
            "title": "Alternative-Routes in Road Networks",
            "description": [
                "Simulates road network with dynamic traffic using Dijkstra's Algorithm.",
                "Visualizations with NetworkX & Matplotlib.",
                "Technologies: Python, NetworkX, Matplotlib"
            ],
            "color": "#f28e2b",
            "icon": "road"
        },
        {
            "title": "Real-Time Chat Application",
            "description": [
                "Flask and Socket.IO with instant messaging.",
                "Built-in chatbot with predefined auto-responses.",
                "Technologies: Flask, WebSockets, Python"
            ],
            "color": "#edc948",
            "icon": "comments"
        }
    ],
    "certifications": [
        "Advanced to penultimate round of Walmart Sparkplug, Flipkart Grid, TVS Credit EPIC",
        "Master Python, Python for Data Science, Web Development (Udemy)",
        "ChatGPT and AI Tools (Skill Nation), AI for AI (IBM)",
        "Data Science and Machine Learning (Edureka)"
    ],
    "contact": {
        "email": "ruchikamahajan3007@gmail.com",
        "phone": "+91-9729002208",
        "location": "Delhi, India",
        "github": "https://github.com/ruch-proj/Projects?tab=readme-ov-file#projects"
    }
}

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.name }} - Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        :root {
            --primary-color: #6C63FF;
            --secondary-color: #4D44DB;
            --accent-color: #FF6584;
            --light-color: #1E1E2E;
            --dark-color: #12121B;
            --text-color: #E0E0E0;
            --text-light: #A0A0A0;
            --success-color: #28A745;
            --warning-color: #FFC107;
            --info-color: #17A2B8;
            --project-1-color: #4e79a7;
            --project-2-color: #e15759;
            --project-3-color: #76b7b2;
            --project-4-color: #f28e2b;
            --project-5-color: #edc948;
            --card-bg: #2A2A3A;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.7;
            color: var(--text-color);
            background-color: var(--dark-color);
            overflow-x: hidden;
        }

        h1, h2, h3, h4 {
            font-family: 'Playfair Display', serif;
            font-weight: 600;
            color: #FFFFFF;
        }

        .section-title {
            font-family: 'Montserrat', sans-serif;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        header {
            background-color: rgba(30, 30, 46, 0.95);
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            backdrop-filter: blur(5px);
            transition: all 0.3s ease;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 1.5rem 0;
        }

        nav ul li {
            margin: 0 1.5rem;
            position: relative;
        }

        nav ul li a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 500;
            transition: color 0.3s;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            letter-spacing: 1px;
        }

        nav ul li a:hover {
            color: var(--primary-color);
        }

        nav ul li a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -5px;
            left: 0;
            background-color: var(--primary-color);
            transition: width 0.3s;
        }

        nav ul li a:hover::after {
            width: 100%;
        }

        .hero {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10rem 5% 6rem;
            min-height: 100vh;
            background: linear-gradient(135deg, #2A2A3A 0%, #1E1E2E 100%);
            position: relative;
            overflow: hidden;
            text-align: center;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 80%;
            height: 200%;
            background: radial-gradient(circle, rgba(108, 99, 255, 0.1) 0%, rgba(30, 30, 46, 0) 70%);
            z-index: 0;
        }

        .hero-content {
            max-width: 800px;
            position: relative;
            z-index: 1;
        }

        .profile-image {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid var(--primary-color);
            margin: 0 auto 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }

        .profile-image:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(108, 99, 255, 0.4);
        }

        .hero-content h1 {
            font-size: 4.5rem;
            margin-bottom: 1.5rem;
            color: #FFFFFF;
            line-height: 1.2;
            text-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }

        .hero-content h2 {
            font-size: 2rem;
            font-weight: 400;
            margin-bottom: 2rem;
            color: var(--text-light);
            font-family: 'Montserrat', sans-serif;
        }

        .hero-content p {
            font-size: 1.2rem;
            margin-bottom: 3rem;
            color: var(--text-color);
        }

        .btn {
            display: inline-block;
            background-color: var(--primary-color);
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
            font-family: 'Montserrat', sans-serif;
            letter-spacing: 1px;
            box-shadow: 0 5px 15px rgba(108, 99, 255, 0.3);
            border: none;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .btn:hover {
            background-color: var(--secondary-color);
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(108, 99, 255, 0.4);
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: 0.5s;
        }

        .btn:hover::before {
            left: 100%;
        }

        section {
            padding: 6rem 5%;
            position: relative;
            background-color: var(--dark-color);
        }

        section h1 {
            font-size: 2.8rem;
            margin-bottom: 3rem;
            color: #FFFFFF;
            text-align: center;
            position: relative;
            display: inline-block;
            left: 50%;
            transform: translateX(-50%);
        }

        section h1::after {
            content: '';
            position: absolute;
            width: 50%;
            height: 4px;
            bottom: -10px;
            left: 25%;
            background: linear-gradient(to right, var(--primary-color), var(--accent-color));
            border-radius: 2px;
        }

        .about {
            text-align: center;
        }

        .about p {
            max-width: 800px;
            margin: 0 auto;
            font-size: 1.2rem;
            line-height: 1.8;
            color: var(--text-color);
        }

        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .skill-category {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: all 0.4s;
            border: 1px solid rgba(255, 255, 255, 0.05);
            position: relative;
            overflow: hidden;
        }

        .skill-category:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        }

        .skill-category::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(to bottom, var(--primary-color), var(--accent-color));
        }

        .skill-category h3 {
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            color: #FFFFFF;
            position: relative;
            padding-left: 1.5rem;
        }

        .skill-category h3::before {
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 8px;
            height: 8px;
            background-color: var(--primary-color);
            border-radius: 50%;
        }

        .skill-category ul {
            list-style: none;
        }

        .skill-category ul li {
            margin-bottom: 0.8rem;
            position: relative;
            padding-left: 2rem;
            font-family: 'Montserrat', sans-serif;
            color: var(--text-color);
        }

        .skill-category ul li::before {
            content: "▹";
            position: absolute;
            left: 0;
            color: var(--primary-color);
            font-size: 1.2rem;
        }

        .experience-item {
            background-color: var(--card-bg);
            padding: 2.5rem;
            margin-bottom: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: all 0.3s;
            border: 1px solid rgba(255, 255, 255, 0.05);
            position: relative;
        }

        .experience-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        }

        .experience-item h2 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            color: #FFFFFF;
            display: flex;
            align-items: center;
        }

        .experience-item h2 i {
            margin-right: 1rem;
            color: var(--primary-color);
            font-size: 1.5rem;
            width: 2.5rem;
            height: 2.5rem;
            background-color: rgba(108, 99, 255, 0.1);
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }

        .experience-item ul {
            margin-left: 3.5rem;
            list-style-type: none;
        }

        .experience-item ul li {
            margin-bottom: 1rem;
            position: relative;
            padding-left: 1.5rem;
            line-height: 1.6;
            color: var(--text-color);
        }

        .experience-item ul li::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0.7rem;
            width: 8px;
            height: 8px;
            background-color: var(--primary-color);
            border-radius: 50%;
        }

        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 2.5rem;
            margin-top: 3rem;
        }

        .project-card {
            background-color: var(--card-bg);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: all 0.4s;
            border: 1px solid rgba(255, 255, 255, 0.05);
            position: relative;
            overflow: hidden;
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background-color: var(--project-color, var(--primary-color));
        }

        .project-card h2 {
            font-size: 1.6rem;
            margin-bottom: 1.5rem;
            color: #FFFFFF;
            display: flex;
            align-items: center;
        }

        .project-card h2 i {
            margin-right: 1rem;
            color: var(--project-color, var(--primary-color));
            font-size: 1.5rem;
        }

        .project-card ul {
            margin-left: 1rem;
            margin-bottom: 2rem;
            list-style-type: none;
        }

        .project-card ul li {
            margin-bottom: 1rem;
            position: relative;
            padding-left: 1.8rem;
            line-height: 1.6;
            color: var(--text-color);
        }

        .project-card ul li::before {
            content: '•';
            position: absolute;
            left: 0;
            color: var(--project-color, var(--primary-color));
            font-size: 1.5rem;
            line-height: 1;
        }

        .certifications {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            margin-top: 3rem;
        }

        .certifications ul {
            list-style-type: none;
            columns: 2;
            column-gap: 3rem;
        }

        .certifications ul li {
            margin-bottom: 1rem;
            position: relative;
            padding-left: 2rem;
            break-inside: avoid;
            color: var(--text-color);
        }

        .certifications ul li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--success-color);
            font-weight: bold;
        }

        .contact-container {
            display: flex;
            justify-content: center;
            gap: 4rem;
            margin-top: 3rem;
            flex-wrap: wrap;
        }

        .contact-info {
            max-width: 500px;
            background-color: var(--card-bg);
            padding: 3rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            flex: 1;
            min-width: 300px;
        }

        .contact-info h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #FFFFFF;
            position: relative;
            padding-bottom: 1rem;
        }

        .contact-info h2::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 50px;
            height: 3px;
            background: linear-gradient(to right, var(--primary-color), var(--accent-color));
        }

        .contact-info p {
            margin-bottom: 2rem;
            color: var(--text-color);
            line-height: 1.8;
        }

        .contact-details {
            margin-top: 2rem;
        }

        .contact-details p {
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            color: var(--text-color);
            transition: all 0.3s;
        }

        .contact-details p:hover {
            color: var(--primary-color);
        }

        .contact-details i {
            margin-right: 1.5rem;
            color: var(--primary-color);
            font-size: 1.2rem;
            width: 2.5rem;
            height: 2.5rem;
            background-color: rgba(108, 99, 255, 0.1);
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }

        .contact-details p:hover i {
            background-color: rgba(108, 99, 255, 0.2);
            transform: scale(1.1);
        }

        .contact-details a {
            color: inherit;
            text-decoration: none;
        }

        footer {
            background: linear-gradient(135deg, var(--dark-color) 0%, #0A0A12 100%);
            color: white;
            text-align: center;
            padding: 3rem 0;
            margin-top: 5rem;
        }

        .social-links {
            margin-bottom: 2rem;
        }

        .social-links a {
            color: white;
            margin: 0 1rem;
            font-size: 1.5rem;
            transition: all 0.3s;
            display: inline-block;
        }

        .social-links a:hover {
            color: var(--primary-color);
            transform: translateY(-5px);
        }

        .back-to-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 3rem;
            height: 3rem;
            background-color: var(--primary-color);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s;
            z-index: 999;
        }

        .back-to-top.visible {
            opacity: 1;
            visibility: visible;
        }

        .back-to-top:hover {
            background-color: var(--secondary-color);
            transform: translateY(-3px);
        }

        @media (max-width: 1024px) {
            .hero-content h1 {
                font-size: 3.5rem;
            }
            
            .hero-content h2 {
                font-size: 1.8rem;
            }
        }

        @media (max-width: 768px) {
            .hero {
                flex-direction: column;
                text-align: center;
                padding-top: 8rem;
                padding-bottom: 4rem;
            }
            
            .hero-content {
                padding-right: 0;
                margin-bottom: 0;
            }

            nav ul {
                padding: 1rem 0;
                flex-wrap: wrap;
            }
            
            nav ul li {
                margin: 0.5rem 1rem;
            }

            .certifications ul {
                columns: 1;
            }

            section {
                padding: 4rem 5%;
            }

            section h1 {
                font-size: 2.2rem;
                margin-bottom: 2rem;
            }
        }

        @media (max-width: 480px) {
            .hero-content h1 {
                font-size: 3rem;
            }
            
            .hero-content h2 {
                font-size: 1.5rem;
            }

            .profile-image {
                width: 150px;
                height: 150px;
            }

            nav ul li {
                margin: 0.5rem;
                font-size: 0.8rem;
            }

            .project-card, .experience-item, .skill-category {
                padding: 1.5rem;
            }

            .contact-info {
                padding: 2rem;
            }
        }

        /* Animation classes */
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .delay-1 { animation-delay: 0.2s; }
        .delay-2 { animation-delay: 0.4s; }
        .delay-3 { animation-delay: 0.6s; }
        .delay-4 { animation-delay: 0.8s; }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="hero" id="home">
            <div class="hero-content fade-in">
                {% if data.image_url %}
                <img src="{{ data.image_url }}" alt="{{ data.name }}" class="profile-image">
                {% endif %}
                <h1>{{ data.name }}</h1>
                <h2>{{ data.tagline }}</h2>
                <p>{{ data.about }}</p>
                <a href="#contact" class="btn">Contact Me</a>
            </div>
        </section>

        <section class="about fade-in delay-1" id="about">
            <h1>About Me</h1>
            <p>{{ data.about }}</p>
        </section>

        <section class="skills fade-in delay-1">
            <h1>Technical Skills</h1>
            <div class="skills-container">
                {% for category, skills in data.skills.items() %}
                <div class="skill-category fade-in delay-{{ loop.index }}">
                    <h3>{{ category }}</h3>
                    <ul>
                        {% for skill in skills %}
                        <li>{{ skill }}</li>
                        {% endfor %}
                    </ul>
                </div>
                {% endfor %}
            </div>
        </section>

        <section class="experience" id="experience">
            <h1 class="fade-in">Experience</h1>
            {% for job in data.experience %}
            <div class="experience-item fade-in delay-{{ loop.index }}">
                <h2><i class="fas fa-{{ job.icon }}"></i> {{ job.title }}</h2>
                <ul>
                    {% for desc in job.description %}
                    <li>{{ desc }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endfor %}

            <div class="certifications fade-in delay-3">
                <h2>Certifications and Achievements</h2>
                <ul>
                    {% for cert in data.certifications %}
                    <li>{{ cert }}</li>
                    {% endfor %}
                </ul>
            </div>
        </section>

        <section class="projects" id="projects">
            <h1 class="fade-in">Projects</h1>
            <div class="project-grid">
                {% for project in data.projects %}
                <div class="project-card fade-in delay-{{ loop.index }}" style="--project-color: {{ project.color }};">
                    <h2><i class="fas fa-{{ project.icon }}"></i> {{ project.title }}</h2>
                    <ul>
                        {% for desc in project.description %}
                        <li>{{ desc }}</li>
                        {% endfor %}
                    </ul>
                </div>
                {% endfor %}
            </div>
        </section>

        <section class="contact" id="contact">
            <h1 class="fade-in">Contact Information</h1>
            <div class="contact-container">
                <div class="contact-info fade-in delay-1">
                    <h2>Get in Touch</h2>
                    <p>I'm genuinely excited about the opportunity to contribute to HENNGE's innovative work in cloud security and productivity solutions. With my strong technical background and passion for creating impactful solutions, I'm eager to bring my skills to your team. Please feel free to reach out—I'd welcome the chance to discuss how I can add value to HENNGE.</p>
                    
                    <div class="contact-details">
                        <p><i class="fas fa-envelope"></i> <a href="mailto:{{ data.contact.email }}">{{ data.contact.email }}</a></p>
                        <p><i class="fas fa-phone"></i> <a href="tel:{{ data.contact.phone }}">{{ data.contact.phone }}</a></p>
                        <p><i class="fas fa-map-marker-alt"></i> {{ data.contact.location }}</p>
                        <p><i class="fab fa-github"></i> <a href="{{ data.contact.github }}" target="_blank">GitHub Profile</a></p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <a href="#home" class="back-to-top" id="backToTop"><i class="fas fa-arrow-up"></i></a>

    <footer class="fade-in delay-2">
        <div class="social-links">
            <a href="{{ data.contact.github }}" target="_blank"><i class="fab fa-github"></i></a>
            <a href="mailto:{{ data.contact.email }}"><i class="fas fa-envelope"></i></a>
        </div>
        <p>{{ data.name }}. All rights reserved.</p>
    </footer>

    <script>
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Back to top button
        const backToTopButton = document.getElementById('backToTop');
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });

        // Animation on scroll
        const animateOnScroll = () => {
            const elements = document.querySelectorAll('.fade-in');
            elements.forEach(element => {
                const elementPosition = element.getBoundingClientRect().top;
                const screenPosition = window.innerHeight / 1.2;
                
                if (elementPosition < screenPosition) {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0)';
                }
            });
        };

        window.addEventListener('scroll', animateOnScroll);
        window.addEventListener('load', animateOnScroll);

        // Header shadow on scroll
        window.addEventListener('scroll', function() {
            const scrollPosition = window.scrollY;
            const header = document.querySelector('header');
            
            if (scrollPosition > 100) {
                header.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.3)';
            } else {
                header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
            }
        });

        // Initialize animations
        document.querySelectorAll('.fade-in').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        });
    </script>
</body>
</html>
    ''', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
