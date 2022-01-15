import React from 'react';
import { List, Header, Rating, Table } from "semantic-ui-react";


export const Tasks = ({tasks}) => {
    return (
        <Table singleLine>
        <Table.Header>
            <Table.Row>
                <Table.HeaderCell>paperId</Table.HeaderCell>
                <Table.HeaderCell>numOfTimeReferenced</Table.HeaderCell>
            </Table.Row>
        </Table.Header>

        <Table.Body>
            {
                tasks.map(task => {
                    return (
                        <Table.Row key={task.paperId}>
                            <Table.Cell>
                                {task.paperId}
                            </Table.Cell>
                            <Table.Cell>
                                {task.numOfTimeReferenced}
                            </Table.Cell>
                        </Table.Row>
                    )
                    
                })
            }
        </Table.Body>
    </Table>
    )
    
}

// export default Tasks
// export const Tasks = ({ tasks }) => {
//     return (
//       <List>
//         {tasks.map(task => {
//           return (
//             <List.Item key={task.paperId}>
//               <Header>{task.paperId}</Header>
//               <p>
//                   {task.numOfTimeReferenced}
//               </p>
//             </List.Item>
//           );
//         })}
//       </List>
//     );
//   };