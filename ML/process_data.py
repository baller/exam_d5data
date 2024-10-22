import json
import re
from datetime import datetime

# Initialize an empty list to store the transformed data
transformed_data = []
# Function to parse the input data and extract questions and answers
id = 0 
def parse_data(input_data):
    global id
    for entry in input_data:
        
        # Split the input text into individual questions and answers
        for paragraph in entry['input'].split("\n\n"):
                # Extract the id, gold_index, and class_id
                entry_id = entry['id']
                gold_index = entry['gold_index']
                class_id = entry['class_id']
                if paragraph.strip()=="":
                    continue
                question, answer = paragraph, paragraph.split(" ")[-1]

                if answer.strip()=="Yes" or answer.strip()=="No":
                    answer = answer.strip()
                    question = question.split("?")[0] + "?"
                else:
                     answer = "No answer"
                     question = question.strip()

                # Add the entry to the transformed data list
                transformed_data.append({
                    "id": id,
                    "origin_id": entry_id,
                    "gold_index": gold_index,
                    "class_id": class_id,
                    "question": question,
                    "answer" : answer
                })
                id+=1

if __name__ == '__main__':

    # Start the timer
    start_time = datetime.now()

    # Load the input data
    with open('/home/user_3/exam_d5data/ML/test.json') as f:
        input_data = json.load(f)
    # Parse the input data
    parse_data(input_data)

    # Calculate the time taken to complete the transformation
    end_time = datetime.now()
    time_taken = end_time - start_time

    # Print the statistics
    print(f"Total number of question-answer pairs extracted: {id}")
    print(f"Time taken to complete the dataset cleanup and transformation process: {time_taken}")

    # Save the transformed data to a JSON file
    with open('./transformed_data.json', 'w') as f:
        json.dump(transformed_data, f, indent=2)