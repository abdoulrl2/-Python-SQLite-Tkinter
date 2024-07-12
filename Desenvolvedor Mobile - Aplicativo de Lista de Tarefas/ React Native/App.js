import React, { useState } from 'react';
import { StyleSheet, View, FlatList } from 'react-native';
import TaskInput from './components/TaskInput';
import TaskItem from './components/TaskItem';

export default function App() {
  const [tasks, setTasks] = useState([]);

  const addTaskHandler = taskTitle => {
    setTasks(currentTasks => [
      ...currentTasks,
      { id: Math.random().toString(), value: taskTitle }
    ]);
  };

  const removeTaskHandler = taskId => {
    setTasks(currentTasks => {
      return currentTasks.filter(task => task.id !== taskId);
    });
  };

  return (
    <View style={styles.screen}>
      <TaskInput onAddTask={addTaskHandler} />
      <FlatList
        keyExtractor={(item, index) => item.id}
        data={tasks}
        renderItem={itemData => (
          <TaskItem
            id={itemData.item.id}
            onDelete={removeTaskHandler}
            title={itemData.item.value}
          />
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  screen: {
    padding: 50
  }
});
