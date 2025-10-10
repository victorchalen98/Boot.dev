from l13_find_an_item_in_a_list import *

run_cases = [
    (["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"], True),
    (["Potion", "Shortsword", "Buckler", "Iron Mace"], False),
]

submit_cases = run_cases + [
    ([], False),
    (["Leather Scraps"], True),
    (["Potion", "Leather Scraps", "Leather Scraps"], True),
    (["Potion", "Healing Potion"], False),
    (["Leather scraps"], False),
    (["Leather", "Scraps"], False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = contains_leather_scraps(input1)
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
