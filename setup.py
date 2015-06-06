#!/usr/bin/python2.7
"""Git_fake project"""

from seuptools import find_packages, setup

setup(name = 'gitfake',
	version = '0.1',
	descripiton = "Git_fake module.",
	long_description ="A module for faking git push.",
	platforms = ["Linux"],
	author = "Rahul Mishra",
	author_email = "priyrahulmishra@gmail.com",
	url= "https://github.com/Rahul91/gitfake",
	license = "None",
	packages = find_packages()
	)