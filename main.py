import pyperclip
import pyautogui
import time
import webbrowser

# URL of the ChatGPT website
url = "https://www.chatgpt.com/"

# Open the ChatGPT website in a web browser
webbrowser.open(url)

# Wait for the website to load
time.sleep(5)

# Click on the input field to bring up the cursor
pyautogui.click(x=640, y=564)

# Copy text from the clipboard
text_to_ask = pyperclip.paste()

# Type the text into the input field
pyautogui.typewrite(text_to_ask)

# Click on the submit button
pyautogui.click(x=906, y=564)

# Wait for the answer to be generated
time.sleep(10)

# Click on the output field to select the answer
pyautogui.click(x=640, y=704)

# Copy the answer to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Get the answer from the clipboard
answer = pyperclip.paste()

# Print the answer
print("Answer: ", answer)
