import React from 'react';
import { List, Header, Rating } from "semantic-ui-react";

export const Tasks = ({ tasks }) => {
    return (
      <List>
        {tasks.map(task => {
          return (
            <List.Item key={movie.title}>
              <Header>{movie.title}</Header>
              <Rating rating={movie.rating} maxRating={5} disabled />
            </List.Item>
          );
        })}
      </List>
    );
  };