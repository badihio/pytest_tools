registry = {}


def clear_parametrize(
    tests,
    **kwargs,
):
    def decorator(
        f,
    ):
        registry[f.__name__] = (
            tests,
            kwargs,
        )

        return f

    return decorator


def pytest_generate_tests(
    metafunc,
):
    func_name = metafunc.function.__name__
    if func_name in registry:
        funcarglist, kwargs = registry[func_name]
        argnames = sorted(
            [
                key
                for key in funcarglist[0].__dict__
                if key != 'id'
            ],
        )
        metafunc.parametrize(
            argnames,
            [
                [
                    getattr(funcargs, name)
                    for name in argnames
                ]
                for funcargs in funcarglist
            ],
            ids=[
                funcargs.id
                for funcargs in funcarglist
            ],
            **kwargs,
        )
