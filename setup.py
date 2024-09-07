from setuptools import setup, find_packages

setup(
    name="audio-services",
    version="0.1.0",
    description="A package for various audio-related services and APIs.",
    author="Mat Silva",
    author_email="matsilva@hey.com",
    license="UNLICENSED",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["apps", "libs", "cmd"]),
    python_requires=">=3.12.4,<3.13",
    install_requires=["pyinstaller>=6.9.0,<7.0.0"],
    extras_require={
        "record": ["pyaudio>=0.2.14,<0.3.0", "pyobjc>=10.3.1,<10.4.0"],
        "transcribe": ["openai-whisper @ git+https://github.com/openai/whisper.git"],
        "dev": [
            "pytest>=8.3.1,<9.0.0",
            "pytest-cov>=5.0.0,<6.0.0",
            "flake8>=7.1.0,<8.0.0",
            "black>=24.4.2,<25.0.0",
            "pytest-watch>=4.2.0,<5.0.0",
        ],
    },
    entry_points={
        "console_scripts": ["transcribe=cmd.transcribe.transcribe:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
