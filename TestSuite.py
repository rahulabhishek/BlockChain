__author__ = 'rahul'
from io import StringIO
import unittest
import youtube_search
import pof_login
import wikitest
import os
import nose_html_reporting



direct = os.getcwd()


class MyTestSuite(unittest.TestCase):
    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(wikitest.MyWikiTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(pof_login.PofLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(youtube_search.YoutubeSearch),
        ])

        outfile = open(direct + "\SmokeTest.html", "w")

        runner1 = nose_html_reporting.nose_html_reporting(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )

        runner1.run(smoke_test)
if __name__ == '__main__':
    unittest.main()