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
        loading_label.pack(pady=10)  
        submit_button.pack_forget()  
        answer_text.config(state=tk.NORMAL) 
        answer_text.delete(1.0, tk.END)  
        answer_text.config(state=tk.DISABLED)  
        threading.Thread(target=process_question, args=(question,)).start()


def process_question(question):
    llm = Llama(model_path=path)
    response = llm(question)
    answer = response['choices'][0]['text']
    loading_label.pack_forget()  
    submit_button.pack(pady=10)  

    answer_text.config(state=tk.NORMAL)  
    answer_text.insert(tk.END, f"Answer:\n{answer}\n\n")  
    answer_text.config(state=tk.DISABLED) 


def create_gui():
    root = tk.Tk()
    root.title("Llama 7B Quantized")

    style = ThemedStyle(root)
    style.set_theme("equilux")  
    
    root.geometry("600x500")

    root.configure(bg="#323232")

    frame = ttk.Frame(root, padding=10, relief=tk.RAISED)
    frame.pack(padx=20, pady=20)

    label = ttk.Label(frame, text="Ask Llama 7B Quantized", font=("Helvetica", 14))
    label.pack(pady=10)

    global entry_var
    entry_var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=entry_var, font=("Helvetica", 12), width=30)
    entry.pack(pady=5)

    global submit_button
    submit_button = ttk.Button(frame, text="Submit", command=get_answer, style="flat.TButton")
    submit_button.pack(pady=10)

    global loading_label
    loading_label = ttk.Label(frame, text="Generating answer...", font=("Helvetica", 12),
                              foreground="white")  
    

    paned_window = ttk.PanedWindow(root, orient=tk.VERTICAL)
    paned_window.pack(fill=tk.BOTH, expand=True)

    question_frame = ttk.Frame(paned_window, relief=tk.RAISED)
    paned_window.add(question_frame)

    answer_frame = ttk.Frame(paned_window, relief=tk.RAISED)
    paned_window.add(answer_frame)

    answer_label_frame = ttk.LabelFrame(answer_frame, text="Answer", padding=10)
    answer_label_frame.pack(fill=tk.BOTH, expand=True)

    global answer_text
    answer_text = ScrolledText(answer_label_frame, wrap=tk.WORD, bg="#323232", fg="white")
    answer_text.pack(fill=tk.BOTH, expand=True)

    answer_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    answer_text.tag_configure("answer", font=answer_font, foreground="white") 

    root.mainloop()


if __name__ == "__main__":
    path = r"C:\Users\gj979\Document_Assistance\models\llama-7b.ggmlv3.q4_0.bin"
    create_gui()
