import React, { useState } from 'react'

export default function Homepage() {
    const [title, settitle] = useState("")
    const [description, setdescription] = useState("")
    const [isCompleted, setisCompleted] = useState(false)

  async function addTodo(){
    try{
        const response = await fetch("http://localhost:8000/api/todos/create/",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                title,
                description,
                isCompleted
            })
        })
        const data = await response.json()
        alert(data.message)


    }catch(error){
        console.log(error)

    }

  }
  return (
    <div>
    <input type='text' onChange={(e)=>{settitle(e.target.value)}} value={title}/>
    <input type='text' onChange={(e)=>{setdescription(e.target.value)}} value={description}/>
    <input type='checkbox' onChange={(e)=>{setisCompleted(e.target.checked)}} value={isCompleted}/>
    <button onClick={addTodo}>submit</button>

    </div>
  )
}
