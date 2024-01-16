import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def one_more_print(name):
    print(f'Hello, {name} {name}')


def make_request():
    return requests.get("https://www.google.com.ua/")


def loop():
    count = 0
    while count < 5:
        count += 1
        print(f"Iteration no. {count}")
    else:
        print("While loop over. Now in else block")
    print("End of while loop")


# to skip test
# @pytest.mark.skip("outdated")
def test_google():
    response = make_request()
    expected_code = 400
    assert response.status_code == expected_code, \
        f"Actual status code {response.status_code} differs from expected {expected_code}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_request()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
