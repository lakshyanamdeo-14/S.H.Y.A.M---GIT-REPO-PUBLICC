import openai

openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the GPT version or choose another model
        prompt=prompt,
        max_tokens=100,              # Adjust the length of the response as needed
        n=1,                         # Specify the number of responses to generate
        stop=None,                   # Customize the stop conditions for GPT's response
        temperature=0.7              # Control the randomness of the response (lower value is more deterministic)
    )
    reply = response.choices[0].text.strip()
    return reply


while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)

