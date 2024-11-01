# crews
Various crews for [CrewAI](https://crewai.com) LLM orchestration.
- each directory is a self-contained "crew"
- some of these are from the training material on deeplearning.ai, and some have been adapted from the official CrewAI examples.
- most have been developed in a python 3.12.x environment, but should work >=3.10 <=3.13


## Blog writer
Attempts to write a blog post based upon recent article titles on the web.

### Tools
- DuckDuckGo


## Trip Planner
Can plan a trip for a given destination and date range.


## CrewAI training
The following were built during the DeepLearning.ai training material.  The `requirements.txt` 
for these is in the event_planning folder, however, I upgraded CrewAI toa  much newer
version while working on these exercises.
- write_article
- customer_support
- customer_outreach
- event_planning

### Tools that are probably used in one or more of the specific crews
- Serper
- Browserless
- Calculator
