def double_to_single_callable(application):
    """
    Transforms a double-callable ASGI application into a single-callable one.
    """

    async def new_application(scope, receive, send):
        instance = application(scope)
        return await instance(receive, send)

    return new_application


def guarantee_single_callable(application):
    """
    Takes either a single- or double-callable application and always returns it
    in single-callable style. Use this to add backwards compatibility for ASGI
    2.0 applications to your server/test harness/etc.
    """
    if is_double_callable(application):
        application = double_to_single_callable(application)
    return application
