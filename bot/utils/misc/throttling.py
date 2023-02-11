def rate_limit(limit: int, key=None):
    """
    Decorator for configuring rate limit and key in different functions.

    :param limit:
    :param key:
    :return:
    """

    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)  # noqa: ignore B010
        if key:
            setattr(func, "throttling_key", key)  # noqa: ignore B010
        return func

    return decorator
