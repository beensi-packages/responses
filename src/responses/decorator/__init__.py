from functools import wraps
from responses import exception


def clean_response(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        rsp = {}
        try:
            kwargs['logger_func'].info('Start requesting.', kwargs['request'].url._url)

            rsp = await func(*args, **kwargs)
        except Exception as exp:
            if 'logger' in kwargs:
                kwargs['logger_func'].error(exp.args[0], kwargs['request'].url._url)
            rsp = exception(exp.args[0])
        finally:
            kwargs['logger_func'].info('End of request.', kwargs['request'].url._url)
            return rsp

    return wrapper
