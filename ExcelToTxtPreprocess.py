import numpy as np
import xlrd

class ExcelToTxtPreprocess:
    def __init__(self) -> None:
        pass
    def totxt(self,path,txt_path,sheet_name):
        data= xlrd.open_workbook(path)
        sh=data.sheet_by_name(sheet_name)
        print(sh.nrows)
        print(sh.ncols)
        n=0
        i=0
        file=open(txt_path,"a")
        for n in range(sh.nrows):
            text = sh.cell_value(n,0)
            file.write(text) 
            file.write('\n') 
            
        print("All Set")
