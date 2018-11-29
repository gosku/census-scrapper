from splinter.browser import Browser
from bs4 import BeautifulSoup
import wget
from time import sleep

class CensusExport(object):
    def __init__(self):
        # executable_path = {'executable_path':'/usr/bin/google-chrome'}
        browser = Browser('chrome')
        url = "https://ledextract.ces.census.gov/static/data.html"
        browser.visit(url)


        sidebar = browser.find_by_id("states_list")

        states = sidebar.find_by_css("a.QwiFilteringListItem")

        for state in states:
            name = state.find_by_tag('span')[1].html
            if name == 'United States':
                continue
            print('''Downloading cvs for %s''' % name )
            self.export_state(browser, state, name)


    def export_state(self, browser, state, state_name):
        self.run_geography_tab(browser, state, state_name)

    def run_geography_tab(self, browser, state, state_name):
        browser.find_by_id('tabs_tablist_area_tab').first.click()
        state.click()
        sleep(5)

        # Click Select All
        browser.execute_script(
            '''
            document.querySelectorAll("#dijit_layout_BorderContainer_2 .FilteringListActions a")[0].click()
            '''
        )
        continue_button = browser.find_by_id('continue_with_selection_label').first
        continue_button.click()
        self.run_firm_tab(browser, state_name)

    def run_firm_tab(self, browser, state_name):
        # Click Select All
        browser.execute_script(
            '''
            document.querySelectorAll('#dijit_layout_ContentPane_9 a')[0].click()
            '''
        )
        continue_button = browser.find_by_id('continue_to_worker_char_label').first
        continue_button.click()
        self.run_worker_tab(browser, state_name)

    def run_worker_tab(self, browser, state_name):
        continue_button = browser.find_by_id('continue_to_indicators_label').first
        continue_button.click()
        self.run_indicators_tab(browser, state_name)

    def run_indicators_tab(self, browser, state_name):
        continue_button = browser.find_by_id('continue_to_quarters_label').first
        continue_button.click()
        self.run_quarters_tab(browser, state_name)

    def run_quarters_tab(self, browser, state_name):
        #Click on quarter columns
        browser.execute_script("document.querySelectorAll('table thead span')[0].click()")
        browser.execute_script("document.querySelectorAll('table thead span')[1].click()")
        browser.execute_script("document.querySelectorAll('table thead span')[2].click()")
        browser.execute_script("document.querySelectorAll('table thead span')[3].click()")

        continue_button = browser.find_by_id('continue_to_export_label').first
        continue_button.click()
        self.run_summary_tab(browser, state_name)

    def run_summary_tab(self, browser, state_name):
        sleep(5)
        continue_button = browser.find_by_id('submit_request_label').first
        continue_button.click()
        self.wait_until_finish(browser)
        link = browser.evaluate_script("document.querySelector('#current_result .DownloadCSV').href")

        file = wget.download(link, out=state_name+'.csv')
        print("""File %s downloaded""" % file)

    def wait_until_finish(self, browser):
        while 1:
            html = browser.evaluate_script("document.querySelector('#current_result').innerHTML")
            if html != "":
                return
            sleep(5)

CensusExport()




