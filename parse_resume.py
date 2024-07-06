import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_API_KEY'

prompt = """
You are a parsing assistant. Given a resume, convert its content into a structured JSON format with the following fields: 

- "name": (Full name of the individual)
- "contact_information": {
    "email": (Email address),
    "phone": (Phone number),
    "address": (Physical address)
  }
- "summary": (A brief summary or objective)
- "experience": [
    {
      "job_title": (Title of the job),
      "company": (Company name),
      "location": (Location of the company),
      "start_date": (Start date of the job),
      "end_date": (End date of the job or "Present" if currently employed),
      "responsibilities": (Brief description of responsibilities)
    }
  ]
- "education": [
    {
      "degree": (Degree obtained),
      "institution": (Name of the institution),
      "location": (Location of the institution),
      "start_date": (Start date of the education),
      "end_date": (End date of the education or "Present" if currently studying),
      "details": (Brief description of the course or any notable achievements)
    }
  ]
- "skills": [
    (List of skills)
  ]
- "certifications": [
    {
      "name": (Name of the certification),
      "institution": (Institution awarding the certification),
      "date": (Date of certification)
    }
  ]
- "projects": [
    {
      "name": (Name of the project),
      "description": (Brief description of the project),
      "technologies": (Technologies used in the project),
      "date": (Date or duration of the project)
    }
  ]
- "languages": [
    (Languages known)
  ]

Please parse the following resume into the above JSON format:

7004783254 
Sritika Choudhary
github.com/sritikachoudhary04
sritikachoudhary@gmail.com
Education
linkedin.com/in/sritikachoudhary 
SRM University
Bachelor of Technology in Computer Science
Cambrian Public School
CBSE(12th)
St.Anthony’s School
ICSE(10th)
Experience
2021–2025
CGPA : 9.2
2019–2021
Percentage : 92.8
2007–2019
Percentage : 90.2
HEC Ranchi
Machine Learning Intern
May 2023–June 2023
Ranchi, Jharkhand
∗ Gather and preprocess historical data on machinery usage, maintenance, and failures and train models using
cross-validation to fine-tune hyperparameters, ensuring robust evaluation with training and testing data splits.
∗ Engineer relevant features like usage hours, maintenance frequency, and operational conditions, and select suitable
machine learning models such as Random Forest or Neural Networks.
∗ Deploy the best model for real-time lifecycle predictions, and implement monitoring to track performance, retraining
periodically to address prediction drift.
Prasunet Company
Front End Developer Intern
July 2024–August 2024
Remote
∗ Create a responsive web page using HTML, CSS, and JavaScript that dynamically adjusts its layout for optimal viewing
across various devices and screen sizes. Implemented features such as flexible grids, media queries, and responsive images
to ensure a seamless user experience on desktops, tablets, and smartphones.
∗ Develop a responsive weather application using HTML, CSS, and JavaScript that displays real-time weather data fetched
from an API, adjusting its layout for different devices. Implemented features like geo location for local weather updates,
interactive weather icons, and media queries to ensure the app is user-friendly on desktops, tablets, and smartphones.
∗ Create a responsive stopwatch application using HTML, CSS, and JavaScript that features start, stop, and reset
functionalities.
Projects
Credit Card Fraud Detection | Python, Machine Learning, Deep Learning
January 2024
∗ Machine learning and deep learning techniques analyze transaction patterns to identify anomalies indicating potential
fraud.
∗ Big data analytics and real-time processing frameworks handle large data volumes and provide immediate responses to
suspicious activities.
∗ Behavioral analytics monitor deviations from normal user behavior to enhance fraud detection.
Inventory System for Blood Bank | DBMS, PHP
May 2024
∗ Design a relational database schema to store information about blood donors, blood types, inventory levels, and
transactions.
∗ Use PHP for server-side scripting to handle requests and interact with the database.
∗ Implement functionalities such as adding new donors, updating donor information, recording blood donations, and
updating inventory levels.
Invoice Generator | HTML,CSS
October 2023
∗ Creating an invoice generator in front-end web development typically involves using JavaScript for dynamic content
generation and HTML/CSS for structure and styling.
∗ Key considerations include ensuring the interface is intuitive for entering invoice details and implementing responsive
design for compatibility across devices.
Technical Skills
Languages: Python, PHP, CPP, HTML, CSS, JavaScript, SQL
Tools: MySQL, SQLite, PowerBi, PostgreSQL
Frameworks: Scikit-learn, TensorFlow, Pandas, Matpotlib, NumPy
Coursework
∗ Database Management Systems
∗ Operating Systems
∗ Object-Oriented Programming
∗ Data Structures
"""

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1500
)

print(response.choices[0].text.strip())
