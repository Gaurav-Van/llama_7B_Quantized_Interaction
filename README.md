# llama_7B_Quantized_Interaction

Basic GUI to interact with llama 7B Quantized LLM. Although way way better ones exist but why not + i was bored . Let's Go

<hr>

## What is the Quantization of AI Models?

LLM weights are floating point (decimal) numbers. Just like it requires more space to represent a large integer (e.g. 1000) compared to a small integer (e.g. 1), it requires more space to represent a high-precision floating point number (e.g. 0.0001) compared to a low-precision floating number (e.g. 0.1). The process of quantizing a large language model involves reducing the precision with which weights are represented in order to reduce the resources required to use the model. GGML supports a number of different quantization strategies (e.g. 4-bit, 5-bit, and 8-bit quantization), each of which offers different trade-offs between efficiency and performance.

Reference Video - https://www.youtube.com/watch?v=ZKdMbQq5T30

![image](https://github.com/Gaurav-Van/llama_7B_Quantized_Interaction/assets/50765800/ea2d2757-329a-415d-aefd-60fb89168cfd)


<hr>

## Folder Structure 

**Folder Name** - Document Assistance (or any other name of your choice but make sure to change the code accordingly)

    - Document Assistance 
    
        - models
            - "To store models"
            
        - Interact_llama_7B_Quantized.py

<hr>

## Requirements 

 - llama_cpp

         pip install llama-cpp-python
   
- Python https://www.python.org/downloads/

- To install tkinter, you don't need to explicitly install it because tkinter is included with Python by default.
  
- ttkthemes
  
         pip install ttkthemes

<hr>

### STEPS
 - Download the Quantized Model (the .bin file ) and place it in the model folder - https://huggingface.co/TheBloke/LLaMa-7B-GGML/tree/main
 - Then run the python file and you are good to go.

<hr>

I know it's a really small thing that I did and WAY BETTER ALTERNATIVES Exist but why not. I was bored so hehe (: 
