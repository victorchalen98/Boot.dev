from l12_mount_rental import *

run_cases = [
    (3, 4, "no charges yet"),
    (5, 2, "overtime charged"),
]

submit_cases = run_cases + [
    (2, 2, "overtime charged"),
    (0, 1, "no charges yet"),
    (1, 1, "overtime charged"),
    (100, 2, "overtime charged"),
    (2500, 3, "overtime charged"),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = check_mount_rental(input1, input2)
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
