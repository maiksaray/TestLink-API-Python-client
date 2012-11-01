#! /usr/bin/python
# -*- coding: UTF-8 -*-

#  Copyright 2012 Luiko Czub, TestLink-API-Python-client developers
#
#  Licensed under ???
#  see https://github.com/orenault/TestLink-API-Python-client/issues/4

# this test requires an online TestLink Server, which connection parameters
# are defined in environment variables
#     TESTLINK_API_PYTHON_DEVKEY and TESTLINK_API_PYTHON_DEVKEY

import unittest
from testlink import TestlinkAPIClient, TestLinkHelper
from testlink import testlinkerrors


class TestLinkAPIcallServerTestCase(unittest.TestCase):
    """ TestCases for TestLinkAPICleint._callServer()  """


    def test_callServer_noArgs(self):
        """ test _callServer() - calling method with no args """
        
        client = TestLinkHelper().connect(TestlinkAPIClient)
        response = client._callServer('sayHello')
        self.assertEqual('Hello!', response)
        
    def test_callServer_withArgs(self):
        """ test _callServer() - calling method with args """
        
        client = TestLinkHelper().connect(TestlinkAPIClient)
        response = client._callServer('repeat', {'str' : 'some arg'})
        self.assertEqual('You said: some arg', response)
        
    def test_callServer_ProtocollError(self):
        """ test _callServer() - Server raises ProtocollError """
        
        server_url = TestLinkHelper()._server_url
        bad_server_url = server_url.split('xmlrpc.php')[0] 
        client = TestLinkHelper(bad_server_url).connect(TestlinkAPIClient)
        def a_func(api_client): api_client._callServer('sayHello')
        self.assertRaises(testlinkerrors.TLConnectionError, a_func, client)
        
    def test_callServer_socketError(self):
        """ test _callServer() - Server raises a socket Error (IOError) """
        
        bad_server_url = 'http://111.222.333.4/testlink/lib/api/xmlrpc.php' 
        client = TestLinkHelper(bad_server_url).connect(TestlinkAPIClient)
        def a_func(api_client): api_client._callServer('sayHello')
        self.assertRaises(testlinkerrors.TLConnectionError, a_func, client)

    def test_callServer_FaultError(self):
        """ test _callServer() - Server raises Fault Error """
        
        client = TestLinkHelper().connect(TestlinkAPIClient)
        def a_func(api_client): api_client._callServer('sayGoodBye')
        self.assertRaises(testlinkerrors.TLAPIError, a_func, client)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()