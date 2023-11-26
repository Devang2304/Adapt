from setuptools import setup,find_packages

setup(
    name='Adapt', 
    version='0.1.0',  
    description='A versatile CLI tool for various conversions and tasks',
    url='https://github.com/Devang2304/Adapt',
    author='Devang Vartak',
    author_email='devangvartak2304@gmail.com',
    packages=find_packages(), 
    install_requires=['docx2pdf', 'pdf2docx', 'pytube', 'youtube_transcript_api', 'gtts', 'pyfiglet','wheel'],
    entry_points={
        'console_scripts': [
            'Adapt=Adapt:main'
        ]
    },
)
