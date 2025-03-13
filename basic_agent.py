from agents import Agent, Runner
from dotenv import load_dotenv
from agents import set_default_openai_key
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
set_default_openai_key(openai_api_key)


agent = Agent(
    name= "Assistant", 
    instructions="You're a badass code assistant that can do anything. You are a helpful assistant that can answer any question and write code for any task. You are a very good programmer and can write code in any programming language. You are very good at writing code and can write code for any task. You are very good at writing code and can write code for any task.",
    model="gpt-4o-mini",
)

result = Runner.run_sync(agent, input="Write a Python script to solve Leetcode 1508. Just output the code and nothing else.")

print(result.final_output)