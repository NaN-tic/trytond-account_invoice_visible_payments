#!/usr/bin/env python
# This file is part of the account_invoice_visible_payments module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_view, test_depends
import trytond.tests.test_tryton
import unittest


class AccountInvoiceVisiblePaymentsTestCase(unittest.TestCase):
    'Test Account Invoice Visible Payments module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('account_invoice_visible_payments')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountInvoiceVisiblePaymentsTestCase))
    return suite
