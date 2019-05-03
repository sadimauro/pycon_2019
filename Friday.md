Welcome to PyCon
================

Speaker: Ernest Durbin

Lots on accessibility and conduct, to make PyCon accessible and 'comfortable' for all.  Gender-neutral bathrooms, mothers' rooms, quiet room, etc.

"Remember to phrase your question in the form of a question." <applause>

Hallway track, and pac-man rule (when standing in a group, always leave room for one other to join your group).

cat /etc/motd ?

@pycon, #PyCon2019


Keynote - Russell Keith-Magee
=============================

From Perth, Australia.
beeware.org, @freakboy3742
Member of django (Py web framework) core team.

Look at us!  Python is powerful!  Where do you see Python in 10 years?
What is Python's Black Swan (event that is obvious in hindsight, but currently everyone discounts it)
e.g. "everyone uses a laptop".  Not really true anymore.  What happens to Python when laptops don't exist anymore?
e.g. "Python can stay on the server".  Now, more logic performed in the browser, and usually js.  
e.g. "Python installation is solved".  It is *not*.  This is an "existential threat".
e.g. "code distribution doesn't matter". 
...or will the Python black swan be different than these? 

America's Cup.  Perth's Australia 2 beat NY yacht club in 1983 for the first time in 150 years.

WASM is Python "winged keel" (innovation).  Python on WASM is our opportunity to innovate.

We need everyone on the team, including non-devs.

Money is important.  We need sponsors and donors.  Volunteering on weekends can't be the only way to push Python forward.  e.g. PyPI's rewrite, b/c Mozilla's big donation.  Python needs an R&D division  Citing start of UNIX.  Consider Common Pooled Resources (CPRs), Elinor Ostrom.

C.Y. O'Connor and his water pipeline into the Western Australia desert. ... burnout.  Dealing with open-source community, esp. folks that feel entitled to FOSS, is very draining.  There is human cost to F(L)OSS.  We should restructure our community to put the right people in the right roles, and better-fund everyone, to avoid this burnout.


Break the Cycle
===============

Looks great - check out video!


Practical Decorators
====================

Speaker: Reuven Lerner, @reuvenmlerner, weekly python exercise, author

```python
@mydeco
def add():
```

is really

```python
add = mydeco(add)
```

Are decorators a solution looking for a problem?  **No!**  Application examples:

* Timing - how long does it take for my function to run?
* Run once per minute

Args to decorators!

```python
@once_per_n(5)
def add(a, b):
    return a + b

def once_per_n(n):
    def middle(func):
        last_invoked = 0

        def wrapper(*args, **kwargs):
            nonlocal last)_invoked

            # more logic

            return func(*args, **kwargs)
# more
```

* memoization [sic] - cache the results of function calls, so we don't need to call them again

See presentation/video for code snippets.  Better yet, see [Reuven's website](http://PracticalDecorators.com)

* attributes - give many objects the same attributes, but without using inheritance (because that's only appropirate if the classes are inherently similar to one another)

*Classes*, and/or objects of classes, can be decorated too!... of course, because they're callable!


A Snake in the Bits: Security Automation with Python
====================================================

Speakers: Moses Schwartz, Andy Culler, box

Overall: Feed logs into some central system; feed through them; someone has to take a look.

Splunk used to do much of this (aggregate logs, trigger alerts.

They used *flask* for simple API app?/web? development.

Speakers created Jira ticket with Splunk alert JSON as description.  Next, created a webhook in Jira to fire on these type of tickets and clean JSON, lookup md5 in virustotal, more via call back to speakers' automation server.


Migrating Pinterest from Python2 to Python3
===========================================

Speakers: Jordan Adler, Joe Gordon

Python with django.

2.6 million lines of code, 1,000 lifetime authors, 3.5k changes monthly!

caniusepython3.

Iterative process.  Make changes; CI and linters; run unit tests under 2 and 3; ...

Some errors detectable by flake8, some at import time, some at runtime (unit testing, production).

The good:  using libfuturize and lib2to3 to fix print, absolute import (not import foo, but from . import foo), more

The bad:  
* numbers: 1/2 was 0, now 0.5; round(2.5) was 2, now 3 ("banker's rounding"); x = None; x > 1 was False but now is TypeError; many other numbers examples
* scoping, e.g. [i for i in range(10)]; print(i).  In 2, 9; in 3, NameError: 'i' is not defined; others

The ugly:
* Hashable types (???)
* Unicode


Mocking and Patching Pitfalls
=============================

Speaker: Edwin Jung

```python
from unittest.mock import patch
#...
```

Mock hell!  Mocking can get confusing, tedious.

Be careful about over-mocking.

...discussion...

So, how do you test without mocks?  Lots of strategies:
* Mock *roles*, not *objects*.
* Find a seam, patch a fake. (?)
* Dependency injection.
* Inject the collaborator. (?)
* Go functional. (?)


Everything at Once: Python's Many Concurrency Models
====================================================

First, understand concurrency, minimum scheduleable unit, data sharing and isolation, other concepts.

.:Various models:
* asyncio coroutines.
...code samples...
* Python threads.  One thread runs; global satate is shared; MSU is 'bytecode' (but that unit is hard to understand).
...Others...


Maintaining a Python Project When It's Not Your Job
===================================================

How to feel less crappy about the stress and management of maintaining an OS project.

If you define your own project, you can define scope, etc.  That's good.

Support and emotional "labor" will burn you out.

Use short feedback loops -- mencourages experimentation, etc.

Removing friction.  How?:
* Act 1: development.  Speaker encourages OS development through welcome message in repo, CONTRIBUTING.rst, outlines code standards, other things (CODE_OF_CONDUCT.rst)  
Use tox, which (I think) helps you build and run in virtual envs.
```python
[tox]
envlist = py27,py37,pypy,pypy3
[testenv]
extras = tests
commands = pytest {posargs}
```
then
```
# tox -e py27 -- -x
``` 

Linting - checking code without actually running it.
flake8 is the most famous.
black is similar and awesome.
isort is related too.

Aside:  twine to upload your Python package to PyPI.

Another option:  .pre-commit-config.yaml which will ensure checking before a git commit.  e.g. run 'hook' e.g. flake8.

Add other tox environment, e.g. one to ensure sphinx documentation is built:
```python
[testenv:docs]
basepython = python3.7
extras - docs
commands = 
    sphinx-build ...
```

Add a pull request ("pr") checklist.  "Checklists are the reason that doctors wash their hands before they cut you open, or why airplanes don't crash."

Idera bought travis (CI project?, company?).  Speaker thinks that's bad.  'github actions' is another CI coming.

Project leads should celebrate their contributors.  And let anyone in!  If they make bad commits, just revert and kick them out.

Speaker moved his support to stackoverflow.

* Act 3: release.
Automate and simplify as much as you can!  Edit just a few strings in __init__.py and CHANGELOG, check doc links using splinx check links, CI, twine to push to PyPI.  Done!

**ox.cx/oss**
@hynek
vrmd.de


Scraping a Million Pokemon Battles: Distributed Systems By Example
==================================================================

Speaker: Duy Nguyen

.:Scraping unauthenticated Pokemon battles on AWS -- learn about Distributed Systems

This Pokemon game ("Pokemon Showdown" (?)) is on github, all open source.  Duy went there to understand logs, which can be used to replay the battles.

Focus of this talk:  finding new battles and downloading them.

(Aside: Raymond Hettinger - Thinking About Concurrence - PyCon Russia 2016 - great talk to learn concurrency.)

Producers (producing urls); consumers (scraping the data); plus messaging between them.  Considerations:  concurrency, loss of message (solution: SQSQueue), others.


(Some) Lightning Talks
======================

Snappy Code - Python for K-5.  snappycode.org

Less gentle, less kind pandas DataFrame (called "StaticFrame")


