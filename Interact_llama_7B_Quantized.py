import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import threading
from llama_cpp import Llama
from tkinter.scrolledtext import ScrolledText
import tkinter.font as tkfont


def get_answer():
    question = entry_var.get()
    if question.strip():
        loading_label.pack(pady=10)  # Show loading label while generating the answer
        submit_button.pack_forget()  # Hide the "Submit" button
        answer_text.config(state=tk.NORMAL)  # Enable text widget to update content
        answer_text.delete(1.0, tk.END)  # Clear previous answer content
        answer_text.config(state=tk.DISABLED)  # Disable text widget again
        threading.Thread(target=process_question, args=(question,)).start()


def process_question(question):
    llm = Llama(model_path=path)
    response = llm(question)
    answer = response['choices'][0]['text']
    # Remove the question mark from the answer
    loading_label.pack_forget()  # Hide loading label after getting the answer
    submit_button.pack(pady=10)  # Show the "Submit" button again

    # Update the answer text in the answer block
    answer_text.config(state=tk.NORMAL)  # Enable text widget to update content
    answer_text.insert(tk.END, f"Answer:\n{answer}\n\n")  # Insert new content with a new line
    answer_text.config(state=tk.DISABLED)  # Disable text widget again


def create_gui():
    root = tk.Tk()
    root.title("Llama 7B Quantized")

    style = ThemedStyle(root)
    style.set_theme("equilux")  # Choose the "equilux" theme for a modern look

    # Set fixed window size
    root.geometry("600x500")

    # Set GUI background color (equilux theme uses '#323232' for the background)
    root.configure(bg="#323232")

    # Create a frame with a 3D-like border
    frame = ttk.Frame(root, padding=10, relief=tk.RAISED)
    frame.pack(padx=20, pady=20)

    # Create a label and an entry widget for user input
    label = ttk.Label(frame, text="Ask Llama 7B Quantized", font=("Helvetica", 14))
    label.pack(pady=10)

    # Create a StringVar to store the user's input
    global entry_var
    entry_var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=entry_var, font=("Helvetica", 12), width=30)
    entry.pack(pady=5)

    # Create a submit button with a 3D-like effect using the "flat" style
    global submit_button
    submit_button = ttk.Button(frame, text="Submit", command=get_answer, style="flat.TButton")
    submit_button.pack(pady=10)

    # Create a label to display the loading message
    global loading_label
    loading_label = ttk.Label(frame, text="Generating answer...", font=("Helvetica", 12),
                              foreground="white")  # Set text color to white

    # Create a PanedWindow to make the question and answer blocks adjustable
    paned_window = ttk.PanedWindow(root, orient=tk.VERTICAL)
    paned_window.pack(fill=tk.BOTH, expand=True)

    # Create a frame for the question block
    question_frame = ttk.Frame(paned_window, relief=tk.RAISED)
    paned_window.add(question_frame)

    # Create a frame for the answer block
    answer_frame = ttk.Frame(paned_window, relief=tk.RAISED)
    paned_window.add(answer_frame)

    # Create a label frame to hold the answer
    answer_label_frame = ttk.LabelFrame(answer_frame, text="Answer", padding=10)
    answer_label_frame.pack(fill=tk.BOTH, expand=True)

    # Create a scrolled text widget for the answer
    global answer_text
    answer_text = ScrolledText(answer_label_frame, wrap=tk.WORD, bg="#323232", fg="white")  # Set text color to white
    answer_text.pack(fill=tk.BOTH, expand=True)

    # Set the font style for the answer text
    answer_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    answer_text.tag_configure("answer", font=answer_font, foreground="white")  # Set text color to white

    root.mainloop()


if __name__ == "__main__":
    path = r"C:\Users\gj979\Document_Assistance\models\llama-7b.ggmlv3.q4_0.bin"
    create_gui()
