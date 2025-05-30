from test_pypi_example import square


def test_function():
    for i in [1, 2, 3, 2, 10, 123, 1.4, 3.2, 0]:
        assert square(i) == i ** 2