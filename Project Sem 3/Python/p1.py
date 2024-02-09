import tkinter as tk

def open_new_frame():
    # Destroy the current frame
    current_frame.destroy()

    # Create a new frame
    new_frame = tk.Frame(root, width=20, height=10, bg='blue')
    new_frame.pack()

    # Add widgets to the new frame
    label = tk.Label(new_frame, text="New Frame Created", fg="white", bg="blue")
    label.pack()

# Create the main Tkinter window
root = tk.Tk()
root.geometry("300x200")

# Create the initial frame
current_frame = tk.Frame(root, width=200, height=100, bg='red')
current_frame.pack()

# Add widgets to the initial frame
button = tk.Button(current_frame, text="Click Me", command=open_new_frame)
button.pack()

# Run the Tkinter event loop
root.mainloop()
