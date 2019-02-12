import camelot
def Camelot(path):
    tables=camelot.read_pdf(path,pages='all',flavor='stream')
    for i in range(1,28):
        print('page {}'.format(i))
        print(tables[i].data)
if __name__=='__main__':
    Camelot('../data/list.pdf')