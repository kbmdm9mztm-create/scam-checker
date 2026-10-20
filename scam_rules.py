import re

# Each rule: (name, pattern to look for, points, plain-English reason)
RULES = [
    ("Urgency",
     r"\b(urgent|immediately|act now|last chance|final notice|within \d+ (hours|minutes)|expires? (today|soon))\b",
     2, "Scammers rush you so you don't stop and think."),
    ("Account threat",
     r"(account (has been |is )?(suspended|locked|blocked|compromised|closed)|unusual activity|verify your (account|identity))",
     3, "Threats about your account are a common trick to make you click."),
    ("Asks for secret details",
     r"(password|\bpin\b|\botp\b|one.?time (code|passcode)|verification code|card number|\bcvv\b|security code)",
     3, "Real companies don't ask you to send codes or passwords by message."),
    ("Prize or refund bait",
     r"(you('ve| have) won|\bprize\b|lottery|claim your|\brefund\b|gift card|bitcoin|crypto)",
     2, "Surprise money or prizes are a classic lure."),
    ("Delivery bait",
     r"(parcel|package).{0,40}(could not|couldn't|unable to|waiting|held)|redelivery|delivery fee",
     2, "Fake delivery problems are a very common scam."),
    ("Shortened link",
     r"(bit\.ly|tinyurl|t\.co/|goo\.gl|is\.gd|cutt\.ly)",
     3, "Short links hide where they really go."),
    ("Odd link ending",
     r"\.(xyz|top|click|buzz|live|icu)\b",
     2, "Scam sites often use unusual web address endings."),
    ("Contains a link",
     r"(https?://|www\.)",
     1, "Links in unexpected messages deserve caution."),
    ("Generic greeting",
     r"dear (customer|user|client|sir|madam|account holder)",
     1, "Real companies usually use your actual name."),
]


def analyze(text):
    score = 0
    reasons = []

    for name, pattern, points, why in RULES:
        if re.search(pattern, text, re.IGNORECASE):
            score += points
            reasons.append({"name": name, "points": points, "why": why})

    if score >= 6:
        verdict = "Likely scam"
    elif score >= 3:
        verdict = "Suspicious"
    else:
        verdict = "No obvious red flags"

    return {"verdict": verdict, "score": score, "reasons": reasons}


if __name__ == "__main__":
    samples = [
        "URGENT: Your account has been suspended. Verify your identity within 24 hours: bit.ly/x1y2",
        "Hi mum, I'll be home around 6. Can you pick up milk?",
    ]
    for s in samples:
        print(s)
        print(analyze(s))
        print()