# ambiyansyah-risyal.github.io

Personal website and blog built with Hugo and deployed on GitHub Pages.

## Overview

This repository contains the source code for my personal website, featuring:
- Portfolio showcasing my projects
- Blog with technical articles and insights
- Responsive design optimized for all devices
- WCAG AA accessibility compliance

## Local Development

1. Install Hugo (extended version):
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install hugo

   # On macOS
   brew install hugo

   # On Windows with Chocolatey
   choco install hugo-extended
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/ambiyansyah-risyal/ambiyansyah-risyal.github.io.git
   cd ambiyansyah-risyal.github.io
   git submodule update --init --recursive
   ```

3. Run the development server:
   ```bash
   hugo server -D
   ```

4. Visit `http://localhost:1313` to view the site

## Project Structure

```
.
├── archetypes/       # Content templates
├── assets/           # Source files for processing
├── config/_default/  # Configuration files
├── content/          # Content files
│   ├── posts/        # Blog posts
│   └── portfolio/    # Portfolio items
├── data/             # Data files
├── layouts/          # HTML templates
├── static/           # Static assets (CSS, JS, images)
└── themes/           # Hugo themes
```

## Content Creation

To create a new blog post:
```bash
hugo new posts/my-new-post.md
```

To create a new portfolio item:
```bash
hugo new portfolio/my-project.md
```

## Contributing

For issues or suggestions, please open an issue in the repository.

## License

Content and code are available under the MIT License unless otherwise specified.