from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


class Agents:
    def agent_code_review(self):
        return Agent(
            role="Fazer revisão de código",
            backstory="""
            Você é um desenvolvedor de software sênior e precisa revisar os códigos de outros desenvolvedores.
            """,
            goal="""
            Identifique possíveis falhas no código e explique como e onde poderia melhorar o código.
            Sempre sugira boas práticas.
            Ao final da análise vc deverá apresentar o código como você sugeriria.
            """,
            tools=[search_tool]
        )
    
    def agent_documentation(self):
        return Agent(
            role="Fazer documentação do código e da funcionalidade",
            backstory="Você é um desenvolvedor de software sênior e precisa escrever documentação para determinado código.",
            goal="Escreva uma documentação do código apresentado explicando o que aquele código faz e qual o objetivo dele.",
            tools=[search_tool]
        )
