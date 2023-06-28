# @TODO: Your code here
hobbyBook = {
    "Name": "Peter Solis",
    "Age": "21",
    "Hobbies": ["Video Games","Reading","Trivia"],
    "Wake Time": {
        "Monday": "8:00am",
        "Saturday": "10:00am",
        "Sunday": "8:30am"
    }
}

print(f'I am {hobbyBook["Name"]}, I am {hobbyBook["Age"]} years old, and enjoy {hobbyBook["Hobbies"][0]} and {hobbyBook["Hobbies"][1]}. On Monday I wake up at {hobbyBook["Wake Time"]["Monday"]}.')