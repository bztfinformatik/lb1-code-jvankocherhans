import { useState } from 'react'
import './App.css'

// React Components
import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';

// Bootstrap Library
import 'bootstrap/dist/css/bootstrap.min.css'

// selfmade components
import { Home } from './Components/Home'
import { Login } from './Components/Login'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/logedin/home" element={<Home />} />
          <Route path="*" element={<h1>Wrong Direction</h1>}></Route>
        </Routes>
      </Router>
    </>
  )
}

export default App
