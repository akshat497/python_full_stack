import Header from "./components/Header"

import Footer from "./components/Footer"
import Aboutus from "./pages/Aboutus"
import Contactus from "./pages/Contactus"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Login from "./pages/Login"
import Singnup from "./pages/Singnup"
import Homepage from "./pages/Homepage"
export default function App() {
  return (
    <>
     
      <BrowserRouter>
       <Header/>
        <Routes>
          <Route path="/" element={<Aboutus/>} />
          <Route path="/contact" element={<Contactus/>} />
          <Route path="/Login" element={<Login/>} />
          <Route path="/homepage" element={<Homepage/>} />
          
          <Route path="/Signup" element={<Singnup/>} />
          
          
        </Routes>
         <Footer />
      </BrowserRouter>
     
    </>
  )
}
