def log_function(func):
        def wrapper(*args, **kwargs):
                    logger.info("Calling function {} with arguments {}".format(func.__name__, args))
                            result = func(*args, **kwargs)
                                    logger.info("Function {} returned {}".format(func.__name__, result))
                                            return result
                                            return wrapper

                                        @log_function
                                        def factorial(n):
                                                if n == 0:
                                                            return 1
                                                            else:
                                                                        return n * factorial(n - 1)

                                                                    print(factorial(5))

# Decorators: Decorators are a powerful way to modify the behavior of functions. They can be used to add logging, caching, or other functionality to functions without having to modify the original code. For example, the following code defines a decorator that logs the arguments and return value of a function:
