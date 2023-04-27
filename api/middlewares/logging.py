import logging
from fastapi import Request

logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s %(message)s")


async def log_requests(request: Request, call_next):
    """Log incoming requests and outgoing response's codes."""
    logging.info(f"{request.method} {request.url}")

    response = await call_next(request)

    logging.info(f"Response status code: {response.status_code}")

    return response
