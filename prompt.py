import openai


PROMPT = """Your task as an exceptional writer is to convert a recorded transcript into a well-organized material suitable for future study. To achieve this, it is crucial that you utilize the MARKDOWN language, as the final output will be compiled in markdown format. Another crucial aspect is to create a new section whenever there is a slight jump in topic, as this will make the material look more sectioned and easier to read. Additionally, if necessary, you may include relevant images by providing detailed descriptions. It is important to maintain a clear and concise writing style, ensuring that the material is easily comprehensible for students. Your focus should be on creating a structured document that students can easily navigate and understand."""

class Prompt():
    def __init__(self, prompt: str, refine: bool= False):
        if prompt is None:
            self._prompt = PROMPT
        else:
            self._prompt = prompt
        if refine:
            self._prompt = self._refine()
            
    def _refine(self):
        refining_prompt = """refine the prompt for a for better language model generation"""
        new_prompt = self._generate(self._prompt, refining_prompt)
        return new_prompt
        
    def _generate(self, base_prompt: str, refining_prompt: str):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": f"{refining_prompt}"},
                {"role": "user", "content": f'{base_prompt}'}
            ]
        )
        return response.choices[0]['message']['content']
            
    @property
    def prompt(self):
        return self._prompt