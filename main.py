from selenium import webdriver

nameplate = "MDX61B0110"

driver = webdriver.Chrome()
for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            serial_number = f"25.81873{x}{y}{z}01.0001.20"
            print(serial_number)
            url = f"https://www.sew-eurodrive.de/os/ecs/?SEARCH_STRING={serial_number}"
            driver.set_window_position(0, 0)
            driver.set_window_size(1280, 720)
            driver.get(url)
            main_page = driver.page_source
            if nameplate in main_page:
                print(f"Find {nameplate} in: {serial_number}")
                break
