from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from logger import CustomLogger  # Import CustomLogger
from prompts.qna_prompts import qna_prompy_template


class QnAModule:
    """
    Handles Q&A functionality.
    """

    def __init__(self, api_key):
        """
        Initialize the QnA module.
        """
        # Initialize logger
        self.logger = CustomLogger().get_logger()
        self.logger.info("Initializing QnAModule.")

        # Initialize Groq LLM
        self.llm = ChatGroq(
            api_key=api_key,
            model="llama3-8b-8192",
            temperature=0.6,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        self.logger.info("Groq LLM initialized for QnA module.")

        # Custom Prompt
        self.prompt = qna_prompy_template
        self.logger.info("Custom prompt initialized for QnA module.")

        # Initialize memory
        self.memory = ConversationBufferMemory(memory_key="history", input_key="question")
        self.logger.info("Conversation memory initialized for QnA module.")

        # Create chain with memory
        self.qa_chain = LLMChain(llm=self.llm, prompt=self.prompt, memory=self.memory)
        self.logger.info("LLMChain created with memory for QnA module.")

    def handle_qna(self, user_input):
        """
        Handles user queries for Q&A functionality.
        """
        self.logger.info(f"Received user query: {user_input}")
        try:
            response = self.qa_chain.run(user_input)
            self.logger.info(f"Response generated: {response}")
            return response
        except Exception as e:
            self.logger.error(f"An error occurred while processing the question: {e}")
            return f"An error occurred while processing your question: {e}"
