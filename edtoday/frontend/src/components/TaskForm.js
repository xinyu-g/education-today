import React, { useEffect, useState } from "react";
import { Form, Input, Rating, Button } from "semantic-ui-react";


export const TaskForm = ({ onAuthorId }) => {
    const [authorId, setAuthorId] = useState("");
    // var [tasks, setTasks] = useState([])
    // const [paperId, setPaperId] = useState();
    // const [cnt, setCnt] = useState(0);

    // const search = () => {
    //     // async () => {
    //         // const movie = { title, rating };
    //         fetch("/task1", {
    //           method: "POST",
    //           headers: {
    //             "Content-Type": "application/json"
    //           },
    //           body: JSON.stringify(authorId)
    //         })
    //         .then(function(response){
    //             console.log("response worked!", response);
    //             // onAuthorId(response)
    //             return response.json()
    //         }).then(function(data) {
    //             console.log(data)
    //             setTasks(data.tasks)
    //         })
    //         .catch(error => {
    //             console.log(error)
    //         });

    //         // if (response.ok) {
    //         //     console.log("response worked!", response);
    //         //     onAuthorId(response.json())
    //         //     setAuthorId("")
    //         // }
    //     //   }
    // }
    
    // useEffect(()=>{
    //     search()
    // },[])

    return (
        <Form>
            <Form.Field>
                <Input 
                 placeholder="author id"
                 value={authorId}
                 onChange={e => setAuthorId(e.target.value)}
                 />
            </Form.Field>
            <Form.Field>
                <Button 
                    onClick={
                        async () => {
                            console.log(authorId)
                            fetch("/task1", {
                                method: "POST",
                                headers: {
                                "Content-Type": "application/json"
                                },
                                body: JSON.stringify(authorId)
                            })
                            .then(response => {
                                console.log("response worked!", response);
                                // onAuthorId(response)
                                response.json()
                                .then(data => {
                                    console.log(data.tasks);
                                    onAuthorId(data.tasks);
                                    setAuthorId("")
                                })
                            })
                            


                            
                        }
                        // onAuthorId(tasks);

                    }
                >
                    submit
                </Button>
            </Form.Field>
        </Form>
        
    );
};