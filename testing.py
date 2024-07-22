import os
import pandas as pd
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
import streamlit as st
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tts_pdf_reader_key.json"





def generate(pre_prompt,input_text,prompt_input):
  vertexai.init(project="gen-lang-client-0551214413", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-pro-001",
  )
  full_prompt = f"""{pre_prompt} {input_text} {prompt_input} Assistant: """
  responses = model.generate_content(
      [full_prompt],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )
  ans = """"""

  for response in responses:
    ans += response.text
    
  print(ans)
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
input_text = "ICICI BANK"
prompt_input = "...Generate a phrase showcasing the bank as a stock to invest for a 6-month range. Provide response to just this and nothing else."
generate(pre_prompt,input_text,prompt_input)

# # Initialize Vertex AI client
# aiplatform.init(project="gen-lang-client-0551214413", location="us-central1")

# # Define your model ID (make sure it matches your deployed model ID)
# model_id = "gemini-1.5-pro-001"

# # Define the prompt and other parameters
# pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
# prompt_input = '...Generate a phrase showcasing the bank as a stock to invest for a 6-month range. Provide response to just this and nothing else.'

# full_prompt = f"{pre_prompt} ICICI BANK {prompt_input} Assistant: "

# # Create a Vertex AI client
# client = aiplatform.gapic.PredictionServiceClient(client_options={"api_endpoint": "us-central1-aiplatform.googleapis.com"})

# # Set up the request
# endpoint = f"projects/gen-lang-client-0551214413/locations/us-central1/endpoints/{model_id}"
# instances = [{"content": full_prompt}]

# # Make the prediction request
# response = client.predict(endpoint=endpoint, instances=instances)

# # Extract the response
# full_response = response.predictions[0]['content']

# # Print the response
# print(full_response)
