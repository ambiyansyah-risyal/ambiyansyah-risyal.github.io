# Quickstart Guide: Hugo Site Setup

## Prerequisites
- Hugo (v0.120.0 or latest stable)
- Git
- GitHub account

## Setup Process

1. **Install Hugo**
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install hugo
   
   # On macOS
   brew install hugo
   
   # On Windows with Chocolatey
   choco install hugo-extended
   ```

2. **Initialize the Hugo site**
   ```bash
   hugo new site ambiyansyah-risyal.github.io
   cd ambiyansyah-risyal.github.io
   ```

3. **Add a minimalist theme**
   ```bash
   # Initialize git repo to add themes as submodule
   git init
   git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
   
   # Add theme to config
   echo 'theme = "ananke"' >> config.toml
   ```

4. **Update config.toml with site details**
   ```toml
   baseURL = 'https://ambiyansyah-risyal.github.io/'
   languageCode = 'en-us'
   title = 'Risyal Ambiyansyah - Personal Website'
   author = 'Risyal Ambiyansyah'
   
   # Enable RSS
   [outputs]
   home = ["HTML", "RSS"]
   ```

5. **Create example content**
   ```bash
   # Create a new blog post
   hugo new posts/my-first-post.md
   
   # Create a portfolio item
   hugo new portfolio/my-project.md
   ```

6. **Start development server**
   ```bash
   hugo server -D
   ```

7. **Build for production**
   ```bash
   hugo
   ```

8. **Deploy to GitHub Pages**
   - Push the source code to the main branch of the repository
   - Configure GitHub Pages in repository settings to use the `/public` directory or the main branch
   - GitHub Actions will automatically build and deploy the site

## Validation Steps
1. Check that the site builds without errors: `hugo --minify`
2. Verify mobile responsiveness on different screen sizes
3. Run accessibility check using aXe or Lighthouse
4. Verify all links are working correctly