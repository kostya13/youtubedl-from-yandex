from distutils.core import setup

setup(name='youtubedl-from-yandex',
      version='1.0',
      description='Download video from youtube',
      author='Konstantin Ilyashenko',
      author_email='kx13@ya.ru',
      py_modules = ['yandexmail'],
      entry_points={
          'console_scripts': [
              'yandex-youtube=yandexmail:main']})
