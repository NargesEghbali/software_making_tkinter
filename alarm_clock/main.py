import tkinter as tk 
from tkinter import ttk,messagebox
import datetime
from PIL import ImageTk
from PIL import Image
import pygame
pygame.mixer.init()
import threading

###############################################
# Hours List.
hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23', '24']

# Minutes List.
minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '30', '31',
        '32', '33', '34', '35', '36', '37', '38', '39',
        '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59']



# DAY_ list.
day_list=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

# Ringtones list.
ringtones_list = ['bird', 'old', 'ku ku', 'morning']

# Ringtones Path.
ringtones_path = {
    'bird': 'ralarm_tones/bird_alarmtone.mp3',
    'old': 'ralarm_tones/old_alarmtone.mp3',
    'ku ku': 'ralarm_tones/ku_ku.mp3',
    'morning': 'ralarm_tones/morning_alarmtone.mp3'
    
}
############################################
def show_time():
    current_time = datetime.datetime.now().strftime('%H:%M:%S    %A')
    # Placing the time format level.
    display.config(text = current_time)
    display.after(100, show_time)

def test_alarm_sound():
    global alarm_combobox
    alarm_selected_name=alarm_combobox.get()
    alarm_selected_path=ringtones_path [alarm_selected_name]
    alarm=pygame.mixer.Sound(alarm_selected_path)
    alarm.play(maxtime=3000)

def set_alarm():
    global alarm_combobox,hours_combobox,minutes_combobox,AM_PM_combobox,day_combobox,message_entry
    current_time = datetime.datetime.now().strftime('%H:%M    %A')
    # print(current_time)
    h=hours_combobox.get()
    m=minutes_combobox.get()
    day=day_combobox.get()

    set_time=h+":"+m+'    '+day
    while current_time!=set_time:
        
        pygame.time.delay(1000)
        current_time = datetime.datetime.now().strftime('%H:%M    %A')

        
    test_alarm_sound()
    messagebox.showinfo(message=str(message_entry.get()))
    

def window2():
    global alarm_combobox,hours_combobox,minutes_combobox,day_combobox,message_entry
    win2 =tk.Toplevel()
    win2.title("Set Alarm")
    win2.geometry("500x400+200+200")

    img= Image.open('back2.jpg')
    resized_image= img.resize((500,400))
    bg_image = ImageTk.PhotoImage(resized_image)

    background = tk.Label(win2, image=bg_image)  #Create a Label Widget to display the text or Image
    background.place(x=0,y=0)


    # Hour Label and comb.
    hours_label = tk.Label(win2, text="Hours", font=("times new roman",18))
    hours_label.place(x=50, y=50)

    # Hour Combobox.
    set_hour= tk.StringVar()
    hours_combobox = ttk.Combobox(win2, width=10, height=10, textvariable=set_hour,font=("times new roman",10))
    hours_combobox['values'] = hours_list
    hours_combobox.current(0)
    hours_combobox.place(x=30,y=90)

    # Minute Label.
    minute_label = tk.Label(win2, text="Minutes", font=("times new roman",18))
    minute_label.place(x=140, y=50)

    # minute Combobox.
    set_minute= tk.StringVar()
    minutes_combobox = ttk.Combobox(win2, width=10, height=10, textvariable=set_minute,font=("times new roman",10))
    minutes_combobox['values'] = minutes_list
    minutes_combobox.current(0)
    minutes_combobox.place(x=130,y=90)

 

    # day Label.
    day_label = tk.Label(win2, text="day", font=("times new roman",18))
    day_label.place(x=270, y=50)

    # day Combobox.
    set_day= tk.StringVar()
    day_combobox = ttk.Combobox(win2, width=10, height=10, textvariable=set_day,font=("times new roman",10))
    day_combobox['values'] = day_list
    day_combobox.current(0)
    day_combobox.place(x=250,y=90)

    # alarm sound Label.
    alarm_sound_label = tk.Label(win2, text="alarm sound", font=("times new roman",18),bg="pink")
    alarm_sound_label.place(x=350, y=50)

    # alarm sound Combobox.
    set_alarm_sound= tk.StringVar()
    alarm_combobox = ttk.Combobox(win2, width=10, height=10, textvariable=set_alarm_sound,font=("times new roman",10))
    alarm_combobox['values'] = ringtones_list
    alarm_combobox.current(0)
    alarm_combobox.place(x=370,y=90)

    # Title or Message Label.
    message_label = tk.Label(win2, text="Message", font=("times new roman",18))
    message_label.place(x=210, y=210)

    # Message Entrybox: This Message will show, when
    # the alarm will ringing.
    message = tk.StringVar()
    message_entry = tk.Entry(win2, textvariable=message, font=("times new roman",13), width=15)
    message_entry.insert(0, 'Wake Up')
    message_entry.place(x=180, y=250)

    # Test Button: For testing the ringtone music.
    test_button = tk.Button(win2, text='Test sound',font=('Helvetica',12), bg="white", fg="black", command=test_alarm_sound)
    test_button.place(x=360, y=120)

    # close win2.
    cancel_button = tk.Button(win2, text='Cancel', font=('Helvetica',15), bg="white",fg="black", command=win2.destroy)
    cancel_button.place(x=320, y=330)

    # The Start Button: For set the alarm time
    start_button = tk.Button(win2, text='Start',font=('Helvetica',15), bg="green", fg="white", command=thread2.start)
    start_button.place(x=400, y=330)

    win2.mainloop()

###################################################
win = tk.Tk()
win.geometry('420x600')
win.title('night clock')
win.iconbitmap('a.ico')

img= Image.open('back3.jpg')
resized_image= img.resize((420,600))
bg_image = ImageTk.PhotoImage(resized_image)

background = tk.Label(win, image=bg_image)  #Create a Label Widget to display the text or Image
background.place(x=0,y=0)

display = tk.Label(win,font=('Arial Rounded MT Bold',24),bg='blue4',fg='khaki1')
display.place(x=20,y=30) 

# Display Label that shows the current time in the
thread1 = threading.Thread(target=show_time)
thread2 = threading.Thread(target=set_alarm)
thread1.start()

set_button =tk.Button(win, text='set Alarm',font=('comic sans ms',16),bg='khaki1',command=window2)
set_button.place(x=270,y=530)

win.mainloop()