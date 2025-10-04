#!/bin/bash

# Git hook to validate commit messages
# Ensures commit message subject is in one line and doesn't contain AI tool keywords

COMMIT_MSG_FILE=$1
COMMIT_MESSAGE=$(cat "$COMMIT_MSG_FILE")

# Extract just the first line (the subject) for validation
COMMIT_SUBJECT=$(echo "$COMMIT_MESSAGE" | head -n 1)

# Check if commit subject is in one line (no newline characters except at the end)
if [[ "$COMMIT_SUBJECT" == *$'
'* ]]; then
    echo "❌ Error: Commit message subject must be in a single line."
    echo "Found multi-line subject:"
    echo "$COMMIT_SUBJECT"
    exit 1
fi

# List of AI tool keywords to avoid
AI_KEYWORDS=(
    "qwen"
    "codex" 
    "copilot"
    "chatgpt"
    "gpt"
    "claude"
    "bard"
    "ai"
    "artificial intelligence"
    "machine learning"
    "ml"
)

# Convert commit subject to lowercase for comparison
COMMIT_SUBJECT_LOWER=$(echo "$COMMIT_SUBJECT" | tr '[:upper:]' '[:lower:]')

# Check for AI keywords in the commit subject (case insensitive)
for keyword in "${AI_KEYWORDS[@]}"; do
    KEYWORD_LOWER=$(echo "$keyword" | tr '[:upper:]' '[:lower:]')
    if [[ "$COMMIT_SUBJECT_LOWER" =~ [^a-zA-Z0-9]${KEYWORD_LOWER}[^a-zA-Z0-9] ]] || [[ "$COMMIT_SUBJECT_LOWER" =~ ^${KEYWORD_LOWER}[^a-zA-Z0-9] ]] || [[ "$COMMIT_SUBJECT_LOWER" =~ [^a-zA-Z0-9]${KEYWORD_LOWER}$ ]] || [[ "$COMMIT_SUBJECT_LOWER" =~ ^${KEYWORD_LOWER}$ ]]; then
        echo "❌ Error: Commit message subject contains AI tool keyword: '$keyword'"
        echo "Commit subject: $COMMIT_SUBJECT"
        echo "Please rewrite your commit message without AI-related terms."
        exit 1
    fi
done

echo "✅ Commit message validation passed: $COMMIT_SUBJECT"
exit 0