import pymysql, sys
import joe_def_v2 as sw
import xlrd
from colorama import init # cmd color.
init() # init color for windows cmd.

# Default List
List = "Test_File.xls"

# DB Args
db_settings = {"host": "192.168.68.252", "user": "python", "password": "Kx12930780@@", "db": "kx_db", "charset": "utf8"
}

# Drag and Drop
if len(sys.argv) > 1:
    dropped_arg = sys.argv
    dropped_file = dropped_arg[1]
    print(sw.col_red() + "Detected Drop File : " + dropped_file + sw.col_def())
    List = dropped_file
else:
    print(sw.col_yellow() + "Not Detected Drag and Drop File, Using Default Parser ./" + List + sw.col_def())

# Read Excel
data = xlrd.open_workbook(List)
sheet = data.sheets()[0]
nrows = sheet.nrows
ncols = sheet.ncols

# Connect DB
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()

# Main
try:
    Success = 0
    Error = 0
    for i in range(1, (nrows)):
        SN = sheet.row_values(i)[0]
        command = "SELECT * FROM TAB_ITM WHERE ITM_SER_NUM = " + "'" + SN + "'"
        cursor.execute(command)
        data = cursor.fetchone()
        if data is None:
            print(sw.col_red() + SN + " No Data in ITAM DB !!" + sw.col_def())
            Error += 1
            continue
        print (data[1] + \
               sw.col_green() + " " + data[4] + \
               sw.col_yellow() + " " + data[9] + sw.col_def())
        Success += 1
    cursor.close()
    conn.close()
    print("")
    print("Success Quary Data : " + sw.col_green() + str(Success) + sw.col_def())
    print("Error Quary Data : " + sw.col_red() + str(Error) + sw.col_def())
    print("")
    input("Press Enter to Exit ...")

except :
    raise
