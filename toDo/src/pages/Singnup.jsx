import React from 'react'

export default function Singnup() {
  return (
    <div id='Signup'>
      <div id='SignupForm'>
        <h1>Signup</h1>
        <input type='text' placeholder='Username' name='username' id='username'/>
        <input type='email' placeholder='Email' name='email' id='email'/>
        <input type='password' placeholder='Password' name='password' id='password'/>
        <button>Signup</button>
      </div>
    </div>
  )
}
