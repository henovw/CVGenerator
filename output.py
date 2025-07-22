from google import genai
from scrape import jobInfo
from google.genai import types

API_KEY = "AIzaSyCRoG0bdEkpUSEWcA2Udur73WvNNVMnJQI"

def genResp(job, resume):
    client = genai.Client(api_key = API_KEY)
    
    resfull = client.files.upload(file = resume)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            resfull,
            f"Given the attached resume, generate a shorter cover letter if you were applying to a job with this description: {job.jobDescription} and the company description of:{job.companyDescription}"            
        ]
    )
    return response.text