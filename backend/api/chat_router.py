from fastapi import APIRouter
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.get("/get-chat-response")
def chat_response( chat_input:str ):
    client = genai.Client()

    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=chat_input
    )

    print(interaction.output_text)
    

    return interaction.output_text 
