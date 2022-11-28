=======================
=== Project Details ===
=======================

Project: Stateful Counter
Created By: Hayden Boshoff (github.com/haydenboshoff)


===========================
=== Project Description ===
===========================

This project is a simple attempt at a stateful counter, this program does store the value, so when you close the program and re-open it, the value will remain the same from when you closed it. The value is stored in a txt file, but I have accounted for instances in which someone would edit the file, so entering a value higher than 8 (numerical) characters, will automatically be formatted to a value that is valid. If you enter ASCII letters or symbols in the txt file the program will automatically detect that and set the value to 0 instead of crashing.


==================
=== How to use ===
==================

Just simply run the main.py file, if you do not have the text file it works with (value.txt), then it will automatically create it for you. Once the program is running you can use the buttons to increment, decrement or reset the value.


===============
=== License ===
===============

MIT License 
Copyright (c) 2022 Hayden Boshoff