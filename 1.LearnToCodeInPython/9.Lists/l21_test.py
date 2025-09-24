from l21_tuples import *

run_cases = [
    (
        [
            (
                "Glorfindel",
                2093,
                True,
            ),
            (
                "Gandalf",
                1054,
                False,
            ),
            (
                "Gimli",
                389,
                False,
            ),
            (
                "Aragorn",
                87,
                False,
            ),
        ]
    ),
]

submit_cases = run_cases


def test(expected_output):
    print("---------------------------------")
    passed = True
    result = get_heroes()
    if not isinstance(result, list):
        print("Expected result to be a list")
        return False

    for i, hero in enumerate(expected_output):
        print(f"Expected: {hero} at index {i}")
        if i >= len(result):
            print(f"Actual: None at index {i}")
            print("Fail")
            passed = False
            continue
        print(f"Actual: {result[i]} at index {i}")
        if hero != result[i]:
            print("Fail")
            passed = False
        else:
            print("Pass")
    return passed


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
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
