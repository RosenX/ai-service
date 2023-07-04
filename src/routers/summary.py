from fastapi import APIRouter, Depends
from models import ServiceResponse, ChatSummaryRequest,  TaskType
from base import CustomException, ErrorType
from models import Config
from ai import LLMFactory

router = APIRouter()


@router.post("/summary/chat", response_model=ServiceResponse)
async def summary(request: ChatSummaryRequest, config: Config = Depends()):
    llm_result = LLMFactory.create(config).summary(
        request.llm_input, request.llm_config
    )

    return ServiceResponse(
        message="Success",
        data=llm_result
    )
