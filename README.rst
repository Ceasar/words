words
=====

Get large collection of words from books.

Usage
-----

1. Make a directory called ``books/``
2. Put ``.txt`` files in it. Presumably large ones, i.e. books, which are easily available from Gutenberg_.
3. Run ``words.py`` and wait a moment.
4. Receive ``dictionary.txt``.

Description
-----------

`words.py` simply reads each of the books and puts each of the words in a book filtering any that obviously aren't words (anything containing numbers or punctuation).

NOTE: This method may generate non-words which look like words. It is worth revieiwng the lexicon before any serious use.

.. _Gutenberg: http://www.gutenberg.org/
