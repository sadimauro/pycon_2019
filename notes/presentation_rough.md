About the Conference
====================

Produced by the nonprofit Python Software Foundation (PSF).

Keynotes:
* Russell Keith-Magee, member of django (Python web framework) core team, and owner? of beeware.org.  "What is Python's Black Swan?"
* Sha Wallace-Stepter.  Python and OS is power.  Inclusion is love.
* Jessica McKellar.  Our criminal jusdtice system is horrible, hella racist, wildly ineffective.  What can we do to help as programmers?

In addition to talks (Fri-Sun): lightning talks (Fri-Sun), tutorials (Wed-Thu), posters (Sun), job fair (Sun), Education Summit (Thu; how to bring coding literacy to wide audiences).


General Impressions of the Conference
=====================================

Lots on diversity, accessibility and inclusion.  Gender-neutral bathrooms, mothers' rooms, quiet room, trained incident responders, pac-man rule, hallway track, etc.  More on [this site](https://us.pycon.org/2019/about/code-of-conduct/).

Lots on pushing for better treatment of Python developers.  "We need sponsors and donors", "volunteering on weekends can't be the way we push Python forward", "Python needs an R&D division".  Dealing with the open-source community, esp folks that feel entitled to FOSS, is very draining.  Leads to burnout, mental health issues.


Useful tidbits
==============

Decorators are neat.  See examples in decorators.py.  Also see dclasses.py for the `@dataclasses.dataclass` decorator. 

Mocking is a thing.  See example code.

Floats act peculiarly, but their behavior mostly makes sense if you think about how they're stored internally.

There are very many (too many?) ways to test.  See code for examples of unittest, unittest mocking, and pytest.  I've also used doctest.

Linters and formatters make your code better:
* linters: source code analysis.  They suggest changes by finding e.g. unused and undefined variables, variables with names not conforming to PEP 8, etc.  In Python, these include 
** flake8 (8 for PEP8, the Python style guide)
** pylint
** mypy, which performs static type checking, which is most useful if you've included type annotations
* (auto-)formatters: reformat code for readability.  In Python, black is one often mentioned; black does auto-formatting in a deterministic way, and without changing the code's AST representation.
See examples of black (auto-formatter).


Less Useful Tidbits
===================

There is new Python governance:  before Guido was BDFL; now, a five-member steering council share that responsibility.

virtualenv, tox, nox, other tools are popular ones to initialize various virtual environments for checking your package installs and testing.

snappycode.org is a neat drag-and-drop Python code 'teacher' for K-5.


Talks I Attended
================

Keynotes
A Snake in the Bits: Security Automation with Python
Migrating Pinterest from Python2 to Python3
Mocking and Patching Pitfalls
Everything at Once: Python's Many Concurrency Models
Maintaining a Python Project When It's Not Your Job
Scraping a Million Pokemon Battles: Distributed Systems By Example
Floats are Friends
PEP 572: The Walrus Operator
Statisical Profiling (and other fun with the sys module)
Exceptional Exceptions - How to properly raise, handle and create them
Getting Started with Deep Learning


Find out more
=============

[About the conference](https://us.pycon.org/2019/about/)

[List of talks](https://us.pycon.org/2019/schedule/talks/)

[PyCon 2019 YouTube channel](https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ/videos) containing full video/audio of many (all?) presentations
