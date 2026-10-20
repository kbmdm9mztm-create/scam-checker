
from scam_rules import analyze

TEST_MESSAGES = [

    {
        "name": "Normal message with a link",
        "text": "Hi, here are the photos from yesterday: https://example.com/photos",
        "expected": "No obvious red flags",
    },
    {
        "name": "Fake delivery fee",
        "text": "Your parcel is held. Pay a delivery fee now at bit.ly/parcel123",
        "expected": "Likely scam",
    },
    {
        "name": "Bank security warning",
        "text": "Never share your one-time code with anyone, including bank staff.",
        "expected": "No obvious red flags",
    },

]

passed = 0

for test in TEST_MESSAGES:
    result = analyze(test["text"])
    actual = result["verdict"]
    success = actual == test["expected"]

    if success:
        passed += 1

    print(f"\nTest: {test['name']}")
    print(f"Expected: {test['expected']}")
    print(f"Actual:   {actual}")
    print(f"Score:    {result['score']}")
    print(f"Result:   {'PASS' if success else 'FAIL'}")

    for reason in result["reasons"]:
        print(f"  - {reason['name']}: {reason['why']}")

print(f"\nPassed {passed}/{len(TEST_MESSAGES)} tests.")
