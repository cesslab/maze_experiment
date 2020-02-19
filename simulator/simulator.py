import random
import math
import time
import os
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
        (self.part, self.quit_game, self.tasks, self.heroku, self.pics) = Game.command_line_args()

    def run(self):

        print(self.heroku)
        if self.heroku:
            self.simulator.open_url(os.environ.get('HEROKU_URL'))
            self.login(os.environ.get('HEROKU_LOGIN'), os.environ.get('HEROKU_PASS'))
            self.simulator.open_link_in_current_tab('Maze Experiment')
            self.simulator.open_links('InitializeParticipant')
        else:
            self.simulator.open_url(os.environ.get('EXPERIMENT_URL'))
            self.simulator.open_links('InitializeParticipant')

        # Select preferred lottery from each pair
        if self.part >= 1:
            self.play_part_one()

        # Enter time to solve maze in each pair
        if self.part >= 2:
            self.play_part_two()

        # Tasks
        if self.part >= 3:
            self.play_part_three(self.tasks)

        # Solve maze for part 1
        if self.part >= 4:
            self.play_part_four()

        # Solve maze for part 2
        if self.part >= 5:
            self.play_part_five()

        # Payoffs
        if self.part >= 6:
            self.play_part_six()

        # Questionnaire
        if self.part >= 7:
            self.play_part_seven()

        if self.quit_game:
            self.quit()

    def login(self, login, password):
        self.enter_input('id_username', login)
        self.enter_input('id_password', password)
        self.next_button('btn-login')

    def play_part_one(self):
        print("Playing part 1")
        lottery_pairs = 7
        self.simulator.go_to_tab(1)
        for round_id in range(1, lottery_pairs + 1):
            print(f"round {round_id}")
            self.screenshot(f'part_1_round_{round_id}_instructions')
            self.instructions()
            self.screenshot(f'part_1_round_{round_id}_lottery_selection')
            self.choose_lottery()

    def play_part_two(self):
        print("Playing part 2")
        lottery_pairs = 7
        for round_id in range(1, lottery_pairs + 1):
            print(f"round {round_id}")
            self.screenshot(f'part_2_round_{round_id}_instructions')
            self.instructions()
            self.screenshot(f'part_2_round_{round_id}_time_allocation')
            self.allocate_time()

    def play_part_three(self, tasks):
        print("Playing part 3")
        self.instructions()
        if tasks >= 1:
            self.enter_pass_code('1984')
            self.screenshot(f'part_3_task_1')
            self.task_one()
        if tasks >= 2:
            self.enter_pass_code('1959')
            self.screenshot(f'part_3_task_2')
            self.task_two()
        if tasks >= 3:
            self.enter_pass_code('1914')
            self.screenshot(f'part_3_task_3')
            self.task_three()
        if tasks >= 4:
            self.enter_pass_code('1929')
            self.screenshot(f'part_3_task_4')
            self.task_four()
        if tasks >= 5:
            self.enter_pass_code('1945')
            self.screenshot(f'part_3_task_5')
            self.task_five()
        if tasks >= 6:
            self.enter_pass_code('1492')
            self.screenshot(f'part_3_task_6')
            self.task_six()
        if tasks >= 7:
            self.enter_pass_code('1776')
            self.screenshot(f'part_3_task_7')
            self.task_seven()
        if tasks >= 8:
            self.enter_pass_code('2020')
            self.screenshot(f'part_3_task_8')
            self.task_eight()

    def play_part_four(self):
        self.screenshot(f'part_4_instructions')
        self.instructions()
        self.screenshot(f'part_4_practice_maze')
        self.practice_maze()
        self.screenshot(f'part_4_outcome')
        self.part_one_outcome()
        self.screenshot(f'part_4_maze_prompt')
        self.maze_prompt()
        self.screenshot(f'part_4_maze_play')
        self.maze()

    def play_part_five(self):
        self.screenshot(f'part_5_instructions')
        self.instructions()
        self.screenshot(f'part_5_left_lottery_maze_prompt')
        self.maze_prompt()
        self.screenshot(f'part_5_left_lottery_maze')
        self.maze()
        self.screenshot(f'part_5_right_lottery_maze_prompt')
        self.maze_prompt()
        self.screenshot(f'part_5_right_lottery_maze')
        self.maze()

    def play_part_six(self):
        self.screenshot(f'part_6_payoff_screen')
        self.next_button('next-button')

    def play_part_seven(self):
        self.demographic()
        self.questionnaire()

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

    def demographic(self):
        self.enter_input('id_gender', ['male', 'female'][random.randint(0, 1)])
        self.enter_input('id_age', random.randint(18, 70))
        self.enter_input('id_major', ['CS', 'Math', 'Econ', 'English Lit', 'Philosophy'][random.randint(0, 4)])
        self.enter_input('id_year_in_college', [1, 2, 3, 4, 5][random.randint(0, 4)])
        self.next_button('task-next-button')

    def questionnaire(self):
        lorem = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin molestie nunc at posuere.
        Vestibulum ac suscipit lorem. Praesent lobortis tempus quam vitae fermentum. Etiam et lacinia ex.
        Donec laoreet interdum felis, sit amet rutrum augue euismod non. Lorem ipsum dolor sit amet,
        consectetur adipiscing elit. Nulla facilisi. Aliquam non ultrices odio. Nulla interdum arcu sed justo mollis,
        sit amet facilisis justo efficitur. Pellentesque habitant morbi tristique senectus et netus et malesuada
        fames ac turpis egestas. Maecenas vitae odio nulla. Duis efficitur sapien at nibh dapibus, in ullamcorper leo
        porta. Proin eget massa sit amet dolor ullamcorper dignissim eu eleifend massa. Phasellus mattis gravida
        placerat. Vestibulum at molestie mauris. Ut viverra porta tellus a fermentum. Sed tempus varius venenatis.
        Ut at neque sed purus semper rhoncus. Pellentesque eu maximus orci. Sed sit amet nisl orci. Curabitur ut
        ultrices nulla. Etiam faucibus lacus pulvinar dui pellentesque porttitor. Donec tempor velit a leo lacinia,
        eget egestas erat tempus. Integer magna arcu, fringilla nec iaculis vel, interdum et quam. Praesent a mauris
        ex.
        """
        for i in range(1, 8):
            start = random.randint(0, math.floor(len(lorem)/4))
            end = math.ceil(random.randint(start + 8, math.ceil(3*len(lorem)/4)))
            self.enter_input(f'id_q{i}', lorem[start:end])
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

    def screenshot(self, screen_name):
        screenshot_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.environ.get('SCREENSHOT_DIR'))
        img = os.path.join(screenshot_directory, screen_name + '.png')
        self.simulator.driver.save_screenshot(img)

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
        parser.add_argument('--part', metavar='P', type=int, default=7, help='list of experiment parts to run')
        parser.add_argument('--tasks', metavar='T', type=int, default=8, help='Tasks to complete in part 3')
        parser.add_argument('--quit', action='store_true', default=False, help='Do not quit at end')
        parser.add_argument('--heroku', action='store_true', default=False, help='Login to Heroku')
        parser.add_argument('--pics', action='store_true', default=False, help='Take screenshots')
        args = parser.parse_args()
        return args.part, args.quit, args.tasks, args.heroku, args.pics


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

    def open_url(self, url):
        self.driver.get(url)
        time.sleep(.5)

    def go_to_tab(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])

    def open_link_in_current_tab(self, link_text):
        link = self.driver.find_element_by_partial_link_text(link_text)
        self.open_url(link.get_attribute('href'))
        time.sleep(.5)

    def open_link(self, link_text):
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text)))
        except TimeoutException:
            print(f"Failed waiting for link with text '{link_text}'")
            self.quit()

        link = self.driver.find_element_by_link_text(link_text)
        link.click()
        time.sleep(1)


    def open_links(self, link_text):
        # try:
        #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text)))
        # except TimeoutException:
        #     print(f"Failed waiting for link with text '{link_text}'")
        #     self.quit()

        print(f'opening link with text {link_text}')

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
