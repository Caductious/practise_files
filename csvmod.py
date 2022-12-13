def load_table(a):
  import csv,pickle
  dic={'names':[], 'values':[]}
  value=[]
  text=''
  if a[-3::]=='csv':
      with open(a, newline='', encoding='utf-8 sig') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for row in reader:
          dic['names']=row
          break
        text=[row for row in reader]
      for x in range(0,len(dic['names'])):
        for y in range(0,len(text)):
          value.append(text[y][x])
        dic['values'].append(value)
        value=[]
      return(dic)
  else: return('указан неверный формат файла для чтения')

def save_table(dict1):
  file_name=input('введите название файла для сохранения(с обозначением формата)')
  import csv
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
    print('Таблица сохранена успешно')
    return
  else: print('указан неверный формат файла для записи')
