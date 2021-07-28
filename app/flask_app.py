from flask import Flask
import functools
import os
import redis


flask_app = Flask(__name__)


r = redis.Redis(host='redis', port=6379, db=0)


@functools.lru_cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



@flask_app.route('/')
def index():
    return 'Привет! Для рассчета числа нужно в поисковой строке после адреса сервера написать /fibo/<число каторое Фибоначчи>'


@flask_app.route('/fibo/<int:n>')
def fib(n):
    a = fibonacci(n)
    if r.exists(n) == 1:
        return str(a) + ' ' + 'this is in base'
    else:
        r.set(n, a)
        return str(a)


if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0')
