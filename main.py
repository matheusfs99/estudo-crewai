import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config
from agents import Agents
from tasks import Tasks


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")


class MyCrew:
    def __init__(self, code):
        self.code = code

    def run(self):
        agents = Agents()
        tasks = Tasks()

        agent_code_review = agents.agent_code_review()
        agent_documentation = agents.agent_documentation()

        task_code_review = tasks.task_code_review(agent_code_review, self.code)
        task_documentation = tasks.task_documentation(agent_documentation, self.code)

        crew = Crew(
            agents=[agent_code_review, agent_documentation],
            tasks=[task_code_review, task_documentation],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# Esta é a principal função que você usará para executar sua crew personalizada.
if __name__ == "__main__":
    print("## Bem-vindo ao Code Review")
    print("-------------------------------")
    code = """
    main.py
    def jokenpo(jogada):
        if jogada == "pedra":
            return "papel"
        elif jogada == "papel":
            return "tesoura"
        elif jogada == "tesoura":
            return "pedra"
    """

    custom_crew = MyCrew(code)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Aqui está seu resultado da revisão do sei código:")
    print("########################\n")
    print(result)
