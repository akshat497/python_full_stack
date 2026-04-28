import React, { useState } from 'react'

export default function Login() {
  const [email, setemail] = useState("")
  const [password, setpassword] = useState("")

  function Login(){
    try {
      let credintials = {
        email,
        password
      }

      localStorage.setItem("credintials",JSON.stringify(credintials))
    } catch (error) {
      console.log(error)
      
    }
  }
  return (
    <div id='Login'>
     <div id='LoginForm'>
     <h1>Login</h1>
       <input type='email' placeholder='Email' name='login' id='login' value={email} onChange={(e) => setemail(e.target.value)}/>
      <input type='password' placeholder='Password' name='password' id='password' value={password} onChange={(e) => setpassword(e.target.value)}/>
      <button onClick={Login}>Login</button>
     </div>
    </div>
  )
}
