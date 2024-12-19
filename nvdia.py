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
    api_key="nvapi-o5lxzQJsQ2u-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-EDBVF9vbmhc"
)

# Create the main window
root = tk.Tk()
root.title("AI Chat Interface")
root.geometry("800x700")

# Create input section
input_label = tk.Label(root, text="Enter your message:")
input_label.pack(pady=5)

input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=10)
input_box.pack(pady=5)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Create output section
output_label = tk.Label(root, text="Response:")
output_label.pack(pady=5)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=18)
output_box.pack(pady=5)

# Start the GUI event loop
root.mainloop()