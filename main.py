from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import os

# Email configuration


app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=465,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
)

# ✅ FINAL CORS FIX (live frontend + localhost)
app.add_middleware(
    CORSMiddleware,
  allow_origins=[
    "https://charan-portfolio-q59i.vercel.app",
    "https://charan-portfolio-q59i-gcpdq3e9j-charan-18-progs-projects.vercel.app",
    "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Model ----------
class Contact(BaseModel):
    name: str
    email: str
    message: str


# ---------- Home Route ----------
@app.get("/")
def home():
    return {"message": "Hello Charan"}


# ---------- Projects API ----------
@app.get("/projects")
def get_projects():
    return [
        {
            "id": 1,
            "title": "Portfolio Website",
            "description": "A full-stack portfolio built using React and FastAPI.",
            "details": "This project includes a responsive UI, a contact form, and a project details pop-up powered by a FastAPI backend.",
            "technologies": "React, FastAPI, MySQL",
            "github": "https://github.com/",
            "live": "#"
        },
        {
            "id": 2,
            "title": "Face Emotion Recognition",
            "description": "AI based project that detects human emotions using camera.",
            "details": "The app captures video input, processes faces with OpenCV, and classifies emotions using a trained ML model.",
            "technologies": "Python, OpenCV, Machine Learning",
            "github": "https://github.com/",
            "live": "#"
        },
        {
            "id": 3,
            "title": "EduPortal",
            "description": "A modern education portal built with React and FastAPI.",
            "details": "EduPortal provides course management, student dashboards, and a fast backend API for secure data access using Python and FastAPI.",
            "technologies": "React, FastAPI, Python",
            "github": "https://github.com/",
            "live": "#"
        },
        {
            "id": 4,
            "title": "Student Mental Health Analysis",
            "description": "A machine learning system that analyzes and predicts student mental health.",
            "details": "This project uses ML models to identify patterns in student data and deliver early mental health predictions and insights.",
            "technologies": "Python, Machine Learning, Data Analysis",
            "github": "https://github.com/",
            "live": "#"
        }
    ]


# ---------- Contact API ----------
# ---------- Contact API ----------
@app.post("/contact")
async def save_contact(contact: Contact):

    message = MessageSchema(
        subject="New Portfolio Contact Form Message",
        recipients=["muraricharan2@gmail.com"],
        body=f"""
Name: {contact.name}

Email: {contact.email}

Message:
{contact.message}
""",
        subtype="plain",
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return {"message": "Message received successfully"}