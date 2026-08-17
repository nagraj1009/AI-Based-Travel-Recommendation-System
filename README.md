# ✈️ AI-Based Travel Recommendation System

An AI-powered web application that helps users create personalized travel plans based on their source, destination, budget, travel duration, and travel style.

The system uses Google Gemini to generate personalized itineraries and provides useful travel resources such as flight, train, bus, and Google Maps search links. Users can also download their generated itinerary as a PDF.

---

## 🚀 Features

### 🔐 User Authentication
- User registration
- Secure login
- Logout functionality
- Password hashing using Flask-Bcrypt
- Protected dashboard and planner routes

### 🤖 AI-Powered Travel Planning
- Personalized itinerary generation using Google Gemini
- Destination-based travel recommendations
- Day-by-day travel itinerary
- Recommendations based on:
  - Destination
  - Budget
  - Number of days
  - Travel style

### 💰 Budget Planning
- Budget-aware itinerary generation
- Estimated accommodation expenses
- Food and beverage recommendations
- Transportation suggestions
- Activity and miscellaneous expense estimation
- Approximate total trip budget

### 🌦️ Travel Information
- Weather-related travel information
- Destination information
- Location-based travel recommendations

### 🌐 Travel Resources
- ✈️ Flight search
- 🚆 Train search
- 🚌 Bus search
- 📍 Google Maps destination search

### 📄 PDF Export
- Generate a downloadable PDF itinerary
- Includes the generated travel plan and trip information

### 👤 Personalized Dashboard
- User-specific dashboard
- Personalized welcome message
- Travel planning interface
- Easy access to the AI Planner

### 🎨 Modern Web Interface
- Responsive interface
- Modern dark-themed design
- Destination-focused visuals
- Simple and user-friendly navigation

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-Bcrypt

### Artificial Intelligence
- Google Gemini API

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- SQLite

### External Services
- Google Gemini
- Weather Service
- Google Maps
- Google Travel / Search

### PDF Generation
- ReportLab

### Environment Configuration
- python-dotenv

---

## 📁 Project Structure

```text
AI-Based-Travel-Recommendation-System/
│
├── auth/
│   ├── decorators.py
│   ├── forms.py
│   ├── routes.py
│   └── utils.py
│
├── database/
│   ├── db.py
│   └── schema.sql
│
├── services/
│   ├── gemini_service.py
│   ├── itinerary_service.py
│   ├── location_service.py
│   ├── pdf_service.py
│   └── weather_service.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── videos/
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── home.html
│   ├── login.html
│   ├── planner.html
│   └── register.html
│
├── exports/
│
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
User
  │
  ▼
Registration / Login
  │
  ▼
Personalized Dashboard
  │
  ▼
AI Travel Planner
  │
  ├── Source
  ├── Destination
  ├── Budget
  ├── Duration
  └── Travel Style
  │
  ▼
Google Gemini AI
  │
  ▼
Personalized Itinerary
  │
  ├── Daily Activities
  ├── Hotel Recommendation
  ├── Food Recommendation
  ├── Transportation
  └── Budget Breakdown
  │
  ▼
Travel Resources
  │
  ├── Flights
  ├── Trains
  ├── Buses
  └── Google Maps
  │
  ▼
Download PDF