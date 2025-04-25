
from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import smtplib
from email.message import EmailMessage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit")
async def submit_form(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    grade: str = Form(...),
    school: str = Form(...),
    program: str = Form(...),
    motivation: str = Form("")
):
    message = EmailMessage()
    message['Subject'] = 'New RoboSZN Signup'
    message['From'] = 'yourappemail@gmail.com'
    message['To'] = 'roboszngrp@gmail.com'
    body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Grade: {grade}
    School: {school}
    Program: {program}
    Motivation: {motivation}
    """
    message.set_content(body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('yourappemail@gmail.com', 'your_app_password')
        server.send_message(message)
        server.quit()
    except Exception as e:
        print("Error:", e)
        return {"status": "error", "message": str(e)}

    return RedirectResponse(url="/thank-you.html", status_code=303)
