#!/usr/bin/env python3

"""
Main.py
"""

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import textwrap


def mock_up():
    """
    MOCK UP - Demo of layout

    :return: Nothing
    """
    print('----------------------------------------------------------------------')
    print('                               MOCKUP')
    print('----------------------------------------------------------------------')
    html = urllib.request.urlopen('http://reddit.com').read()
    print(textwrap.fill(text_from_html(html), width=70))
    print('----------------------------------------------------------------------')
    print('                           CONTROLS (q)uit')
    print('----------------------------------------------------------------------')


def main_event_loop():
    """
    Main event loop

    :return: Nothing
    """
    cmd = None
    while cmd != '':
        cmd = input(mock_up())


def tag_visible(element):
    """
    MOCK UP - Demo of Content

    :param element:
    :return:
    """
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    """
    MOCK up - Demo of Content

    :param body:
    :return:
    """
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


# Entry Point
if __name__ == '__main__':

    main_event_loop()
