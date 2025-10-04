#!/bin/bash

# Script to install git hooks
# This script copies our custom hooks to the .git/hooks directory

HOOKS_DIR=".git/hooks"
SCRIPTS_HOOKS_DIR="scripts/hooks"

# Create the hooks directory if it doesn't exist
mkdir -p "$HOOKS_DIR"

# Install the commit-msg hook (which validates commit messages)
# Git uses the commit-msg hook to validate commit messages
echo "Installing commit-msg validator hook..."
cp "$SCRIPTS_HOOKS_DIR/commit-msg-validator.sh" "$HOOKS_DIR/commit-msg"

# Make the hook executable
chmod +x "$HOOKS_DIR/commit-msg"

echo "Git hook installed successfully!"
echo "The commit-msg hook will now validate that:"
echo "1. Commit messages are in a single line"
echo "2. Commit messages don't contain AI tool keywords"