from functools import wraps
from responses import exception


def clean_response(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        rsp = {}
        try:
            if 'logger' in kwargs and 'request_url' in kwargs:
                kwargs['logger'].info(f"Start requesting \'{kwargs['request_url']}\'.")
            rsp = await func(*args, **kwargs)
        except Exception as exp:
            if 'logger' in kwargs:
                kwargs['logger'].error(exp.args[0])
            rsp = exception(exp.args[0])
        finally:
            if 'logger' in kwargs and 'request_url' in kwargs:
                kwargs['logger'].info(f"End of request \'{kwargs['request_url']}\'.")
            return rsp

    return wrapper
