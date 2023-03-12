import os.path
import os
from playsound import playsound
def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference
def foo():
    playsound('stop-it-japanese-anime-spoken-sample_143bpm_C_major (1) (1).mp3')
    print("New drive introduced")
def ham():
    playsound('Ahh - Girl Sound ! Notification.mp3')
    print("Drive disconnected")
dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print(drives)
while True:
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)
    if x:
        # print("New drives:     " + str(x))
        foo()
    x = diff(drives, uncheckeddrives)
    if x:
        # print("Removed drives: " + str(x))
        ham()
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
