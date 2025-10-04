# QWEN Analysis: ambiyansyah-risyal.github.io

## Project Overview
This is a GitHub Pages repository for `ambiyansyah-risyal.github.io`, which serves as the personal GitHub Pages website for the user `ambiyansyah-risyal`. GitHub Pages allows users to host static websites directly from their GitHub repositories. When a repository is named in the format `username.github.io`, it automatically serves content at `https://username.github.io`.

The project uses Hugo as a static site generator and follows a workflow where AI-generated content is drafted and then reviewed by a human before publication. According to the constitution file, the site serves as both a portfolio and blog with weekly AI-generated draft posts that are edited to appear human-created.

## Repository Structure
- `README.md`: Basic repository description
- `.specify/memory/constitution.md`: Project constitution with principles and guidelines
- `docs/`: Documentation directory (currently empty)
- `scripts/`: Contains scripts including git hooks
- `.qwen/commands/`: Qwen-specific command configurations
- `QWEN.md`: This file with project analysis

## Technology Stack
- **Static Site Generator**: Hugo
- **Hosting**: GitHub Pages
- **Programming Language**: Python (for scripts)
- **AI Integration**: OpenAI API for content generation

## Project Constitution & Guidelines
Based on `.specify/memory/constitution.md`, the project follows these core principles:

### Core Principles
- **Clarity First**: Simple, fast, and readable
- **Human-in-Loop**: AI drafts, human edits
- **Enhanced Transparency**: AI use is disclosed during draft creation but content must appear human-generated when published
- **Automation**: Build, lint, deploy, and generate drafts via GitHub Actions
- **Privacy-Safe**: No trackers or data leaks
- **Versioned Truth**: All changes via PRs to main branch

### Development Guidelines
- **Stack**: Hugo + GitHub Pages + Python + OpenAI API
- **Structure**:
  - `/content/posts/` → articles & drafts
  - `/scripts/` → AI draft generator
  - `/config/` → interests.yml
  - `/.github/workflows/` → CI/CD

### Workflow
1. Weekly Action runs → creates AI draft (`draft: true`, `noindex`)
2. PR opened → human reviews/edits and applies authenticity techniques
3. Merge to publish → auto-deploy

### Content Authenticity Guidelines
- AI-generated content must be undetectable by AI detection tools
- Human editing includes techniques to make content appear naturally created
- Use of varied sentence structures, personal anecdotes, and human-like imperfections
- Verification that content passes AI detection tools before final publication

## Directory Structure and Components
- **Content**: `/content/posts/` directory (not yet created) will contain articles and drafts
- **Scripts**: `/scripts/` contains automation scripts, including git hooks
- **Configuration**: `/config/` (directory not yet created) will contain configuration like interests.yml
- **CI/CD**: `/.github/workflows/` (not yet created) will contain GitHub Action workflows
- **Documentation**: `/docs/` directory exists but is currently empty

## GitHub Pages Configuration
GitHub Pages sites in repositories following the `username.github.io` naming convention are automatically published from the default branch (typically `main` or `master`). The site will be accessible at:
- https://ambiyansyah-risyal.github.io

## Building and Running
For Hugo-based GitHub Pages sites:
1. **Local Development**: Install Hugo and build/test your site locally:
   ```bash
   # Install Hugo (check https://gohugo.io/getting-started/installing/ for your OS)
   # For example on Ubuntu/Debian:
   sudo apt-get install hugo
   
   # Or using snap:
   sudo snap install hugo
   
   # Navigate to your repository and start the Hugo server
   cd /home/risyal/project/github.com/ambiyansyah-risyal/ambiyansyah-risyal.github.io
   hugo server
   ```
   This will start a local server, typically accessible at `http://localhost:1313`

2. **Build the Site**: Generate the static files:
   ```bash
   hugo
   ```
   This will create a `public/` directory with all the static files

3. **Publishing**: After building with Hugo, commit and push the generated files to the `main` branch to update the live site automatically.

## Current Status
The site is currently minimal with only basic configuration files and documentation. The main components (content, config, workflows) still need to be added according to the project constitution. The Hugo site needs to be initialized and configured with a theme.

## Development Conventions
Since this is a Hugo-based GitHub Pages site with AI content generation:
- Create content as markdown files in the `content/posts/` directory
- Follow Hugo conventions for layouts, templates, and partials
- Use Hugo's data files feature for configuration data
- Leverage Hugo's built-in shortcode functionality for reusable components
- Follow the content authenticity guidelines for AI-generated content
- Use semantic versioning if tracking the source of the site
- Store API keys in GitHub Secrets
- No secrets or trackers in the repository
- All changes must go through PRs for review