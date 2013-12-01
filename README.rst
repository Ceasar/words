words
=====

.. image:: https://badge.fury.io/py/words.png
    :target: http://badge.fury.io/py/words

.. image:: https://pypip.in/d/words/badge.png
        :target: https://crate.io/packages/words/

Get large collection of words from books.

Installation
------------

To install, simply:

.. code-block:: bash

    $ pip install words

Quickstart
----------

Begin by making a directory called ``books/``::

    $ mkdir books

Next, insert files you wish to extract words from. Presumably large ones,
i.e. books, which are easily available from Gutenberg_.

Then, execute ``words.py`` (which can be run anywhere).::

    $ words.py

You should now have a file called ``dictionary.txt`` containing a large list
of words.::

    $ ls
    books/  dictionary.txt

Description
-----------

`words.py` simply reads each of the books and puts each of the words in a book filtering any that obviously aren't words (anything containing numbers or punctuation).

NOTE: This method may generate non-words which look like words. It is worth revieiwng the lexicon before any serious use.

.. _Gutenberg: http://www.gutenberg.org/
