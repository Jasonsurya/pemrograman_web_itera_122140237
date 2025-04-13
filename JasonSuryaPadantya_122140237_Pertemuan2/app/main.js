import { getTasks, saveTask, deleteTask } from './storage.js';

const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const dueDateInput = document.getElementById('dueDateInput');
const taskTableBody = document.querySelector('#taskTable tbody');

const renderTasks = () => {
  const tasks = getTasks();
  taskTableBody.innerHTML = '';

  tasks.forEach((task, index) => {
    const row = document.createElement('tr');

    row.innerHTML = `
      <td>${index + 1}</td>
      <td>${task.name}</td>
      <td>${task.dueDate}</td>
      <td><button class="deleteBtn" data-index="${index}">Hapus</button></td>
    `;

    taskTableBody.appendChild(row);
  });

  document.querySelectorAll('.deleteBtn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const index = e.target.dataset.index;
      deleteTask(index);
      renderTasks();
    });
  });
};

taskForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const name = taskInput.value.trim();
  const dueDate = dueDateInput.value;

  if (!name || !dueDate) return;

  saveTask({ name, dueDate });
  taskInput.value = '';
  dueDateInput.value = '';

  renderTasks();
});

document.addEventListener('DOMContentLoaded', renderTasks);
