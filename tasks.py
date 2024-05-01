from datetime import datetime
from crewai import Task

class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top news stories on marketing, social media, AI, and tech from the past week. They should be relevant for entrepreneurs, founders, and brand managers. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""A list of top news story titles, URLs, and a brief summary for each story from the past week. Topics include marketing, social media, AI, and tech. 
                Example Output: 
                [
                    {'title': 'New AI tools revolutionize small business marketing', 
                     'url': 'https://example.com/story1', 
                     'summary': 'Emerging AI technologies are transforming how small businesses approach marketing...'
                    },
                    {'title': 'Top strategies for growing your business on social media in 2024', 
                     'url': 'https://example.com/story2', 
                     'summary': 'Experts share top tips for leveraging social media platforms to boost business growth...'
                    },
                    {...}
                ]
            """
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze news stories to curate at least 5 well-formatted articles on marketing, social media, AI, and tech. Your audience is founders, entrepreneurs, and brand managers.',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, 
                and a "Why it matters" section. Each summary should be followed by a clickable source URL in parentheses.
                Example Output: 
                '## [New AI tools revolutionize small business marketing](https://example.com/story1)\\n\\n
                **The Rundown:** Emerging AI technologies are transforming how small businesses approach marketing...\\n\\n
                **The details:**\\n\\n
                - AI-driven analytics tools offer insights into customer behaviors...\\n\\n
                **Why it matters:** These technologies allow small businesses to compete on a larger scale.\\n\\n
                [source](https://example.com/story1)'
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter, incorporating news on marketing, social media, AI, and tech',
            agent=agent,
            context=context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
                Example Output: 
                '# Today's top stories in marketing, social media, AI, and business growth:\\n\\n
                - [New AI tools revolutionize small business marketing](https://example.com/story1)\\n
                - [Top strategies for growing your business on social media in 2024](https://example.com/story2)\\n\\n

                ## [New AI tools revolutionize small business marketing](https://example.com/story1)\\n\\n
                **The Rundown:** Emerging AI technologies are transforming how small businesses approach marketing...\\n\\n
                **The details:**...\\n\\n
                **Why it matters:**...\\n\\n
                [source](https://example.com/story1)\\n\\n

                ## [Top strategies for growing your business on social media in 2024](https://example.com/story2)\\n\\n
                **The Rundown:** Experts share top tips for leveraging social media platforms to boost business growth...\\n\\n
                **The details:**...\\n\\n
                **Why it matters:**...\\n\\n
                [source](https://example.com/story2)\\n\\n
            """,
            callback=callback_function
        )
