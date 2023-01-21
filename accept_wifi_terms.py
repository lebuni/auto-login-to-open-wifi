#!/usr/bin/env python
"""Connects to wifi in case terms and conditions need to be accepted"""
import mechanize


def accept_wifi_terms():

    URL = 'https://www.google.com/'

    br = mechanize.Browser()
    br.set_handle_redirect(True)
    br.set_handle_equiv(True)
    br.set_handle_robots(False)
    br.open(URL)
    if URL == br.geturl():
        print("internet already working")
        return True

    try:
        br.select_form(nr=0)
    except mechanize.FormNotFoundError:
        print("No form found")
        return False

    br.submit()
    print("Terms accepted")
    return True


if __name__ == "__main__":
    accept_wifi_terms()
