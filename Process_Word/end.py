from ast import Lambda, literal_eval
import json
from tkinter import E
from tokenize import String
import ast


json_file = "letter_po.json"

with open(json_file) as alphabets:
    data = json.load(alphabets)


   # letter_1_word = data["alphabets"][0]["letter_1"]["letter"]
   # letter_1_isGreen = bool(data["alphabets"][0]["letter_1"][0]["IsGreen"])
   # letter_1_isYellow = bool(data["alphabets"][0]["letter_1"][0]["IsYellow"])
   # letter_1_isGray = bool(data["alphabets"][0]["letter_1"][0]["IsGray"])
    
    letter_1 = {
        "word": data["alphabets"][0]["letter_1"][0]["letter"],
        "isGreen": bool(data["alphabets"][0]["letter_1"][0]["IsGreen"]),
        "isYellow": bool(data["alphabets"][0]["letter_1"][0]["IsYellow"]),
        "isGray": bool(data["alphabets"][0]["letter_1"][0]["IsGray"]),
        "index": int(data["alphabets"][0]["letter_1"][0]["index"])
    }
      
    letter_2 = {
        "word": data["alphabets"][0]["letter_2"][0]["letter"],
        "isGreen": bool(data["alphabets"][0]["letter_2"][0]["IsGreen"]),
        "isYellow": bool(data["alphabets"][0]["letter_2"][0]["IsYellow"]),
        "isGray": bool(data["alphabets"][0]["letter_2"][0]["IsGray"]),
        "index": int(data["alphabets"][0]["letter_2"][0]["index"])
    }    
    letter_3 = {
        "word": data["alphabets"][0]["letter_3"][0]["letter"],
        "isGreen": bool(data["alphabets"][0]["letter_3"][0]["IsGreen"]),
        "isYellow": bool(data["alphabets"][0]["letter_3"][0]["IsYellow"]),
        "isGray": bool(data["alphabets"][0]["letter_3"][0]["IsGray"]),
        "index": int(data["alphabets"][0]["letter_3"][0]["index"])
    }    
    letter_4 = {
        "word": data["alphabets"][0]["letter_4"][0]["letter"],
        "isGreen": bool(data["alphabets"][0]["letter_4"][0]["IsGreen"]),
        "isYellow": bool(data["alphabets"][0]["letter_4"][0]["IsYellow"]),
        "isGray": bool(data["alphabets"][0]["letter_4"][0]["IsGray"]),
        "index": int(data["alphabets"][0]["letter_4"][0]["index"])
    }    
    letter_5 = {
        "word": data["alphabets"][0]["letter_5"][0]["letter"],
        "isGreen": bool(data["alphabets"][0]["letter_5"][0]["IsGreen"]),
        "isYellow": bool(data["alphabets"][0]["letter_5"][0]["IsYellow"]),
        "isGray": bool(data["alphabets"][0]["letter_5"][0]["IsGray"]),
        "index": int(data["alphabets"][0]["letter_5"][0]["index"])
    }
    letters = [letter_1, letter_2, letter_3, letter_4, letter_5]

    isLetterPresentinIndexWordOne = False
    isLetterYellowInWordOne = False
    isLetterPresentInWordOne = False

    isLetterTwoPresentinIndexWordOne = False
    isLetterTwoYellowInWordOne = False
    isLetterTwoPresentInWordOne = False

    isLetterThreePresentinIndexWordOne = False
    isLetterThreeYellowInWordOne = False
    isLetterThreePresentInWordOne = False

    isLetteFourPresentinIndexWordOne = False
    isLetteFourYellowInWordOne = False
    isLetteFourPresentInWordOne = False

    isLetteFivePresentinIndexWordOne = False
    isLetteFiveYellowInWordOne = False
    isLetteFivePresentInWordOne = False

    for dict_item in letters:
        if dict_item["index"] == 1:
            print(dict_item["word"])
            if dict_item["isGreen"] is False:
                isLetterPresentinIndexWordOne = False
            elif dict_item["isGreen"] is True:
                isLetterPresentinIndexWordOne = True
            elif dict_item["isYellow"] is False:
                isLetterYellowInWordOne = False
            elif dict_item["isYellow"] is True:
               isLetterYellowInWordOne = True
            elif dict_item["isGray"] is False:
                isLetterPresentInWordOne = True
            elif dict_item["isGray"] is True:
                isLetterPresentinIndexWordOne = False
        elif dict_item["index"] == 2:
            print(dict_item["word"])
            if dict_item["isGreen"] is False:
                isLetterTwoPresentinIndexWordOne = False
            elif dict_item["isGreen"] is True:
                isLetterTwoPresentinIndexWordOne = True
            elif dict_item["isYellow"] is False:
                isLetterTwoYellowInWordOne = False
            elif dict_item["isYellow"] is True:
               isLetterTwoYellowInWordOne = True
            elif dict_item["isGray"] is False:
                isLetterTwoPresentInWordOne = True
            elif dict_item["isGray"] is True:
                isLetterTwoPresentinIndexWordOne = False
        elif dict_item["index"] == 3:
            print(dict_item["word"])
            if dict_item["isGreen"] is False:
                isLetterThreePresentinIndexWordOne = False
            elif dict_item["isGreen"] is True:
                isLetterThreePresentinIndexWordOne = True
            elif dict_item["isYellow"] is False:
                isLetterThreeYellowInWordOne = False
            elif dict_item["isYellow"] is True:
               isLetterThreeYellowInWordOne = True
            elif dict_item["isGray"] is False:
                isLetterThreePresentInWordOne = True
            elif dict_item["isGray"] is True:
                isLetterThreePresentinIndexWordOne = False
        elif dict_item["index"] == 4:
            print(dict_item["word"])
            if dict_item["isGreen"] is False:
                isLetteFourPresentinIndexWordOne = False
            elif dict_item["isGreen"] is True:
                isLetteFourPresentinIndexWordOne = True
            elif dict_item["isYellow"] is False:
                isLetteFourYellowInWordOne = False
            elif dict_item["isYellow"] is True:
               isLetteFourYellowInWordOne = True
            elif dict_item["isGray"] is False:
                isLetteFourPresentInWordOne = True
            elif dict_item["isGray"] is True:
                isLetteFourPresentinIndexWordOne = False
        elif dict_item["index"] == 5:
            print(dict_item["word"])
            if dict_item["isGreen"] is False:
                isLetteFivePresentinIndexWordOne = False
            elif dict_item["isGreen"] is True:
                isLetteFivePresentinIndexWordOne = True
            elif dict_item["isYellow"] is False:
                isLetteFiveYellowInWordOne = False
            elif dict_item["isYellow"] is True:
               isLetteFiveYellowInWordOne = True
            elif dict_item["isGray"] is False:
                isLetteFivePresentInWordOne = True
            elif dict_item["isGray"] is True:
                isLetteFivePresentinIndexWordOne = False
    
    all_words = "./Backup/5letterWords.txt"

    with open(all_words) as all_words:
        word_content = all_words.read()
        word_dict = str(word_content).split(',')
        LambdaFilter = ""
        if isLetterPresentinIndexWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" x[2] == '{letter_1['word'].lower()}'"
            else:
                LambdaFilter = LambdaFilter + f" and x[2] == '{letter_1['word'].lower()}'"
        if isLetterYellowInWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" '{letter_1['word'].lower()}' in x"
            else:
                LambdaFilter = LambdaFilter + f" and '{letter_1['word'].lower()}' in x"
        if isLetterTwoPresentinIndexWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" x[3] == '{letter_2['word'].lower()}'"
            else:
                LambdaFilter = LambdaFilter + f" and x[3] == '{letter_2['word'].lower()}'"
        if isLetterTwoYellowInWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" '{letter_2['word'].lower()}' in x"
            else:
                LambdaFilter = LambdaFilter + f" and '{letter_2['word'].lower()}' in x"
        if isLetterThreePresentinIndexWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" x[4] == '{letter_3['word'].lower()}'"
            else:
                LambdaFilter = LambdaFilter + f" and x[4] == '{letter_3['word'].lower()}'"
        if isLetterThreeYellowInWordOne is True:
            print("present")

            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" '{letter_3['word'].lower()}' in x"
            else:
                LambdaFilter = LambdaFilter + f" and '{letter_3['word'].lower()}' in x"

        if isLetteFourPresentinIndexWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" x[5] == '{letter_4['word'].lower()}'"
            else:
                LambdaFilter = LambdaFilter + f" and x[5] == '{letter_4['word'].lower()}'"
        if isLetteFourYellowInWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" '{letter_4['word'].lower()}' in x"
            else:
                LambdaFilter = LambdaFilter + f" and '{letter_4['word'].lower()}' in x"

        if isLetteFivePresentinIndexWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" x[6] == '{letter_5['word'].lower()}'"
            else:
                LambdaFilter = LambdaFilter + f" and x[6] == '{letter_5['word'].lower()}'"
        if isLetteFiveYellowInWordOne is True:
            if not LambdaFilter:
                LambdaFilter = LambdaFilter + f" '{letter_5['word'].lower()}' in x"
            else:
                LambdaFilter = LambdaFilter + f" and '{letter_5['word'].lower()}' in x"
        print(f'filter: {LambdaFilter}')
            #print(letter_1["word"])
            #words = list(filter(lambda x: x[2] == letter_1["word"].lower(), word_dict))
            #print(words)
        

    
           