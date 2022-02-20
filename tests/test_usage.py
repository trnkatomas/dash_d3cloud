from selenium.webdriver.chrome.options import Options
from dash.testing.application_runners import import_app

from selenium import webdriver

def pytest_setup_options():
    options = Options()
    options.add_argument('--disable-gpu')
    return options

# Basic test for the component rendering.
def test_render_component(dash_duo):
    app = import_app('usage')
    dash_duo.start_server(app)

    # select the main wordcloud component
    my_component = dash_duo.wait_for_element_by_css_selector('#wordcloud')

    # select one of the options for controlling the input, the last one from the list
    # so we know it will be disabled in the begging
    input_selection = dash_duo.wait_for_element_by_css_selector('#choice > label:last-child')

    # we click it
    input_selection.click()

    # than let's wait again for the svg to render again
    dash_duo.wait_for_element_by_css_selector('#wordcloud > svg > g > text')
