import pyautogui
import pyperclip
import time
import requests

# Gemini API key
GEMINI_API_KEY = "AIzaSyA0a-fWg7NuRpZFoETwv79ih0Q7XostlMY"
API_URL = "https://api.gemini.com/v1/chat"  # Replace this with the actual API endpoint

def get_reply_from_gemini(copied_text):
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"  # Or as specified by the API
    }

    payload = {
        "message": copied_text
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json().get("reply")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return "I'm sorry, I couldn't generate a reply at this time."
    
# Step 1: Click on the icon at position (1052, 1043)
pyautogui.click(1052, 1043)

# Give a brief pause to ensure the click action is completed
time.sleep(0.5)

# Step 2: Drag from (853, 210) to (1876, 904) to select the text
pyautogui.moveTo(853, 210)
pyautogui.dragTo(1876, 904, duration=1.0)  # duration in seconds

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Give a brief pause to ensure the text is copied to clipboard
time.sleep(0.5)

# Step 4: Get the clipboard content and store it in a variable
copied_text = pyperclip.paste()

# Step 5: Click on the chatbox at position (961, 942)
pyautogui.click(961, 942)

# Give a brief pause to ensure the click action is completed
time.sleep(0.5)

# Step 6: Paste the clipboard content into the chatbox (Optional)
pyautogui.hotkey('ctrl', 'v')

# Give a brief pause to ensure the paste action is completed
time.sleep(0.5)

# Step 7: Generate a new reply message using the Gemini API
new_reply_message = get_reply_from_gemini(copied_text)

# Copy the new reply message to the clipboard
pyperclip.copy(new_reply_message)

# Step 8: Paste and send the new reply message to the chatbox
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

print("Script executed successfully.")
