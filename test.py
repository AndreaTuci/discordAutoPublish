import pytest

target = __import__('dabot')

# from dabot import
# click = target.click_btn
#
# def test_click():
#     assert type(click('markeplace.png')) == "<class 'pyscreeze.Box'>"[1:-1], 'Messaggio'

def split_list(list):
    print(list)
    first, *_, last = iter(list)
    return first, last


def test_split_first():
    assert split_list([1,3,5,7,8,9]) == (1, 9), 'Il risultato dovrebbe essere 1'

    # click_first_btn('declan.png')
    # pyautogui.moveTo(36, 108)
    # pyautogui.leftClick()