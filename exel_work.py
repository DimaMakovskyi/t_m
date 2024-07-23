from openpyxl import load_workbook
import translator_words
from time import sleep
count = 2
# for i in ["A", "B", "C", "D", "E"]:
trans = translator_words.Trans()

fn = r"words\words.xlsx"
wb = load_workbook(fn)
ws = wb["en"]
wu = wb["ua"]
count = int(input())
for letter in ["C"]:
    while True:
        word = ws[f"{letter}{count}"].value
        if count == 33362:
            count = 21
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
            sleep(20)
        count += 1


wb.save(fn)
wb.close()


# print("".join(result))
# from re import findall

# result = findall(r"(.+)", z)
# result = [word for word in result if len(word) > 1]
# print(result)
# fn = r"words\words.xlsx"
# wb = load_workbook(fn)
# ws = wb["en"]
# for i in range(len(result)):
#     ws[f"E{i+2}"] = result[i]
# wb.save(fn)
# wb.close()