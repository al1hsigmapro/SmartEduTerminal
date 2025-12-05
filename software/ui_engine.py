import serial

# current page
page = 1

def show(page):
    if page == 1:
        open("ui/step1.html", "w").write("<h1>Step 1: Choose interest</h1>")
    elif page == 2:
        open("ui/step2.html", "w").write("<h1>Step 2: Priority</h1>")
    elif page == 3:
        open("ui/thinking.html", "w").write("<h1>AI Thinking...</h1>")
    elif page == 4:
        open("ui/result.html", "w").write("<h1>Result: NU</h1>")

# serial connection
ser = serial.Serial("/dev/ttyACM0", 9600)

show(page)

while True:
    if ser.in_waiting:
        data = ser.readline().decode().strip()

        print(data)

        if "SW:0" in data:   # joystick click
            page += 1
            show(page)
