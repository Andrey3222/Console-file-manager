import time


def limit_requests(func):
    def real_limiter(*args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(1)
        return result
    return real_limiter

@limit_requests
def get_something_from_api():
    return 'Hello there!'

res = get_something_from_api()
print(res)