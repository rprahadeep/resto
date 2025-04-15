from secret_key import gemini_api
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
os.environ["GOOGLE_API_KEY"] = gemini_api

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", temperature=0.7)


def generate_restaurantname_items(cuisine):
  #chain1
  prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a {cuisine} food restaurant, just give me a single name for my new restaurant"
  )

  name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "restaurant_name")

  #chain2
  prompt_template_menu_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "Just list me 10 menu items for my restaurant named {restaurant_name}. Return it as a comma seperated string"
  )

  food_items_chain = LLMChain(llm = llm, prompt = prompt_template_menu_items, output_key = "menu_items")

  chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items']
  )

  response = chain.invoke({'cuisine':cuisine})

  return response


if __name__ == "__main__":
  print(generate_restaurantname_items("Italian"))


