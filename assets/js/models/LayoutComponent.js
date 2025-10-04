/**
 * Layout Component Model
 * Represents the structural elements that organize content in a readable manner.
 */
export class LayoutComponent {
  constructor(componentType, styling = {}, accessibilityProps = {}, responsiveBehavior = {}) {
    this.componentType = this.validateComponentType(componentType);
    this.styling = this.validateStyling(styling);
    this.accessibilityProps = this.validateAccessibilityProps(accessibilityProps);
    this.responsiveBehavior = this.validateResponsiveBehavior(responsiveBehavior);
  }

  validateComponentType(componentType) {
    const validTypes = ['header', 'sidebar', 'container', 'main', 'footer', 'article', 'section', 'nav'];
    if (!validTypes.includes(componentType)) {
      throw new Error(`Component type must be one of: ${validTypes.join(', ')}`);
    }
    return componentType;
  }

  validateStyling(styling) {
    // Basic validation for CSS properties
    if (typeof styling !== 'object') {
      throw new Error('Styling must be an object containing CSS properties');
    }
    
    // In a real implementation, we would validate specific CSS properties
    // For now, we'll just ensure it's an object
    return styling;
  }

  validateAccessibilityProps(accessibilityProps) {
    // Basic validation for accessibility properties
    if (typeof accessibilityProps !== 'object') {
      throw new Error('Accessibility properties must be an object');
    }

    // Ensure common accessibility props are valid
    if (accessibilityProps.role && typeof accessibilityProps.role !== 'string') {
      throw new Error('Role property must be a string');
    }

    if (accessibilityProps['aria-label'] && typeof accessibilityProps['aria-label'] !== 'string') {
      throw new Error('Aria-label property must be a string');
    }

    if (accessibilityProps['aria-labelledby'] && typeof accessibilityProps['aria-labelledby'] !== 'string') {
      throw new Error('Aria-labelledby property must be a string');
    }

    // In a real implementation, we would validate for WCAG 2.1 AA compliance
    return accessibilityProps;
  }

  validateResponsiveBehavior(responsiveBehavior) {
    if (typeof responsiveBehavior !== 'object') {
      throw new Error('Responsive behavior must be an object');
    }

    // Validate screen size related properties
    const screens = ['mobile', 'tablet', 'desktop'];
    for (const screen of screens) {
      if (responsiveBehavior[screen] && typeof responsiveBehavior[screen] !== 'object') {
        throw new Error(`Responsive behavior for ${screen} must be an object`);
      }
    }

    return responsiveBehavior;
  }

  /**
   * Applies the styling to a DOM element
   */
  applyStyling(element) {
    if (!(element instanceof HTMLElement)) {
      throw new Error('Element must be an instance of HTMLElement');
    }

    // Apply styling properties to the element
    Object.keys(this.styling).forEach(property => {
      // Convert camelCase to kebab-case for CSS properties
      const cssProperty = property.replace(/([A-Z])/g, '-$1').toLowerCase();
      element.style[cssProperty] = this.styling[property];
    });
  }

  /**
   * Applies accessibility attributes to a DOM element
   */
  applyAccessibility(element) {
    if (!(element instanceof HTMLElement)) {
      throw new Error('Element must be an instance of HTMLElement');
    }

    // Apply accessibility properties to the element
    Object.keys(this.accessibilityProps).forEach(attr => {
      element.setAttribute(attr, this.accessibilityProps[attr]);
    });
  }

  /**
   * Returns a plain object representation of this LayoutComponent
   */
  toJSON() {
    return {
      componentType: this.componentType,
      styling: this.styling,
      accessibilityProps: this.accessibilityProps,
      responsiveBehavior: this.responsiveBehavior
    };
  }
}