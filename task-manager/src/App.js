import React, { useState, useEffect } from 'react';
import TaskList from './components/TaskList';
import TaskForm from './components/TaskForm';
import { taskAPI } from './api';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Загрузка задач при запуске приложения
  const loadTasks = async () => {
    try {
      setLoading(true);
      setError(null);
      const activeTasks = await taskAPI.getActiveTasks();
      setTasks(activeTasks);
    } catch (err) {
      console.error('Ошибка при загрузке задач:', err);
      setError('Не удалось загрузить задачи. Проверьте подключение к серверу.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTasks();
  }, []);

  // Создание новой задачи
  const handleCreateTask = async (taskData) => {
    try {
      await taskAPI.createTask(taskData);
      // Перезагружаем список задач после создания
      await loadTasks();
    } catch (error) {
      console.error('Ошибка при создании задачи:', error);
      throw error;
    }
  };

  // Отметка задачи как выполненной
  const handleCompleteTask = async (taskId) => {
    try {
      await taskAPI.updateTask(taskId);
      // Перезагружаем список задач после обновления
      await loadTasks();
    } catch (error) {
      console.error('Ошибка при обновлении задачи:', error);
      alert('Ошибка при отметке задачи как выполненной');
    }
  };

  if (loading) {
    return (
      <div className="App">
        <div className="container">
          <div className="loading">Загрузка задач...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <div className="container">
        <h1>Менеджер задач</h1>

        {error && (
          <div className="error">
            {error}
            <button onClick={loadTasks} className="retry-btn">
              Попробовать снова
            </button>
          </div>
        )}

        <TaskForm onCreateTask={handleCreateTask} />
        <TaskList tasks={tasks} onCompleteTask={handleCompleteTask} />
      </div>
    </div>
  );
}

export default App;