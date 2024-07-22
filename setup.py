from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(include=['libs.transcript_processor', 'apps']),
    install_requires=[
        'whisper @ git+https://github.com/openai/whisper.git',
    ],
    entry_points={
        'console_scripts': [
            'whisper-process=apps.app1.app:main',
            'record-mic=libs.audio_recorder.audio_recorder:main',
        ],
    },
    author='Mat Silva',
    author_email='matsilva@hey.com',
    description='Services for apps that need audio parsing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/matsilva/my_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
