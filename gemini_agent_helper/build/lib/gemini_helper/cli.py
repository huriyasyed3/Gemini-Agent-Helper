# gemini_helper/cli.py
import click
from .core import get_gemini_model

@click.command()
@click.argument("prompt")
def main(prompt):
    """Gemini Agent se koi bhi input lo"""
    model = get_gemini_model()

    from agents import Agent, Runner
    agent = Agent(
        name="GeminiHelper",
        instructions="You are a helpful Gemini agent.",
        model=model
    )

    result = Runner.run_sync(agent, prompt)
    print("👉 Gemini says:\n", result.final_output)
