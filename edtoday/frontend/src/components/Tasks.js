import React from 'react';
import { List, Header, Rating } from "semantic-ui-react";

export const Tasks = ({ tasks }) => {
    return (
      <List>
        {tasks.map(task => {
          return (
            <List.Item key={task.paperId}>
              <Header>{task.paperId}</Header>
              <p>
                  {task.numOfTimeReferenced}
              </p>
            </List.Item>
          );
        })}
      </List>
    );
  };