def save_table(file_name,dict1):
  import csv,pickle
  names=dict1['names']
  rownumber=len(dict1['values'][0])
  lst1=[]
  if file_name[-3::]=='csv':
    for x in range(rownumber):
      dic2={}
      for y in range(len(names)):
        dic={dict1['names'][y]:dict1['values'][y][x]}
        dic2.update(dic)
      lst1.append(dic2)
    with open(file_name, 'w+') as csvfile:
      writer=csv.DictWriter(csvfile, fieldnames=names)
      writer.writeheader()
      writer.writerows(lst1)
  elif file_name[-3::]=='pkl':
    string=','.join(dict1['names'])+','
    for x in range(rownumber):
      string=string[:-1]
      string=string+'\n'
      for y in range(len(dict1['names'])):
        string+=''.join(dict1['values'][y][x])+','
    with open(file_name, 'wb') as f:
      pickle.dump(string[:-1], f)

def get_column_types(dict2):
  booleanExcel=['ИСТИНА','1','ЛОЖЬ','0']
  by_number=input('Столбец будет искаться по индексу? ДА/НЕТ').upper()
  assert by_number=='ДА' or by_number=='НЕТ', 'введено неверное значение'
  if by_number=='ДА':
    by_number=True
  elif by_number=='НЕТ':
    by_number=False
  if by_number:
    number=int(input('введите номер столбца'))-1
  else:
    name=input('введите заголовок столбца')
    assert name in dict2['names'], 'Такого столбца нет'
    number=dict2['names'].index(name)
  if dict2['values'][number][1] in booleanExcel:
    typp=bool
  else:
    try:
      int(dict2['values'][number][0])
      typp=int
    except ValueError:
      try:
        float(dict2['values'][number][0])
        typp=float
      except ValueError:
          typp=str
  typ={(dict2['names'][number]):typp}
  return typ

def get_rows_by_number(dict1grn):
  try:
    start=int(input('введите начало промежутка'))-1
    stop=input('введите конец промежутка')
    if stop=='':
      stop=start+1
    else:
      stop=int(stop)
    import csv
    copy_table=input('создавать новую таблицу? ДА/НЕТ').upper()
    assert copy_table=='ДА' or copy_table=='НЕТ', "введено неверное значение"
    if copy_table=='ДА':
      copy_table=True
    elif copy_table=='НЕТ':
      copy_table=False
    newdictgrn={'names':dict1grn['names'],'values':[]}
    for y in range(len(dict1grn['names'])):
        lst=[dict1grn['values'][y][x] for x in range(start,stop)]
        newdictgrn['values'].append(lst)
    if copy_table:
      save_table(input('введите название файла с указанием формата'),newdictgrn)
    else:
      save_table(input('введите название изначального файла с указанием формата'),newdictgrn)
    return(newdictgrn)
  except ValueError:
    print('введены неверные значения для промежутка')

def get_rows_by_index(dict1gri):
  lst_of_indx=[]
  x=input('введите индекс первой строки')
  while x!='':
    lst_of_indx.append(int(x)-1)
    x=input('введите индекс, для окончания, нажмите Enter')
  print(lst_of_indx)
  copy_table=input('создавать новую таблицу? ДА/НЕТ').upper()
  assert copy_table=='ДА' or copy_table=='НЕТ', "введено неверное значение"
  if copy_table=='ДА':
    copy_table=True
  elif copy_table=='НЕТ':
    copy_table=False
  newdictgri={'names':dict1gri['names'],'values':[]}
  for name in newdictgri['names']:
    z=newdictgri['names'].index(name)
    lstgri=[]
    for x in lst_of_indx:
      lstgri.append(dict1gri['values'][z][x])
    newdictgri['values'].append(lstgri)
  if copy_table:
    save_table(input('введите название файла с указанием формата'), newdictgri)
  else:
    save_table(input('введите название изначального файла с указанием формата'), newdictgri)
  return(newdictgri)

def get_values(dict1):
  lst=[]
  column=input('введите название или номер колонки')
  if column=='':
    column=1
  try:
    column=int(column)-1
  except ValueError:
    assert column in dict1['names'],'такой колонки нет'
    column=dict1['names'].index(column)
  lst=[name for name in (dict1['values'][column])]
  return(lst)

def get_value(dict3):
  column=input('введите название или номер колонки')
  if column=='':
    column=1
  try:
    column=int(column)-1
  except ValueError:
    assert column in dict3['names'],'такой колонки нет'
    column=dict3['names'].index(column)
  return(dict3['values'][column][0])

def print_table(dict4):
  out1=dict4['names']
  out2=''
  for x in range(0,len(out1)):
    out2+=("{:^50}|".format(out1[x]))
  print('-'*len(out2))
  print('|'+out2)
  print('-'*len(out2))
  for x in range(len(out1)):
    out2=''
    for y in range(len(dict4['names'])):
      out2+=("{:^50}|".format(dict4['values'][y][x]))
    print('|'+out2)
    print('-'*len(out2))

def save_table(file_name,dict1):
  import csv,pickle
  names=dict1['names']
  rownumber=len(dict1['values'][0])
  lst1=[]
  if file_name[-3::]=='csv':
    for x in range(rownumber):
      dic2={}
      for y in range(len(names)):
        dic={dict1['names'][y]:dict1['values'][y][x]}
        dic2.update(dic)
      lst1.append(dic2)
    with open(file_name, 'w+') as csvfile:
      writer=csv.DictWriter(csvfile, fieldnames=names)
      writer.writeheader()
      writer.writerows(lst1)
  elif file_name[-3::]=='pkl':
    string=','.join(dict1['names'])+','
    for x in range(rownumber):
      string=string[:-1]
      string=string+'\n'
      for y in range(len(dict1['names'])):
        string+=''.join(dict1['values'][y][x])+','
    with open(file_name, 'wb') as f:
      pickle.dump(string[:-1], f)
  elif file_name[-3::]=='txt':
    with open(file_name, 'w+') as textfile:
      out1=dict1['names']
      out2=''
      for x in range(0,len(out1)):
        out2+=("{:^50}|".format(out1[x]))
      textfile.write('-'*len(out2)+'\n')
      textfile.write(('|'+out2)+'\n')
      textfile.write('-'*len(out2)+'\n')
      for x in range(len(out1)):
        out2=''
        for y in range(len(dict1['values'][0])):
          out2+=("{:^50}|".format(dict1['values'][y][x]))
        textfile.write('|'+out2+'\n')
        textfile.write('-'*len(out2)+'\n')
    textfile.close()

def set_column_types(dict5):
  by_number = input('Столбец будет изменяться по индексу? ДА/НЕТ').upper()
  assert by_number == 'ДА' or by_number == 'НЕТ', 'введено неверное значение'
  if by_number == 'ДА':
    by_number = True
  elif by_number == 'НЕТ':
    by_number = False
  if by_number:
    number = int(input('введите номер столбца')) - 1
  else:
    name = input('введите заголовок столбца')
    assert name in dict5['names'], 'Такого столбца нет'
    number = dict5['names'].index(name)
  typ=input('Введите требуемый тип значений')
  typp={name:typ}
  return typp

def set_values(values,dict6):
  lst = []
  column=input('введите название или номер колонки')
  if column=='':
    column=1
  try:
    column = int(column) - 1
  except ValueError:
    assert column in dict6['names'], 'такой колонки нет'
    column = dict6['names'].index(column)
  dict6['values'][column]=[name for name in (values)]
  return (dict6['values'][column])

def set_value(value,dict7):
  column=input('введите название или номер колонки')
  if column == '':
    column = 1
  try:
    column=int(column)-1
  except ValueError:
    assert column in dict7['names'],'такой колонки нет'
    column=dict7['names'].index(column)
  dict7['values'][column][0]=value
  return(dict7['values'][column][0])