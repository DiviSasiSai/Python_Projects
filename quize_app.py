import numpy as np

india_gk = {
    "What is the capital of India?": "New Delhi",
    "Who was the first Prime Minister of India?": "Jawaharlal Nehru",
    "Which river is considered the holiest in India?": "Ganga (Ganges)",
    "Who wrote the Indian national anthem?": "Rabindranath Tagore",
    "What is the national animal of India?": "Bengal Tiger",
    "In which year did India gain independence?": "1947",
    "Which Indian city is known as the 'Pink City'?": "Jaipur",
    "What is the currency of India?": "Indian Rupee (INR)",
    "Who is known as the Father of the Nation in India?": "Mahatma Gandhi",
    "Which monument is also known as the symbol of love in India?": "Taj Mahal"
}
score = 0

questions = np.random.permutation(list(india_gk.keys()))

print("Welcome to India GK")
for question in questions:
    ans = input(question+": ")
    if ans == india_gk[question]:
        score +=1
        print(f"Correct answer... Got 1 score.")
    else:
        print("Incorrect answer...")
print(f"Total score: {score}/10")

