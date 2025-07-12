import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const taskAPI = {
  // Получить активные задачи
  getActiveTasks: async () => {
    const response = await api.get('/i_can_do_it/get_active_task');
    return response.data.result;
  },

  // Создать новую задачу
  createTask: async (taskData) => {
    const response = await api.post('/i_can_do_it/create_task', taskData);
    return response.data;
  },

  // Отметить задачу как выполненную
  updateTask: async (taskId) => {
    const response = await api.patch('/i_can_do_it/update_task', { id: taskId });
    return response.data;
  },
};