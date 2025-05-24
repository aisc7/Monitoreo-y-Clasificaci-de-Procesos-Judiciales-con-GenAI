import os
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
from app.config import Config

def generate_summary(content, max_length=4000):
    """
    Generate a summary of document content using LLM
    
    Args:
        content: Text content to summarize
        max_length: Maximum length for summary
    
    Returns:
        str: Generated summary
    """
    api_key = os.environ.get("AI_API_KEY")
    model = os.environ.get("AI_MODEL", "gpt-4")
    
    # Truncate content if it's too large
    if len(content) > 25000:  # Arbitrary limit to avoid token limits
        content = content[:25000] + "...[content truncated]"
    
    try:
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=api_key)
        
        # Generate summary using OpenAI
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert legal assistant tasked with summarizing judicial documents. Create a concise summary that captures the key legal points, arguments, decisions, and relevant details."},
                {"role": "user", "content": f"Please summarize the following judicial document:\n\n{content}"}
            ],
            max_tokens=1000,
            temperature=0.5
        )
        
        summary = response.choices[0].message.content.strip()
        return summary
        
    except Exception as e:
        # Fallback to a simple summary in case of API errors
        print(f"Error generating AI summary: {str(e)}")
        return f"Document contains approximately {len(content)} characters. AI summary generation failed."