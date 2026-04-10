import openpyxl


def export_excel(data):

    wb = openpyxl.Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    wb.save("cards.xlsx")