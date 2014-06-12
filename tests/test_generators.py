#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, with_statement, unicode_literals

import sys
import os
import os.path as osp
import unittest

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.realpath(os.path.join(TESTS_ROOT, '..'))) 

from simiki.configs import parse_configs
from simiki.generators import PageGenerator

TEST_INPUT_FILE = osp.join(TESTS_ROOT, "sample/hellosimiki.md")

EXPECTED_OUTPUT = "./expected_output.html"

class TestPageGenerator(unittest.TestCase):
    def setUp(self):
        self.config_file = osp.join(
            osp.dirname(osp.dirname(osp.abspath(__file__))),
            "simiki/conf_templates/_config.yml.in"
        )

        configs = parse_configs(self.config_file)
        self.generator = PageGenerator(configs, TESTS_ROOT, TEST_INPUT_FILE)

#    def test_get_category_and_file(self):
#        category_name, filename = self.generator.get_category_and_file()
#        self.assertEqual((category_name, filename), (u'sample', u'hellosimiki.md'))

    def test_get_layout(self):
        layout = self.generator.get_layout()
        self.assertEqual(layout, "page")


if __name__ == "__main__":
    unittest.main()
