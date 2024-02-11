import tkinter as tk
from datetime import datetime
import pywhatkit

def send_message():
    mobile = mobile_entry.get()
    message = message_entry.get()
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())

    # Get current time
    now = datetime.now()
    current_hour = now.strftime("%H")

    # Check if it's not too late to send the message
    if int(current_hour) <= hour:
        # Send the WhatsApp message
        pywhatkit.sendwhatmsg(mobile, message, hour, minute)
        result_label.config(text="WhatsApp message sent successfully!")
    else:
        result_label.config(text="Sorry, it's too late to send the message.")

# Create the main window
root = tk.Tk()
root.title("WhatsApp Message Sender")

# Create and place labels, entries, and button
mobile_label = tk.Label(root, text="Mobile No of Receiver:")
mobile_label.grid(row=0, column=0, padx=10, pady=5)
mobile_entry = tk.Entry(root)
mobile_entry.grid(row=0, column=1, padx=10, pady=5)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=1, column=0, padx=10, pady=5)
message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1, padx=10, pady=5)

hour_label = tk.Label(root, text="Hour:")
hour_label.grid(row=2, column=0, padx=10, pady=5)
hour_entry = tk.Entry(root)
hour_entry.grid(row=2, column=1, padx=10, pady=5)

minute_label = tk.Label(root, text="Minute:")
minute_label.grid(row=3, column=0, padx=10, pady=5)
minute_entry = tk.Entry(root)
minute_entry.grid(row=3, column=1, padx=10, pady=5)

send_button = tk.Button(root, text="Send WhatsApp Message", command=send_message)
send_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()
