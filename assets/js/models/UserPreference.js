/**
 * User Preference Model
 * Represents user-specific preferences for content presentation.
 */
export class UserPreference {
  constructor(fontSizePreference = 'medium', highContrastMode = false, readingWidth = 'medium') {
    this.fontSizePreference = this.validateFontSizePreference(fontSizePreference);
    this.highContrastMode = this.validateHighContrastMode(highContrastMode);
    this.readingWidth = this.validateReadingWidth(readingWidth);
  }

  validateFontSizePreference(fontSizePreference) {
    const validSizes = ['small', 'medium', 'large'];
    if (!validSizes.includes(fontSizePreference)) {
      throw new Error('Font size preference must be one of: small, medium, large');
    }
    return fontSizePreference;
  }

  validateHighContrastMode(highContrastMode) {
    if (typeof highContrastMode !== 'boolean') {
      throw new Error('High contrast mode must be a boolean value');
    }
    return highContrastMode;
  }

  validateReadingWidth(readingWidth) {
    const validWidths = ['narrow', 'medium', 'wide'];
    if (!validWidths.includes(readingWidth)) {
      throw new Error('Reading width must be one of: narrow, medium, wide');
    }
    return readingWidth;
  }

  /**
   * Updates the font size preference
   */
  updateFontSize(fontSize) {
    this.fontSizePreference = this.validateFontSizePreference(fontSize);
  }

  /**
   * Toggles the high contrast mode
   */
  toggleHighContrast() {
    this.highContrastMode = !this.highContrastMode;
  }

  /**
   * Updates the reading width
   */
  updateReadingWidth(width) {
    this.readingWidth = this.validateReadingWidth(width);
  }

  /**
   * Applies these preferences to a document or element
   */
  applyToDocument(doc = document) {
    // Apply font size
    const fontSizeMap = {
      'small': '14px',
      'medium': '16px',
      'large': '18px'
    };
    doc.documentElement.style.setProperty('--font-size', fontSizeMap[this.fontSizePreference]);

    // Apply high contrast
    if (this.highContrastMode) {
      doc.documentElement.classList.add('high-contrast');
    } else {
      doc.documentElement.classList.remove('high-contrast');
    }

    // Apply reading width
    const widthMap = {
      'narrow': '50%',
      'medium': '70%',
      'wide': '90%'
    };
    doc.documentElement.style.setProperty('--reading-width', widthMap[this.readingWidth]);
  }

  /**
   * Loads preferences from local storage
   */
  static loadFromStorage() {
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
      // Return default preferences if none are stored
      return new UserPreference();
    } catch (error) {
      console.warn('Could not load user preferences from storage:', error);
      return new UserPreference();
    }
  }

  /**
   * Saves preferences to local storage
   */
  saveToStorage() {
    try {
      localStorage.setItem('userPreferences', JSON.stringify(this));
    } catch (error) {
      console.warn('Could not save user preferences to storage:', error);
    }
  }

  /**
   * Returns a plain object representation of this UserPreference
   */
  toJSON() {
    return {
      fontSizePreference: this.fontSizePreference,
      highContrastMode: this.highContrastMode,
      readingWidth: this.readingWidth
    };
  }
}