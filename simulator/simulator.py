import random
import time
import os
import glob
from os import environ

from argparse import ArgumentParser

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def instructions(driver):
    print("Clicking through instruction screen...")
    driver.find_element(By.XPATH, '//button').click()
    # try:
    #     btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button')))
    #     btn.click()
    # finally:
    #     print("Unable to find instructions button.")
    #     driver.quit()


def practice_maze(browser):
    print("Clicking through practice maze...")
    browser.find_element(By.XPATH, '//button').click()


def single_entry_task(browser, browser_tab, task_id):
    task_input = browser.find_element_by_id('task_input')
    max_value = int(task_input.get_attribute('max'))
    entry = random.randint(0, max_value)
    print('Browser Tab {}: For task {}, value {} was entered.'.format(browser_tab, task_id, entry))
    task_input.send_keys(str(entry))

    browser.find_element(By.XPATH, '//button').click()


def hold_wait_page(driver, pass_code):
    input_field = driver.find_element_by_id('pass_code')
    input_field.send_keys(pass_code)
    driver.find_element(By.XPATH, '//button').click()

def choose_lottery(driver, pair_id, browser_tab):
    preference = random.randint(0, 2)
    preference_text = {0: "Option V", 1: "Option W", 2: "Either"}
    print('Browser Tab {}: Preferred lottery for pair {} was {}'.format(browser_tab, pair_id, preference_text[preference]))

    element = driver.find_element_by_id('id-preference-{}'.format(preference))
    element.click()
    driver.find_element(By.XPATH, '//button').click()


def allocate_lottery_pair_time(browser, pair_id, browser_tab):
    random_side = random.randint(1, 2)
    # Left
    if random_side == 1:
        left_lottery_input = browser.find_element_by_id('left_lottery_time')

        max_value = int(left_lottery_input.get_attribute('max'))
        left_lottery_allocation = random.randint(0, max_value)
        print('Browser Tab {}: For pair {}: Left lottery allocated {} seconds, Right lottery allocated {} seconds.'.format(
            browser_tab, pair_id, left_lottery_allocation, max_value - left_lottery_allocation
        ))

        left_lottery_input.send_keys(str(left_lottery_allocation))
    # Right
    else:
        right_lottery_input = browser.find_element_by_id('right_lottery_time')

        max_value = int(right_lottery_input.get_attribute('max'))
        right_lottery_allocation = random.randint(0, max_value)

        right_lottery_input.__setattr__('value', right_lottery_allocation)

        print('Browser Tab {}: For pair {}: Left lottery allocated {} seconds, Right lottery allocated {} seconds.'.format(
            browser_tab, pair_id, max_value - right_lottery_allocation, right_lottery_allocation
        ))

        right_lottery_input.send_keys(str(right_lottery_allocation))

    browser.find_element(By.XPATH, '//button').click()


def task_one(browser, browser_tab):
    choice_ids = ['left_label', 'middle_label', 'right_label']
    options = ['A', 'B', 'C']
    choice = random.randint(0, 2)
    print('Browser Tab {}: Option {} was chosen for task 1.'.format(browser_tab, options[choice]))

    element = browser.find_element_by_id(choice_ids[choice])
    element.click()
    browser.find_element(By.XPATH, '//button').click()


def task_alpha(browser):
    cases = 10
    choice_labels = ['A', 'B']
    choice_id_templates = ['{}_maze_{}', '{}_lottery_{}']
    choices = [
        choice_id_templates[random.randint(0, 1)].format('a', str(random.randint(1, 11))),
        choice_id_templates[random.randint(0, 1)].format('b', str(random.randint(1, 11))),
        choice_id_templates[random.randint(0, 1)].format('c', str(random.randint(1, 11)))
    ]
    for choice_id in choices:
        element = browser.find_element_by_id(choice_id)
        element.click()
    browser.find_element(By.XPATH, '//button').click()


def task_eight(browser, browser_tab):
    cases = 11
    choice_labels = ['A', 'B']
    choice_ids = ['a_row_{}', 'b_row_{}']
    for case_id in range(1, cases + 1):
        random_choice = random.randint(0, 1)
        choice = choice_ids[random_choice]
        print('Browser Tab {}: For task 8 Case {}, option {} was chosen.'.format(browser_tab, case_id, choice_labels[random_choice]))
        element = browser.find_element_by_id(choice.format(case_id))
        element.click()
    browser.find_element(By.XPATH, '//button').click()


def task_nine(browser, browser_tab):
    cases = 11
    choice_labels = ['A', 'B']
    choice_ids = ['a_row_{}', 'b_row_{}']
    for case_id in range(1, cases + 1):
        random_choice = random.randint(0, 1)
        choice = choice_ids[random_choice]
        print('Browser Tab {}: For task 9 Case {}, option {} was chosen.'.format(browser_tab, case_id, choice_labels[random_choice]))
        element = browser.find_element_by_id(choice.format(case_id))
        element.click()
    browser.find_element(By.XPATH, '//button').click()


def task_five(browser, browser_tab, task_id):
    input_field = browser.find_element_by_id('task_input')
    max_value = int(input_field.get_attribute('max'))
    entry = random.randint(0, max_value)
    input_field.send_keys(str(entry))
    print('Browser Tab {}: For task {}, value {} was entered.'.format(browser_tab, task_id, entry))
    browser.find_element(By.XPATH, '//button').click()


def task_seven(browser, browser_tab, task_id):
    distance_input_field = browser.find_element_by_id('task_input')
    distance = random.randint(0, 500)
    distance_input_field.send_keys(str(distance))
    print('Browser Tab {}: For task {}, value {} was entered.'.format(browser_tab, task_id, distance))

    browser.find_element_by_id('inlineRadio1').click()

    confidence_input_field = browser.find_element_by_id('confidence_input')
    confidence = random.randint(0, 100)
    confidence_input_field.send_keys(str(confidence))

    browser.find_element(By.XPATH, '//button').click()


def bet_case_select_task(browser, browser_tab, task_id):
    cases = 10
    button_ids = ['left_button', 'right_button']
    random_choice = random.randint(0, 1)
    button = browser.find_element_by_id(button_ids[random_choice])

    choice_labels = ['A', 'B']
    print('Browser Tab {}: For task {} color {} was chosen.'.format(browser_tab, task_id, choice_labels[random_choice]))
    button.click()

    choice_labels = ['A', 'B']
    choice_ids = ['a_row_{}', 'b_row_{}']
    for case_id in range(1, cases + 1):
        random_choice = random.randint(0, 1)
        choice = choice_ids[random_choice]
        print('Browser Tab {}: For task {} Case {}, option {} was chosen.'.format(browser_tab, task_id, case_id, choice_labels[random_choice]))
        element = browser.find_element_by_id(choice.format(case_id))
        element.click()
    browser.find_element(By.XPATH, '//button').click()




class Game:
    def __init__(self):
        self.simulator = Simulator()

    def run(self):
        (self.part, self.quit) = Game.command_line_args()

        self.simulator.open_url(environ.get('EXPERIMENT_URL'))
        link_elements = self.simulator.get_link_elements("InitializeParticipant")
        self.simulator.open_links(link_elements)

        # num_players = len(player_links)
        # print(f'{num_players} player links were found.')

        # create a new tab for each player
        # for player in range(1, num_players + 1):
        #     driver.switch_to.window(driver.window_handles[0])
        #     player_links[player-1].send_keys(Keys.COMMAND + Keys.ENTER)
        #     time.sleep(1)
        #     print(f'Created player tab {player}.')

    @staticmethod
    def command_line_args():
        parser = ArgumentParser(description='Parse arguments to the selenium simulator')
        parser.add_argument('part', metavar='N', type=int, help='list of experiment parts to run')
        parser.add_argument('--quit', action='store_true', help='Do not quit at end')
        args = parser.parse_args()
        return (args.part, args.quit)


class Simulator:
    chrome_options = ['--disable-infobars', '--window-size=1200,900', '--disable-device-discovery-notifications']

    def __init__(self):
        self.driver = Chrome(options=self.options())
        self.driver.implicitly_wait(30)

    def get_link_elements(self, txt):
        return self.driver.find_elements_by_partial_link_text(txt)

    def open_url(self, url):
        self.driver.get(url)

    def open_links(self, link_elements):
        for index, link_element in enumerate(link_elements):
            self.go_to_browser_tab(1)
            link_element.send_keys(Keys.COMMAND + Keys.ENTER)
            WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) != index + 1)

    def go_to_browser_tab(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number - 1])

    def options(self):
        chrome_options = ChromeOptions()
        for option in self.chrome_options:
            chrome_options.add_argument(option)
        return chrome_options



# Run with python -m selenium.simulator
if __name__ == "__main__":
    game = Game()
    game.run()
    #
    # args = command_line_args()
    # part = args.part
    # quit_at_end = args.quit
    #
    # driver = init_driver()
    # open_player_tabs(driver)
    #
    # # create a new tab for each player
    # for player in range(1, num_players + 1):
    #     driver.switch_to.window(driver.window_handles[0])
    #     player_links[player-1].send_keys(Keys.COMMAND + Keys.ENTER)
    #     time.sleep(1)
    #     print(f'Created player tab {player}.')
    #
    # # Part 1: Preference selection phase
    # lottery_pairs = 8
    # if 1 <= part:
    #     for round_id in range(1, lottery_pairs + 1):
    #         for player in range(1, num_players + 1):
    #             # switch to new tab
    #             print("window handles: {}".format(len(driver.window_handles)))
    #             driver.switch_to.window(driver.window_handles[player])
    #             instructions(driver)
    #             time.sleep(.5)
    #             choose_lottery(driver, round_id, player)
    #             time.sleep(.5)
    #
    # if 2 <= part:
    #     for round_id in range(1, lottery_pairs + 1):
    #         for player in range(1, num_players + 1):
    #             # switch to new tab
    #             if num_players > 1:
    #                 driver.switch_to.window(driver.window_handles[player])
    #             instructions(driver)
    #             time.sleep(.5)
    #             allocate_lottery_pair_time(driver, round_id, player)
    #             time.sleep(.5)
    #
    # if 3 <= part:
    #     for round_id in range(1, lottery_pairs + 1):
    #         for player in range(1, num_players + 1):
    #             # switch to new tab
    #             if num_players > 1:
    #                 driver.switch_to.window(driver.window_handles[player])
    #             instructions(driver)
    #             hold_wait_page(driver, 1984)
    #             task_alpha(driver)
    #             # hold_wait_page(driver, HoldWaitPageTwo.pass_code)
    #             # task_two(driver, player)
    #             # hold_wait_page(driver, HoldWaitPageThree.pass_code)
    #             # bet_case_select_task(driver, player, 3)
    #             # # Task 4 is the same as three
    #             # hold_wait_page(driver, HoldWaitPageFour.pass_code)
    #             # bet_case_select_task(driver, player, 4)
    #             # hold_wait_page(driver, HoldWaitPageFive.pass_code)
    #             # task_five(driver, player, 5)
    #             # # Task 6
    #             # hold_wait_page(driver, HoldWaitPageSix.pass_code)
    #             # task_five(driver, player, 6)
    #             # # Task 7
    #             # hold_wait_page(driver, HoldWaitPageSeven.pass_code)
    #             # task_seven(driver, player, 7)
    #             # # Task 8
    #             # hold_wait_page(driver, HoldWaitPageEight.pass_code)
    #             # task_eight(driver, player)
    #             # # Task 9
    #             # task_nine(driver, player)
    #
    # if 4 <= part:
    #     for round_id in range(1, lottery_pairs + 1):
    #         for player in range(1, num_players + 1):
    #             # switch to new tab
    #             if num_players > 1:
    #                 driver.switch_to.window(driver.window_handles[player])
    #             instructions(driver)
    #             practice_maze(driver)
    #
    # if quit_at_end:
    #     driver.quit()
