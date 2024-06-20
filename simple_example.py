from crewai import Agent, Task, Crew

agent = Agent(
  role='Buscar destinos',
  goal='Encontre as melhores opções de destinos',
  backstory="""Você é um viajante e deseja ir para um país com praia.
  Você precisa encontrar as 5 melhores opções de países na américa latina que possuam excelentes praias e que tenha um clima bom para o verão.
  Você deseja economizar na viagem como um todo, então precisa buscar por lugares que sejam mais baratos, porém que seja um bom lugar para passar as férias.
  Você reside em Recife-PE no Brasil e tem preferência por viajar para outro país.""",
)

task = Task(
    description="Encontre as melhores opções de destinos",
    agent=agent,
    expected_output="Uma lista com 5 opções de destinos"
)

crew = Crew(
    tasks=[task],
    agents=[agent]
)

print("Minha crew: ", crew.kickoff())