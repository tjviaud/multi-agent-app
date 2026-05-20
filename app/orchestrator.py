from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.coder import coder_agent
from agents.reviewer import reviewer_agent

def run_multi_agent_system(task):
    plan = planner_agent(task)
    research = research_agent(plan)
    code = coder_agent(task, research)
    review = reviewer_agent(code)

    return {
        "plan": plan,
        "research": research,
        "code": code,
        "review": review
    }