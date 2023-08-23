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

from zope.authentication.loginpassword import LoginPassword
from zope.component import adapter
from zope.publisher.interfaces.http import IHTTPCredentials


@adapter(IHTTPCredentials)
class BasicAuthAdapter(LoginPassword):
    """
    ILoginPassword adapter for handling HTTP Basic authentication.

    Adapts :class:`zope.publisher.interfaces.http.IHTTPCredentials`
    into :class:`zope.authentication.interfaces.ILoginPassword`.
    """

    def __init__(self, request):
        self.__request = request
        # TODO base64 decoding should be done here, not in request
        lpw = request._authUserPW()
        if lpw is None:
            login, password = None, None
        else:
            login, password = lpw
        super().__init__(login, password)

    def needLogin(self, realm):
        self.__request.unauthorized('basic realm="%s"' % realm)
