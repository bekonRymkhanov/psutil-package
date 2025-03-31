from setuptools import setup, find_packages

setup(
    name="snapshot",
    version="1.0.0",
    author="Bekarys Rymkhnaov",
    author_email="b_rymkhanov@kbtu.kz",
    description="A tool to monitor CPU, memory, and processes.",
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "snapshot=snapshot.snapshot:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
