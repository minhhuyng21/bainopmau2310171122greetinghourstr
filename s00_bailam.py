#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310171122greetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/mb6ZrFw4pXW8DqeBA

--- debai / problem
Viết hàm 
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày 
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử 
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai
def greeting(hour_str):
  hour_str = hour_str.lower()
  import re
  t = re.findall("[A-Za-z+]",hour_str)
  k = re.findall("\d+",hour_str)
  k1 = k[0]
  if (len(k[0]) == 4) and (t == []):
    k1 = int(k1)
    if (k1 >= 600) and (k1 <= 1200):
       return "Good morning!"
    return "Good evening!"

  if ":" in hour_str:
    if "pm" in hour_str: 
      hour_str = hour_str.split(":")
      a = int(hour_str[0])
      if (a > 1):
        return "Good evening!"  
      else:
        return "Good afternoon! "
    elif "am" in hour_str:
      return "Good morning!"
    else:
      hour_str = hour_str.split(":")
      a = int(hour_str[0])
      if (a>=6) and (a<=12):
        return "Good morning!"
      else:
        return "Good evening!"  
    
  if "am" in hour_str:
    m = re.findall("\d+",hour_str)
    return "Good morning!"
  elif "pm" in hour_str:
    m = re.findall("\d+",hour_str)
    m1 = int(m[0]) 
    if (m1>1):
      return "Good evening!"
    else:
      return "Good afternoon!"
#region bailam

#endregion bailam
