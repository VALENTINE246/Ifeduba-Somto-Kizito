def grading(value):
  if value >= 70 and value <= 100:
    return "A"
  elif value >= 60 and value < 70:
    return "B"
  elif value >= 50 and value < 60:
    return "C"
  elif value >= 45 and value < 50:
    return "D"
  elif value >= 0 and value < 40:
    return "F"
  
score = float(input("Enter your score: "))

if score < 0 or score > 100:
  print("Score must be between 0 - 100")
else:
  grade = grading(score)
  print(f"Grade: {grade}")