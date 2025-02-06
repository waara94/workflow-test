import nox

# py_versions = ['3.11', '3.12']
py_versions = ["3.12"]


@nox.session(python=py_versions)
def tests(session):
    # session.run('uv', 'pip', 'sync', 'pyproject.toml', external=True)
    session.run("uv", "pip", "install", "pytest", "pytest-cov", external=True)
    session.run("pytest", "-v", "--durations=0", "--cov", "--cov-report=json")
