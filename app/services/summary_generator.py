import openai

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_text(self, model, prompt):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']