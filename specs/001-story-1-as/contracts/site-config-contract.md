# Site Configuration Contract

## Overview
This contract defines the expected structure and configuration of the Hugo-based personal website.

## Configuration Contract

### Site Configuration (config/_default/config.toml)
```
baseURL = "https://ambiyansyah-risyal.github.io/"
languageCode = "en-us"
title = "Risyal Ambiyansyah - Personal Website"
author = "Risyal Ambiyansyah"
copyright = "Risyal Ambiyansyah"
paginate = 5

# Enable RSS
[outputs]
home = ["HTML", "RSS"]

[params]
# Site parameters for the theme
description = "Personal website of Risyal Ambiyansyah - Portfolio and Blog"
# Enable WCAG AA compliance features
# Configure social media links
# Set up analytics (if needed, though we're privacy-focused)
```

### Content Structure Contract
The site will support these content types in the `content/` directory:

#### Blog Posts (content/posts/)
- Path: `/posts/<slug>/`
- Front Matter:
  - title: string (required)
  - date: datetime (required) 
  - description: string (optional)
  - draft: boolean (default: false)
  - tags: array<string> (optional)
  - categories: array<string> (optional)

#### Portfolio Items (content/portfolio/)
- Path: `/portfolio/<slug>/`
- Front Matter:
  - title: string (required)
  - date: datetime (required)
  - description: string (required)
  - draft: boolean (default: false)
  - tags: array<string> (optional)
  - url: string (optional)
  - images: array<string> (optional)

## Accessibility Contract
The site must meet WCAG AA compliance standards:
- Proper heading hierarchy (H1, H2, H3, etc.)
- Alt text for all images
- Sufficient color contrast
- Semantic HTML elements
- Keyboard navigation support
- ARIA attributes where appropriate

## Performance Contract
- Page load time < 3 seconds on 3G connection
- Total page weight < 1MB
- Proper image optimization
- Minimal JavaScript usage
- Proper caching headers

## Mobile Responsiveness Contract
- Works flawlessly on screen sizes from 320px to 1200px
- Touch-friendly navigation
- Readable text without zooming
- Properly sized interactive elements