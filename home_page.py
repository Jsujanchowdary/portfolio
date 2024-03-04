import os
import numpy as np
import pandas as pd
import streamlit as st 
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import base64

st.set_page_config(layout='wide')
with open("../portfolio/style/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(r"../portfolio/images/sujan-updated.jpg", "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()  

    # PDF CV file
with open(r"../portfolio/assets/JUJJAVARAPU_SUJAN_CHOWDARY_20bci7294_RESUME.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()      


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder1 = "https://lottie.host/399392d0-1618-4c55-ba7b-85bed624dc0e/HnWfEiXtWH.json"
lottie_coder2 = "https://lottie.host/3ddb6ce9-ef1c-4ce8-93fc-cafe45eb38a3/pebaVKGGOu.json"
lottie_coder3 = "https://lottie.host/3785216c-ebad-4800-9446-de4f845b7387/yZPoCBmO6b.json"
lottie_coder4 = "https://lottie.host/6ac7c01c-d7cc-4cc2-a442-7d207d8b9ebc/4UEYPvUuXz.json"
lottie_coder5 = "https://lottie.host/852fb661-941b-4d79-a612-e2ab7818c1a9/byMsBSfYvg.json"
lottie_coder6 = "https://lottie.host/542e9962-264f-47cc-bff2-6bccb2d0f205/HhsCmsGjmK.json"

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About','Education', 'Projects','Achievement', 'Contact'],
        icons=['person','bi bi-book', 'code-slash','bi bi-award', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':
    st.title("Hello!!!!👋 I am ")
    
    # Adding animation to the text "JUJJAVARAPU SUJAN CHOWDARY"
    st.markdown("""
    <style>
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-30px);
            }
            60% {
                transform: translateY(-15px);
            }
        }
        .bounce {
            animation: bounce 2s infinite;
        }
    </style>
    <h1 class="bounce" style='text-align: center; color: red;'>JUJJAVARAPU SUJAN CHOWDARY</h1>
    """, unsafe_allow_html=True)
    
    # Adding animation to the text "VIT AMARAVATI '24, B.Tech Student"
    st.markdown("""
    <style>
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-30px);
            }
            60% {
                transform: translateY(-15px);
            }
        }
        .bounce {
            animation: bounce 2s infinite;
        }
        
    </style>
    <h3 class="bounce" style='text-align: center;'>Computer Science Student, VIT AMARAVATI '24, B.Tech Student</h3>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.title(" ")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("")
            st.write('''Hello! I am a highly motivated fourth-year student pursuing a degree in Computer Science and Engineering with a focused specialization in Artificial Intelligence. My academic journey has equipped me with a strong foundation in computer science principles, and I have honed my skills through hands-on experience in the realms of data science and machine learning.''')
            st.write("Passionate about the limitless possibilities that artificial intelligence offers, I am driven by a commitment to pushing the boundaries of this transformative field. My academic pursuits have not only provided me with theoretical knowledge but have also allowed me to apply these concepts to real-world scenarios. I thrive on the challenges that AI presents and am enthusiastic about leveraging my skills to develop innovative solutions to complex problems.")
            st.download_button(
            label="📄 Download my RESUME",
            data=pdf_bytes,
            file_name="JUJJAVARAPU_SUJAN_resume.pdf",
            mime="application/pdf",
        )
        with col2:
            st.write(f"""
            <div class="container">
                <div class="box">
                    <div class="spin-container">
                        <div class="shape">
                            <div class="bd">
                                <img src="{img}" alt="Enric Domingo" width="500" height="500">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            """, 
            unsafe_allow_html=True)
            # st.write(f"""
            # <div style="display: flex; justify-content: center;">
            # <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
            # </div>
            # """, unsafe_allow_html=True)
        st.write("---")

        col3,col4 = st.columns(2)
        with col4:
            st.subheader('''Skills: 
                     
                     - Tech Skills:
                     - Java ♨️
                     - Python 🐍
                     - SQL 🛢
                     - Machine Learning 🤖
                     - Natural Language Processing 👾
                     - MongoDB 🛢
                     - Pandas 
                     - Classification 
                     - Tensorflow
                     - Pytorch
                     - Keras
                     - SciKit Learn''')
            
            st_lottie(lottie_coder2)
        with col3:
            st_lottie(lottie_coder1)
            st.subheader('''Skills:
                         - Soft Skills:
                         - Time Management ⏳
                         - Critical Thinking 🤔
                         - Organizational Skills 🗂️
                         - Presentation Skills 👨🏻‍🏫
                         - Teamwork and Collaboration 🤝
                         - Problem Solving 🧩
                         - Attention to Detail 🔎
                         - Leadership 🧑🏻‍💼
                         - Communication skill 🗣''')

        col34, col35 = st.columns(2)

        with col34:
                st.subheader("Club Activities")
                st.write("Computer Society of India - VIT 🖥️")	
                st.write("Outreach Department Co-Lead 🤝 2020 - 2021")
                st.write("Fostering intercollegiate connections and collaboration to expand the organization’s reach and impact.🌐")
                social_icons_data = {
                # Platform: [URL, Icon]
                "LinkedIn": ["https://www.linkedin.com/company/csivitap/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
                "GitHub": ["https://github.com/CSI-VIT-AP", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
                "Instagram": ["https://www.instagram.com/p/CTppnbrBeoA/?igsh=M29lanJkNXJ2NWFp", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"],
                }
        
                social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]
                st.write(f"""
                <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                    {''.join(social_icons_html)}
                </div>""", 
                unsafe_allow_html=True)
        with col35:
                st.subheader(" ")
                st.image(r"../portfolio/images/csi_logo.jpeg")
         
            
if selected == 'Education':
    
    st.markdown("""<h1 class="bounce" style='text-align: center; color: white;'>EDUCATION & CERTIFICATIONS</h1>""",unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        st.image(r"../portfolio/images/vitap-logo.png")
        st.write(" ")
        
        st.markdown("""
        🎓 Bachelor of Technology(B.Tech)   (SEP 2020 - Present)
        - Computer Science and Engineering Specialization in Artificial Intelligence (CSE AI) 
        - Vellore Institute of Technology (VIT)
        - CGPA: 8.54/10.0""")
    with col6:
        st.image(r"../portfolio/images/sri-logo.png")
        st.write(" ")
        st.markdown("""
        🏫 Higher secondary education or Intermediate(XII)   (Feb 2018 - Mar 2020)
        - MPC
        - BIEAP: Andhra Pradesh Board of Intermediate Education             
        - Sri Chaitanya junior college
        - CGPA: 8.50/10.0""")

    st.write("---")

    col7, col8 = st.columns(2)
    with col7:
        st.subheader(" ")
        st.subheader("Certifications")
        st.markdown("""
                    Oracle Cloud Infrastructure 2023 Certified Foundations Associate
                    - Oracle University
                    - July 15, 2023
                    - Certification ID: 303508312OCIF2023CA
                    """)
        st.link_button("Certificate","https://drive.google.com/file/d/1RDV8ASK5CzRiqobdnyJHQsdlToZzjnym/view?usp=sharing")
        st.subheader(" ")
        st.markdown("""
                    AWS Academy Graduate - AWS Academy Cloud Foundations
                    - AWS Academy
                    - Issued on: June 01, 2023
                    - Digital Badge: https://www.credly.com/go/LHVmtHIY
                    """)
        st.link_button("Certificate","https://drive.google.com/file/d/1oYo0--h0GoUWZwXEs7Iy47Qo2j1Ddp85/view?usp=sharing")
        st.subheader(" ")
        st.markdown("""
                    Modern Application Development(Java Spring Boot)
                    - VMware IT Academy
                    - Issued on: July 23, 2023
                    - Certification ID: Ext-2023-61730
                    """)
        st.link_button("certificate","https://drive.google.com/file/d/1s9A-cKJ4Qe4DmtL4HD9j2PV0na_vDLWH/view?usp=sharing")
    
    with col8:
        st.lottie(lottie_coder4, height=600, width=600)

if selected == 'Projects':
    

    st.markdown("""<h1 class="bounce" style='text-align: center; color: white;'>PROJECTS</h1>""",unsafe_allow_html=True)
    col9, col10 = st.columns(2)

    with col9:
        st.subheader(" ")
        st.subheader("AI ATTORNEY USING LANGCHAIN")
        st.write("Natural language processing (NLP) and machine learning components are integrated into Streamlit, an AI-powered document chat system. Users can interact with the system through interactive conversations where they can discuss uploaded PDF documents or query a language model that has already been trained. In order to enable intelligent responses and document understanding, the application makes use of OpenAI's language models for text embeddings.")
        st.write("When users upload PDFs, the system reads the files and extracts the text. After that, it uses OpenAI's API to create embeddings and breaks the text up into digestible chunks. Because these embeddings are kept in a vector store, retrieving them quickly during user interactions is made possible. An OpenAI chat model handles the conversational part, and a conversation buffer memory keeps track of previous conversations for context-aware replies. Streamlit was used in the design of the user interface to provide a seamless experience.")
        st.link_button("Project Source Code","https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain")

    with col10:
        st.image(r"../portfolio/images/project_image_1_ai.png",channels="RGB")

    st.write("---")

    col11, col12 = st.columns(2)

    with col11:
        st.subheader(" ")
        st.image(r"../portfolio/images/porject_2.jpg")
    
    with col12:
        st.subheader(" ")
        st.subheader("Voice Assistant with OpenAI GPT-3.5 and Speech Recognition")
        st.write("This project implements a voice assistant using OpenAI's GPT-3.5 language model and speech recognition. The assistant is capable of listening to user input, generating responses using GPT-3.5, and speaking back the responses.")
        st.markdown('''
                    Features: 
                    - Speech Recognition: Utilizes the `sounddevice` library to record and transcribe user input.
                    - Chat Interaction: Communicates with the `OpenAI GPT-3.5` model for generating contextual responses.
                    - Text-to-Speech: Employs `pyttsx3` for converting the assistant's responses into speech.
                    ''')
        st.link_button("Project Source Code","https://github.com/Jsujanchowdary/Voice-Assistant-with-OpenAI-GPT-3.5-and-Speech-Recognition")

    st.write("---")

    col13, col14 = st.columns(2)

    with col13:
        st.subheader(" ")
        st.subheader("Instagram Account Classifier")
        st.write("""This project aims to classify Instagram accounts into two categories: "Individual" or "Brand/Organization".""")
        st.markdown("""
                    Profile Data Retrieval
                    - The `fetch_instagram_data`(username) function initializes an Instaloader instance and retrieves an Instagram user's profile data, including information about their posts, followers, and following.
                    
                    Profile Picture Analysis
                    - `The analyze_profile_picture`(profile) function starts by obtaining the URL of the user's profile picture using the `get_profile_pic_url()` method. It then sends an HTTP request to retrieve the picture data. If successful, the image is decoded using OpenCV, grayscaled, and analyzed for faces using a Haar Cascade classifier.
                    """)
        st.link_button("Project Source Code","https://github.com/Jsujanchowdary/classify-if-the-account-belongs-to-an-individual-user-or-a-brand-organization.") 

    with col14:
        st.image(r"../portfolio/images/project_3.jpg")

    st.write("---")

    col15, col16 = st.columns(2)

    with col15:
        st.image(r"../portfolio/images/project_4")
    
    with col16:
        st.subheader(" ")
        st.subheader("Lung Cancer Detection using Convolutional Neural Network and OpenAI")
        st.write("This project focuses on the development of a lung cancer detection system using Convolutional Neural Networks (CNN) and OpenAI. The goal is to build an image classification model that can identify lung cancer from histopathological images. Additionally, it integrates OpenAI's GPT-3 for generating image descriptions based on the predicted class labels.")
        st.write("Lung cancer is a major health concern globally, and early detection plays a crucial role in improving patient outcomes. Histopathological image analysis is a powerful tool in the early diagnosis of lung cancer. By developing a deep learning-based system, we aim to assist pathologists in identifying malignant tissue patterns more accurately and quickly.Utilizes state-of-the-art deep learning techniques for image classification. Leverages data augmentation to enhance model robustness. Integrates OpenAI's GPT-3 to generate detailed descriptions of image findings. Aims to improve the accuracy of lung cancer detection and provide interpretability through generated text descriptions.")
        st.link_button("Project Source Code","https://github.com/Jsujanchowdary/-Lung-Cancer-Detection-using-Convolutional-Neural-Network-and-Open-Ai")

    st.write("---")

    col17, col18 = st.columns(2)

    with col17:
        st.subheader(" ")
        st.subheader("KEYWORD EXTRATION USING NLTK")
        st.write("Keyword extraction is commonly used to extract key information from a series of paragraphs or documents. Keyword extraction is an automated method of extracting the most relevant words and phrases from text input. It is a text analysis method that involves automatically extracting the most important words and expressions from a page. Keyword Extraction with Python programming language. I will start by importing the necessary libraries and the dataset. preprocess our textual data. For this task.")
        st.write(" I will use the NLTK library in Python. Using the tf-idf weighting scheme, the keywords are the words with the highest TF-IDF score. For this task, I’ll first use the CountVectorizer method in Scikit-learn to create a vocabulary and generate the word count. to use the TfidfTransformer in Scikit-learn to calculate the reverse frequency of documents. the final step. In this step, I will create a function for the task of Keyword Extraction with Python by using the Tf-IDF vectorization")
        st.link_button("Project Source Code","https://github.com/Jsujanchowdary/KEYWORD-EXTRATION-USING-NLTK/tree/main")

    with col18:
        st.image(r"../portfolio/images/project_5.jpeg")
    st.write("---")

    col30, col31 = st.columns(2)

    with col30:
        st.image(r"../portfolio/images/project_6.png")
    
    with col31:
        st.subheader(" ")
        st.subheader("ANOMALY DETECTION IN TIME SERIES DATA OF NEW YORK CITY TAXI DEMAND")
        st.write("Finding anomalies in the New York City Taxi Demand dataset is the goal of this project. The NYC Taxi and Limousine Commission is the source of the dataset, which offers a detailed account of all taxi passengers combined into 30-minute blocks. The dataset is notable for having anomalies associated with significant occasions like the NYC Marathon, Thanksgiving, Christmas, New Year's Day, and a snowfall.")
        st.write("An essential component of data analysis is anomaly detection, which makes it possible to spot odd trends or occurrences that greatly depart from the norm. Understanding and spotting abnormalities in the context of taxi demand is crucial for maximizing resource allocation and service scheduling. In order to find anomalies in the taxi demand dataset, this project uses a machine learning technique called the Isolation Forest algorithm. The Isolation Forest works well in situations where anomalies are distinct and uncommon, and it is especially useful for finding outliers in large datasets.")
        st.link_button("Project Source Code","https://github.com/Jsujanchowdary/ANOMALY-DETECTION-IN-TIME-SERIES-DATA-OF-NEW-YORK-CITY-TAXI-DEMAND")
    st.write("---")

    col32, col33 = st.columns(2)

    with col32:
        st.subheader(" ")
        st.subheader("Twitter Sentiment Analysis Project")
        st.write("Twitter Sentiment Analysis is a data analytics project aimed at analyzing a dataset of tweets to determine the sentiment expressed in each tweet — whether it is positive, negative, or neutral. The project provides insights into public opinions, trends, and sentiments shared on Twitter, utilizing data analytics techniques.")
        st.write("Exploration of the dataset through descriptive statistics, visualization, and understanding of data types. Extensive data cleaning steps, including lowercasing, removing stop words, punctuations, URLs, and more. Tokenization, stemming, and lemmatization to prepare text data for modeling. Implementation of three models: Bernoulli Naive Bayes, Support Vector Machine (SVM), and Logistic Regression. Evaluation of each model using common metrics and visualization of ROC-AUC curves.")
        st.link_button("Project Source Code","https://github.com/Jsujanchowdary/Twitter-Sentiment-Analysis")

    with col33:
        st.image(r"../portfolio/images/project_7.jpg")
    st.write("---")

    col19, col20 = st.columns(2)

    with col19:
        st.lottie(lottie_coder5, height=600, width=600)

    with col20:
        st.title(" ")
        st.header(" ")
        st.title(" ")
        st.header(" ")
        st.title(" ")
        st.header(" ")
        st.write("Thank you for visiting! If you're interested in exploring more of my projects, you can find a variety of open-source contributions and personal endeavors on my GitHub profile. Dive into the world of coding, development, and innovation by checking out my repositories. Your feedback and contributions are always welcome! ")
        st.link_button("My Github 🌐","https://github.com/Jsujanchowdary")

if selected == 'Achievement':
    st.markdown("""<h1 class="bounce" style='text-align: center; color: white;'>ACHIEVEMENTS</h1>""",unsafe_allow_html=True)

    col21, col22 = st.columns(2)

    with col21:
        st.image(r"../portfolio/images/Engg Clinics Winter 2022-23 Merit Cert-2_page-0001.jpg")
        st.write("Certificate of Appreciation on Vellore Institute of Technology University Day")

    with col22:
        st.image(r"../portfolio/images/EC Winter Sem Merit Cert-6_page-0001.jpg")
        st.write("Certificate of Merit for securing One in the Top Ten among all Engineering Clinics at Vellore Institute of Technology")

    st.write("---")

    col23, col24 = st.columns(2)

    with col23:
        st.image(r"../portfolio/images/Certificate - SmartInternz_page-0001.jpg")
        st.write("""Certificate of Merit form SmartInternz for developed the project entitled "Hotel Management System" under the supervision of mentor and secured 30 out of 30 marks in the Grand Assessment.""")

    with col24:
        st.image(r"../portfolio/images/CHCS 1017-1-1.png")

    st.write("---")

    st.markdown("""<h1 class="bounce" style='text-align: center; color: white;'>GALLERY</h1>""",unsafe_allow_html=True)

    col25, col26, col27 = st.columns(3)

    with col25:
        st.image(r"../portfolio/images/KKK_1351.jpg")
        st.image(r"../portfolio/images/IMG-20230609-WA0018.jpg")

    with col26:
        st.image(r"../portfolio/images/KKK_1352.jpg")
        st.image(r"../portfolio/images/IMG20230609180701.jpg")

    with col27:
        st.image(r"../portfolio/images/KKK_1380.jpg")


if selected == "Contact":

    st.subheader("Current Location")

    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [16.4942796, 80.5007368],
    columns=['lat', 'lon'])

    st.map(df)

    col28, col29 = st.columns(2)

    with col28:
        st_lottie(lottie_coder6)



    with col29:
        st.header(":mailbox: Get In Touch With Me!")

        contact_form = """
        <form action="https://formsubmit.co/sujanchowdary2001@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")

        social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/j-sujan-chowdary-39027021b/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/Jsujanchowdary", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Instagram": ["https://www.instagram.com/jsujanchowdary/", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"],
        "Facebook": ["https://www.facebook.com/sujan.chowdary.129", "https://upload.wikimedia.org/wikipedia/commons/6/6c/Facebook_Logo_2023.png"]
        }

        social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]
        st.write(f"""
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            {''.join(social_icons_html)}
        </div>""", 
        unsafe_allow_html=True)


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>© 2024 "JUJJAVARAPU SUJAN CHOWDARY" All rights reserved. <a style='display: block; text-align: center;target="_blank">JUJJAVARAPU SUJAN CHOWDARY</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)





     
