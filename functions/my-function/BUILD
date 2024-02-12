python_requirements(name="requirements")

python_sources(name="src", sources=["src/**/*.py"], dependencies=[":requirements"])

python_google_cloud_function(
    name="my_function_gcf",
    runtime="python311",
    handler="src/main.py:handler",
    type="http",
)
