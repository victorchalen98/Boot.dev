from l10_counting_the_items_in_a_list import *

run_cases = [
    (["Bread", "Potion", "Shortsword", "Bread"], (1, 2, 1)),
    (["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"], (2, 0, 1)),
]

submit_cases = run_cases + [
    ([], (0, 0, 0)),
    (
        [
            "Potion",
            "Leather Scraps",
            "Bread",
            "Iron Ore",
            "Light Leather",
            "Bread",
            "Shortsword",
            "Longsword",
            "Ironwood Branch",
            "Shortsword",
            "Shortsword",
        ],
        (1, 2, 3),
    ),
    (["Bread", "Bread", "Bread", "Bread"], (0, 4, 0)),
    (["Shortsword", "Shortsword", "Shortsword", "Shortsword"], (0, 0, 4)),
    (["Potion"], (1, 0, 0)),
    (["Potion", "Bread", "Shortsword"], (1, 1, 1)),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    result = get_item_counts(input)
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
