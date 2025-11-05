import streamlit as st
from parser_engine import parse_code, tree_to_graphviz, get_lmd_steps, get_rmd_steps

st.title("Interactive Parser for Programming Languages")

code_input = st.text_area("Enter code snippet to parse:", height=150)

if st.button("Parse"):
    result = parse_code(code_input, mode='both')
    if isinstance(result, str):
        st.error(f"Parsing error: {result}")
    else:
        st.success("Parsing Successful! Parse trees visualized below.")
        
        # Display LMD Parse Tree
        st.subheader("Left-Most Derivation (LMD) Parse Tree")
        dot_lmd = tree_to_graphviz(result['lmd'])
        st.graphviz_chart(dot_lmd.source)

        # Show LMD steps in a nicer format
        st.markdown("**LMD Derivation Steps:**")
        lmd_steps = get_lmd_steps(result['lmd'])
        for i, step in enumerate(lmd_steps):
            st.code(f"Step {i+1}: {step}")
        
        st.markdown("---")  # Separator
        
        # Display RMD Parse Tree
        st.subheader("Right-Most Derivation (RMD) Parse Tree")
        dot_rmd = tree_to_graphviz(result['rmd'])
        st.graphviz_chart(dot_rmd.source)

        # Show RMD steps in a nicer format
        st.markdown("**RMD Derivation Steps:**")
        rmd_steps = get_rmd_steps(result['rmd'])
        for i, step in enumerate(rmd_steps):
            st.code(f"Step {i+1}: {step}")

# Helper function to generate derivation steps
def get_lmd_steps(tree):
    steps = []
    expr = str(tree)
    current = "start"
    tokens = expr.split()
    for i in range(len(tokens)):
        current += f" ⟹ {' '.join(tokens[:i+1])}"
        steps.append(current)
    return steps

def get_rmd_steps(tree):
    steps = []
    expr = str(tree)
    current = "start"
    tokens = expr.split()
    for i in range(len(tokens)-1, -1, -1):
        current += f" ⟹ {' '.join(tokens[i:])}"
        steps.append(current)
    return steps
