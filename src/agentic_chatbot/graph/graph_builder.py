from langgraph.graph import StateGraph, START, END
from src.agentic_chatbot.state.state import State
from src.agentic_chatbot.node.agentic_chatbot_node import ChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def chatbot_build_graph(self):
        """
        Builds a chatbot graph using LangGraph.
        This method initializes a chatbot node using the `ChatbotNode` class
        and integrates it into the graph. The chatbot node is set as both the entry and exit point of the graph.
        
        """

        self.chatbot_node = ChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self):   
        self.chatbot_build_graph()
        return self.graph_builder.compile()
