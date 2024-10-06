'''
librari
'''
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
'''
buttons of boks and main
'''
def main_button():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = KeyboardButton("Boks")
    btn2 = KeyboardButton("Kursh")
    btn3 = KeyboardButton("Shahmat ")
    markup.add(btn1, btn2,btn3)
    return markup

def boks_buttons(boks: str):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1, btn2, btn3, btn4 = None, None, None, None
    if boks == "Boks":
        btn1 = KeyboardButton("Hasanboy Do‘stmatov")
        btn2 = KeyboardButton("Bektimir Meliqo‘ziyev")
        btn3 = KeyboardButton("Shahobiddin Zoirov")
        btn4 = KeyboardButton("Rustam Saidov")
    back = KeyboardButton("Ortga")
    markup.add(btn1, btn2, btn3,btn4, back)
    return markup

def kursh_buttons(Kursh: str):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1, btn2, btn3, btn4 = None, None, None, None
    if Kursh == "Kursh":
        btn1 = KeyboardButton("O‘ktamjon Karomatov")
        btn2 = KeyboardButton("Jasurbek Qurbonov")
        btn3 = KeyboardButton("Komiljon Tog‘ayev")
        btn4 = KeyboardButton("Sherzod Tohirov")
    back = KeyboardButton("Ortga")
    markup.add(btn1, btn2, btn3,btn4, back)
    return markup

def shahmat_buttons(Shahmat: str):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1, btn2, btn3, btn4 = None, None, None, None
    if Shahmat == "Shahmat":
        btn1 = KeyboardButton("Nodirbek Abdusattorov")
        btn2 = KeyboardButton("Shamsiddin Vohidov")
        btn3 = KeyboardButton("Dinara Saduakasova")
        btn4 = KeyboardButton("Javohir Sindorov")
    back = KeyboardButton("Ortga")
    markup.add(btn1, btn2, btn3,btn4, back)
    return markup
