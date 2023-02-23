import pyperclip
import pyautogui
import pytesseract
import time
import webbrowser

# URL of the ChatGPT website
url = "https://chat.openai.com/chat"

# Open the ChatGPT website in a web browser
webbrowser.open(url)

# Wait for the website to load
time.sleep(2)

# Copy text from the clipboard
text_to_ask = pyperclip.paste()

# Type the text into the input field
pyautogui.typewrite(text_to_ask)

# Press enter to submit the question
pyautogui.press("enter")

#Logic to detect the answer

# wait for the chatgpt window to load
time.sleep(5)
print("Waited to print")

#function to interact with chatgpt
def get_chatgpt_answer():
    while arrow is not True:
        arrow = pyautogui.locateOnScreen('arrow_symbol.png')
    if arrow is None:
        raise ValueError('Answer not generated')
    
    logo = None
    while logo is None:
        logo = pyautogui.locateOnScreen('chatgpt_logo.png', region=(arrow.left, arrow.top, arrow.width, 500))
        if logo is None:
            pyautogui.scroll(-500)
            time.sleep(1)
    
    answer_region = (0, logo.top + 30, pyautogui.size().width, pyautogui.size().height - logo.top - 30)
    answer_screenshot = pyautogui.screenshot(region=answer_region)
    
    answer = pytesseract.image_to_string(answer_screenshot)
    
    return answer

print("Testing 123")

get_chatgpt_answer()
