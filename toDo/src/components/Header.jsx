import { Link } from 'react-router-dom'
import './Header.css'
export default function Header() {
  return (
    <div className='Header'>

    <h3>Logo</h3>

    <div className='HeaderButtonHolder'>
         <Link to='/' style={{textDecoration:"none",color:"black"}}><div>About Us</div></Link> 
         <Link to='/contact' style={{textDecoration:"none",color:"black"}}><div>Contact Us</div></Link>
     
    </div>

    <div className='HeaderAuthHolder'>
       <Link to='/Login' style={{textDecoration:"none",color:"black"}}> <div style={{textDecoration:"none"}}>Login</div></Link>
        <Link to='/Signup' style={{textDecoration:"none",color:"black"}}><div style={{textDecoration:"none"}}>Signup</div></Link>
    </div>

    </div>
  )
}
