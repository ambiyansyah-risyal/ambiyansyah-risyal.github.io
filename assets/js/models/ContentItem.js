/**
 * Content Item Model
 * Represents the written content that needs to be presented clearly to users.
 */
export class ContentItem {
  constructor(title, content, author = '', date = new Date(), tags = [], readTime = 0, contentType = 'article') {
    this.title = this.validateTitle(title);
    this.content = this.validateContent(content);
    this.author = author;
    this.date = this.validateDate(date);
    this.tags = tags;
    this.readTime = this.validateReadTime(readTime);
    this.contentType = contentType;
  }

  validateTitle(title) {
    if (typeof title !== 'string' || title.length < 1 || title.length > 200) {
      throw new Error('Title must be a string between 1 and 200 characters');
    }
    return title;
  }

  validateContent(content) {
    if (typeof content !== 'string' || content.trim() === '') {
      throw new Error('Content must be a non-empty string');
    }
    return content;
  }

  validateDate(date) {
    if (!(date instanceof Date) && isNaN(Date.parse(date))) {
      throw new Error('Date must be a valid date');
    }
    return new Date(date);
  }

  validateReadTime(readTime) {
    if (typeof readTime !== 'number' || readTime <= 0) {
      throw new Error('Read time must be a positive number');
    }
    return readTime;
  }

  /**
   * Updates the content of this item
   */
  updateContent(newContent) {
    this.content = this.validateContent(newContent);
    // Recalculate read time based on new content
    this.readTime = this.calculateReadTime(newContent);
  }

  /**
   * Calculates estimated reading time in minutes based on content length
   */
  calculateReadTime(content) {
    const wordsPerMinute = 200; // Average reading speed
    const wordCount = content.trim().split(/\s+/).length;
    return Math.ceil(wordCount / wordsPerMinute);
  }

  /**
   * Returns a plain object representation of this ContentItem
   */
  toJSON() {
    return {
      title: this.title,
      content: this.content,
      author: this.author,
      date: this.date.toISOString(),
      tags: this.tags,
      readTime: this.readTime,
      contentType: this.contentType
    };
  }
}