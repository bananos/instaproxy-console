#!/usr/bin/env python

import argparse
import requests
import re


class InvalidAuth(Exception):
    pass


class InvalidResponse(Exception):
    pass


class ParserError(Exception):
    pass

LOGIN_PAGE = "http://admin.instantproxies.com/login_do.php"
IPS_REGEXP = re.compile('<textarea *[^>]*>(.*)</textarea>')


def web_login(username, password):
    """
    Login to the admin page and returns its contents.
    :param username: Login
    :type username: str

    :param password: Password
    :type password: str

    :rtype: unicode
    """
    resp = requests.post(LOGIN_PAGE, {"username": username, "password": password})

    if resp.status_code != 200:
        raise InvalidResponse("HTTP Error %i" % resp.status_code)
    if "Invalid username" in resp.text:
        raise InvalidAuth()
    return resp.text


def get_proxy_list(html_response):
    """
    Returns list of proxies scraped from html_response.
    :param html_response: Raw HTML text
    :type html_response: unicode

    :rtype: list[unicode]
    """
    try:
        tmp = IPS_REGEXP.findall(html_response.replace("\n", ","))[0]
        proxies = tmp.split("</textarea>")[0].split(",")
    except Exception:
        raise ParserError()

    return proxies


def main():
    """
    Main entry point
    """

    parser = argparse.ArgumentParser(description="""
        A command-line tool to read list of proxies from http://instantproxies.com service.
    """)
    parser.add_argument("--username", help="User ID", type=str)
    parser.add_argument("--password", help="password", type=str)
    args = parser.parse_args()

    if args.username is None or args.password is None:
        print "Please, provide valid username and/or password"
        return 1

    try:
        resp = web_login(args.username, args.password)
        proxies = get_proxy_list(resp)
        for p in proxies:
            print p
        return 0
    except Exception as e:
        print "Error: %s" % type(e)
        return 1

if __name__ == "__main__":
    exit(main())
