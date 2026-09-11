import json

def json_reader():
    data=[]
    try:
        file_path=input('Enter the file path of your json file:  ')
        with open(file_path,'r') as file:
            data=json.load(file)
        return data
    except json.JSONDecodeError:
        print('Invalid JSON file')
    except FileNotFoundError:
        print('file not found')


def show_data(file_path):
    for item in file_path:
        print(f"Name:{item['name']}, Type: {item['type']},Level:{item['level']}")


def main():
    my_data=json_reader()
    while my_data is None:
            my_data=json_reader()
            if my_data is not None:
                break
    show_data(my_data)

if __name__=='__main__':
    main()

    