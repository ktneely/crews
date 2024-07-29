import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun# Initialize the tool


search_tool = DuckDuckGoSearchRun()



researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)




# Hey guys, what about this?

framework: crewai
topic: Research the company Knostic and identify a way to get hired as their head
  of cybersecurity.
roles:
  company_researcher:
    backstory: Experienced in corporate research, adept at extracting relevant information
      from multiple resources.
    goal: Gather detailed information about Knostic
    role: Company Researcher
    tasks:
      information_gathering:
        description: Utilize online search tools and website scraping to collect comprehensive
          information about Knostic, including its history, mission, key personnel,
          and current cybersecurity practices.
        expected_output: Detailed report containing Knostic’s history, mission, key
          personnel, and current cybersecurity practices.
    tools:
    - ''
  cybersecurity_specialist:
    backstory: Professional with a strong background in cybersecurity, focusing on
      identifying vulnerabilities and suggesting improvements.
    goal: Analyze Knostic's current cybersecurity practices and identify potential
      areas of improvement or enhancement
    role: Cybersecurity Specialist
    tasks:
      cybersecurity_analysis:
        description: Review the detailed report on Knostic and analyze their cybersecurity
          practices to identify potential gaps or areas for improvement.
        expected_output: Analytical report highlighting current cybersecurity practices
          at Knostic and potential areas for enhancement.
    tools:
    - ''
  strategy_developer:
    backstory: Expert in career strategy development, skilled in aligning personal
      capabilities with organizational needs.
    goal: Develop a targeted strategy to secure a role as the head of cybersecurity
      at Knostic
    role: Strategy Developer
    tasks:
      hiring_strategy:
        description: Using the cybersecurity analysis report, create a compelling
          strategy document that outlines how to leverage identified cybersecurity
          gaps and enhancements to secure the head of cybersecurity position at Knostic.
        expected_output: Strategic document detailing the plan to approach Knostic
          for the head of cybersecurity role, emphasizing identified opportunities
          for cybersecurity improvements.
    tools:
    - ''
dependencies: []
