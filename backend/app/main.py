from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Sale(BaseModel):
    model: str = None
    volume: int = 0 

sales = []

@app.get("/")
async def root():
    return {"message": "Sales Dashboard API"}

@app.post("/sales")
def create_sale(sale: Sale):
    sales.append(sale)
    return sale

@app.get("/sales")
def list_sales(limit: int = 10):
    return sales[0:limit]

@app.get("/sales/{sales_id}")
def get_sale(sales_id: int) -> Sale:
    if sales_id < len(sales):
        return sales[sales_id]
    else:
        raise HTTPException(status_code=404, detail=f"Sales {sales_id} not found")