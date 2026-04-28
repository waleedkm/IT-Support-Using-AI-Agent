from agents.support_agent import handle_support
from agents.rag_agent import retrieve_answer

def orchestrate(query):
    if "password" in query.lower():
        return handle_support(query)
    elif "how" in query.lower() or "what" in query.lower():
        return retrieve_answer(query)
    else:
        return "Escalating to human technician..."
