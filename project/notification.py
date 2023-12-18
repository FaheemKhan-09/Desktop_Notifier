import plyer as p
import tkinter as tk
from PIL import ImageTk
from queue import Queue


def notify():
    if not message_queue.empty():
        title, message = message_queue.get()
        p.notification.notify(
            title=title,
            message=message,
            app_name="Desktop Notifier",
            app_icon='icon1.ico',
            timeout=10
        )
        # Proceed to schedule the next notification
        root.after(0, notify)


def schedule_notification():
    try:
        timer_seconds = int(seconds_entry.get())
    except ValueError:
        return

    title = title_entry.get().strip()
    message = message_entry.get().strip()
    message_queue.put((title, message))

    # Clear the contents in the entry widgets
    title_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    seconds_entry.delete(0, tk.END)

    # Schedule the notification after the specified timer duration
    root.after(timer_seconds * 1000, notify)


# Set up Window Application
root = tk.Tk()
root.title("Desktop Notifier App")
root.geometry("400x300")
root.resizable()

# Image Path
image_path = 'Untitled.png'
img = ImageTk.PhotoImage(file=image_path)

# Image Label
image_label = tk.Label(root, image=img, width=400, height=100)
image_label.grid(row=0, column=0, columnspan=2)

# Title Text
title_label = tk.Label(root, text="Enter Title:", font=("Candara", 10))
title_label.grid(row=1, column=0, padx=9, pady=9)

# Text Entry
title_entry = tk.Entry(root, width=25, font=("Candara", 12))
title_entry.grid(row=1, column=1, padx=10, pady=10)

# Message Text
message_label = tk.Label(root, text="Enter Your Message:", font=("Candara", 10))
message_label.grid(row=2, column=0, padx=9, pady=9)

# Message Entry
message_entry = tk.Entry(root, width=25, font=("Candara", 12))
message_entry.grid(row=2, column=1, padx=10, pady=10)

# Set Seconds label
seconds_label = tk.Label(root, text="Seconds:", font=("Candara", 10))
seconds_label.grid(row=3, column=0, padx=9, pady=9)

# Set Second Entry
seconds_entry = tk.Entry(root, width=5, font=("Candara", 12))
seconds_entry.grid(row=3, column=1, padx=10, pady=10)

# Add Button
button = tk.Button(root, text="Submit For Notify", command=schedule_notification)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Initialize Message Queue
message_queue = Queue()

# Run The Application To Display the Design
root.mainloop()
