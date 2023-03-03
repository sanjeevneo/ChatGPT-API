import os
import openai

def get_api_key(file_name):
    with open(file_name, 'r') as file:
        api_key = file.read().strip()
    return api_key

def run_chatbot(model):
    messages = []

    print("Say hello to your new chatbot! Type quit() when done.")

    while True:
        user_message = input("YOU: ")
        if user_message == "quit()":
            break

        messages.append({"role": "user", "content": user_message})
        try:
            response = openai.Completion.create(model=model, prompt=user_message)
        except openai.error.RateLimitError as e:
            print("Error: " + str(e))
            break
        reply = response["choices"][0]["text"]
        messages.append({"role": "assistant", "content": reply})
        print("\nAI: " + reply + "\n")

def main():
    api_key = get_api_key('openaiapikey.txt')
    openai.api_key = api_key
    model = "gpt-3.5-turbo"
    system_message = input("What type of chatbot would you like to create?\n")
    if "small" in system_message.lower():
        model = "text-davinci-002"
    run_chatbot(model)

if __name__ == "__main__":
    main()
