from langgraph.graph import Graph,END
import os 
from nodes import inference_node, confidence_check, fallback_node
def build_workflow(model, tokenizer):
    builder = Graph()
    
    # Add nodes with custom parameters
    builder.add_node("inference", lambda state: inference_node.inference_node(state, model, tokenizer))
    builder.add_node("confidence_check", confidence_check.confidence_check_node)
    builder.add_node("fallback", fallback_node.fallback_node)
    
    # Set entry point
    builder.set_entry_point("inference")
    
    # Define edges
    builder.add_edge("inference", "confidence_check")
    
    # Conditional edge
    def route_after_confidence(state):
        if state.get("needs_fallback", False):
            return "fallback"
        return "end"
    
    builder.add_conditional_edges(
        "confidence_check",
        route_after_confidence,
        {"fallback": "fallback", "end": END}
    )
    
    builder.add_edge("fallback", END)
    
    return builder.compile()

