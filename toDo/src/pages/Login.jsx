import React from 'react'

export default function Login() {
  return (
    <div id='Login'>
     <div id='LoginForm'>
     <h1>Login</h1>
       <input type='email' placeholder='Email' name='login' id='login'/>
      <input type='password' placeholder='Password' name='password' id='password'/>
      <button>Login</button>
     </div>
    </div>
  )
}
