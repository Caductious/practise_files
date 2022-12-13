def load_table(a):
    import pickle
    dic = {'names': [], 'values': []}
    value = []
    if a[-3::] == 'pkl':
        with open(a, 'rb') as pklfile:
            reader = pickle.load(pklfile)
            reader = reader.split('\n')
            rows = ([reader[v].split(',') for v in range(len(reader))])
            dic['names'] = rows[0]
            text=[rows[z] for z in range(1, len(rows))]
        for x in range(0, len(dic['names'])):
            for y in range(0, len(text)):
                value.append(text[y][x])
            dic['values'].append(value)
            value = []
        return (dic)
    else: return ('указан неверный формат файла для чтения')

def save_table(dict1):
  import pickle
  file_name=input('введите название файла для сохранения(с обозначением формата)')
  names=dict1['names']
  rownumber=len(dict1['values'][0])
  lst1=[]
  if file_name[-3::]=='pkl':
    string=','.join(dict1['names'])+','
    for x in range(rownumber):
      string=string[:-1]
      string=string+'\n'
      for y in range(len(dict1['names'])):
        string+=''.join(dict1['values'][y][x])+','
    with open(file_name, 'wb') as f:
      pickle.dump(string[:-1], f)
    print('файл записан успешно')
    return
  else: print ('указан неверный формат файла для записи')