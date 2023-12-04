from setuptools import setup,find_packages

setup(
    name='SyncPulse', 
    version='2.9.0',  
    description='A versatile CLI tool for various conversions and tasks',
    url='https://github.com/Devang2304/SyncPulse',
    author='Devang Vartak',
    author_email='devangvartak2304@gmail.com',
    packages=['SyncPulse'], 
    install_requires=['docx2pdf', 'pdf2docx', 'pytube', 'youtube_transcript_api', 'gtts', 'pyfiglet','wheel'],
    entry_points={
        'console_scripts': [
            'SyncPulse = SyncPulse.__main__:main'
        ]
    },
)
