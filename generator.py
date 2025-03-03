from openai import OpenAI
from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#Get env vars
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

#Creation of user prompt specific to generating MCQ questions
def learning_objective_prompt(learning_objective):
    return f"""
    You will be provided with a single learning objective for any STEM topic.

    We have been given this learning objective: {learning_objective}
    Please provide a multiple choice question with 4 answers regarding that topic, with ONLY ONE ANSWER being the right answer.
    
    Ensure the questions are suitable to students in Higher Education, and are in English.
   
    IMPORTANT FORMATTING INSTRUCTIONS:
    - Use <strong> or <b> tags for bold text (not ** markdown)
    - Use <sub> tags for subscripts in chemical formulas (e.g., H<sub>2</sub>O)
    - Use <sup> tags for superscripts (e.g., E=mc<sup>2</sup>)
    - Use <br> for line breaks
    - Format the question with <strong>Question:</strong> at the beginning
    - Format the correct answer with <strong>Correct Answer:</strong> at the end
    """

#Sending the learning objective and user prompt to OpenAI's API
def generate_mcq(learning_objective):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": learning_objective_prompt(learning_objective)}
        ]
    )

    query = response.choices[0].message.content

    query = query.replace('\n', '<br>')
    print(query)
    return query

#Creating API endpoint for receiving learning objectives via POST requests
@app.route('/', methods=['POST'])
def api_generate_question():
    #Getting learning objective data from JSON
    data = request.get_json()
    learning_objective = data.get("learning_objective", "")

    #Return an error if no learning objective is provided
    if not learning_objective:
        return jsonify({"error": "Missing learning objective"}), 400
    
    #Generate and return the MCQ 
    question = generate_mcq(learning_objective)
    return jsonify({"question": question})


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
