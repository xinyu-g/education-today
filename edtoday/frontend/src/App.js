import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import { Tasks } from "./components/Tasks";
import { TaskForm } from "./components/TaskForm";
import { Container } from "semantic-ui-react";
// import axios from 'axios'



function App() {
  const [tasks, setTasks] = useState([])
  const [authorId, setAuthorId] = useState("0")
  // let search = () => {};
  // console.log(authorId)
  
  // const  search = () => {
  //     // async () => {
  //         // const movie = { title, rating };
  //         console.log(authorId)
  //         fetch("/task1", {
  //           method: "POST",
  //           headers: {
  //             "Content-Type": "application/json"
  //           },
  //           body: JSON.stringify(authorId)
  //         })
  //         .then(response => {
  //             console.log("response worked!", response);
  //             // onAuthorId(response)
  //             response.json()
  //         .then(data => {
  //             console.log(data.tasks);
  //             setTasks(data.tasks)
  //         })
  //       })
          // .catch(error => {
          //     console.log(error)
          // });

        // if (response.ok) {
        //     console.log("response worked!", response);
        //     onAuthorId(response.json())
        //     setAuthorId("")
        // }
    //   }
// }

// useEffect(()=>{
//   search()
// },[])

// if (authorId !== '0') {
//   search()
//   setAuthorId("0")
// }




  return (
    <Container style={{ marginTop: 40 }}>
      <TaskForm
        onAuthorId={tasks => 
          // console.log(data.tasks)
          setTasks(tasks)
        }  
      />
      
      <Tasks tasks={tasks} />
    </Container>
    // <div className="App">
      
    // </div>
  );
}



export default App;
