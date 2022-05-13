python_requirement(
    name="dep__tap_facebook",
    requirements=["tap_facebook@ git+https://github.com/singer-io/tap-facebook.git@3318ad972a4c0df7b5f1c8bd57b942d5f6b39bf4"],
)

pex_binary(
    name="pex__tap_facebook",
    entry_point="tap_facebook:main",
    dependencies=[":dep__tap_facebook"],
)
