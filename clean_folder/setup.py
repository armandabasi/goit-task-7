from setuptools import setup, find_namespace_packages


setup(name="clean",
      version="1.0",
      description="",
      url="https://github.com/armandabasi/goit-task-7.git",
      author="Tetiana Fedoryshena",
      author_email="514ftg@gmail.com",
      packages=find_namespace_packages(),
      entry_points = {
            "console_scripts": ['clean-folder=clean_folder.clean:main']
      }
      )