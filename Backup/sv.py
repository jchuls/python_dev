
import Query as q
import os
import os.path
# import test as ts
import pandas as pd
import csv


#Category
# q.result12.to_csv(r'C:\Users\youn\Category\Category_Cheonahn.csv', header=False, index=False, encoding='utf-8-sig')
# q.result13.to_csv(r'C:\Users\youn\Category\Category_Geumchon.csv', header=False, index=False, encoding='utf-8-sig')
# q.result14.to_csv(r'C:\Users\youn\Category\Category_Hwagok.csv', header=False, index=False, encoding='utf-8-sig')

#Member
# # q.result23.to_csv(r'C:\Users\youn\Member\Member_Cheonahn.csv', header=False, index=False, encoding='utf-8-sig')
# q.result24.to_csv(r'C:\Users\youn\Member\Member_Geumchon.csv', header=False, index=False, encoding='utf-8-sig')
# q.result25.to_csv(r'C:\Users\youn\Member\Member_Hwagok.csv', header=False, index=False, encoding='utf-8-sig')

#Sales
q.result35.to_csv(r'C:\Users\youn\Sales\Sales_Cheonahn_06.csv', header=False, index=False, encoding='utf-8-sig')
q.result36.to_csv(r'C:\Users\youn\Sales\sales_Geumchon_06.csv', header=False, index=False, encoding='utf-8-sig')
q.result37.to_csv(r'C:\Users\youn\Sales\Sales_Hwagok_06.csv', header=False, index=False, encoding='utf-8-sig')

#Item
# q.result45.to_csv(r'C:\Users\youn\Item\Item_Cheonahn.csv', header=False, index=False, encoding='utf-8-sig')
# q.result46.to_csv(r'C:\Users\youn\Item\Item_Geumchon.csv', header=False, index=False, encoding='utf-8-sig')
# q.result47.to_csv(r'C:\Users\youn\Item\Item_Hwagok.csv', header=False, index=False, encoding='utf-8-sig')

#Point
# q.result55.to_csv(r'C:\Users\youn\Point\Point_Cheonahn.csv', header=False, index=False, encoding='utf-8-sig')
# q.result56.to_csv(r'C:\Users\youn\Point\Point_Geumchon.csv', header=False, index=False, encoding='utf-8-sig')
# q.result57.to_csv(r'C:\Users\youn\Point\Point_Hwagok.csv', header=False, index=False, encoding='utf-8-sig')

#CJS
# q.result65.to_csv(r'C:\Users\youn\CJS\CJS_Cheonahn.csv', header=False, index=False, encoding='utf-8-sig')
# q.result66.to_csv(r'C:\Users\youn\CJS\CJS_Geumchon.csv', header=False, index=False, encoding='utf-8-sig')
# q.result67.to_csv(r'C:\Users\youn\CJS\CJS_Hwagok.csv', header=False, index=False, encoding='utf-8-sig')

#GRC
# q.result75.to_csv(r'C:\Users\youn\GRC\GRC_Cheonahn.csv', header=False, index=False, encoding='utf-8-sig')
# q.result76.to_csv(r'C:\Users\youn\GRC\GRC_Geumchon.csv', header=False, index=False, encoding='utf-8-sig')
# q.result77.to_csv(r'C:\Users\youn\GRC\GRC_Hwagok.csv', header=False, index=False, encoding='utf-8-sig')

#DC
# q.result85.to_csv(r'C:\Users\youn\DC\DC_Cheonahn.csv', header=False, index=False, encoding='utf-8-sig')
# q.result86.to_csv(r'C:\Users\youn\DC\DC_Geumchon.csv', header=False, index=False, encoding='utf-8-sig')
# q.result87.to_csv(r'C:\Users\youn\DC\DC_Hwagok.csv', header=False, index=False, encoding='utf-8-sig')

#
# cursor_t = ts.conn.cursor()
#
# moi = ts.mdata['mai_Company_num']
#
# cursor_t.execute(ts.query)
#
# result_t = cursor_t.fetchall()
#
# result_t_df = pd.DataFrame(result_t)
# result_a = result_t_df.insert(2, 'moi_idx', moi)
#
# result_t_df.to_csv(r'C:\Users\youn\test\test_attr.csv', header=False,index=False, encoding='utf-8-sig')


def print_file(dir):
    files = os.listdir(dir)

    for item in files:

        if os.path.isdir(dir + r"\\" + item) == True:

            print_file(dir + r"\\" + item)

        else:

            print(dir + r"\\" + item)

if __name__ == '__main__':
    dir = r"C:\Users\youn"
