from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.security import APIKeyHeader
from .auth import users
from ..services.stock_service import stock_service
from ..middlewares.throttling import limiter


router = APIRouter()
api_key_header = APIKeyHeader(name="Eureka-API-Key", auto_error=False)


@router.get("/stock/{symbol}")
@limiter.limit("5/minute")
def get_stock_info(request: Request, symbol: str, api_key: str = Depends(api_key_header)):
    """Get information for a stock.

    Args:
        request (Request): The incoming HTTP request.
        symbol (str): The stock symbol to retrieve information for.
        api_key (str, optional): The API key to use for authentication.

    Raises:
        HTTPException: If the API key is missing or invalid.

    Returns:
        dict: A dictionary with stock information.
    """
    if api_key is None:
        raise HTTPException(status_code=400, detail="API key required")

    for email, key in users.items():
        if key == api_key:
            try:
                return stock_service(symbol)
            except Exception as error:
                raise HTTPException(status_code=500, detail=f"Error on Data Requests {error}")

    raise HTTPException(status_code=401, detail="API Key invalid")
