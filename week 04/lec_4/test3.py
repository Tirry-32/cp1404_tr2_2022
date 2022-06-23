scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
if len(scores) > 0:
    print("Your highest score is", max(scores))
else:
    print("empty list")
