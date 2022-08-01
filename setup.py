from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]


setup(
    name='Spotify2YoutubeAudio',
    version='1.0',
    description='An application that gets your Spotify songs and downloads the YoutubeMP3 version',
    author='Gerald Matolo',
    author_email='',
    keywords='flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
    