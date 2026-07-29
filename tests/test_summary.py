from Project.src.Agent.SummaryMemory import SummaryServiceClass


class FakeAgent:

    def Answer(self, prompt, memory):
        return "Ez egy teszt összefoglaló"


def test_create_summary():

    agent = FakeAgent()

    summary_service = SummaryServiceClass(agent)

    messages = [
        {
            "role": "user",
            "content": "Szia"
        },
        {
            "role": "assistant",
            "content": "Szia, miben segíthetek?"
        }
    ]

    result = summary_service.create_summary(messages)

    assert result == "Ez egy teszt összefoglaló"