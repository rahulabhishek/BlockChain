# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class GaApplication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://docs.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_ga_application(self):
        driver = self.driver
        driver.get(self.base_url + "/forms/d/e/1FAIpQLSd_E0GyOCBnnpF_6d6JCRTHDyr5zhKoc6VujmjrvHmU9GshSg/viewform")
        driver.find_element_by_name("entry.89642107").click()
        driver.find_element_by_name("entry.89642107").clear()
        driver.find_element_by_name("entry.89642107").send_keys("Rahul Singh")
        driver.find_element_by_name("entry.89642107").clear()
        driver.find_element_by_name("entry.89642107").send_keys("Rahul Singh")
        driver.find_element_by_name("entry.992346250").click()
        driver.find_element_by_name("entry.992346250").clear()
        driver.find_element_by_name("entry.992346250").send_keys("001322745")
        driver.find_element_by_name("entry.992346250").clear()
        driver.find_element_by_name("entry.992346250").send_keys("001322745")
        driver.find_element_by_name("entry.293819814").click()
        driver.find_element_by_name("entry.293819814").clear()
        driver.find_element_by_name("entry.293819814").send_keys("rsingh5@albany.edu")
        driver.find_element_by_name("entry.293819814").clear()
        driver.find_element_by_name("entry.293819814").send_keys("rsingh5@albany.edu")
        driver.find_element_by_name("entry.1175490529").clear()
        driver.find_element_by_name("entry.1175490529").send_keys("6603833766")
        driver.find_element_by_name("entry.1175490529").clear()
        driver.find_element_by_name("entry.1175490529").send_keys("6603833766")
        driver.find_element_by_name("entry.1792889779").click()
        driver.find_element_by_name("entry.1792889779").clear()
        driver.find_element_by_name("entry.1792889779").send_keys("masters in computer science")
        driver.find_element_by_name("entry.1792889779").clear()
        driver.find_element_by_name("entry.1792889779").send_keys("masters in computer science")
        driver.find_element_by_name("entry.203902984").click()
        driver.find_element_by_name("entry.203902984").clear()
        driver.find_element_by_name("entry.203902984").send_keys("2019")
        driver.find_element_by_name("entry.203902984").clear()
        driver.find_element_by_name("entry.203902984").send_keys("2019")
        driver.find_element_by_name("entry.51973597").click()
        driver.find_element_by_name("entry.1659388094").click()
        driver.find_element_by_name("entry.1659388094").clear()
        driver.find_element_by_name("entry.1659388094").send_keys("I can start with the work ASAP")
        driver.find_element_by_name("entry.1659388094").clear()
        driver.find_element_by_name("entry.1659388094").send_keys("I can start with the work ASAP")
        driver.find_element_by_css_selector("div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox").click()
        driver.find_element_by_xpath(
            "//form[@id='mG61Hd']/div/div[2]/div[2]/div[10]/div[2]/div[4]/div/label/div/div/div[2]").click()
        driver.find_element_by_xpath(
            "//form[@id='mG61Hd']/div/div[2]/div[2]/div[10]/div[2]/div[6]/div/label/div/div/div[2]").click()
        driver.find_element_by_xpath(
            "//form[@id='mG61Hd']/div/div[2]/div[2]/div[10]/div[2]/div[7]/div/label/div/div").click()
        driver.find_element_by_xpath(
            "//form[@id='mG61Hd']/div/div[2]/div[2]/div[10]/div[2]/div[8]/div/label/div/div/div[2]").click()
        driver.find_element_by_name("entry.1712759586").click()
        driver.find_element_by_name("entry.1712759586").clear()
        driver.find_element_by_name("entry.1712759586").send_keys("Due to my past experience, my professionalism")
        driver.find_element_by_name("entry.1712759586").clear()
        driver.find_element_by_name("entry.1712759586").send_keys("Due to my past experience, my professionalism")
        driver.find_element_by_name("entry.51973597").click()
        driver.find_element_by_name("entry.51973597").clear()
        driver.find_element_by_name("entry.51973597").send_keys("It gives me an opportunity to work with")
        driver.find_element_by_name("entry.51973597").clear()
        driver.find_element_by_name("entry.51973597").send_keys("It gives me an opportunity to work with")
        driver.find_element_by_name("entry.1623345122").click()
        driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[8]/div[2]").click()
        driver.find_element_by_name("entry.1623345122").click()
        driver.find_element_by_name("entry.1623345122").send_keys(
            "I my self is an international student. And it has been an interesting journey coming to USA from INDIA. I was a member in one online forum called as yocket and used to share my experience with other international student. When we work with diverse students, we need to make sure that we understand their background.")
        driver.find_element_by_name("entry.1623345122").clear()
        driver.find_element_by_name("entry.1623345122").send_keys(
            "I my self is an international student. And it has been an interesting journey coming to USA from INDIA. I was a member in one online forum called as yocket and used to share my experience with other international student. When we work with diverse students, we need to make sure that we understand their background.")
        driver.find_element_by_link_text("What do leaders need to understand about diversity? | Yale Insights").click()
        driver.find_element_by_link_text("What do leaders need to understand about diversity? | Yale Insights").click()
        driver.find_element_by_link_text("Section 1. Understanding Culture and Diversity in Building").click()
        driver.find_element_by_link_text("Section 1. Understanding Culture and Diversity in Building").click()
        driver.find_element_by_name("entry.1623345122").click()
        driver.find_element_by_name("entry.1623345122").clear()
        driver.find_element_by_name("entry.1623345122").send_keys(
            "I my self is an international student. And it has been an interesting journey coming to USA from INDIA. I was a member in one online forum called as yocket and used to share my experience with other international student. When we work with diverse students, we need to make sure that we understand their background. Most important part is to embrace their diversity")
        driver.find_element_by_name("entry.1623345122").clear()
        driver.find_element_by_name("entry.1623345122").send_keys(
            "I my self is an international student. And it has been an interesting journey coming to USA from INDIA. I was a member in one online forum called as yocket and used to share my experience with other international student. When we work with diverse students, we need to make sure that we understand their background. Most important part is to embrace their diversity")
        driver.find_element_by_name("entry.1712759586").click()
        driver.find_element_by_name("entry.1712759586").click()
        driver.find_element_by_name("entry.1712759586").clear()
        driver.find_element_by_name("entry.1712759586").send_keys(
            "My past experience and my  professionalism makes me an ideal candidate for this role.")
        driver.find_element_by_name("entry.1712759586").clear()
        driver.find_element_by_name("entry.1712759586").send_keys(
            "My past experience and my  professionalism makes me an ideal candidate for this role.")
        driver.find_element_by_css_selector("content.quantumWizButtonPaperbuttonContent").click()
        driver.find_element_by_name("entry.2008093663").click()
        driver.find_element_by_name("entry.2008093663").click()
        driver.find_element_by_name("entry.2008093663").clear()
        driver.find_element_by_name("entry.2008093663").send_keys(
            "I used to work as a software consultant working along with cross-cultural team.\nI do have a professional experience of 7 years and quite familiar with ualbany campus and near by areas.\nI am familiar with Microsoft office suite and other social networking sites.")
        driver.find_element_by_name("entry.2008093663").clear()
        driver.find_element_by_name("entry.2008093663").send_keys(
            "I used to work as a software consultant working along with cross-cultural team.\nI do have a professional experience of 7 years and quite familiar with ualbany campus and near by areas.\nI am familiar with Microsoft office suite and other social networking sites.")
        driver.find_element_by_css_selector("span.quantumWizButtonPaperbuttonLabel.exportLabel").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
