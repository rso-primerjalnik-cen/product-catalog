from fastapi import HTTPException
from requests import Response


def check_response_errors(response: Response):
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
