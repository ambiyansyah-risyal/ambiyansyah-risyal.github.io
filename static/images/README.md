# Image Optimization Guidelines

This directory contains optimized images for the website.

## Optimization Standards
- Format: JPEG for photos, PNG for graphics with few colors, SVG for vector graphics
- Maximum width: 1920px for full-width images
- Maximum file size: 200KB for photos, 100KB for other images
- Use WebP format as alternative when possible

## Naming Convention
- Use descriptive names with hyphens: `project-screenshot.jpg`
- Include dimensions when relevant: `avatar-200x200.jpg`

## Tools for Optimization
- ImageMagick: `convert input.jpg -resize 800x600 -quality 85% output.jpg`
- Online tools: https://squoosh.app/, https://tinypng.com/
- For bulk optimization: `find . -name "*.jpg" -exec jpegoptim {} \;`