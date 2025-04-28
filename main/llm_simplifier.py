import ollama

def simplify_prescription(text):
    try:
        response = ollama.chat(
            model='mistral',  # you can use 'llama3', 'mistral', 'tinyllama' etc
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a medical prescription simplifier. Simplify the given prescription into easy-to-understand instructions for a patient.'
                },
                {
                    'role': 'user',
                    'content': text
                }
            ]
        )
        simplified_text = response['message']['content']
        return simplified_text
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't simplify the prescription."
