days = ['Sun', 'Mon', 'Tue', 'Wed','Thur', 'Fri', 'Sat']
numbers = [1,2,3,4,5,6,7,8,9,10]
working_days = days[1:6]
print(working_days)
work_hours = numbers[5:9]
print(work_hours)
print(id (days))

events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'
print(events)

print(events.count('9/14'))
print(events.index('9/14'))

lst = events.find('9/14')
print(lst)

ev = events.split('\n')
print(ev)
print(ev.counts())
newlst = []
#for i in ev.count:
 #   n = 1
  #  if '9/14' in ev[n]
   #     newlst.append(ev[n])
    #print(n)

