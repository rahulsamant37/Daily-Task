"""
🔍 Question:
You are given a dataset of students with their scores in different subjects as a list of dictionaries. Each dictionary represents one student.

Write a Python function top_performers(data, min_avg_score) that returns a list of names of students whose average score is greater than or equal to min_avg_score.

Use an inbuilt dataset structured like this (in your example):
"""
students_data = [
    {"name": "Alice", "scores": {"math": 88, "science": 92, "english": 85}},
    {"name": "Bob", "scores": {"math": 70, "science": 65, "english": 72}},
    {"name": "Charlie", "scores": {"math": 95, "science": 98, "english": 100}},
    {"name": "Diana", "scores": {"math": 60, "science": 70, "english": 58}},
]
def top_performers(data, min_avg_score):
    return [
        student["name"]
        for student in data
        if (sum(student["scores"].values()) / len(student["scores"])) >= min_avg_score
    ]

# Example usage with the inbuilt dataset
students_data = [
    {"name": "Alice", "scores": {"math": 88, "science": 92, "english": 85}},
    {"name": "Bob", "scores": {"math": 70, "science": 65, "english": 72}},
    {"name": "Charlie", "scores": {"math": 95, "science": 98, "english": 100}},
    {"name": "Diana", "scores": {"math": 60, "science": 70, "english": 58}},
]

print(top_performers(students_data, 85))
# Output: ['Alice', 'Charlie']
