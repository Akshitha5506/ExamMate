import json

def get_question(subject):
    try:
        with open(f"dataset/{subject}.json", "r") as file:
            data = json.load(file)
            return data["questions"][0]
    except:
        return "Sorry,the selected subject is not found"
