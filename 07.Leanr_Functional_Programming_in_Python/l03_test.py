from l03_immutability import *

run_cases = [
    (
        ("hello there", "sonny", "how ya doing"),
        ("0. hello there", "1. sonny", "2. how ya doing"),
    )
]

submit_cases = run_cases + [
    (
        ("go", "python", "java", "javascript"),
        ("0. go", "1. python", "2. java", "3. javascript"),
    ),
    (
        ("boots", "everyone else"),
        ("0. boots", "1. everyone else"),
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * documents: {input1}")
    print(f"Expected: {expected_output}")
    try:
        documents = ()
        for doc in input1:
            documents = add_prefix(doc, documents)
    except Exception as e:
        documents = f"Error: {e}"
    print(f"Actual: {documents}")
    if documents == expected_output:
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
