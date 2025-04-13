const TASKS_KEY = 'dashboard_tasks';

export const getTasks = () => {
  return JSON.parse(localStorage.getItem(TASKS_KEY)) || [];
};

export const saveTask = (task) => {
  const tasks = getTasks();
  tasks.push(task);
  localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
};

export const deleteTask = (index) => {
  const tasks = getTasks();
  tasks.splice(index, 1);
  localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
};
