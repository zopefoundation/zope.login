##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import unittest

from zope.interface import implementer
from zope.publisher.interfaces.http import IHTTPCredentials
from zope.testing import cleanup


@implementer(IHTTPCredentials)
class Request:

    def __init__(self, lpw):
        self.lpw = lpw

    def _authUserPW(self):
        return self.lpw

    challenge = None

    def unauthorized(self, challenge):
        self.challenge = challenge


class Test(unittest.TestCase):

    def _makeOne(self, request):
        from zope.publisher.http import BasicAuthAdapter
        return BasicAuthAdapter(request)

    def testBasicAuthAdapter(self):
        r = Request(None)
        a = self._makeOne(r)
        self.assertEqual(a.getLogin(), None)
        self.assertEqual(a.getPassword(), None)
        r = Request(("tim", "123"))
        a = self._makeOne(r)
        self.assertEqual(a.getLogin(), "tim")
        self.assertEqual(a.getPassword(), "123")

    def testUnauthorized(self):
        r = Request(None)
        a = self._makeOne(r)
        a.needLogin("tim")
        self.assertEqual(r.challenge, 'basic realm="tim"')


class TestConfigured(cleanup.CleanUp,
                     Test):

    def setUp(self):
        from zope.configuration import xmlconfig

        import zope.login
        xmlconfig.file('configure.zcml', zope.login)

    def _makeOne(self, request):
        from zope.authentication.interfaces import ILoginPassword
        return ILoginPassword(request)
