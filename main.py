from fastapi import FastAPI, Query,status
from fastapi.middleware.cors import CORSMiddleware
from functions import is_prime, is_perfect, classify_number, digit_sum,integer,get_fun_fact


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Enter an integer number")):
    try:
        
        num = int(number)
        
    except ValueError:
        return {
            "number": number,
            "error": True
        }
    return {
            "number": integer(num),
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": classify_number(num),
            "digit_sum": digit_sum(num),
            "fun_fact": get_fun_fact(num),
         }