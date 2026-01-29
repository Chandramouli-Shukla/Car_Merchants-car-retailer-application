#import section

import mysql.connector as sqltor
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


#main

print(r'''
   _____             __  __               _                 _
  / ____|           |  \/  |             | |               | |
 | |     __ _ _ __  | \  / | ___ _ __ ___| |__   __ _ _ __ | |_ ___
 | |    / _` | '__| | |\/| |/ _ \ '__/ __| '_ \ / _` | '_ \| __/ __|
 | |___| (_| | |    | |  | |  __/ | | (__| | | | (_| | | | | |_\__ \
  \_____\__,_|_|    |_|  |_|\___|_|  \___|_| |_|\__,_|_| |_|\__|___/

                                                                    ''')

#main variables

mycon = sqltor.connect(host="localhost", user="root", passwd="12346", database="car_mearchents")
engine = create_engine('mysql+pymysql://root:123456@localhost/car_merchents')
mypysqlcon = engine.connect()

cursor = mycon.cursor()

#tables

user_list = pd.read_sql("select * from user_list",mycon)
uname_list = list(user_list['name'])
pass_list = list(user_list['pass'])

stock = pd.read_sql("select * from stock",mycon)
sales = pd.read_sql("select * from sales",mycon)

profit_list = sales['sales_price']-sales['cost_price']
profit = sales.loc[:,['name','cost_price','sales_price']]
profit['profit'] = profit_list

future_purcahes = pd.read_sql("select * from future_purcahes",mycon)

run = True
run2 = True

#login func

def login(username,password):
  if username in uname_list:
    if password in pass_list:
      print('login successful')
      if username == 'admin':
        if password == user_list.loc[0,'pass']:
          user_title = 'admin'
          print('welcome admin')
          return user_title
        else:
          print('login failed...')
          print('enter proper credentials')

      elif username == 'salesman1':
        if password == user_list.loc[1,'pass']:
          user_title = 'salesman'
          print('welcome salesman1')
          return user_title
        else:
          print('login failed...')
          print('enter proper credentials')

      elif username == 'salesman2':
        if password == user_list.loc[2,'pass']:
          user_title = 'salesman'
          print('welcome salesman2')
          return user_title
        else:
          print('login failed...')
          print('enter proper credentials')

      elif username == 'customer':
        if password == user_list.loc[3,'pass']:
          user_title = 'customer'
          print('welcome customer')
          return user_title
        else:
          print('login failed...')
          print('enter proper credentials')


    else:
      print('login failed...')
      print('enter proper credentials')

  else:
    print('login failed...')
    print('enter proper credentials')

#admin show func

def admin_stock_show():

  print('1. specific records')
  print('2. all records')
  print('98. Back')
  show_choice = input('how do you want to view the records:')
  print()

  if show_choice == '1':
    print('1. plate no')
    print('2. name')
    print('3. fule')
    print('4. company')
    print('5. odometer')
    print('6. car condition')
    print('7. price')
    print('98. back')
    specific_choice = input('select the criteria to show records')
    print()

    if specific_choice == '1':
      p_no = input('enter plate no')
      print(stock[stock['plate_no']==p_no])

    elif specific_choice == '2':
      name = input('enter name')
      print(stock[stock['name']==name])

    elif specific_choice == '3':
      fule = input('enter fule')
      print(stock[stock['fule']==fule])

    elif specific_choice == '4':
      company = input('enter company')
      print(stock[stock['company']==company])

    elif specific_choice == '5':
      odometer = input('enter odometer')
      print(stock[stock['odometer']==odometer])

    elif specific_choice == '6':
      car_condition = input('enter car condition')
      print(stock[stock['car_condition']==car_condition])

    elif specific_choice == '7':
      price = input('enter price')
      print(stock[stock['price']==price])

    elif specific_choice == '98':
      return

    else:
      print('enter correct oppretor')
  elif show_choice == '2':
    print(stock)

  elif show_choice == '98':
    return
  else:
    print('enter correct oppretor')

def admin_sales_show():

  print('1. specific records')
  print('2. all records')
  print('3. name and profit')
  print('98. Back')
  show_choice = input('how do you want to view the records:')
  print()

  if show_choice == '1':
    print('1. plate no')
    print('2. name')
    print('3. fule')
    print('4. company')
    print('5. odometer')
    print('6. car condition')
    print('7. price')
    print('98. back')
    specific_choice = input('select the criteria to show records:')
    print()

    if specific_choice == '1':
      p_no = input('enter plate no')
      print(sales[sales['plate_no']==p_no])

    elif specific_choice == '2':
      name = input('enter name')
      print(sales[sales['name']==name])

    elif specific_choice == '3':
      fule = input('enter fule')
      print(sales[sales['fule']==fule])

    elif specific_choice == '4':
      company = input('enter company')
      print(sales[sales['company']==company])

    elif specific_choice == '5':
      odometer = input('enter odometer')
      print(sales[sales['odometer']==odometer])

    elif specific_choice == '6':
      car_condition = input('enter car condition')
      print(sales[sales['car_condition']==car_condition])

    elif specific_choice == '7':
      price = input('enter price')
      print(sales[sales['price']==price])

    elif specific_choice == '98':
      return

    else:
      print('enter correct oppretor')
  elif show_choice == '2':
    print(sales)
    print()
  elif show_choice == '3':
    print(profit)

  elif show_choice == '98':
    return
  else:
    print('enter correct oppretor')

def admin_future_purcahes_show():
  print(future_purcahes)

#admin edit, add or remove func

def admin_edit_stock():

  print(stock)
  print()
  col = input('which column do you want to edit:')
  row = int(input('which row(index) do you want to edit:'))
  value = input('what value do you want to put:')
  stock.loc[row,col] = value
  print()

  qry = "update stock set %s = '%s' where plate_no = '%s'" %(col,value,stock.loc[row,'plate_no'])
  cursor.execute(qry)
  mycon.commit()

  print('updated records')
  print(stock)
  return

def admin_edit_sales():
  print(sales)
  print()
  col = input('which column do you want to edit:')
  row = int(input('which row(index) do you want to edit:'))
  value = input('what value do you want to put:')
  sales.loc[row,col] = value
  print()

  qry = "update sales set %s = '%s' where plate_no = '%s'" %(col,value,sales.loc[row,'plate_no'])
  cursor.execute(qry)
  mycon.commit()

  print('updated records')
  print(sales)
  return


def admin_edit_future_purchases():
  print(future_purcahes)
  print()
  col = input('which column do you want to edit:')
  row = int(input('which row(index) do you want to edit:'))
  value = input('what value do you want to put:')
  future_purcahes.loc[row,col] = value
  print()
  qry = "update future_purcahes set %s = '%s' where plate_no = '%s'" %(col,value,future_purcahes.loc[row,'plate_no'])
  cursor.execute(qry)
  mycon.commit()

  print('updated records')
  print(future_purcahes)
  return

def admin_add_stock():
  print(stock)
  print()
  plate_no = input('enter plate no.')
  name = input('enter name')
  fule = input('enter fule')
  company = input('enter company')
  odometer = int(input('enter odometer'))
  car_condition = input('enter car condition')
  price = int(input('enter price'))
  stock.loc[len(stock)] = [plate_no,name,fule,company,odometer,car_condition,price]
  print()
  qry = "insert into stock values('%s','%s','%s','%s',%d,'%s',%d)" %(plate_no,name,fule,company,odometer,car_condition,price)
  cursor.execute(qry)
  mycon.commit()
  print('updated records')
  print(stock)
  return

def admin_add_sales():
  print(sales)
  print()
  plate_no = input('enter plate no.')
  name = input('enter name')
  fule = input('enter fule')
  company = input('enter company')
  odometer = int(input('enter odometer'))
  car_condition = input('enter car condition')
  cost_price = int(input('enter cost price'))
  sales_price = int(input('enter sales price'))
  sales.loc[len(sales)] = [plate_no,name,fule,company,odometer,car_condition,cost_price,sales_price]
  print()
  qry = "insert into sales values('%s','%s','%s','%s',%d,'%s',%d,%d)" %(plate_no,name,fule,company,odometer,car_condition,cost_price,sales_price)
  cursor.execute(qry)
  mycon.commit()
  print('updated records')
  print(sales)
  return


def admin_add_future_purcahes():
  print(future_purcahes)
  print()
  plate_no = input('enter plate no')
  name = input('enter name')
  fule = input('enter fule')
  company = input('enter company')
  odometer = int(input('enter odometer'))
  car_condition = input('enter car condition')
  expected_price = int(input('enter expected price'))
  future_purcahes.loc[len(future_purcahes)] = [plate_no,name,fule,company,odometer,car_condition,expected_price]
  print()
  qry = "insert into future_purcahes values('%s','%s','%s','%s',%d,'%s',%d)" %(plate_no,name,fule,company,odometer,car_condition,expected_price)
  cursor.execute(qry)
  mycon.commit()
  print('updated records')
  print(future_purcahes)
  return

def admin_remove_stock():
  print(stock)
  print()
  row = int(input('which row(index) do you want to remove:'))
  print()
  qry = "delete from stock where plate_no = '%s'" %(stock.loc[row,'plate_no'])
  stock.drop(row,axis=0,inplace=True)
  cursor.execute(qry)
  mycon.commit()
  print('updated records')
  print(stock)
  return

def admin_remove_sales():
  print(sales)
  print()
  row = int(input('which row(index) do you want to remove:'))
  print()
  qry = "delete from sales where plate_no = '%s'" %(sales.loc[row,'plate_no'])
  sales.drop(row,inplace=True)
  cursor.execute(qry)
  mycon.commit()
  print('updated records')
  print(sales)
  return

def admin_remove_future_purcahes():
  print(future_purcahes)
  print()
  row = int(input('which row(index) do you want to remove:'))
  print()
  qry = "delete from future_purcahes where plate_no = '%s'" %(future_purcahes.loc[row,'plate_no'])
  future_purcahes.drop(row,inplace=True)
  cursor.execute(qry)
  mycon.commit()
  print('updated records')
  print(future_purcahes)
  return

#admin sales

def admin_sales():
  print('1. total sales graph')
  print('2. total profit graph')
  print('98. Back')

  admin_sales_choice = input('what do you want to do:')

  if admin_sales_choice == '1':
    print('total sales graph')
    sales['sales_price'].plot(x=+0.50,kind='bar',color='green',xlabel='cars',ylabel='sales',width=0.50,label='sales_price')
    sales['cost_price'].plot(x=+0.50,kind='bar',color='red',xlabel='cars',ylabel='sales',width=0.50,label='cost_price')
    plt.legend(loc='upper left')

  elif admin_sales_choice == '2':
    pl = []
    a = 0
    for i in profit_list:
      a += i
      pl.append(a)
    plt.plot(pl,color='green')
    plt.xlabel('cars')
    plt.ylabel('profit')

  elif admin_sales_choice == '98':
    return

  else:
    print('enter correct operator')




#salesman show func

def salesman_stock_show():

  print('1. specific records')
  print('2. all records')
  print('98. Back')
  show_choice = input('how do you want to view the records:')
  print()

  if show_choice == '1':
    print('1. plate no')
    print('2. name')
    print('3. fule')
    print('4. company')
    print('5. odometer')
    print('6. car condition')
    print('7. price')
    print('98. back')
    specific_choice = input('select the criteria to show records')
    print()

    if specific_choice == '1':
      p_no = input('enter plate no')
      print(stock[stock['plate_no']==p_no])

    elif specific_choice == '2':
      name = input('enter name')
      print(stock[stock['name']==name])

    elif specific_choice == '3':
      fule = input('enter fule')
      print(stock[stock['fule']==fule])

    elif specific_choice == '4':
      company = input('enter company')
      print(stock[stock['company']==company])

    elif specific_choice == '5':
      odometer = input('enter odometer')
      print(stock[stock['odometer']==odometer])

    elif specific_choice == '6':
      car_condition = input('enter car condition')
      print(stock[stock['car_condition']==car_condition])

    elif specific_choice == '7':
      price = input('enter price')
      print(stock[stock['price']==price])

    elif specific_choice == '98':
      return

    else:
      print('enter correct oppretor')
  elif show_choice == '2':
    print(stock)

  elif show_choice == '98':
    return
  else:
    print('enter correct oppretor')

def salesman_sales_show():

  print('1. specific records')
  print('2. all records')
  print('3. name and profit')
  print('98. Back')
  show_choice = input('how do you want to view the records:')
  print()

  if show_choice == '1':
    print('1. plate no')
    print('2. name')
    print('3. fule')
    print('4. company')
    print('5. odometer')
    print('6. car condition')
    print('7. price')
    print('98. back')
    specific_choice = input('select the criteria to show records:')
    print()

    if specific_choice == '1':
      p_no = input('enter plate no')
      print(sales[sales['plate_no']==p_no])

    elif specific_choice == '2':
      name = input('enter name')
      print(sales[sales['name']==name])

    elif specific_choice == '3':
      fule = input('enter fule')
      print(sales[sales['fule']==fule])

    elif specific_choice == '4':
      company = input('enter company')
      print(sales[sales['company']==company])

    elif specific_choice == '5':
      odometer = input('enter odometer')
      print(sales[sales['odometer']==odometer])

    elif specific_choice == '6':
      car_condition = input('enter car condition')
      print(sales[sales['car_condition']==car_condition])

    elif specific_choice == '7':
      price = input('enter price')
      print(sales[sales['price']==price])

    elif specific_choice == '98':
      return

    else:
      print('enter correct oppretor')
  elif show_choice == '2':
    print(sales)
    print()
  elif show_choice == '3':
    print(profit)

  elif show_choice == '98':
    return
  else:
    print('enter correct oppretor')

def salesman_future_purcahes_show():
  print(future_purcahes)

#salesman sales

def salesman_sales():
  print('1. total sales graph')
  print('2. total profit graph')
  print('98. Back')

  admin_sales_choice = input('what do you want to do:')

  if admin_sales_choice == '1':
    print('total sales graph')
    sales['sales_price'].plot(x=+0.50,kind='bar',color='green',xlabel='cars',ylabel='sales',width=0.50,label='sales_price')
    sales['cost_price'].plot(x=+0.50,kind='bar',color='red',xlabel='cars',ylabel='sales',width=0.50,label='cost_price')
    plt.legend(loc='upper left')

  elif admin_sales_choice == '2':
    pl = []
    a = 0
    for i in profit_list:
      a += i
      pl.append(a)
    plt.plot(pl,color='green')
    plt.xlabel('cars')
    plt.ylabel('profit')


  elif admin_sales_choice == '98':
    return

#customer show

def customer_stock_show():
  print('1. specific records')
  print('2. all records')
  print('98. Back')
  show_choice = input('how do you want to view the records:')
  print()

  if show_choice == '1':
    print('1. plate no')
    print('2. name')
    print('3. fule')
    print('4. company')
    print('5. odometer')
    print('6. car condition')
    print('7. price')
    print('98. back')
    specific_choice = input('select the criteria to show records')
    print()

    if specific_choice == '1':
      p_no = input('enter plate no')
      print(stock[stock['plate_no']==p_no])

    elif specific_choice == '2':
      name = input('enter name')
      print(stock[stock['name']==name])

    elif specific_choice == '3':
      fule = input('enter fule')
      print(stock[stock['fule']==fule])

    elif specific_choice == '4':
      company = input('enter company')
      print(stock[stock['company']==company])

    elif specific_choice == '5':
      odometer = input('enter odometer')
      print(stock[stock['odometer']==odometer])

    elif specific_choice == '6':
      car_condition = input('enter car condition')
      print(stock[stock['car_condition']==car_condition])

    elif specific_choice == '7':
      price = input('enter price')
      print(stock[stock['price']==price])

    elif specific_choice == '98':
      return

    else:
      print('enter correct oppretor')
  elif show_choice == '2':
    print(stock)

  elif show_choice == '98':
    return
  else:
    print('enter correct oppretor')


#menu1 func

def menu1(user_title):

  if user_title == 'admin':
    print('1. Show records')
    print('2. Edit, add or remove records')
    print('3. Show sales graph')
    print('98. Back')
    print('99. Exit')
    c2 = input('What do you want to do:')
  elif user_title == 'salesman':
    print('1. Show records')
    print('2. Show sales graph')
    print('98. Back')
    print('99. Exit')
    c2 = input('What do you want to do:')
  elif user_title == 'customer':
    print('1. Show available stock')
    print('98. Back')
    print('99. Exit')
    c2 = input('What do you want to do:')

  return c2


#main loop

while run==True:


  print()
  print('Welcome to car merchents')
  print('1. Login')
  print('99. Exit')
  c1 = input('What do you want to do:')
  print()

  if c1 == '1':

    #loging in
    print('login')
    uname = input('enter your username:')
    passwd = input('enter your password:')

    utitle = login(uname,passwd)
    print()

    #menu1

    #c2 = menu1(utitle)

    run2 = True
    while run2 == True:
      c2 = menu1(utitle)
      print()
      if utitle == 'admin':
        if c2 == '1':
          print('1. Show stock records')
          print('2. Show sales records')
          print('3. Future purcahes')
          print('98. Back')
          c_record = input('What do you want to do')
          print()
          if c_record == '1':
            admin_stock_show()
            print()
          elif c_record == '2':
            admin_sales_show()
            print()
          elif c_record == '3':
            admin_future_purcahes_show()
            print()
          elif c_record == '98':
            run2 = False
          print()
        elif c2 == '2':
          print('1. Edit')
          print('2. Add')
          print('3. Remove')
          print('98. Back')
          c_e_or_a = input('What do you want to do')
          print()
          if c_e_or_a == '1':
            print('1. Edit stock records')
            print('2. Edit sales records')
            print('3. Edit Future purcahes')
            print('98. Back')
            c_edit = input('What do you want to do:')
            if c_edit == '1':
              admin_edit_stock()
              print()
            elif c_edit == '2':
              admin_edit_sales()
              print()
            elif c_edit == '3':
              admin_edit_future_purchases()
              print()
            elif c_edit == '98':
              run2 = False
            print()
          elif c_e_or_a == '2':
            print('1. Add stock records')
            print('2. Add sales records')
            print('3. Add Future purcahes')
            print('98. Back')
            c_add = input('What do you want to do:')
            if c_add == '1':
              admin_add_stock()
              print()
            elif c_add == '2':
              admin_add_sales()
              print()
            elif c_add == '3':
              admin_add_future_purcahes()
              print()
            elif c_add == '98':
              run2 = False
            else:
              print('enter correct oppretor')
            print()
          elif c_e_or_a == '3':
            print('1. Remove stock records')
            print('2. Remove sales records')
            print('3. Remove Future purcahes')
            print('98. Back')
            c_remove = input('What do you want to do:')
            if c_remove == '1':
              admin_remove_stock()
              print()
            elif c_remove == '2':
              admin_remove_sales()
              print()
            elif c_remove == '3':
              admin_remove_future_purcahes()
              print()
            elif c_remove == '98':
              run2 = False
            else:
              print('enter correct oppretor')
            print()
          elif c_e_or_a == '98':
            run2 = False
          else:
            print('enter correct oppretor')
          print()
        elif c2 == '3':
          admin_sales()
          plt.show()
          plt.close()
          print()
        elif c2 == '98':
          run2 = False
        elif c2 == '99':
          print(r'''Thank You for concidering us

     ___            __  __            _             _
    / __|__ _ _ _  |  \/  |___ _ _ __| |_  __ _ _ _| |_ ___
   | (__/ _` | '_| | |\/| / -_) '_/ _| ' \/ _` | ' \  _(_-<
    \___\__,_|_|   |_|  |_\___|_| \__|_||_\__,_|_||_\__/__/


            ''')
          run = False
          run2 = False
        else:
          print('enter correct oppretor')

      elif utitle == 'salesman':
        if c2 == '1':
          print('1. Show stock records')
          print('2. Show sales records')
          print('3. Future purcahes')
          print('98. Back')
          c_record = input('What do you want to do')
          print()
          if c_record == '1':
            salesman_stock_show()
            print()
          elif c_record == '2':
            salesman_sales_show()
            print()
          elif c_record == '3':
            salesman_future_purcahes_show()
            print()
          elif c_record == '98':
            run2 = False
          print()
        elif c2 == '2':
          salesman_sales()
          plt.show()
          plt.close()
          print()
        elif c2 == '98':
          run2 = False
        elif c2 == '99':
          print(r'''Thank You for concidering us

     ___            __  __            _             _
    / __|__ _ _ _  |  \/  |___ _ _ __| |_  __ _ _ _| |_ ___
   | (__/ _` | '_| | |\/| / -_) '_/ _| ' \/ _` | ' \  _(_-<
    \___\__,_|_|   |_|  |_\___|_| \__|_||_\__,_|_||_\__/__/


            ''')
          run = False
          run2 = False
        else:
          print('enter correct oppretor')

      elif utitle == 'customer':
        if c2 == '1':
          customer_stock_show()
          print()
        elif c2 == '98':
          run2 = False
        elif c2 == '99':
          print(r'''Thank You for concidering us

     ___            __  __            _             _
    / __|__ _ _ _  |  \/  |___ _ _ __| |_  __ _ _ _| |_ ___
   | (__/ _` | '_| | |\/| / -_) '_/ _| ' \/ _` | ' \  _(_-<
    \___\__,_|_|   |_|  |_\___|_| \__|_||_\__,_|_||_\__/__/


            ''')
          run = False
          run2 = False
        else:
          print('enter correct oppretor')


  elif c1 == '99':
    print(r'''Thank You for concidering us

   ___            __  __            _             _
  / __|__ _ _ _  |  \/  |___ _ _ __| |_  __ _ _ _| |_ ___
 | (__/ _` | '_| | |\/| / -_) '_/ _| ' \/ _` | ' \  _(_-<
  \___\__,_|_|   |_|  |_\___|_| \__|_||_\__,_|_||_\__/__/


    ''')
    run = False
  else:
    print('enter correct oppretor')






mycon.close()
mypysqlcon.close()
engine.dispose()

