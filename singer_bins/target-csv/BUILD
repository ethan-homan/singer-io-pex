python_requirement(
    name="dep__target_csv",
    requirements=["target-csv==0.2.2", "setuptools"],
)

pex_binary(
    name="bin",
    entry_point="target_csv:main",
    dependencies=[":dep__target_csv"],
)
