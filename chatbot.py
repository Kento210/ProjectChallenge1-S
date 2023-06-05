import openai
import tkinter as tk

# API Keyは環境変数よりロードするのがベストだが効率を重視し平文でロードする
openai.api_key = "" #API Key 
openai.organization = '' #Organization ID

def send_text():
    input_text = input_box.get("1.0", "end-1c")

    #推論実行
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは優秀な相談相手です。"},
        {"role": "user", "content": "あなたの名前は何ですか？"},
        {"role": "assistant", "content": "私の名前はメイです。"},
        {"role": "user", "content": input_text},
    ]
    )
    output_text = response["choices"][0]["message"]["content"]

    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", output_text)
    output_box.config(state="disabled")

window = tk.Tk()
window.title("ChatGPT相談アプリ")
input_box = tk.Text(window, height=5, width=50)
input_box.pack()
send_button = tk.Button(window, text="Send", command=send_text)
send_button.pack()

output_box = tk.Text(window, height=5, width=50)
output_box.config(state="disabled")
output_box.pack()

window.mainloop()