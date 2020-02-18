import random
import time
from os import environ
from contextlib import contextmanager

from argparse import ArgumentParser

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Game:
    def __init__(self):
        self.simulator = Simulator()

    def run(self):
        (part, quit_game, tasks) = Game.command_line_args()

        self.simulator.open_url(environ.get('EXPERIMENT_URL'), 'Maze Experiment')
        self.simulator.open_links('InitializeParticipant')

        if part >= 1:
            self.play_part_one()

        if part >= 2:
            self.play_part_two()

        if part >= 3:
            self.play_part_three(tasks)

        if part >= 4:
            self.play_part_four()

        if part >= 5:
            self.play_part_five()

        if part >= 6:
            self.play_part_six()

        if quit_game:
            self.quit()

    def play_part_one(self):
        print("Playing part 1")
        lottery_pairs = 7
        self.simulator.go_to_tab(1)
        for round_id in range(1, lottery_pairs + 1):
            print(f"round {round_id}")
            self.instructions()
            self.choose_lottery()

    def play_part_two(self):
        print("Playing part 2")
        lottery_pairs = 7
        for round_id in range(1, lottery_pairs + 1):
            print(f"round {round_id}")
            self.instructions()
            self.allocate_time()

    def play_part_three(self, tasks):
        print("Playing part 3")
        self.instructions()
        if tasks >= 1:
            self.enter_pass_code('1984')
            self.task_one()
        if tasks >= 2:
            self.enter_pass_code('1959')
            self.task_two()
        if tasks >= 3:
            self.enter_pass_code('1914')
            self.task_three()
        if tasks >= 4:
            self.enter_pass_code('1929')
            self.task_four()
        if tasks >= 5:
            self.enter_pass_code('1945')
            self.task_five()
        if tasks >= 6:
            self.enter_pass_code('1492')
            self.task_six()
        if tasks >= 7:
            self.enter_pass_code('1776')
            self.task_seven()
        if tasks >= 8:
            self.enter_pass_code('2020')
            self.task_eight()

    def play_part_four(self):
        self.instructions()
        self.practice_maze()
        self.part_one_outcome()
        self.maze_prompt()
        self.maze()

    def play_part_five(self):
        self.instructions()
        self.maze_prompt()
        self.maze()
        self.maze_prompt()
        self.maze()

    def play_part_six(self):
        self.next_button('next-button')

    def task_one(self):
        self.sub_task('a')
        self.sub_task('b')
        self.sub_task('c')
        self.next_button('task-next-button')

    def task_two(self):
        self.sub_task('a')
        self.sub_task('b')
        self.next_button('task-next-button')

    def task_three(self):
        self.enter_input('id_task_gamma_1', random.randint(0, 100))
        self.enter_input('id_task_gamma_2', random.randint(0, 100))
        self.enter_input('id_task_gamma_3', random.randint(0, 100))
        self.enter_input('id_task_gamma_4', random.randint(0, 100))
        self.next_button('task-next-button')

    def task_four(self):
        self.click(['left_label', 'middle_label', 'right_label'][random.randint(0, 2)])
        self.next_button('task-next-button')

    def task_five(self):
        self.sub_task('a')
        self.next_button('task-next-button')

    def task_six(self):
        self.enter_input('task_input', random.randint(1, 100))
        self.click(['inlineRadio1', 'inlineRadio2'][random.randint(0, 1)])
        self.enter_input('confidence_input', random.randint(0, 100))
        self.next_button('task-next-button')

    def task_seven(self):
        self.enter_input('task_input', random.randint(0, 100))
        self.next_button('task-next-button')

    def task_eight(self):
        self.enter_input('task_input', random.randint(0, 100))
        self.next_button('task-next-button')

    def practice_maze(self):
        self.next_button('next-button')

    def part_one_outcome(self):
        self.next_button('next-button')

    def maze_prompt(self):
        self.next_button('next-button')

    def maze(self):
        seconds_to_solve = int(self.js_var_value('secondsToSolve'))
        print(f"seconds to solve {seconds_to_solve}")
        if seconds_to_solve > 0:
            time.sleep(seconds_to_solve+2)

        solved = random.randint(0, 1)
        print('Did not solved maze' if solved == 0 else 'Solved maze')
        if solved == 0:
            self.enter_hidden_input('solved', 0)
            self.enter_hidden_input('solve_time_seconds', seconds_to_solve)
        else:
            self.enter_hidden_input('solved', 1)
            self.enter_hidden_input('solve_time_seconds', random.randint(1, seconds_to_solve - 1))

        self.next_button('next-button')

    def js_var_value(self, var_name):
        return self.simulator.get_js_var_value(var_name)

    def sub_task(self, sub_task_id):
        option = ['lottery', 'maze'][random.randint(0, 1)]
        case = random.randint(1, 11)
        self.click(f"{sub_task_id}_{option}_{case}")

    def enter_pass_code(self, pass_code):
        self.enter_input('pass_code', pass_code)
        self.next_button('next-button')

    def allocate_time(self):
        random_side = random.randint(1, 2)
        # Left
        if random_side == 1:
            self.enter_input('left_lottery_time', random.randint(0, 120))
        # Right
        else:
            self.enter_input('right_lottery_time', random.randint(0, 120))

        self.next_button('allocation-next-button')

    def instructions(self):
        self.next_button('instructions-next-button')

    def choose_lottery(self):
        self.click(f"id-preference-{random.randint(0, 2)}")
        self.next_button('choice-next-button')

    def next_button(self, element_id):
        time.sleep(.5)
        self.simulator.click_continue_button(element_id)
        time.sleep(.5)

    def enter_input(self, element_id, value):
        e = self.simulator.get_element_by_id(element_id)
        e.clear()
        e.send_keys(str(value))

    def enter_hidden_input(self, element_id, value):
        self.simulator.hidden_input_to_text_input(element_id)
        self.enter_input(element_id, value)

    def click(self, element_id):
        self.simulator.click_element_by_id(element_id)

    def quit(self):
        self.simulator.quit()

    @staticmethod
    def command_line_args():
        parser = ArgumentParser(description='Parse arguments to the selenium simulator')
        parser.add_argument('--part', metavar='P', type=int, default=6, help='list of experiment parts to run')
        parser.add_argument('--tasks', metavar='T', type=int, default=8, help='Tasks to complete in part 3')
        parser.add_argument('--quit', action='store_true', default=False, help='Do not quit at end')
        args = parser.parse_args()
        return args.part, args.quit, args.tasks


class Simulator:
    chrome_options = ['--disable-infobars', '--window-size=1200,900', '--disable-device-discovery-notifications']

    def __init__(self):
        self.driver = Chrome(options=self.options())
        self.driver.implicitly_wait(10)

    def quit(self):
        self.driver.quit()

    def hidden_input_to_text_input(self, element_id):
        js = f"document.getElementById('{element_id}').setAttribute('type', 'text');"
        self.driver.execute_script(js)
        time.sleep(.2)

    def click_element_by_id(self, element_id):
        self.wait_for_continue_button(element_id)
        element = self.driver.find_element_by_id(element_id)
        element.click()

    def click_continue_button(self, element_id):
        self.wait_for_continue_button(element_id)
        self.driver.find_element(By.ID, element_id).click()

    def get_element_by_id(self, element_id):
        self.wait_for_element(element_id)
        return self.driver.find_element_by_id(element_id)

    def wait_for_page_with_title(self, title, max_wait_time=10):
        try:
            WebDriverWait(self.driver, max_wait_time).until(EC.title_contains(title))
        except TimeoutException:
            print(f"Failed waiting for page tile {title}")
            self.quit()

    def wait_for_element(self, element_id, max_wait_time=10):
        try:
            WebDriverWait(self.driver, max_wait_time).until(EC.presence_of_element_located((By.ID, element_id)))
        except TimeoutException:
            print(f"Failed waiting for page element with id={element_id}")
            self.quit()

    def wait_for_continue_button(self, button_id, max_wait_time=10):
        try:
            WebDriverWait(self.driver, max_wait_time).until(EC.element_to_be_clickable((By.ID, button_id)))
        except TimeoutException:
            print(f"Failed waiting for continue button with id {button_id}")
            self.quit()

    def open_url(self, url, title):
        self.driver.get(url)
        self.wait_for_page_with_title(title)

    def go_to_tab(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])

    def open_links(self, link_text):
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text)))
        except TimeoutException:
            print(f"Failed waiting for link with text '{link_text}'")
            self.quit()

        links = self.driver.find_elements_by_partial_link_text(link_text)
        for index, link_element in enumerate(links):
            self.go_to_tab(0)

            with self.wait_for_new_tab():
                open_tab_js = 'window.open("{}","_blank");'.format(link_element.get_attribute('href'))
                self.driver.execute_script(open_tab_js)

    def get_js_var_value(self, var_name):
        return self.driver.execute_script(f"return {var_name}")

    def options(self):
        chrome_options = ChromeOptions()
        for option in self.chrome_options:
            chrome_options.add_argument(option)
        return chrome_options

    @contextmanager
    def wait_for_new_tab(self, timeout=10):
        handles_before = len(self.driver.window_handles)
        yield
        WebDriverWait(self.driver, timeout).until(
            lambda driver: handles_before != len(self.driver.window_handles)
        )


# Run with python -m selenium.simulator
if __name__ == '__main__':
    game = Game()
    game.run()
