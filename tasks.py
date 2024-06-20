from crewai import Task


class Tasks:
    def task_code_review(self, agent, code):
        return Task(
            description=f"""
            Revise o código para implantação de produção, fornecendo feedback detalhado
            nas mudanças necessárias, com foco na sintaxe e no estilo. Identificando possíveis bugs.
            Garanta recuo consistente, uso adequado de espaços, linhas apropriadas
            comprimentos, convenções de nomenclatura significativas. Identifique possíveis problemas, como
            desreferências de ponteiro nulo, erros off-by-one, tratamento adequado de exceções,
            e gerenciamento correto de recursos.
            
            Código: \n{code}
            """,
            agent=agent,
            expected_output="""Sua resposta final deve ser uma revisão detalhada do código fornecido. Mostrando
            trechos de código e o que deve ser alterado. Pode usar marcadores ou outros
            métodos de organizar as mudanças."""
        )

    def task_documentation(self, agent, code):
        return Task(
            description=f"""
            Escreva uma visão geral do código com algumas palavras em um ou dois parágrafos. 
            
            Código: \n{code}
            """,
            agent=agent,
            expected_output="Sua resposta final deve ser uma pequena documentação do código fornecido."
        )
