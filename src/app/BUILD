python_requirements(name="deps__app")

pex_binary(
    name="app",
    entry_point="main.py",
    restartable=True,
    dependencies=[
        ":deps__app",
    ],
)

python_sources(
        name="app0",
)
