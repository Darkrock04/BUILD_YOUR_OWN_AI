from openai import OpenAI
import tkinter as tk
from tkinter import scrolledtext

def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if user_input:
        completion = client.chat.completions.create(
            model="meta/llama-3.3-70b-instruct",
            messages=[{"role": "user", "content": user_input}],                                                                                                                                                                                                
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            stream=True
        )
        output_box.delete("1.0", tk.END)
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                output_box.insert(tk.END, chunk.choices[0].delta.content)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="nvapi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-VSkHJIa"
)

# Create the main window
root = tk.Tk()
root.title("AI Chat Interface")
root.geometry("800x700")
root.configure(bg="#34495e")

# Create input section
input_frame = tk.Frame(root, bg="#34495e")
input_frame.pack(pady=10, padx=10, fill=tk.X)

input_label = tk.Label(input_frame, text="Enter your message:", bg="#34495e", fg="white", font=("Helvetica", 14, "bold"))
input_label.pack(anchor="w", padx=5)

input_box = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=75, height=10, font=("Helvetica", 12))
input_box.pack(pady=5, padx=5)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message, bg="#1abc9c", fg="white", font=("Helvetica", 14, "bold"), relief=tk.RAISED, bd=3)
send_button.pack(pady=10)

# Create output section
output_frame = tk.Frame(root, bg="#34495e")
output_frame.pack(pady=10, padx=10, fill=tk.X)

output_label = tk.Label(output_frame, text="Response:", bg="#34495e", fg="white", font=("Helvetica", 14, "bold"))
output_label.pack(anchor="w", padx=5)

output_box = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=75, height=18, font=("Helvetica", 12))
output_box.pack(pady=5, padx=5)

# Start the GUI event loop
root.mainloop()