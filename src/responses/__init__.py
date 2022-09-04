from typing import List
from messages import (
    ACCESS_TO_THIS_AREA_IS_PROHIBITED,
    PLEASE_DO_NOT_TRY_AGAIN,
    THERE_IS_NO_DATA_WITH_THIS_ID,
)


def msg(status: str, code: int, message: str):
    return {
        'status': status,
        'code': code,
        'message': message,
    }


def response(success: bool = True, status_code: int = 200, messages: List[dict] | None = None,
             data: dict | List[dict] | None = None, language='english'):
    return {
        'success': success,
        'status_code': status_code,
        'messages': messages,
        'data': data,
    }


def not_access():
    return response(
        success=False,
        status_code=403,
        messages=[
            ACCESS_TO_THIS_AREA_IS_PROHIBITED,
            PLEASE_DO_NOT_TRY_AGAIN,
        ],
    )


def ok():
    return response()


def exception(message):
    return response(
        success=False,
        status_code=500,
        messages=[{'status': 'exception', 'code': None, 'message': message}]
    )


def not_found():
    return response(
        success=False,
        status_code=404,
        messages=[
            THERE_IS_NO_DATA_WITH_THIS_ID,
        ]
    )
