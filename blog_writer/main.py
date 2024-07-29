#!/usr/bin/python

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI   # For using OpenAI models
# from langchain.llms import Ollama  # For using locally-hosted Ollama inference
from langchain_community.llms import Ollama # For using locally-hosted Ollama inference

from langchain_community.tools import DuckDuckGoSearchRun


# Initialize variables from `.env`
load_dotenv()

## Tools
# Initialize DDG
search_tool = DuckDuckGoSearchRun()

## LLMs

llama31 = Ollama(
    model = "llama3.1:8b",
    base_url = "http://192.168.0.235:11434"
    )

gemma2 =  Ollama(
    model = "gemma2:latest",
    base_url = "http://192.168.0.235:11434"
    )



## Agents

researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in Cybersecurity, with a focus on attack patterns and methods to defend against them.',
  backstory="""You formerly led a highly-performing cybersecurity team. 
  You now work at a leading tech think tank focused on cyber threats to corporations and national interests..
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=llama31
#  llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on activity in the cybersecurity threat landscape.',
  backstory="""You are a renowned Content Strategist, widely lauded for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True,
  llm=gemma2
#  llm=ChatOpenAI(model_name="gpt-4o", temperature=0.85, top_p=1, stream=True, max_iter=8)
)

## Tasks
# Task definitions
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in Cybersecurity in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.
  Deeply research this topic, reviewing the content from many results, not just the first
  """,
  expected_output="Full analysis report in bullet points",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights the cybersecurity developments that should be of most concern to company leadership and lawmakers.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid restatingt he problem at the beginning of each paragraph so it doesn't sound like AI.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer
)


# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  process=Process.sequential,
  verbose=2, # You can set it to 1 or 2 to different logging levels
)


# Get your crew to work!
result = crew.kickoff()