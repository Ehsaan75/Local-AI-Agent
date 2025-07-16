from unittest import result
from langchain_ollama.llms import OllamaLLM # type: ignore
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are a fitness expert and your goal is to help users achieve their fitness objectives. You have access to a wealth of knowledge about exercise science. Use this knowledge to provide personalized advice and support to users seeking to improve their fitness.

Here is the user's workout data from the Hevy app: {workouts}

Here is the question from the user: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-----------------------------------------------------")
    print("Welcome to the Fitness Expert AI!")
    print("\n\n")
    question = input("Enter your question (or 'q' to quit): ")
    if question.lower() == 'q':
        break

    workouts = retriever.invoke(question)
    result = chain.invoke({"workouts": workouts, "question": question})
    print(result)