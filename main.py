# Import necessary modules and classes
from unittest import result
from langchain_ollama.llms import OllamaLLM # type: ignore
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Initialise the Ollama LLM model
model = OllamaLLM(model="llama3.2")

# Define the prompt template for the fitness expert AI
template = """
You are a fitness expert and your goal is to help users achieve their fitness objectives. You have access to a wealth of knowledge about exercise science. Use this knowledge to provide personalized advice and support to users seeking to improve their fitness.

Here is the user's workout data from the Hevy app: {workouts}

Here is the question from the user: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Main loop for user interaction
while True:
    print("\n-----------------------------------------------------")
    print("Welcome to the Fitness Expert AI!")
    print("-----------------------------------------------------")
    print("Your Hevy app data is being used to provide personalised fitness advice.\n")
    print("You can ask questions about your workouts, exercise techniques, or general fitness advice.\n")
    question = input("Enter your question (or 'q' to quit): ")
    if question.lower() == 'q':
        break

    # Retrieve relevant workout data based on the user's question
    workouts = retriever.invoke(question)
    # Invoke the LLM chain with the workout data and user's question
    result = chain.invoke({"workouts": workouts, "question": question})
    # Display the result to the user
    print(result)