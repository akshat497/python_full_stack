import React, { useState } from 'react'

export default function Singnup() {
  const [username, setusername] = useState("")
  const [email, setemail] = useState("")
  const [passwordfirst, setPasswordfirst] = useState("")
  const [passwordsecond, setPasswordsecond] = useState("")



  function Signup(){
    try {
      let credintials = {
        username,
        email,
        passwordfirst,
        passwordsecond
      }
    
      localStorage.setItem("Signup",JSON.stringify(credintials))
    } catch (error) {
      console.log(error)
      
    }
  }
  return (
    <div id='Signup'>
      <div id='SignupForm'>
        <h1>Signup</h1>
        <input type='text' placeholder='Username' name='username' id='username' value={username} onChange={(e) => setusername(e.target.value)}/>
        <input type='email' placeholder='Email' name='email' id='email' value={email} onChange={(e) => setemail(e.target.value)}/>
        <input type='password' placeholder='Password' name='password' id='password' value={passwordfirst} onChange={(e) => setPasswordfirst(e.target.value)}/>
        <input type='password' placeholder='Confirm Password' name='confirmPassword' id='confirmPassword' value={passwordsecond} onChange={(e) => setPasswordsecond(e.target.value)}/>
        <button onClick={Signup}>Signup</button>
      </div>
    </div>
  )
}
