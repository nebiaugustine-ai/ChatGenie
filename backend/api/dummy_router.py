from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def chat_endpoint():
    return "hello world"

@router.get("/get-sum")
def cal_sum(a:int, b:int):
    result = a+b
    return result