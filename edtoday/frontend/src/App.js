import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
// import axios from 'axios'



function App() {
  const [tasks, setTasks] = useState({})

  useEffect(()=>{
    fetch('/flask/hello').then(response => 
      response.json().then(data => {
        console.log(data)
      })      
    );
  }, [])


  return (
    <div className="App">
      
    </div>
  );
}

export default App;
