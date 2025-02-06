import nox

py_versions = ["3.10", "3.11", "3.12"]


@nox.session(python=py_versions)
def tests(session):
    session.run("pytest -v --durations=0 --cov --cov-report=xml")
