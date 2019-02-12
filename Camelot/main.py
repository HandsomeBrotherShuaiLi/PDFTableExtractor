import camelot,prettytable as pt
def Camelot(path):
    tables=camelot.read_pdf(path,pages='all',flavor='stream')
    tb=pt.PrettyTable()
    tb.field_names=['1','2','3']
    # print(tb)
    for i in range(1,28):
        # print('page {}'.format(i))
        # print(tables[i].data)
        for j in tables[i].data:
            if len(j)==3:
                tb.add_row(j)
            else:
                res=[' ']
                res.append(j[0])
                res.append(j[1])
                tb.add_row(res)
    print(tb)

if __name__=='__main__':
    Camelot('../data/list.pdf')