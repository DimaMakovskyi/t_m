from music import Speech
from openpyxl import load_workbook
import translator_words
from time import sleep
trans = translator_words.Trans()
fn = r"words\words.xlsx"
wb = load_workbook(fn)
ws = wb["en"]
wu = wb["ua"]
count = int(input())
for letter in ["E"]:
    while True:
        word = ws[f"{letter}{count}"].value
        if count == 1319:
            wb.save(fn)
            wb.close()
            break
        was_translate = trans.trans(word)
        print(was_translate)
        wu[f"{letter}{count}"] = was_translate
        if count%20 == 0:
            print("відпочинок")
            print(count)
            wb.save(fn)
            sleep(5)
        count += 1


wb.save(fn)
wb.close()