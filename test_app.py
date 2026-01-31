import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from app import app

@pytest.fixture
def dash_duo(dash_duo):
    # This specifically tells the manager to go find version 144
    # which matches your browser version 144.0.7559.110
    driver_path = ChromeDriverManager(driver_version="144.0.7559.109").install()
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    dash_duo.driver = webdriver.Chrome(service=ChromeService(driver_path), options=options)
    yield dash_duo
    dash_duo.driver.quit()

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=15)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualiser"

def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph", timeout=15)
    assert dash_duo.find_element("#sales-graph") is not None

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=15)
    assert dash_duo.find_element("#region-filter") is not None