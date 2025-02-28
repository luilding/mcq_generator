from openai import OpenAI
from dotenv import load_dotenv
import os



load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def learning_objective_prompt(learning_objective):
    return f"""We have been given this learning objective {learning_objective}
    Please provide a multiple choice question with 4 answers regarding that topic, with one being the right answer"""

#Single learning objective
#Output formatted in human readable form
#Question suited to higher education
#Generator has to provide an api 
#Only one right answer


def generate_mcq(learning_objective):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": learning_objective_prompt(learning_objective)}
        ]
    )

    query = response.choices[0].message.content

    print(query)

question = input("Please enter your learning objective:")

generate_mcq(question)