# Development Documentation

This document provides guidelines and information for developing and maintaining the Hugo-based personal website.

## Technologies Used

- **Hugo**: Static site generator (version 0.150.1 or later)
- **Ananke Theme**: Minimalist theme focused on content
- **GitHub Pages**: Hosting platform
- **GitHub Actions**: CI/CD pipeline

## Project Structure

The site follows Hugo's standard directory structure:

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

## Development Workflow

1. **Content Creation**:
   - Create new posts: `hugo new posts/post-title.md`
   - Create new portfolio items: `hugo new portfolio/project-title.md`
   - Use appropriate front matter as defined in archetypes

2. **Local Development**:
   - Start server: `hugo server -D`
   - View at: `http://localhost:1313`
   - The `-D` flag includes draft content

3. **Building for Production**:
   - Run: `hugo --minify`
   - Output is placed in the `public/` directory

## Content Guidelines

### Front Matter Standards

All content files should include appropriate front matter:

For blog posts:
```yaml
---
title: "Post Title"
date: YYYY-MM-DDTHH:MM:SSZ
description: "Brief description"
draft: true  # Set to false when ready to publish
tags: ["tag1", "tag2"]
categories: ["Category"]
---
```

For portfolio items:
```yaml
---
title: "Project Title"
date: YYYY-MM-DDTHH:MM:SSZ
description: "Project description"
draft: true  # Set to false when ready to publish
tags: ["tag1", "tag2"]
url: "https://project-url.com"
images: ["/images/image1.jpg", "/images/image2.jpg"]
---
```

## Theme Customization

The site uses the Ananke theme with customizations in the `layouts/` directory. To customize:

1. Override specific templates by creating files with the same path in `layouts/`
2. Add custom CSS in `static/css/custom.css`
3. Add custom JavaScript in `static/js/`

## Accessibility Standards

The site follows WCAG 2.1 AA standards:

- Semantic HTML structure
- Proper heading hierarchy
- Alt text for images
- Color contrast ratios
- Keyboard navigation support
- ARIA attributes where appropriate

## Performance Optimization

- Images are optimized and compressed
- CSS and JavaScript are minified
- External resources are limited
- Efficient template structures

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions:
- Workflow file: `.github/workflows/deploy.yml`
- Trigger: Push to main branch
- Output: Built site in `gh-pages` branch