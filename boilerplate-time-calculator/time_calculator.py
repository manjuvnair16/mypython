import math
def add_time(time, duration,today = ""):
  day_names_lst = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

  #split the time into hrs and mins by finding the position of ':'
  col_posn = time.find(':')
  time_hrs = time[0:col_posn]                  #slicing time before ':'
  time_mins = time[col_posn +1 : len(time)-3]  #slicing time after ':'
  if time.find('PM') != -1:
    time_hrs = int(time_hrs) + 12


  #split the time into hrs and mins by finding the position of ':'
  col_posn = duration.find(':')
  durn_hrs = duration[0:col_posn]                    #slicing time before ':'
  durn_mins = duration[col_posn +1 : len(duration)]  #slicing time after ':'

  #add the minutes first
  mins = int(time_mins) + int(durn_mins)
  inc_hrs = 0
  str_mins = str(mins)
  if mins >= 60:
    inc_hrs = math.floor(mins/60)
    mins = mins % 60
  if len(str(mins)) == 1:
    str_mins = '0' + str(mins)



  #add the hours next
  hrs = int(time_hrs) + int(durn_hrs) + inc_hrs


  #calculate result AM/PM
  day = 0
  if hrs >= 24:
    day = math.floor(hrs / 24)
    hrs = hrs % 12
  if hrs >= 12:
    if hrs > 12:
        hrs = hrs % 12
    total_hrs = str(hrs) + ':' + str_mins + ' PM'
  else:
    if hrs == 0:
        hrs = 12
    total_hrs = str(hrs) + ':' + str_mins + ' AM'

  #calculate the day name
  if today != '':
    today = today.lower()
    today = today[0].upper() + today[1:]
    index_today = day_names_lst.index(today)
    indx = index_today + day
    if indx > 6:
        indx = indx % 7
    today = day_names_lst[indx]
    total_hrs += ', ' + today

  #calculate if its another day/days
  if day > 0:
    if day == 1:
        total_hrs += ' (next day)'
    else:
        total_hrs += ' (' + str(day) + ' days later)'

  new_time = total_hrs
  return new_time