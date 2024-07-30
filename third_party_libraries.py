# We can install libraries using pip
# A package manager that is included with Python 3
# Pip is a standard package manager for Python, but isn't the only one
# One popular alternative is Anaconda - designed specifically for data science

# To install a package using pip, just enter "pip install" followed 
# by the name of the package in your command line like this: 
# pip install package_name. 
# This downloads and installs the package so that it's available to 
# import in your programs. Once installed, you can import third-party
# packages using the same syntax used to import from the standard 
# library.






# Example
# pip install pytz

from datetime import datetime  # Import the datetime class
import pytz  # Import the pytz library for time zones

# Define the UTC time zone
utc = pytz.utc
# Define the Kenya time zone
ke = pytz.timezone('Africa/Nairobi')

# Get the current time in UTC
now = datetime.now(tz=utc)
# Convert the UTC time to Kenya's time zone
ke_now = now.astimezone(ke)

# Print the current UTC time
print(now)
# Print the current time in Kenya
print(ke_now)






# Using a requirements.txt File
# Larger Python programs might depend on dozens of third party
# packages. 
# To make it easier to share these programs, programmers often list
# a project's dependencies in a file called requirements.txt.
# This is an example of a requirements.txt file.


# beautifulsoup4==4.5.1
# bs4==0.0.1
# pytz==2016.7
# requests==2.11.1


# Each line of the file includes the name of a package and its
# version number. The version number is optional, but it usually 
# should be included. Libraries can change subtly, or dramatically, 
# between versions, so it's important to use the same library 
# versions that the program's author used when they wrote the program.

# You can use pip to install all of a project's dependencies at
#  once by typing
# pip install -r requirements.txt
# in your command line.






# USEFUL THIRD-PARTY PACKAGES
# IPython - A better interactive Python interpreter
# requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
# Flask - a lightweight framework for making web applications and APIs.
# Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
# Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
# pytest - extends Python's builtin assertions and unittest module.
# PyYAML - For reading and writing YAML(opens in a new tab) files.
# NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
# pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
# Matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
# ggplot - Another 2D plotting library, based on R's ggplot2 library.
# Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
# pyglet - A cross-platform application framework intended for game development.
# Pygame - A set of Python modules designed for writing games.
# pytz - World Timezone Definitions for Python