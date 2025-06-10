from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopment():
    """LatestAiDevelopment crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def product_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['product_researcher'],
            verbose=True
        )

    @agent
    def recommendation_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_analyst'],
            verbose=True
        )
    
    
    

    @task
    def product_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_research_task'],
            agent=self.product_researcher(),
            output_file='research.md'
        )

    @task
    def product_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_recommendation_task'],
            agent=self.recommendation_analyst(),
            output_file='recommendation.md'
        )
    
    
    

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )