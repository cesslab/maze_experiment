import random
import os
import glob
from os import environ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def instructions(browser):
    browser.find_element(By.XPATH, '//button').click()


def single_entry_task(browser, browser_tab, task_id):
    task_input = browser.find_element_by_id('task_input')
    max_value = int(task_input.get_attribute('max'))
    entry = random.randint(0, max_value)
    print('Browser Tab {}: For task {}, value {} was entered.'.format(browser_tab, task_id, entry))
    task_input.send_keys(str(entry))

    browser.find_element(By.XPATH, '//button').click()


def choose_lottery(browser, pair_id, browser_tab):
    preference = random.randint(1, 3)
    print('Browser Tab {}: Preferred lottery for pair {} was {}'.format(browser_tab, pair_id, preference))

    element = browser.find_element_by_id('id-preference-{}'.format(preference))
    element.click()
    browser.find_element(By.XPATH, '//button').click()


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


def task_two(browser, browser_tab):
    cases = 10
    choice_labels = ['A', 'B']
    choice_ids = ['a_row_{}', 'b_row_{}']
    for case_id in range(1, cases + 1):
        random_choice = random.randint(0, 1)
        choice = choice_ids[random_choice]
        print('Browser Tab {}: For task 2 Case {}, option {} was chosen.'.format(browser_tab, case_id, choice_labels[random_choice]))
        element = browser.find_element_by_id(choice.format(case_id))
        element.click()
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

# Run with python -m selenium.simulator
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument('--window-size=1200,900')
    chrome_options.add_argument("--disable-device-discovery-notifications")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)

    driver.get(environ.get('EXPERIMENT_URL'))
    player_links = driver.find_elements_by_partial_link_text("InitializeParticipant")
    print('there are {} players'.format(len(player_links)))

    # create a new tab for each player
    for player in range(1, len(player_links) + 1):
        driver.switch_to.window(driver.window_handles[0])
        player_links[player-1].send_keys(Keys.COMMAND + Keys.ENTER)

    # Preference selection phase
    lottery_pairs = 4
    for round_id in range(1, lottery_pairs + 1):
        for player in range(1, len(player_links) + 1):
            # switch to new tab
            driver.switch_to.window(driver.window_handles[player])
            if round_id == 1:
                instructions(driver)
            choose_lottery(driver, round_id, player)

    for round_id in range(1, lottery_pairs + 1):
        for player in range(1, len(player_links) + 1):
            # switch to new tab
            driver.switch_to.window(driver.window_handles[player])
            if round_id == 1:
                instructions(driver)
            allocate_lottery_pair_time(driver, round_id, player)

    for round_id in range(1, lottery_pairs + 1):
        for player in range(1, len(player_links) + 1):
            # switch to new tab
            driver.switch_to.window(driver.window_handles[player])
            if round_id == 1:
                instructions(driver)
            task_one(driver, player)
            task_two(driver, player)
            bet_case_select_task(driver, player, 3)
            # Task 4 is the same as three
            bet_case_select_task(driver, player, 4)
            single_entry_task(driver, player)
