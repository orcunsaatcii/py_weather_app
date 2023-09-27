import requests
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image
from tkinter import messagebox


window = Tk()
window.geometry("600x600")
window.config(pady=10, padx=50, bg="#009DFF")
window.title("Weather Application")

api_key = "63a09a6a8075485cb37190019232309"


def show_weather():
    unit = "°C"
    temp = ""
    feelslike = ""
    city = city_entry.get()
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    weather_data = response.json()

    if rb.get() == 1:
        if city_entry.get() == "":
            pass
        else:
            unit = "°C"
            temp = str(weather_data["current"]["temp_c"])
            feelslike = str(weather_data["current"]["feelslike_c"])

    elif rb.get() == 2:
        if city_entry.get() == "":
            pass
        else:
            unit = "°F"
            temp = str(weather_data["current"]["temp_f"])
            feelslike = str(weather_data["current"]["feelslike_f"])

    if response.status_code == 200:

        location_label.config(text=str(weather_data["location"]["name"]) + ", " + str(weather_data["location"]["country"]))
        temperature_label.config(text=temp + unit)
        wind_direction_label.config(text="Wind Direction    " + str(weather_data["current"]["wind_dir"]))
        wind_speed_label.config(text=str(weather_data["current"]["wind_kph"]) + " kp/h")
        humidity_value.config(text=str(weather_data["current"]["humidity"]) + "%")
        feel_value.config(text=feelslike + "°")
        uv_value.config(text=weather_data["current"]["uv"])
        pressure_value.config(text=weather_data["current"]["pressure_mb"])
        forecast_value.config(text=weather_data["current"]["condition"]["text"])
        image_response = requests.get("https:" + str(weather_data["current"]["condition"]["icon"]))
        image_data = BytesIO(image_response.content)
        image = Image.open(image_data)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        print(weather_data)

    else:
        messagebox.showinfo(title="INFO", message="Please enter a city")


search_bar_frame = Frame(window, bg="#009DFF")
search_bar_frame.pack()

city_entry = Entry(search_bar_frame, font=("Arial", 15, "normal"))
city_entry.focus()
city_entry.pack(padx=7, side=LEFT)

img_button = PhotoImage(file="zoom_icon.png")
button = Button(search_bar_frame, text="Search", command=show_weather, image=img_button, width=60, height=22)
button.image = img_button
button.pack(side=RIGHT)

temp_frame = Frame(window, bg="#009DFF")
temp_frame.pack(pady=20)

temperature_label = Label(temp_frame, font=("Arial", 50, "normal"), bg="#009DFF", fg="white")
temperature_label.pack()

location_label = Label(temp_frame, font=("Arial", 15, "normal"), bg="#009DFF", fg="white")
location_label.pack()

image_label = Label(temp_frame, bg="#009DFF")
image_label.pack()

forecast_info_canvas = Canvas(window,bg="#0067B9", width=230, height=112)
forecast_info_canvas.place(x=5, y=250)

text = Label(forecast_info_canvas, text="Weather", font=("Fixedsys", 14, "normal"), bg="#0067B9", fg="#F1F1F1")
text.place(relx=0.5, rely=0.13, anchor=CENTER)

forecast_value = Label(forecast_info_canvas, font=("Arial", 18, "normal"), bg="#0067B9", fg="white")
forecast_value.place(relx=0.5, rely=0.5, anchor=CENTER)

wind_info_canvas = Canvas(window, bg="#0067B9", width=230, height=112)
wind_info_canvas.place(x=5, y=373)

text2 = Label(wind_info_canvas, text="Wind", font=("Fixedsys", 14, "normal"), bg="#0067B9", fg="#F1F1F1")
text2.place(relx=0.5, rely=0.13, anchor=CENTER)

wind_direction_label = Label(wind_info_canvas, font=("Arial", 15, "normal"), bg="#0067B9", fg="white")
wind_direction_label.place(relx=0.5, rely=0.3, anchor=CENTER)

wind_speed_label = Label(wind_info_canvas, font=("Arial", 25, "normal"), bg="#0067B9", fg="white")
wind_speed_label.place(relx=0.5, rely=0.6, anchor=CENTER)

general_info_canvas = Canvas(window, bg="#0067B9", width=230, height=235)
general_info_canvas.place(x=250, y=250)

humidity_label = Label(general_info_canvas, text="Humidity", font=("Fixedsys", 15, "normal"), bg="#0067B9", fg="#F1F1F1")
humidity_label.place(x=15, y=10)

humidity_value = Label(general_info_canvas, font=("Arial", 20, "normal"), bg="#0067B9", fg="white")
humidity_value.place(x=160, y=6)

feel_label = Label(general_info_canvas, text="Real feel", font=("Fixedsys", 15, "normal"), bg="#0067B9", fg="#F1F1F1")
feel_label.place(x=15, y=66)

feel_value = Label(general_info_canvas, font=("Arial", 20, "normal"), bg="#0067B9", fg="white")
feel_value.place(x=150, y=60)

uv_label = Label(general_info_canvas, text="UV", font=("Fixedsys", 15, "normal"), bg="#0067B9", fg="#F1F1F1")
uv_label.place(x=15, y=122)

uv_value = Label(general_info_canvas, font=("Arial", 20, "normal"), bg="#0067B9", fg="white")
uv_value.place(x=175, y=118)

pressure_label = Label(general_info_canvas, text="Pressure", font=("Fixedsys", 15, "normal"), bg="#0067B9", fg="#F1F1F1")
pressure_label.place(x=15, y=178)

pressure_value = Label(general_info_canvas, font=("Arial", 20, "normal"), bg="#0067B9", fg="white")
pressure_value.place(x=130, y=174)

general_info_canvas.create_line(20, 47, 215, 47, fill="white")
general_info_canvas.create_line(20, 103, 215, 103, fill="white")
general_info_canvas.create_line(20, 159, 215, 159, fill="white")
general_info_canvas.create_line(20, 215, 215, 215, fill="white")



rb = IntVar()
rb.set(1)
c_radio_button = Radiobutton(text="Celsius",value=1,variable=rb, command=show_weather, bg="#009DFF")
f_radio_button = Radiobutton(text="Fahrenheit",value=2,variable=rb, command=show_weather, bg="#009DFF")

c_radio_button.place(relx=0.41, rely=0.9, anchor=CENTER)
f_radio_button.place(relx=0.59, rely=0.9, anchor=CENTER)

window.mainloop()




