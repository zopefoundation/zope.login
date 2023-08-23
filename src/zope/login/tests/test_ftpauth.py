##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
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
from zope.publisher.interfaces.ftp import IFTPCredentials
from zope.testing import cleanup


@implementer(IFTPCredentials)
class FTPCredentials:
    __doc__ = IFTPCredentials.__doc__

    def __init__(self, credentials):
        self.credentials = credentials

    def _authUserPW(self):
        return self.credentials

    unauth = 0

    def unauthorized(self, challenge):
        self.unauth += 1


class Test(unittest.TestCase):

    def _makeOne(self, request):
        from zope.publisher.ftp import FTPAuth
        return FTPAuth(request)

    def test(self):
        request = FTPCredentials(('bob', '123'))
        auth = self._makeOne(request)
        self.assertEqual(auth.getLogin(), 'bob')
        self.assertEqual(auth.getPassword(), '123')

        unauth = request.unauth
        auth.needLogin('xxx')
        self.assertEqual(request.unauth, unauth + 1)

        request = FTPCredentials(None)
        auth = self._makeOne(request)
        self.assertEqual(auth.getLogin(), None)
        self.assertEqual(auth.getPassword(), None)


class TestConfigured(cleanup.CleanUp,
                     Test):

    def setUp(self):
        from zope.configuration import xmlconfig

        import zope.login
        xmlconfig.file('configure.zcml', zope.login)

    def _makeOne(self, request):
        from zope.authentication.interfaces import ILoginPassword
        return ILoginPassword(request)
