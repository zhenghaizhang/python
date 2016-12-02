import xlrd,xlwt

inputfiles = ['first.xlsx','second.xlsx','third.xlsx']
outputfile = 'result.xls'
wb = xlwt.Workbook()
outputList = []


def open_excel(file):
    resultRowIndex = 0;
    workbook = xlrd.open_workbook(filename=file)
    for sheetname in workbook.sheet_names():
        worktable = workbook.sheet_by_name(sheetname)
        for rownum in range(worktable.nrows):
            outputList.append(worktable.row_values(rownum))

def open_inputs(inputfiles):
    for index in range(len(inputfiles)):
        try:
            print('尝试打开文件'+inputfiles[index]+"读取！")
            open_excel(inputfiles[index])
            print('读取文件'+inputfiles[index]+"成功！")
        except Exception as err:
            print('读取文件'+inputfiles[index]+"失败！")

def writeFile(outputList):
    ws = wb.add_sheet("result")
    for rowIndex in range(len(outputList)):
        for colIndex in range(len(outputList[rowIndex])):
            ws.write(rowIndex, colIndex, outputList[rowIndex][colIndex])
    try:
        wb.save(outputfile)
        print('文件写入成功')
    except:
        print('文件写入失败！')

open_inputs(inputfiles)
writeFile(outputList)
