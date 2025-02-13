from selenium import webdriver
from consts import PRACUJ_PL_URL
import os


class JobBot(webdriver.Chrome):
    def __init__(self, driver_path=''):
        self.driver_path = driver_path
        super(JobBot, self).__init__()

    def land_first_page(self):
        self.get(PRACUJ_PL_URL)
        print(self.title)


