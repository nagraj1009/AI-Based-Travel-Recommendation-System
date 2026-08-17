import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_itinerary(
        source,
        destination,
        budget,
        days,
        style):

    prompt = f"""
Create a travel itinerary.

Source: {source}
Destination: {destination}
Budget: {budget}
Days: {days}
Travel Style: {style}

Return ONLY valid JSON.

Example:

{{
  "title":"Goa Adventure",
  "overview":"A beautiful trip to Goa",
  "days":[
    {{
      "day":"Day 1",
      "activities":[
        "Visit Beach",
        "Lunch",
        "Sunset Point"
      ]
    }}
  ],
  "hotel":"Hotel Name",
  "food":"Food Suggestions",
  "transport":"Transport Suggestions",
  "budget":"Budget Breakdown"
}}

No markdown.
No explanation.
Only JSON.
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    return json.loads(text)