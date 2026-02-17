import os
import json
import google.generativeai as genai
import PIL.Image as pi
from dotenv import load_dotenv

#load API KEY
load_dotenv()
Api_Key=os.getenv("Gemini_Api_key")

if not Api_Key:
    raise ValueError("can not find the api key, please check .env")

genai.configure(api_key=Api_Key)
# print("--- getting the list of availaable models ---")
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(f"available model's name: {m.name}")
# print("--------------------------")

#build the function calling tool
def calculate_tax_and_total(net_amount:float, tax_rate:float) -> dict:
    """
    you must to call this tool, when you need to calculate the total price inclusing tax and the specific tax amount on an invoice

    Args:
        net_amount: the net price which dosen't include tax
        tax_rate: the tax rate as a percentage decimal
    Returns:
           a dictionary includes the calculated tax amount and total amount.
    """
    print(f"/n[toolbox] -> AI is calling me! input arguments: net amount{net_amount}, tax rate{tax_rate}")
    tax_amount =round(net_amount * tax_rate, 2)
    total_amount = round(net_amount + tax_amount, 2)
    return {"tax_amount": tax_amount, "total_amount":total_amount}

#define the system command
system_prompt="""
You are an experienced finance agent.
1. Extract: net_amount and tax_rate.
2. MUST use 'calculate_tax_and_total' tool for calculation.
3. OUTPUT ONLY THE FINAL JSON. Do not include any conversational text.
"""


#instantiate the model objects 
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    system_instruction=system_prompt,
    tools=[calculate_tax_and_total],
    generation_config={
        "temperature": 0.0,
    }
)

#define the start-up function 
def start_agent(image_relative_path):
    img=pi.open(image_relative_path)
    chat=model.start_chat(enable_automatic_function_calling=True)
    response=chat.send_message([img, "please anaylize the invoice and ouput JSON"])
    print(response.text)

start_agent("external/invoice.jpg")



