import os
import praw
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Load environment variables
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
client_id = os.getenv("client_id")
client_secret = os.getenv("secret_key")
# Initialize chat model
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base="https://api.mistral.ai/v1",
    model_name="mistral-medium",
    temperature=0.7
)

output_parser = StrOutputParser()

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["username", "context"],
    template="""
You are an expert in psychological profiling. Based on the following Reddit posts and comments, generate a detailed user persona. CITE EACH INSIGHT USING ITS LINK (this is important). Don't ask anything

Include:
- Username = {username}
- Age group,
- Occupation,
- Interests or hobbies,
- Tone of writing,
- Subreddits they frequent,
- Personality traits,
- Rate them as Introvert vs extrovert personality,
- Any political or ideological leanings.

Reddit Activity:
{context}
"""
)


chain = prompt | llm | output_parser


def extract_username(url: str) -> str:
    return url.strip("/").split("/")[-1]


def scrape_reddit(username, post_limit=30, comment_limit=30):
    reddit = praw.Reddit(
        client_id= client_id,
        client_secret= client_secret,
        user_agent="RedditPersonaScript"
    )

    user = reddit.redditor(username)
    posts = []
    comments = []

    for i, submission in enumerate(user.submissions.new(limit=post_limit)):
        posts.append(f"[Post {i+1}] Title: {submission.title}\n{submission.selftext}\n")

    for i, comment in enumerate(user.comments.new(limit=comment_limit)):
        comments.append(f"[Comment {i+1}] {comment.body}\n")

    return "\n".join(posts + comments)


def generate_persona(profile_url: str):
    username = extract_username(profile_url)
    reddit_data = scrape_reddit(username)

    result = chain.invoke({
        "username": username,
        "context": reddit_data
    })
    return result


