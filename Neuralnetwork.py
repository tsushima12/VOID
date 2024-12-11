import tkinter as tk
from tkinter import ttk
import random
import time

# Global flag to control blinking
running = False

def simulate_network():
    global running
    running = True  # Set flag to True to start blinking

    num_inputs = int(input_neurons.get())
    num_hidden = int(hidden_neurons.get())
    num_outputs = int(output_neurons.get())
    
    canvas.delete("all")  # Clear previous simulation
    
    width = canvas.winfo_width()  # Get the current width of the canvas
    height = canvas.winfo_height()  # Get the current height of the canvas
    margin = 50
    layer_spacing = width // 4
    neuron_spacing = 40

    # Store positions for blinking effect
    input_positions = []
    hidden_positions = []
    output_positions = []

    # Draw input layer
    for i in range(num_inputs):
        x = margin
        y = margin + i * neuron_spacing
        pos = (x, y, x + 20, y + 20)
        input_positions.append(pos)
        canvas.create_oval(*pos, fill="skyblue", outline="black")
    
    # Draw hidden layer
    for i in range(num_hidden):
        x = margin + layer_spacing
        y = margin + i * neuron_spacing
        pos = (x, y, x + 20, y + 20)
        hidden_positions.append(pos)
        canvas.create_oval(*pos, fill="lightgreen", outline="black")

    # Draw output layer
    for i in range(num_outputs):
        x = margin + 2 * layer_spacing
        y = margin + i * neuron_spacing
        pos = (x, y, x + 20, y + 20)
        output_positions.append(pos)
        canvas.create_oval(*pos, fill="orange", outline="black")

    # Connect layers with lines
    for i in range(num_inputs):
        for j in range(num_hidden):
            canvas.create_line(
                margin + 10,
                margin + i * neuron_spacing + 10,
                margin + layer_spacing + 10,
                margin + j * neuron_spacing + 10,
                fill="gray",
            )

    for i in range(num_hidden):
        for j in range(num_outputs):
            canvas.create_line(
                margin + layer_spacing + 10,
                margin + i * neuron_spacing + 10,
                margin + 2 * layer_spacing + 10,
                margin + j * neuron_spacing + 10,
                fill="gray",
            )

    # Start the random blinking animation
    blink_random_neurons(input_positions, hidden_positions, output_positions)

def blink_random_neurons(input_pos, hidden_pos, output_pos):
    global running
    all_positions = input_pos + hidden_pos + output_pos  # Combine all neuron positions
    while running:  # Only blink while the flag is True
        # Randomly select a neuron position
        random_neuron = random.choice(all_positions)

        # Blink the selected neuron (change to yellow, then back to original color)
        x1, y1, x2, y2 = random_neuron
        original_color = "skyblue" if random_neuron in input_pos else "lightgreen" if random_neuron in hidden_pos else "orange"
        
        # Highlight the neuron (yellow)
        canvas.create_oval(x1, y1, x2, y2, fill="yellow", outline="black")
        canvas.update()
        time.sleep(0.1)  # Wait for 100ms to simulate blinking
        
        # Return the neuron to its original color
        canvas.create_oval(x1, y1, x2, y2, fill=original_color, outline="black")
        canvas.update()
        time.sleep(0.1)  # Wait for another 100ms

        # Repeat the blinking for random neurons
        canvas.after(200, blink_random_neurons, input_pos, hidden_pos, output_pos)  # Call again to repeat

def stop_blinking():
    global running
    running = False  # Stop the blinking

# Create the main window
root = tk.Tk()
root.title("Neural Network Simulation")

# Allow window resizing
root.resizable(True, True)  # Makes the window resizable in both directions

# Input section
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Input Neurons:").grid(row=0, column=0)
input_neurons = ttk.Entry(frame, width=5)
input_neurons.grid(row=0, column=1)
input_neurons.insert(0, "3")

ttk.Label(frame, text="Hidden Neurons:").grid(row=1, column=0)
hidden_neurons = ttk.Entry(frame, width=5)
hidden_neurons.grid(row=1, column=1)
hidden_neurons.insert(0, "4")

ttk.Label(frame, text="Output Neurons:").grid(row=2, column=0)
output_neurons = ttk.Entry(frame, width=5)
output_neurons.grid(row=2, column=1)
output_neurons.insert(0, "2")

simulate_button = ttk.Button(frame, text="Simulate", command=simulate_network)
simulate_button.grid(row=3, columnspan=2, pady=10)

# Stop Button
stop_button = ttk.Button(frame, text="Stop", command=stop_blinking)
stop_button.grid(row=4, columnspan=2, pady=10)

# Canvas for drawing the network
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.grid(row=1, column=0, pady=10, sticky="nsew")  # Make the canvas stretch

# Make the grid expand with resizing
root.grid_rowconfigure(1, weight=1)  # Allow row 1 (where the canvas is) to expand
root.grid_columnconfigure(0, weight=1)  # Allow column 0 (where the canvas is) to expand

root.mainloop()