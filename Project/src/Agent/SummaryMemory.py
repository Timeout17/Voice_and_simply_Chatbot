from Project.src.Agent.AI_Agent import AIAgentClass


class SummaryServiceClass:

    def __init__(self, agent):
        self.agent = agent


    def create_summary(self, messages):

        summary_prompt = """
        Készíts rövid összefoglalót a beszélgetésről.

        Tartsd meg:
        - fontos felhasználói információkat
        - korábbi kérdéseket
        - fontos döntéseket
        - kontextust a következő beszélgetéshez

        Ne írj választ a felhasználónak.
        Csak az összefoglalót add vissza.

        Beszélgetés:
        """

        return self.agent.Answer(
            summary_prompt,
            messages
        )