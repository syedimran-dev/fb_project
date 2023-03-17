import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react'
import SignUp from "./SignUp";
import Login from "./Login"
import Home from "./Home";

const routes = () => {
  const logged = localStorage.getItem('REACT_TOKEN_AUTH_KEY')
  return (
    <>
      <BrowserRouter>
        <Routes>
          {!logged ?(
            <>
              <Route path="/signup" element={<SignUp />} />
              <Route path="/" element={<Login />} />
            </>
          ): 
          <Route path="/home" element={<Home />} />
        }
          
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default routes