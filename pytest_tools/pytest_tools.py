import weakref


_registry = weakref.WeakKeyDictionary()


def parametrize(
    tests,
    **kwargs,
):
    def decorator(
        f,
    ):
        _registry[f] = (
            tests,
            kwargs,
        )

        return f

    return decorator


def pytest_generate_tests(
    metafunc,
):
    if metafunc.function in _registry:
        func_arg_list, kwargs = _registry[metafunc.function]
        arg_names = sorted(
            [
                arg_name
                for arg_name in func_arg_list[0].__dict__
                if arg_name != 'id'
            ],
        )
        metafunc.parametrize(
            arg_names,
            [
                [
                    getattr(arg, arg_name)
                    for arg_name in arg_names
                ]
                for arg in func_arg_list
            ],
            ids=[
                arg.id
                for arg in func_arg_list
            ],
            **kwargs,
        )


pytest_generate_tests.parametrize = parametrize
