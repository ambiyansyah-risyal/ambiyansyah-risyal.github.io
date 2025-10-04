/**
 * Readability Settings JavaScript
 * Handles user preferences for font size, contrast, and layout
 */

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  // Load saved preferences
  const userPreferences = loadUserPreferences();
  
  // Apply preferences to the document
  userPreferences.applyToDocument();
  
  // Set up event listeners for readability controls
  setupReadabilityControls();
});

/**
 * Load user preferences from storage or create defaults
 */
function loadUserPreferences() {
  // Try to load from localStorage
  try {
    const stored = localStorage.getItem('userPreferences');
    if (stored) {
      const parsed = JSON.parse(stored);
      return new UserPreference(
        parsed.fontSizePreference,
        parsed.highContrastMode,
        parsed.readingWidth
      );
    }
  } catch (error) {
    console.warn('Could not load user preferences from storage:', error);
  }
  
  // Return default preferences if none are stored
  return new UserPreference();
}

/**
 * Set up event listeners for readability controls
 */
function setupReadabilityControls() {
  // Font size control
  const fontSizeControl = document.getElementById('readability-font-size');
  if (fontSizeControl) {
    fontSizeControl.addEventListener('change', function() {
      const userPreferences = loadUserPreferences();
      userPreferences.updateFontSize(this.value);
      userPreferences.applyToDocument();
      userPreferences.saveToStorage();
    });
  }

  // High contrast control
  const contrastControl = document.getElementById('readability-contrast');
  if (contrastControl) {
    contrastControl.addEventListener('change', function() {
      const userPreferences = loadUserPreferences();
      userPreferences.highContrastMode = this.checked;
      userPreferences.applyToDocument();
      userPreferences.saveToStorage();
    });
  }

  // Reading width control
  const widthControl = document.getElementById('readability-width');
  if (widthControl) {
    widthControl.addEventListener('change', function() {
      const userPreferences = loadUserPreferences();
      userPreferences.updateReadingWidth(this.value);
      userPreferences.applyToDocument();
      userPreferences.saveToStorage();
    });
  }

  // Line spacing control
  const spacingControl = document.getElementById('readability-spacing');
  if (spacingControl) {
    spacingControl.addEventListener('change', function() {
      // Handle line spacing change
      document.documentElement.style.setProperty('--line-height-base', this.value === 'compact' ? '1.2' : this.value === 'spacious' ? '1.8' : '1.5');
    });
  }

  // Apply settings button
  const applyButton = document.getElementById('apply-readability-settings');
  if (applyButton) {
    applyButton.addEventListener('click', function() {
      // This is handled by individual control changes, but we can add any additional logic here
      console.log('Readability settings applied');
    });
  }

  // Reset settings button
  const resetButton = document.getElementById('reset-readability-settings');
  if (resetButton) {
    resetButton.addEventListener('click', function() {
      // Create default preferences and save them
      const defaultPreferences = new UserPreference();
      defaultPreferences.applyToDocument();
      defaultPreferences.saveToStorage();
      
      // Reset form controls to default values
      if (fontSizeControl) fontSizeControl.value = defaultPreferences.fontSizePreference;
      if (contrastControl) contrastControl.checked = defaultPreferences.highContrastMode;
      if (widthControl) widthControl.value = defaultPreferences.readingWidth;
      if (spacingControl) spacingControl.value = 'normal'; // Default line spacing
      
      // Reset the line height to default
      document.documentElement.style.setProperty('--line-height-base', '1.5');
      
      console.log('Readability settings reset to defaults');
    });
  }
}

/**
 * Add keyboard navigation support for readability controls
 */
function setupKeyboardNavigation() {
  // Add tabindex to important elements if not already present
  const controls = document.querySelectorAll('.readability-control');
  controls.forEach((control, index) => {
    if (!control.hasAttribute('tabindex')) {
      control.setAttribute('tabindex', '0');
    }
  });
}

/**
 * Add focus indicators for better accessibility
 */
function setupFocusIndicators() {
  // This is handled via CSS, but we could enhance it programmatically if needed
}

// Make sure to include the model classes in the global scope
// These would typically be loaded via separate script files or modules