from fastapi import APIRouter

import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))))
from evaluation import recommend

api_router = APIRouter()

@api_router.get("/recommend/{product_id}")
def read_item(product_id: str):
    recommendations = recommend.recommend_products(product_id)
    
    return f"""{recommendations}"""