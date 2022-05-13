python_requirement(
    name="dep__tap_github",
    requirements=["tap_github@ git+https://github.com/singer-io/tap-github.git@3126c9dc125333451fff6004397c5bcb716c7b64"],
)

pex_binary(
    name="pex__tap_github",
    entry_point="tap_github:main",
    dependencies=[":dep__tap_github"],
)
