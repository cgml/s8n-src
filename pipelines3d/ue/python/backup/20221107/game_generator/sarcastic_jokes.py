import os
import openai

openai.api_key = "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"

class SarcasticResponsesGenerator:

  def request(self, question):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\n"
             "You: How many pounds are in a kilogram?\n"
             "Marv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\n"
             "You: What does HTML stand for?\n"
             "Marv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\n"
             "You: When did the first airplane fly?\n"
             "Marv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\n"
             "You: What is the meaning of life?\n"
             "Marv: I’m not sure. I’ll ask my friend Google.\n"
             f"You: {question}\n"
             "Marv:",
      temperature=1.0,
      max_tokens=60,
      top_p=0.3,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )
    result = response['choices'][0]['text']
    return result