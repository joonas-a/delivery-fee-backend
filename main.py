from fastapi import FastAPI, HTTPException

from utils import fee_calculator, validate_input, DeliveryDetails

app = FastAPI()


@app.post("/api/calculate_fee")
async def calculate_fee(body: DeliveryDetails):
    error_msg = validate_input(body)
    if error_msg:
        raise HTTPException(status_code=400, detail=error_msg)
    fee = fee_calculator(body)
    return {"delivery_fee": fee}
