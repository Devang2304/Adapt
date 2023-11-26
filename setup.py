from setuptools import setup

setup(
    name='Adapt', 
    version='0.1.0',  
    description='A versatile CLI tool for various conversions and tasks',
    url='',
    author='Devang Vartak',
    author_email='devangvartak2304@gmail.com',
    packages=['Adapt'], 
    install_requires=['docx2pdf', 'pdf2docx', 'pytube', 'youtube_transcript_api', 'gtts', 'pyfiglet'],
    entry_points={
        'console_scripts': [
            'Adapt=Adapt:main'
        ]
    },
)