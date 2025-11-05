# Interactive Programming Language Parser

This project implements an interactive parser that demonstrates both Left-Most Derivation (LMD) and Right-Most Derivation (RMD) approaches for parsing programming language expressions.

## Features

- Interactive web interface using Streamlit
- Support for basic arithmetic expressions
- Visual parse tree generation
- Both LMD and RMD parsing approaches
- Step-by-step derivation visualization

## Tech Stack

- Python 3.x
- Streamlit (Web Interface)
- Lark Parser (Grammar Processing)
- Graphviz (Tree Visualization)

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── parser_engine.py    # Parser implementation
├── grammar.lark        # Grammar definition file
└── requirements.txt    # Project dependencies
```

## Setup and Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd parse-tree
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Enter a code snippet in the text area (e.g., `a + b * (c + 2)`)
2. Click the "Parse" button
3. View both LMD and RMD parse trees and their derivation steps

## Grammar Support

Currently supports:
- Basic arithmetic operations (+, *)
- Parentheses for grouping
- Variables and numbers
- Proper operator precedence

## Contributing

Feel free to open issues or submit pull requests for improvements.
