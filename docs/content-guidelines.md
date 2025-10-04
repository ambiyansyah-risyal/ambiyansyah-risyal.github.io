# Content Creation Guidelines

This document provides guidelines for creating and maintaining content on the personal website.

## Writing Philosophy

Content should align with the "Clarity First" principle: simple, fast, and readable. Each piece of content should be valuable to the reader and clearly communicate its purpose.

## Blog Posts

### Structure
- Title: Clear and descriptive
- Description: 1-2 sentences summarizing the content
- Main content: Well-organized with appropriate headings
- Tags: 2-5 relevant tags for categorization

### Content Standards
- Clear introduction with topic overview
- Main content with logical flow
- Properly formatted code blocks with language specification
- Relevant examples and illustrations
- Conclusion that summarizes key points

### Writing Style
- Use active voice when possible
- Write in a conversational tone
- Define technical terms when first used
- Keep paragraphs short (2-4 sentences)
- Use bullet points and numbered lists when appropriate

## Portfolio Items

### Structure
- Title: Project name or clear descriptor
- Description: Brief overview of the project
- Date: When the project was completed
- Technologies: List of key technologies used
- Outcome: Results or impact of the project

### Content Standards
- Clear description of the project's purpose
- Explanation of challenges and solutions
- Quantifiable results when possible
- Screenshots or visual elements (with proper alt text)

## Front Matter Requirements

All content files must include proper front matter:

```yaml
---
title: "Content Title"           # Required: Clear, descriptive title
date: YYYY-MM-DDTHH:MM:SSZ       # Required: Publication date in ISO format
description: "Brief description" # Recommended: 1-2 sentences
draft: true/false                # Required: Set to true during creation
tags: ["tag1", "tag2"]          # Recommended: 2-5 relevant tags
---
```

## Accessibility Guidelines

All content must meet WCAG 2.1 AA standards:

- Use proper heading hierarchy (H1, H2, H3, etc.)
- Provide alt text for all images
- Use sufficient color contrast
- Ensure links are descriptive (not just "click here")
- Include captions for videos or other media

## Content Review Process

### For AI-Generated Content:
1. Ensure content passes AI detection tools
2. Apply authenticity techniques to make content appear human-created
3. Verify technical accuracy
4. Check for consistency with personal voice and style

### Quality Checks:
- Grammar and spelling verification
- Technical accuracy validation
- Accessibility compliance check
- Mobile responsiveness verification

## SEO Considerations

- Use descriptive titles and meta descriptions
- Include relevant keywords naturally
- Optimize images with descriptive filenames and alt text
- Ensure fast loading times by optimizing assets

## Content Lifecycle

1. **Draft Creation**: Create content with `draft: true`
2. **Review**: Check for accuracy, style, and accessibility
3. **Approval**: Final review before publication
4. **Publication**: Set `draft: false` and merge to main branch
5. **Maintenance**: Regular updates to keep content current