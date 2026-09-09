import csv

def ask_user():
    classification=input("Which videogame's classification are you looking for?:  ")
    classification=classification.upper()
    return classification   


def classification_importer(file_path,classif):
    video_games=" "
    with open(file_path, 'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for line in reader:
            if line['classification']==classif:
                video_games+="\n"+line['name']+ "\n"
            else:
                continue
    return video_games


def main():
    while True:
        classification=ask_user()
        my_video_games=classification_importer('Ejercicios de manejo de CSV/my_videogames.csv', classification)
        if my_video_games!=" ":
            print(f"I've found the following videos games with {classification} classification: {my_video_games}")
            break
        else:
            print("This classification was not found, please try again")
        

if __name__=='__main__':
    main()


