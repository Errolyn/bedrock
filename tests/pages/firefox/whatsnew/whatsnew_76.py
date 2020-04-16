# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.firefox.base import FirefoxBasePage


class FirefoxWhatsNew76Page(FirefoxBasePage):

    URL_TEMPLATE = '/{locale}/firefox/76.0/whatsnew/all/{params}'

    _facebook_container_picto_block_locator = (By.CSS_SELECTOR, '.c-picto-block.facebook-container')
    _column_2_locator = (By.CSS_SELECTOR, '.columns.l-columns-two')
    _column_3_locator = (By.CSS_SELECTOR, '.columns.l-columns-three')


    @property
    def is_facebook_container_picto_block_displayed(self):
        return self.is_element_displayed(*self._facebook_container_picto_block_locator)

    @property
    def are_three_columns_displayed(self):
        return self.is_element_displayed(*self._column_3_locator)

    @property
    def are_two_columns_displayed(self):
        return  self.is_element_displayed(*self._column_2_locator)


