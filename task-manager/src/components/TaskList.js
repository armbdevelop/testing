import React from 'react';
import './TaskList.css';

const TaskList = ({ tasks, onCompleteTask }) => {
  if (!tasks || tasks.length === 0) {
    return (
      <div className="task-list">
        <h2>Активные задачи</h2>
        <p className="no-tasks">Нет активных задач</p>
      </div>
    );
  }

  return (
    <div className="task-list">
      <h2>Активные задачи ({tasks.length})</h2>
      <div className="tasks">
        {tasks.map((task) => (
          <div key={task.id} className="task-item">
            <div className="task-content">
              <h3 className="task-name">{task.name}</h3>
              <p className="task-description">{task.description}</p>
              <small className="task-date">
                Создано: {new Date(task.created_at).toLocaleString('ru-RU')}
              </small>
            </div>
            <button
              className="complete-btn"
              onClick={() => onCompleteTask(task.id)}
            >
              ✓ Выполнено
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TaskList;