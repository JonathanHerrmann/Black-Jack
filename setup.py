from setuptools import setup, find_packages


requirements = open("requirements.txt").readlines()

setup(name="blackjack",
      version="0.0.1",
      author="JonathanHerrmann",
      author_email="jonathan.herrmannn@mobilityhouse.com",
      url="https://github.com/JonathanHerrmann/Black-Jack",
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      install_requires=requirements,
      entry_points={'console_scripts': ["blackjack.cli:main"],
                    }
      )