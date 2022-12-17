from setuptools import setup, find_packages

setup (
        name = "p0verty",
        version = '0.1.0',
        packages = find_packages('.'),
        install_requires = [
            "discord",
            "os",
            "datetime",
            "random",
        ]
)
