from openai import OpenAI

OPENAI_API_KEY = ""

class wrapper:
    def __init__(self, model="gpt-4.1", temp=0.3):
        self.client = OpenAI()
        self.model = model
        self.temp = temp

    def __call__(self, prompt, system_msg=None):
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    def code_snippet(self, prompt):
        return self.call(f'output only python code. \n{prompt}')

    def structured(self, prompt):
        sys = 'you output STRICT JSON,. no extra text. no explanation, if unsure, output null values.'
        return self.call(prompt, system_msg=sys)
    

    
