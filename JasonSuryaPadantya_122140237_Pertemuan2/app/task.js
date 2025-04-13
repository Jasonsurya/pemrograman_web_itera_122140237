export class Task {
    constructor(title, dueDate) {
      this.id = Date.now();
      this.title = title;
      this.dueDate = dueDate;
    }
  }
  