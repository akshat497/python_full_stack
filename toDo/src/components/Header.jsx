import { Link } from 'react-router-dom'
import './Header.css'
export default function Header() {
  return (
    <div className='Header'>

    <h3>Logo</h3>

    <div className='HeaderButtonHolder'>
        <div>About Us</div>
        <div>Contact Us</div>
        <div>Home</div>
    </div>

    <div className='HeaderAuthHolder'>
       <Link to='/Login' style={{textDecoration:"none",color:"black"}}> <div style={{textDecoration:"none"}}>Login</div></Link>
        <Link to='/Signup' style={{textDecoration:"none",color:"black"}}><div style={{textDecoration:"none"}}>Signup</div></Link>
    </div>

    </div>
  )
}
