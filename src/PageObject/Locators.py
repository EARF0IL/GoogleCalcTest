class GoogleCalcPageLocator:
    memory = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/span'  # expression in memory
    result = '//*[@id="cwos"]'
    num_button = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[{}]/div/div'
    algebraic_button = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[{}]/td[4]/div/div'
    equal_button = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div'


class GoogleHomePageLocator:
    searching_bar = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    searching_button = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]'
