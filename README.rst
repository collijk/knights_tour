=============
Knight's Tour
=============

This repository provides a validator (or oracle) for the
`Knight's Tour <https://en.wikipedia.org/wiki/Knight%27s_tour>`_ problem.
You can read more about oracles and oracle machines
`here <https://en.wikipedia.org/wiki/Oracle_machine>`_.

.. contents::
   :depth: 1

Installation
------------

To install the package, run the following commands::

   git clone https://github.com/collijk/knights_tour.git
   cd knights_tour
   pip install .

This will install the repository into your python environment.

Usage
-----

Once installed, you can use the validator from your own code by importing it::

   from knights_tour import is_valid_tour

   def generate_knights_tour():
       # Your solution here

   tour = generate_knights_tour()
   is_valid_tour(tour)
