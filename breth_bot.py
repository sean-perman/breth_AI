import os
import openai

class BrethBot:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.Client()

    def get_llm_response(self,prompt: str) -> str:
        """
        this funchion prompts chat GPT-3.5, and returns the responce  
        """

        response = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role' : 'user', 'content' : prompt}],
            temperature= 0 # temperature is the randomness of your result 
        )
        return response.choices[0].message.content
    

# Example usage
if __name__ == "__main__":
    bot = BrethBot()
    prompt = """
        you are a meditashion AI.
        outputs instructions for a gided meditashion.
        include the different parts of the meditation and the time duration. 

    """
    response = bot.get_llm_response(prompt)
    print(response)