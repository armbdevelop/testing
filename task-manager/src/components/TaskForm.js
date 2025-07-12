import React, { useState } from 'react';
import './TaskForm.css';

const TaskForm = ({ onCreateTask }) => {
  const [formData, setFormData] = useState({
    name: '',
    description: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData.name.trim() || !formData.description.trim()) {
      alert('Пожалуйста, заполните все поля');
      return;
    }

    setIsSubmitting(true);

    try {
      await onCreateTask(formData);
      setFormData({ name: '', description: '' });
    } catch (error) {
      console.error('Ошибка при создании задачи:', error);
      alert('Ошибка при создании задачи');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="task-form">
      <h2>Создать новую задачу</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Название задачи:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Введите название задачи"
            disabled={isSubmitting}
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Описание:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder="Введите описание задачи"
            rows="4"
            disabled={isSubmitting}
          />
        </div>

        <button
          type="submit"
          className="submit-btn"
          disabled={isSubmitting}
        >
          {isSubmitting ? 'Создание...' : 'Создать задачу'}
        </button>
      </form>
    </div>
  );
};

export default TaskForm;