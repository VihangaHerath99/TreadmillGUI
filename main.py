import tkinter as tk
import threading
import time
# import math
from utilities import*

display = ["WELCOME","TreadMill\n\nDashboard","Developed by\nVihanga Herath","Enter gradient\nin degrees","Enter Height\nin inches","Enter Weight\nin kg","Enter RPM"]

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    #def callback(self):
        #self.root.quit()

    def run(self):
        self.root = tk.Tk()
        #self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.geometry("1550x700")
        self.root.title("TreadMill DashBoard")
        self.root['background'] = "Black"
        
        #Speed 
        speed_border = tk.Label(self.root, width=27, bg="Yellow")
        speed_border.grid(row=2, column=1, columnspan=2)
        l_speed = tk.Label(speed_border, text="Speed", bg="Black",fg="white",height=2, width=15, font = "Helvetica 20 bold")
        l_speed.grid(row=1,column=0)
        global v_speed
        v_speed = tk.Label(speed_border, text="0", bg="Black", width=8, height=2, fg="Yellow", font = "Helvetica 20 bold ")
        v_speed.grid(row=1, column=1)

        space_1 = tk.Label(self.root, text="               TreadMill DashBoard", font = "Times 20 italic bold", fg="White", width=50, height=2, bg="Black")
        space_1.grid(row=1, column=0, columnspan=15)

        #Distance
        distance_border = tk.Label(self.root, width=27, bg="Yellow")
        distance_border.grid(row=3, column=1, columnspan=2)
        l_distance = tk.Label(distance_border, text="Distance",  width=15, height=2,bg="Black",fg="white", font = "Helvetica 20 bold ")
        l_distance.grid(row=1,column=0)
        global v_distance
        v_distance = tk.Label(distance_border, text="0", bg="Black", width=8, height=2,fg="Yellow", font = "Helvetica 20 bold ")
        v_distance.grid(row=1, column=1)

        space_2 = tk.Label(self.root, width=5, bg="Black")
        space_2.grid(row=1, column=0, rowspan=5)

        #Calories
        cal_border = tk.Label(self.root, width=27, bg="Yellow")
        cal_border.grid(row=4, column=1, columnspan=2)
        l_cal = tk.Label(cal_border, text="Burned Calories", width=15, height=2,bg="Black",fg="white", font = "Helvetica 20 bold ")
        l_cal.grid(row=1,column=0)
        global v_cal
        v_cal = tk.Label(cal_border, text="0", bg="Black",width=8, height=2,fg="Yellow", font = "Helvetica 20 bold ")
        v_cal.grid(row=1, column=1)

        space_3 = tk.Label(self.root, bg="Black", width=12)
        space_3.grid(row=2, column=5, rowspan=8)

        #Step
        step_border = tk.Label(self.root, width=27, bg="Yellow")
        step_border.grid(row=5, column=1, columnspan=2)
        l_step = tk.Label(step_border, text="Steps",  width=15, height=2,bg="Black",fg="white", font = "Helvetica 20 bold ")
        l_step.grid(row=1,column=0)
        global v_step
        v_step = tk.Label(step_border, text="0", bg="Black",width=8, height=2,fg="Yellow", font = "Helvetica 20 bold ")
        v_step.grid(row=1,column=1)

        #Digital Display
        display_border = tk.Label(self.root, bg="Red")
        display_border.grid(row=2, column=4, rowspan=4)
        display_name = tk.Label(display_border, text="Digital Display", width=33, bg="Black", fg="White", font="Times 20 bold")
        display_name.grid(row=1)
        global digital_display
        digital_display = tk.Label(display_border, width=22,text="Enter RPM", height=4, pady=40, font = "Times 30 bold", fg="Blue")
        digital_display.grid(row=2)

        #Input Display
        RPM_border = tk.Label(self.root, width=27, bg="Green")
        RPM_border.grid(row=7, column=1, columnspan=2)
        l_RPM = tk.Label(RPM_border, text="RPM", bg="Black",fg="white",height=2, width=15, font = "Helvetica 16 bold")
        l_RPM.grid(row=1,column=0)
        global v_RPM
        v_RPM = tk.Label(RPM_border, text="0", bg="Black", width=8, height=2, fg="Yellow", font = "Helvetica 16 bold ")
        v_RPM.grid(row=1, column=1)

        weight_border = tk.Label(self.root, width=27, bg="Green")
        weight_border.grid(row=8, column=1, columnspan=2)
        l_weight = tk.Label(weight_border, text="Weight", bg="Black",fg="white",height=2, width=15, font = "Helvetica 16 bold")
        l_weight.grid(row=1,column=0)
        global v_weight
        v_weight = tk.Label(weight_border, text="0", bg="Black", width=8, height=2, fg="Yellow", font = "Helvetica 16 bold ")
        v_weight.grid(row=1, column=1)

        height_border = tk.Label(self.root, width=27, bg="Green")
        height_border.grid(row=9, column=1, columnspan=2)
        l_height = tk.Label(height_border, text="Height", bg="Black",fg="white",height=2, width=15, font = "Helvetica 16 bold")
        l_height.grid(row=1,column=0)
        global v_height
        v_height = tk.Label(height_border, text="0", bg="Black", width=8, height=2, fg="Yellow", font = "Helvetica 16 bold ")
        v_height.grid(row=1, column=1)

        grade_border = tk.Label(self.root, width=27, bg="Green")
        grade_border.grid(row=10, column=1, columnspan=2)
        l_grade = tk.Label(grade_border, text="Gradient", bg="Black",fg="white",height=2, width=15, font = "Helvetica 16 bold")
        l_grade.grid(row=1,column=0)
        global v_grade
        v_grade = tk.Label(grade_border, text="0", bg="Black", width=8, height=2, fg="Yellow", font = "Helvetica 16 bold ")
        v_grade.grid(row=1, column=1)
        
        #Timer
        l_timer_border = tk.Label(self.root, width=17, height=2, bg="Yellow")
        l_timer_border.grid(row=2, column=6, columnspan=2)
        l_timer = tk.Label(l_timer_border, text="Timer", width=8, height=2,bg="Black",fg="white", font = "Times 20 bold")
        l_timer.grid(row=2, column=4)
        global v_timer
        v_timer = tk.Label(l_timer_border, text="0", width=12, height=2, fg="Yellow", bg="Black", font = "Times 20 bold")
        v_timer.grid(row=2, column=5)

        space_4 = tk.Label(self.root, width=12, bg="Black")
        space_4.grid(row=2, rowspan=6, column=3)

        #Numberpad buttons functions
        def on():
            '''function for ON button'''
            global switch
            global y
            if y==5:
                switch = True
                y = 6
                button_on.config(bg="Red")
        
        def stop():
            '''function for OFF button'''
            digital_display.config(text="GOOD BYE !!!")
            global switch
            switch = False
            button_on.config(bg="DarkRed")
            button_off.config(bg="Red")
            
            
        def button_click(number):
            current = e.get()
            e.delete(0, tk.END)
            e.insert(0, current+str(number))
            
        def enter():#Enter Key
            num = e.get()
            global RPM
            global weight
            global height
            global grade
            global editting
            if len(num)>0:
                global y
                if y==1:
                    RPM = int(e.get())
                    v_RPM.config(text=str(RPM))
                    digital_display.config(text=display[-2])
                    y=2
                elif y==2:
                    weight = float(e.get())
                    v_weight.config(text=str(weight)+" kg")
                    digital_display.config(text=display[-3])
                    y=3
                elif y==3:
                    height = float(e.get())
                    v_height.config(text=str(height)+" inch")
                    digital_display.config(text=display[-4])
                    y=4
                elif y==4:
                    gradient = float(e.get())
                    grade = gradient/100
                    v_grade.config(text=str(gradient)+"'")
                    digital_display.config(text='Are you\nReady?\n"Press ON"')
                    y=5
                elif y==7:
                    in_val=num.split('.')
                    if len(in_val)==2:
                        if int(in_val[0])==1:
                            RPM = int(in_val[1])
                            v_RPM.config(text=str(RPM))
                            editting = "NO"
                        elif int(in_val[0])==2:
                            weight = float(in_val[1])
                            v_weight.config(text=str(weight)+" kg")
                            editting = "NO"
                        elif int(in_val[0])==3:
                            height = float(in_val[1])
                            v_height.config(text=str(height)+" inch")
                            editting = "NO"
                        elif int(in_val[0])==4:
                            grade = int(in_val[1])/100
                            v_grade.config(text=str(grade*100)+"'")
                            editting = "NO"
                        else:digital_display.config(text='incorrect index\n"press edit again"')
                    elif len(in_val)==3:
                        if int(in_val[0])==1:
                            RPM = float(str(in_val[1])+'.'+str(in_val[2]))
                            v_RPM.config(text=str(RPM))
                            editting = "NO"
                        elif int(in_val[0])==2:
                            weight = float(str(in_val[1])+'.'+str(in_val[2]))
                            v_weight.config(text=str(weight)+" kg")
                            editting = "NO"
                        elif int(in_val[0])==3:
                            height = float(str(in_val[1])+'.'+str(in_val[2]))
                            v_height.config(text=str(height)+" inch")
                            editting = "NO"
                        elif int(in_val[0])==4:
                            grade = float(str(in_val[1])+'.'+str(in_val[2]))/100
                            v_grade.config(text=str(grade*100)+"'")
                            editting = "NO"
                        else:digital_display.config(text='incorrect index\n"press edit again"')
                    else:digital_display.config(text='incorrect input\n"press edit again"')
                e.delete(0, tk.END)

        def edit():#edit button
            digital_display.config(text="Indedx\n1-RPM 2-Weight\n3-Height 4-Gradient\n\nInput\n(Index).(NewValue)")
            global editting
            editting = "YES"

        def button_AC():#All clear button(AC)
            e.delete(0, tk.END)

        def button_clear():#clear button
            num = str(e.get())
            digits = list()
            final_num = str()
            for digit in num :
                digits.append(digit)
            if len(digits)>0:
                digits.pop(-1)
                for d in range(len(digits)):
                    final_num = final_num+str(digits[d])
                e.delete(0, tk.END)
                e.insert(0, final_num)

        #unit conversions buttons
        def s_ms(x):
            global unit_speed
            unit_speed = "m/s"
            speed_ms.config(bg="Red")
            speed_mmin.config(bg="DarkRed")

        def s_mmin(x):
            global unit_speed
            unit_speed = "m/min"
            speed_ms.config(bg="DarkRed")
            speed_mmin.config(bg="Red")

        def dis_miles(x):
            global unit_distance
            unit_distance = "miles"
            distance_m.config(bg="DarkRed")
            distance_miles.config(bg="Red")

        def dis_km(x):
            global unit_distance
            unit_distance = "m"
            distance_m.config(bg="Red")
            distance_miles.config(bg="DarkRed")
        
        #Numberpad buttons & entry
        numberpad = tk.Label(self.root, bg="Yellow")
        numberpad.grid(row=3, column=6,columnspan=3, rowspan=10)

        global e
        e = tk.Entry(numberpad, width=53, borderwidth=5)
        e.grid(row=1, column=0, columnspan=3)
        
        button_1 = tk.Button(numberpad, text='1', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(1))
        button_1.grid(row=2, column=0)
        button_2 = tk.Button(numberpad, text='2', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(2))
        button_2.grid(row=2, column=1)
        button_3 = tk.Button(numberpad, text='3', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(3))
        button_3.grid(row=2, column=2)

        button_4 = tk.Button(numberpad, text='4', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(4))
        button_4.grid(row=3, column=0)
        button_5 = tk.Button(numberpad, text='5', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(5))
        button_5.grid(row=3, column=1)
        button_6 = tk.Button(numberpad, text='6', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(6))
        button_6.grid(row=3, column=2)

        button_7 = tk.Button(numberpad, text='7', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(7))
        button_7.grid(row=4, column=0)
        button_8 = tk.Button(numberpad, text='8', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(8))
        button_8.grid(row=4, column=1)
        button_9 = tk.Button(numberpad, text='9', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(9))
        button_9.grid(row=4, column=2)

        button_0 = tk.Button(numberpad, text='0', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click(0))
        button_0.grid(row=5, column=0)
        button_enter = tk.Button(numberpad, text='Enter', width=21, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=enter)
        button_enter.grid(row=5, column=1,columnspan=2)

        button_dot = tk.Button(numberpad, text='.', width=10, height=3, font="Times 13 bold", bg="LightBlue", fg="Blue", command=lambda: button_click('.'))
        button_dot.grid(row=6, column=0)
        button_AC = tk.Button(numberpad, text='AC', width=10, height=3,font="Times 13 bold", bg="LightBlue", fg="Blue", command=button_AC)
        button_AC.grid(row=6, column=2)
        button_clear = tk.Button(numberpad, text='clear', width=10, height=3,font="Times 13 bold", bg="LightBlue", fg="Blue", command=button_clear)
        button_clear.grid(row=6, column=1)

        #ON/OFF border
        power_border = tk.Label(self.root, bg="Blue")
        power_border.grid(row=6, column=4)
        #OFF button
        button_off = tk.Button(power_border,text="OFF",height=2, width=10, bg="DarkRed", fg="White", font="Times 16 bold", command=stop)
        button_off.grid(row=1, column=1)

        #ON button
        button_on = tk.Button(power_border, text="ON",height=2, width=10, bg="DarkRed", fg="White", font="Times 16 bold", command=on)
        button_on.grid(row=1, column=0)

        #Edit button
        edit_border = tk.Label(self.root, bg="Black")
        edit_border.grid(row=11, column=1)
        button_edit = tk.Button(edit_border, text="EDIT", bg="green", width=20, fg="White", font="Times 14 bold", command=edit)
        button_edit.grid(row=1, column=1)
        space_6 = tk.Label(edit_border, bg="black", width=7)
        space_6.grid(row=1, column=0)

        #unit control pad
        controlpad_border = tk.Label(self.root, bg="Blue")
        controlpad_border.grid(row=7, column=3, rowspan=5, columnspan=2)
        L_padname = tk.Label(controlpad_border, bg="Black", text="Unit Conversions",fg="White", width=27, font="Times 20 bold italic")
        L_padname.grid(row=1, columnspan=2)

        unispeed_border = tk.Label(controlpad_border, bg="Yellow")
        unispeed_border.grid(row=2, column=0, rowspan=2)
        L_unispeed = tk.Label(unispeed_border, bg="Yellow", height=1, text="Speed", fg="Black", width=12, font="Times 20 bold")
        L_unispeed.grid(row=1, columnspan=2)
        speed_ms = tk.Button(unispeed_border, bg="Red", text="m/s", fg="White",width=6, height=1, font="Times 20 bold", command=lambda:s_ms(unit_speed))
        speed_ms.grid(row=2, column=0)
        speed_mmin = tk.Button(unispeed_border, bg="DarkRed", text="m/min", fg="White", height=1, width=6, font="Times 20 bold", command=lambda:s_mmin(unit_speed))
        speed_mmin.grid(row=2, column=1)

        unidistance_border = tk.Label(controlpad_border, bg="Yellow")
        unidistance_border.grid(row=2, column=1, rowspan=2)
        L_unidistance = tk.Label(unidistance_border, bg="Yellow", height=1, text="Distance", fg="Black",width=12, font="Times 20 bold")
        L_unidistance.grid(row=1, columnspan=2)
        distance_m = tk.Button(unidistance_border, bg="Red", text="m|km", fg="White", height=1,width=6, font="Times 20 bold", command=lambda:dis_km(unit_distance))
        distance_m.grid(row=2, column=0)
        distance_miles = tk.Button(unidistance_border, bg="DarkRed", text="miles", fg="White", height=1, width=6, font="Times 20 bold", command=lambda:dis_miles(unit_distance))
        distance_miles.grid(row=2, column=1)

        self.root.mainloop()


app = App()
print('Welcome to the Treadmill Dasboard Programme')

# getting inputs
y = 1
editting = "NO"
while True:
    if y==6:break

#realtime loop
radius = 8
unit_speed = "m/s"
unit_distance = "m"
i = 0
begin_time = time.time()
while switch:
    
    #taking time difference
    end_time = time.time()
    time_def = (end_time-begin_time)/(60*60)

    #calculations
    if unit_speed == "m/s":v_speed.config(text=str(round(speed(RPM,radius),3))+" m/s")
    elif unit_speed == "m/min":v_speed.config(text=str(round(speed(RPM,radius)*60))+" m/min")
    
    if unit_distance == "m":
        t_distance = distance(RPM,radius,time_def)
        if t_distance <1000 :v_distance.config(text=str(t_distance)+" m")
        else:v_distance.config(text=str(round(t_distance/1000,2))+" km")
    elif unit_distance == "miles":
        v_distance.config(text=str(round(distance(RPM,radius,time_def)/1609.34,2))+" miles")
                                                     
    v_cal.config(text=str(calories_burnt(RPM,radius,time_def,weight,grade))+" cal")
    v_step.config(text=steps(height,RPM,radius,time_def))

    #calculations for Timer
    if round(end_time-begin_time)< 60:
        v_timer.config(text="00:"+str(round(end_time-begin_time))+" min:sec")
    else:
        v_timer.config(text=str(round(end_time-begin_time)//60)+":"+str(round(end_time-begin_time)%60)+" min:sec")

    #check to edit
    while editting == "YES":
        y = 7
        if editting == "NO":break

    #Display handling
    i = i + 1
    if i == 3000:digital_display.config(text=display[0])
    elif i == 6000:digital_display.config(text=display[1])
    elif i == 9000:digital_display.config(text=display[2])
    elif i == 12000:
        digital_display.config(text="Current Time\n"+str(time.strftime("%H:%M:%S", time.localtime())))
        i = 0