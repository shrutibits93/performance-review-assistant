import openai
import os
from HRdata import roles_context, employee_context

os.environ["OPENAI_API_KEY"] = "Your Key"

def summary(messages):
    client = openai.OpenAI()
    system_message = {
            "role" : "system", "content": (f"""
             You are a performance review assistant providing review to employees of a tech company at the end of the quarter. The employee provids quarterly goals at the beginning of the quarter. 
             Your job is to review the employees performance throughout the quarter and provide a summary by the end of the quarter.
             Employee will provide status updates throughout the quarter.
             
             The roles and responsibilities of the employee as per HR definition are {roles_context}
             Extract employee details like past reviews from Employee details: {employee_context}
             
             Provide a summary in the below format:
             
             Summary of quarters performance:
             
             ...
             
             Next steps to get to the next level:
        
             
             If employee has not provided any updates in the quarter, provide a brief summary of what you think they
             might have done and request more details from the employee.
             FOLLOW_UP: Can you provide more details on your quarterly progress?
            
            """)
            }
    response = client.chat.completions.create(
        model="gpt-4o",
        messages = [system_message] + messages
    )

    return  response.choices[0].message.content


def extract_followup(response):
    if "FOLLOW_UP:" in response:
        return response.split("FOLLOW_UP:")[1].strip()
    return None


