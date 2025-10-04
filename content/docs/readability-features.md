# Readability Features Documentation

This document describes the readability features implemented in the site to ensure content is presented clearly and accessibly to all users.

## Features Overview

The site includes several features designed to improve readability and accessibility:

1. **Adjustable Text Size** - Users can change the font size to small, medium, or large
2. **High Contrast Mode** - Increases contrast for better visibility
3. **Adjustable Content Width** - Allows users to change the content width to narrow, medium, or wide
4. **Adjustable Line Spacing** - Changes line spacing to compact, normal, or spacious
5. **Responsive Design** - Adapts to different screen sizes for optimal reading
6. **Accessibility Optimizations** - Compliant with WCAG 2.1 AA standards

## How to Use Readability Controls

### Location
The readability controls are available in the header navigation. Click on the readability icon (looks like an eye) to open the controls panel.

### Available Settings
- **Font Size**: Choose from Small, Medium, or Large
- **High Contrast**: Toggle high contrast mode on/off
- **Content Width**: Select Narrow, Medium, or Wide
- **Line Spacing**: Choose Compact, Normal, or Spacious

### Persistence
Your readability settings are saved in your browser's local storage, so they will persist between visits to the site.

## Technical Implementation

### CSS Architecture
The readability features are implemented using:
- CSS custom properties (variables) to control styling
- Sass (SCSS) for maintainable stylesheets
- Responsive design principles for different screen sizes

### Files Structure
```
assets/scss/readability/
├── _base.scss          # Base readability styles
├── _typography.scss    # Typography and text styling
├── _accessibility.scss # Accessibility-specific styles
├── _responsive.scss    # Responsive design styles
└── _content-types.scss # Content type-specific styling
```

### JavaScript Implementation
- User preference model stored in `assets/js/models/UserPreference.js`
- Readability controls in `assets/js/readability.js`
- Settings persistence using localStorage

### Hugo Templates
- Readability controls component in `layouts/partials/readability-controls.html`
- Readability settings API in `layouts/partials/readability-settings.html`
- Updated base template with WCAG compliance in `layouts/_default/baseof.html`
- Enhanced navigation with readability controls in `layouts/partials/site-navigation.html`

## Accessibility Compliance

The site implements WCAG 2.1 AA compliance through:
- Sufficient color contrast (minimum 4.5:1 for normal text, 3:1 for large text)
- Keyboard navigation support
- Focus indicators
- Semantic HTML markup
- ARIA attributes where appropriate
- Skip links for screen readers
- Reduced motion support
- High contrast mode

## Performance Considerations

- All CSS is minified and bundled
- JavaScript is optimized for performance
- Images are responsive and properly sized
- Assets are loaded efficiently

## Responsive Design

- Mobile-first approach
- Flexible layouts using CSS Grid and Flexbox
- Responsive typography that adapts to screen size
- Touch targets sized appropriately for mobile devices