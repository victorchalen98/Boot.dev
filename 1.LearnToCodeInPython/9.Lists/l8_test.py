from l8_appending_in_python import *

run_cases = [
    (5, list(range(5))),
    (10, list(range(10))),
]

submit_cases = run_cases + [
    (0, []),
    (1, [0]),
    (100, list(range(100))),
    (25, list(range(25))),
    (50, list(range(50))),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = generate_user_list(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
