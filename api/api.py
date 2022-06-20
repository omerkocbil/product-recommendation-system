from fastapi import APIRouter

from evaluation import recommend

api_router = APIRouter()

@api_router.get("/recommend/{product_id}")
def read_item(product_id: str):
    recommendations = recommend.recommend_products(product_id)
    
    return f"""{recommendations}"""