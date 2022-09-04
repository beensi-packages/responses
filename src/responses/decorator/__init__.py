from functools import wraps
from responses import exception


def clean_response(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        rsp = {}
        try:
            rsp = await func(*args, **kwargs)
        except Exception as exp:
            rsp = exception(exp.args[0])
        finally:
            return rsp

    return wrapper
